# Nutanix API Swaggers

Specs OpenAPI des API v4 Nutanix (Prism Central), récupérées sur <https://developers.nutanix.com/api-reference>,
et référence des appels disponibles par version de Prism Central et par version d'AOS du cluster cible, plus les API historiques du Prism Element (v1, v2.0, v3).

| Chemin | Contenu |
|---|---|
| [`API-CALLS-PC7.md`](API-CALLS-PC7.md) | Tous les appels par namespace, avec la version d'API à utiliser sur PC 7.0 (pc.2024.3), 7.5 et 7.6 |
| [`api-calls-pc7.json`](api-calls-pc7.json) | Même contenu, lisible par programme (`namespaces.<ns>.calls[]`, `version_per_release`) |
| [`API-CALLS-PE7.md`](API-CALLS-PE7.md) | Appels v4 qui dépendent de la version d'AOS du cluster visé (appelés via le PC), version d'API à utiliser sur AOS 7.0, 7.5 et 7.6, et vérification en lab de ce qu'un PE sert lui-même |
| [`api-calls-pe7.json`](api-calls-pe7.json) | Même contenu, lisible par programme |
| [`API-CALLS-PE-LEGACY.md`](API-CALLS-PE-LEGACY.md) | API historiques du PE : v1 (402 appels), v2.0 (311), v3 (212), relevées sur AOS 7.5.1.13 et 7.6.0.6 |
| [`api-calls-pe-legacy.json`](api-calls-pe-legacy.json) | Même contenu, lisible par programme |
| `specs/yaml/swagger-{ns}-{v}-all.yaml` | Specs telles que publiées par Nutanix |
| `specs/json/swagger-{ns}-{v}-all.json` | Mêmes specs converties en JSON |
| `specs/pe-legacy/aos-<version>/` | Specs v1, v2.0 (Swagger 1.2, une déclaration par ressource) et v3 (Swagger 2.0) servies par un PE |
| `checks/pe-v4-aos-<version>.txt` | Codes HTTP des GET v4 envoyés directement à un PE, par version d'API |
| [`gen_api_calls.py`](gen_api_calls.py), [`gen_pe_legacy.py`](gen_pe_legacy.py) | Régénère les références depuis `specs/json/` : `python3 gen_api_calls.py PC` ou `PE`, `python3 gen_pe_legacy.py` (Python 3.9+, bibliothèque standard) |

Toutes les versions GA de chaque namespace sont présentes, plus la dernière pré-version quand elle est plus récente
que la dernière GA. `iam-v4.1.b2` n'est plus publiée par Nutanix et reste pour mémoire.

## Mettre à jour

Les specs sont servies par l'API publique du portail :

```bash
# versions disponibles d'un namespace
curl -sL https://developers.nutanix.com/api/v1/namespaces/vmm/versions/
# spec d'une version
curl -sL https://developers.nutanix.com/api/v1/namespaces/vmm/versions/v4.3/yaml -o specs/yaml/swagger-vmm-v4.3-all.yaml
# conversion JSON (PyYAML), puis régénération
python3 -c "import yaml,json,sys; json.dump(yaml.safe_load(open(sys.argv[1])), open(sys.argv[2],'w'), default=str)" \
  specs/yaml/swagger-vmm-v4.3-all.yaml specs/json/swagger-vmm-v4.3-all.json
python3 gen_api_calls.py PC && python3 gen_api_calls.py PE
```

API historiques : un cluster les publie lui-même (GET avec un compte admin), voir l'en-tête de `gen_pe_legacy.py` :
`/PrismGateway/services/rest/api/api-docs/{v1|v2.0}` (liste des ressources), `.../api-docs/{v1|v2.0}/<ressource>`, `/static/v3/swagger.json`.

Pour une nouvelle release, l'ajouter dans `TARGETS`, `RANK`, `LABEL` et `norm_pc()` du script.

## Limite

Nutanix ne publie pas de correspondance « version d'API → release PC ». Elle est déduite de l'extension
`x-supported-versions` de chaque opération (entrées `PC` et `PE`) ; la méthode et ses incertitudes (versions marquées `*`) sont décrites
en tête de chaque référence. L'entrée `PE` des specs v4 désigne la version d'AOS du cluster visé, pas un appel au PE : en lab, un PE enregistré sur un PC ne sert en v4 que `networking` et une partie de `lifecycle`. Les API historiques n'ont pu être relevées que sur AOS 7.5.1.13 et 7.6.0.6.
