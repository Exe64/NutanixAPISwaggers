"""Build the Nutanix v4 API call reference per Prism Central (PC) or Prism Element (PE) release.

usage: python3 gen_api_calls.py [PC|PE]      (default PC)
       reads specs/json/, writes API-CALLS-{PC|PE}7.md and api-calls-{pc|pe}7.json

Specs come from https://developers.nutanix.com/api/v1/namespaces/{ns}/versions/{v}/yaml
(converted to JSON and stored as specs/json/swagger-{ns}-{v}-all.json).
To add a release: download the new specs, add it to TARGETS/RANK/LABELS and norm_pc().
"""
import glob, re, os, sys, json, collections

PRODUCT = (sys.argv[1] if len(sys.argv) > 1 else 'PC').upper()
assert PRODUCT in ('PC', 'PE'), 'usage: gen_api_calls.py [PC|PE]'
SPECS = 'specs/json'
OUT_MD = f'API-CALLS-{PRODUCT}7.md'
OUT_JSON = f'api-calls-{PRODUCT.lower()}7.json'
METHODS = ('get', 'post', 'put', 'patch', 'delete')
TARGETS = ['7.0', '7.5', '7.6']
RANK = {'7.0': 0, '7.3': 1, '7.5': 2, '7.6': 3}
LABELS = {'PC': {'7.0': 'pc.2024.3 (AOS 7.0)', '7.3': 'pc.7.3', '7.5': 'pc.7.5', '7.6': 'pc.7.6'},
          'PE': {'7.0': 'AOS 7.0', '7.3': 'AOS 7.3', '7.5': 'AOS 7.5', '7.6': 'AOS 7.6'}}
LABEL = LABELS[PRODUCT]


def norm_pc(v):
    """Raw x-supported-versions PC/PE value -> 7.0/7.3/7.5/7.6, or None if unusable."""
    v = str(v).lower().removeprefix('pc.')
    if re.match(r'^(6\.|7\.0)', v):
        return '7.0'                       # PE: AOS 6.1 .. 7.0.1.6, all served by AOS 7.0
    if re.match(r'^20(2[0-4])\.', v):
        return '7.0'                       # 2022.6 .. 2024.3.1: all shipped by pc.2024.3
    if re.match(r'^2025\.', v) or v.startswith('7.3'):
        return '7.3'                       # 2025.1/2025.2 = internal labels of the 7.3 train
    if v.startswith('7.5'):
        return '7.5'
    if v.startswith('7.6'):
        return '7.6'
    if v in ('master', 'janus'):
        return '7.6'                       # unreleased-branch label: assumed latest, flagged in the doc
    return None


def vkey(v):
    return tuple(int(x) for x in re.findall(r'\d+', v))


def load(path):
    s = json.load(open(path, encoding='utf-8'))
    ops = {}
    for p, item in (s.get('paths') or {}).items():
        gpath = re.sub(r'^/([a-z]+)/v4\.\d+(\.[ab]\d+)?/', r'/\1/{v}/', p)
        for m, op in item.items():
            if m not in METHODS:
                continue
            sv = [e for e in op.get('x-supported-versions') or [] if e.get('product') == PRODUCT]
            if PRODUCT == 'PE' and not sv:
                continue                   # not served by Prism Element: PC only
            pcs = [x for x in (norm_pc(e.get('version')) for e in sv) if x]
            ops[(m.upper(), gpath)] = {
                'method': m.upper(), 'path': p, 'generic_path': gpath,
                'operationId': op.get('operationId', ''),
                'summary': ' '.join((op.get('summary') or '').split()).replace('|', '/'),
                'tag': (op.get('tags') or ['-'])[0],
                'min_release': min(pcs, key=RANK.get) if pcs else None,
                'deprecated': bool(op.get('deprecated')),
            }
    return s.get('info', {}).get('title', ''), ops


def build():
    specs, titles = collections.defaultdict(dict), {}
    for f in glob.glob(f'{SPECS}/swagger-*-all.json'):
        ns, ver = re.fullmatch(r'swagger-([a-z]+)-(v[\w.]+)-all\.json', os.path.basename(f)).groups()
        title, ops = load(f)
        if ops:                            # a version with no call for this product does not exist on it
            titles[ns], specs[ns][ver] = title, ops

    hi = lambda xs: max(xs, key=RANK.get) if xs else '7.0'
    gas = {ns: sorted((v for v in vers if re.fullmatch(r'v\d+\.\d+', v)), key=vkey) for ns, vers in specs.items()}
    # evidence: highest min_release among a version's operations
    evid = {(ns, v): hi([o['min_release'] for o in specs[ns][v].values() if o['min_release']]) for ns in gas for v in gas[ns]}
    # floor per version number: earliest release where some namespace introduced new calls in it
    floor = {}
    for ns, ga in gas.items():
        for i, v in enumerate(ga):
            if i == 0 or RANK[evid[ns, v]] > RANK[evid[ns, ga[i - 1]]]:
                floor[v] = min(floor.get(v, evid[ns, v]), evid[ns, v], key=RANK.get)

    out = {'source': 'https://developers.nutanix.com/api-reference', 'product': PRODUCT, 'releases': LABEL, 'namespaces': {}}
    for ns in sorted(specs):
        vers = specs[ns]
        ga = gas[ns]
        pre = sorted((v for v in vers if v not in ga), key=vkey)
        # release of a GA version = max(own evidence, previous version's release, floor of its number);
        # inferred = no call of its own proves that release
        rel, inferred = {}, []
        for i, v in enumerate(ga):
            prev = rel[ga[i - 1]] if i else '7.0'
            rel[v] = hi([evid[ns, v], prev, floor.get(v, '7.0')])
            if i and RANK[evid[ns, v]] <= RANK[evid[ns, ga[i - 1]]]:
                inferred.append(v)
        # for each PC: newest GA version whose operations are all supported by that PC
        pick = {}
        for t in TARGETS:
            ok = [v for v in ga if RANK[rel[v]] <= RANK[t]]
            pick[t] = ok[-1] if ok else None
        calls = {}
        for t in TARGETS:
            if not pick[t]:
                continue
            for k, o in vers[pick[t]].items():
                c = calls.setdefault(k, {**o, 'available': {}})
                c['available'][t] = pick[t]
                c['deprecated'] = c['deprecated'] or o['deprecated']
        preview = {}
        if pre and (not ga or vkey(pre[-1]) > vkey(ga[-1])):
            pv = pre[-1]
            preview = {'version': pv, 'calls': [o for k, o in sorted(vers[pv].items(), key=lambda x: (x[0][1], x[0][0]))
                                                if k not in calls]}
        out['namespaces'][ns] = {
            'title': titles[ns], 'ga_versions': ga, 'prerelease_versions': pre,
            'ga_version_release': rel, 'ga_version_release_inferred': inferred, 'version_per_release': pick,
            'calls': sorted(calls.values(), key=lambda c: (c['tag'], c['generic_path'], c['method'])),
            'preview': preview,
        }
    return out


def to_md(res):
    if PRODUCT == 'PE':
        return to_md_pe(res)
    md = ['# Référence des appels API Nutanix v4 par version de Prism Central\n',
          'Généré par `gen_api_calls.py` depuis les specs OpenAPI de <https://developers.nutanix.com/api-reference> '
          '(dossier `specs/json/`), via l\'extension `x-supported-versions` (product `PC`) de chaque opération. '
          'Version machine : `api-calls-pc7.json`.\n',
          '## Comment lire ce document\n',
          '- **PC 7.0** = `pc.2024.3`, le Prism Central livré avec AOS 7.0 (il n\'existe pas de PC « 7.0 »). '
          'PC 7.3 n\'a pas de colonne mais apparaît dans *Min PC*.\n'
          '- Nutanix ne publie pas de table « version d\'API → PC ». Elle est déduite ainsi : release d\'une version GA = '
          'max(Min PC de ses opérations, release de la version précédente, plus petite release où un autre namespace a '
          'introduit des appels dans ce même numéro de version). Une version marquée **\\*** est datée par ces deux '
          'dernières règles seulement (aucun appel nouveau ne le prouve) : la tester sur le PC visé, ou retomber sur la '
          'version précédente.\n'
          '- Pour chaque PC, la version retenue par namespace est la plus récente version GA dont la release est ≤ ce PC. '
          'Les colonnes 7.0 / 7.5 / 7.6 donnent la version à mettre à la place de `{v}` ; `—` = appel absent de ce PC.\n'
          '- Chemin complet : `https://<pc>:9440/api` + chemin, ex. `/vmm/{v}/ahv/config/vms` → '
          '`https://<pc>:9440/api/vmm/v4.0/ahv/config/vms`.\n'
          '- *Min PC* : version minimale déclarée par Nutanix, normalisée depuis les libellés bruts : '
          '`2022.x`…`2024.3.1` → 7.0 ; `2025.1`, `2025.2`, `7.3`, `pc.7.3` → 7.3 ; `pc.7.5`, `7.5.1` → 7.5 ; '
          '`master`/`Janus` (branches non publiées) → 7.6, **à vérifier**.\n'
          '- Un PC sert aussi les versions d\'API plus anciennes : un appel listé en v4.0 reste appelable en v4.0 sur 7.5 et 7.6.\n'
          '- **Preview** : appels des versions beta/alpha plus récentes que la dernière GA, hors matrice, à ne pas utiliser en production.\n'
          '- ⚠️ = opération marquée `deprecated` dans la spec.\n',
          '## Vue d\'ensemble : version d\'API par namespace et par PC\n',
          '| Namespace | Titre | PC 7.0 | PC 7.5 | PC 7.6 | Appels GA | Preview |',
          '|---|---|---|---|---|---|---|']
    return '\n'.join(md) + '\n' + body(res, 'PC')


def to_md_pe(res):
    md = ['# Référence des appels API Nutanix v4 servis par Prism Element, par version d\'AOS\n',
          'Généré par `gen_api_calls.py PE` depuis les specs OpenAPI de <https://developers.nutanix.com/api-reference> '
          '(dossier `specs/json/`), via l\'extension `x-supported-versions` (product `PE`) de chaque opération. '
          'Version machine : `api-calls-pe7.json`. Pendant côté Prism Central : `API-CALLS-PC7.md`.\n',
          '## Comment lire ce document\n',
          '- Seules figurent les opérations que Nutanix déclare servies par le **Prism Element** (entrée `PE` dans '
          '`x-supported-versions`). Tout le reste n\'existe que sur le Prism Central. Namespaces absents ici '
          '(aiops, files, iam, licensing, microseg, monitoring, opsmgmt, storage, tenancy) : PC uniquement.\n'
          '- Colonnes **AOS 7.0 / 7.5 / 7.6** : version d\'API à mettre à la place de `{v}`, `—` = appel absent. '
          'AOS 7.3 n\'a pas de colonne mais apparaît dans *Min AOS*.\n'
          '- Chemin complet : `https://<cvm-ou-vip>:9440/api` + chemin, ex. `/clustermgmt/{v}/config/clusters` → '
          '`https://<vip>:9440/api/clustermgmt/v4.0/config/clusters`.\n'
          '- Correspondance version d\'API → AOS déduite comme côté PC : release d\'une version GA = max(Min AOS de ses '
          'opérations PE, release de la version précédente, plus petite release où un autre namespace a introduit des '
          'appels PE dans ce numéro de version). **\\*** = version datée par ces deux dernières règles seulement : '
          'la tester sur l\'AOS visé, ou retomber sur la version précédente.\n'
          '- *Min AOS* normalisé : `6.1`…`7.0.1.6` → 7.0 (tout est servi par AOS 7.0) ; `Janus` (branche non publiée) → 7.6, **à vérifier**.\n'
          '- Les API historiques du PE (`/PrismGateway/services/rest/v1`, `v2.0`, `/api/nutanix/v3`) ne sont pas '
          'publiées en OpenAPI sur ce portail et ne figurent pas ici.\n'
          '- **Preview** : appels PE des versions beta/alpha plus récentes que la dernière GA, hors matrice.\n'
          '- ⚠️ = opération marquée `deprecated` dans la spec.\n',
          '## Vue d\'ensemble : version d\'API par namespace et par AOS\n',
          '| Namespace | Titre | AOS 7.0 | AOS 7.5 | AOS 7.6 | Appels GA | Preview |',
          '|---|---|---|---|---|---|---|']
    return '\n'.join(md) + '\n' + body(res, 'AOS')


def body(res, short):
    md = []
    for ns, d in res['namespaces'].items():
        p = {t: (v + ('\\*' if v in d['ga_version_release_inferred'] else '')) if v else '—'
             for t, v in d['version_per_release'].items()}
        pv = d['preview'].get('version', '') if d['preview'] else ''
        md.append(f'| [`{ns}`](#{ns}) | {d["title"]} | {p["7.0"]} | {p["7.5"]} | {p["7.6"]} '
                  f'| {len(d["calls"])} | {pv} |')
    md.append('')
    for ns, d in res['namespaces'].items():
        md.append(f'## {ns}\n')
        line = f'**{d["title"]}** — versions GA : {", ".join(d["ga_versions"]) or "aucune"}'
        if d['prerelease_versions']:
            line += f' ; pré-versions : {", ".join(d["prerelease_versions"])}'
        md.append(line + '\n')
        if d['ga_versions']:
            md.append(f'Release {short} par version : '
                      + ', '.join(f'{v} → {LABEL[r]}' + ('\\*' if v in d['ga_version_release_inferred'] else '')
                                  for v, r in d['ga_version_release'].items()) + '\n')
        if d['calls']:
            md += [f'| Méthode | Chemin | operationId | Résumé | Min {short} | 7.0 | 7.5 | 7.6 |',
                   '|---|---|---|---|---|---|---|---|']
            tag = None
            for c in d['calls']:
                if c['tag'] != tag:
                    tag = c['tag']
                    md.append(f'| | **{tag}** | | | | | | |')
                a = c['available']
                dep = ' ⚠️' if c['deprecated'] else ''
                md.append(f'| `{c["method"]}` | `{c["generic_path"]}` | {c["operationId"]}{dep} | {c["summary"]} | '
                          f'{c["min_release"] or "?"} | {a.get("7.0", "—")} | {a.get("7.5", "—")} | {a.get("7.6", "—")} |')
            md.append('')
        if d['preview'] and d['preview']['calls']:
            p = d['preview']
            md += [f'**Preview `{p["version"]}`** : appels absents des versions GA\n',
                   f'| Méthode | Chemin | operationId | Résumé | Min {short} |', '|---|---|---|---|---|']
            md += [f'| `{c["method"]}` | `{c["generic_path"]}` | {c["operationId"]} | {c["summary"]} | {c["min_release"] or "?"} |'
                   for c in p['calls']]
            md.append('')
    return '\n'.join(md) + '\n'


if __name__ == '__main__':
    assert norm_pc('2024.3.1') == '7.0' and norm_pc('pc.7.6') == '7.6' and norm_pc('2025.2') == '7.3'
    assert norm_pc('None') is None
    assert norm_pc('6.8') == '7.0' and norm_pc('7.0.1.6') == '7.0'
    res = build()
    assert res['namespaces']['vmm']['version_per_release']['7.0'] == 'v4.0'
    for d in res['namespaces'].values():   # a call never shows up on a release older than its declared minimum
        for c in d['calls']:
            assert all(RANK[t] >= RANK[c['min_release'] or '7.0'] for t in c['available']), c
    open(OUT_MD, 'w', encoding='utf-8').write(to_md(res))
    json.dump(res, open(OUT_JSON, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    for ns, d in res['namespaces'].items():
        print(f'{ns:15} {d["version_per_release"]} calls={len(d["calls"])} preview={d["preview"].get("version") if d["preview"] else ""}')
