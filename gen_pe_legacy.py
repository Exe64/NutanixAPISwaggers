"""Build the reference of Prism Element legacy API calls (v1, v2.0, v3) from the specs a cluster serves.

usage: python3 gen_pe_legacy.py      reads specs/pe-legacy/aos-*/, writes API-CALLS-PE-LEGACY.md and api-calls-pe-legacy.json

A cluster publishes them at (GET, admin credentials):
  /PrismGateway/services/rest/api/api-docs/{v1|v2.0}             Swagger 1.2 resource listing
  /PrismGateway/services/rest/api/api-docs/{v1|v2.0}/{resource}  one declaration per resource
  /static/v3/swagger.json                                         Swagger 2.0
Save them as specs/pe-legacy/aos-<version>/{v1,v2.0}/<resource>.json and v3.json.
"""
import glob, json, os, re

ROOT = 'specs/pe-legacy'
BASE = {'v1': '/PrismGateway/services/rest/v1', 'v2.0': '/PrismGateway/services/rest/v2.0', 'v3': '/api/nutanix/v3'}
METHODS = ('get', 'post', 'put', 'patch', 'delete')


def clean(s):
    return ' '.join(str(s or '').split()).replace('|', '/')


def load(d):
    """aos dir -> {(api, method, path): call}"""
    out = {}
    for api in ('v1', 'v2.0'):
        for f in sorted(glob.glob(f'{d}/{api}/*.json')):
            if os.path.basename(f) == '_resources.json':
                continue
            decl = json.load(open(f, encoding='utf-8'))
            base = re.sub(r'^https?://[^/]+', '', decl.get('basePath') or BASE[api])
            for a in decl.get('apis', []):
                for o in a.get('operations', []):
                    path = base + a['path']
                    out[(api, o['method'].upper(), path)] = {
                        'api': api, 'method': o['method'].upper(), 'path': path,
                        'resource': os.path.basename(f)[:-5], 'operationId': o.get('nickname', ''),
                        'summary': clean(o.get('summary')), 'deprecated': str(o.get('deprecated')).lower() == 'true'}
    spec = json.load(open(f'{d}/v3.json', encoding='utf-8'))
    for p, item in spec['paths'].items():
        for m, o in item.items():
            if m in METHODS:
                path = BASE['v3'] + p
                out[('v3', m.upper(), path)] = {
                    'api': 'v3', 'method': m.upper(), 'path': path,
                    'resource': (o.get('tags') or [p.strip('/').split('/')[0]])[0], 'operationId': o.get('operationId', ''),
                    'summary': clean(o.get('summary') or o.get('description', '').split('.')[0]),
                    'deprecated': bool(o.get('deprecated'))}
    return out


def vkey(v):
    return tuple(int(x) for x in re.findall(r'\d+', v))


def build():
    aos = sorted((os.path.basename(d)[4:] for d in glob.glob(f'{ROOT}/aos-*')), key=vkey)
    per = {v: load(f'{ROOT}/aos-{v}') for v in aos}
    calls = {}
    for v in aos:
        for k, c in per[v].items():
            calls.setdefault(k, {**c, 'aos': []})['aos'].append(v)
    order = {'v1': 0, 'v2.0': 1, 'v3': 2}
    return {'source': 'Prism Element api-docs (v1, v2.0) and /static/v3/swagger.json', 'aos_versions': aos,
            'calls': sorted(calls.values(), key=lambda c: (order[c['api']], c['resource'], c['path'], c['method']))}


def to_md(res):
    aos = res['aos_versions']
    md = ['# Référence des appels API historiques du Prism Element (v1, v2.0, v3)\n',
          'Généré par `gen_pe_legacy.py` depuis les specs servies par des clusters réels '
          f'(AOS {", ".join(aos)}), dossier `specs/pe-legacy/`. Version machine : `api-calls-pe-legacy.json`. '
          'Les API v4 sont dans `API-CALLS-PC7.md` et `API-CALLS-PE7.md`.\n',
          '## Comment lire ce document\n',
          '- Chemin complet : `https://<cvm-ou-vip>:9440` + chemin.\n'
          '- Colonnes AOS : ✓ = opération publiée par ce cluster. Les specs ne couvrent que les versions d\'AOS '
          'disponibles en lab ; AOS 7.0 n\'a pas pu être relevé.\n'
          '- **v3** : le PE publie la spec v3 complète (212 opérations, identique sur les deux AOS), mais v3 est d\'abord '
          'l\'API du Prism Central ; ce qui répond réellement sur un PE n\'a pas été testé.\n'
          '- ⚠️ = opération marquée `deprecated` dans la spec.\n',
          '## Vue d\'ensemble\n',
          '| API | Base | Ressources | Opérations | Dépréciées |', '|---|---|---|---|---|']
    for api in ('v1', 'v2.0', 'v3'):
        cs = [c for c in res['calls'] if c['api'] == api]
        md.append(f'| {api} | `{BASE[api]}` | {len({c["resource"] for c in cs})} | {len(cs)} | {sum(c["deprecated"] for c in cs)} |')
    md.append('')
    for api in ('v1', 'v2.0', 'v3'):
        md += [f'## {api}\n', '| Méthode | Chemin | operationId | Résumé | ' + ' | '.join(f'AOS {v}' for v in aos) + ' |',
               '|---|---|---|---|' + '---|' * len(aos)]
        res_name = None
        for c in (c for c in res['calls'] if c['api'] == api):
            if c['resource'] != res_name:
                res_name = c['resource']
                md.append(f'| | **{res_name}** | | |' + ' |' * len(aos))
            dep = ' ⚠️' if c['deprecated'] else ''
            md.append(f'| `{c["method"]}` | `{c["path"]}` | {c["operationId"]}{dep} | {c["summary"]} | '
                      + ' | '.join('✓' if v in c['aos'] else '—' for v in aos) + ' |')
        md.append('')
    return '\n'.join(md) + '\n'


if __name__ == '__main__':
    res = build()
    assert res['calls'] and all(c['path'].startswith(('/PrismGateway/', '/api/nutanix/')) for c in res['calls'])
    open('API-CALLS-PE-LEGACY.md', 'w', encoding='utf-8').write(to_md(res))
    json.dump(res, open('api-calls-pe-legacy.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    for api in ('v1', 'v2.0', 'v3'):
        print(api, sum(1 for c in res['calls'] if c['api'] == api), 'calls')
