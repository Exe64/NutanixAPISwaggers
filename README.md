# Nutanix API Swaggers

Specs OpenAPI des API v4 Nutanix (Prism Central), récupérées sur <https://developers.nutanix.com/api-reference>,
et référence des appels disponibles par version de Prism Central.

| Chemin | Contenu |
|---|---|
| [`API-CALLS-PC7.md`](API-CALLS-PC7.md) | Tous les appels par namespace, avec la version d'API à utiliser sur PC 7.0 (pc.2024.3), 7.5 et 7.6 |
| [`api-calls-pc7.json`](api-calls-pc7.json) | Même contenu, lisible par programme (`namespaces.<ns>.calls[]`, `version_per_pc`) |
| `specs/yaml/swagger-{ns}-{v}-all.yaml` | Specs telles que publiées par Nutanix |
| `specs/json/swagger-{ns}-{v}-all.json` | Mêmes specs converties en JSON |
| [`gen_api_calls.py`](gen_api_calls.py) | Régénère la référence depuis `specs/json/` (Python 3.9+, bibliothèque standard) |

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
python3 gen_api_calls.py
```

Pour une nouvelle release de PC, l'ajouter dans `TARGETS`, `RANK`, `LABEL` et `norm_pc()` du script.

## Limite

Nutanix ne publie pas de correspondance « version d'API → release PC ». Elle est déduite de l'extension
`x-supported-versions` de chaque opération ; la méthode et ses incertitudes (versions marquées `*`) sont décrites
en tête de [`API-CALLS-PC7.md`](API-CALLS-PC7.md).
