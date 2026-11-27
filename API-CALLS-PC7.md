# Référence des appels API Nutanix v4 par version de Prism Central

Généré par `gen_api_calls.py` depuis les specs OpenAPI de <https://developers.nutanix.com/api-reference> (dossier `specs/json/`), via l'extension `x-supported-versions` (product `PC`) de chaque opération. Version machine : `api-calls-pc7.json`.

## Comment lire ce document

- **PC 7.0** = `pc.2024.3`, le Prism Central livré avec AOS 7.0 (il n'existe pas de PC « 7.0 »). PC 7.3 n'a pas de colonne mais apparaît dans *Min PC*.
- Nutanix ne publie pas de table « version d'API → PC ». Elle est déduite ainsi : release d'une version GA = max(Min PC de ses opérations, release de la version précédente, plus petite release où un autre namespace a introduit des appels dans ce même numéro de version). Une version marquée **\*** est datée par ces deux dernières règles seulement (aucun appel nouveau ne le prouve) : la tester sur le PC visé, ou retomber sur la version précédente.
- Pour chaque PC, la version retenue par namespace est la plus récente version GA dont la release est ≤ ce PC. Les colonnes 7.0 / 7.5 / 7.6 donnent la version à mettre à la place de `{v}` ; `—` = appel absent de ce PC.
- Chemin complet : `https://<pc>:9440/api` + chemin, ex. `/vmm/{v}/ahv/config/vms` → `https://<pc>:9440/api/vmm/v4.0/ahv/config/vms`.
- *Min PC* : version minimale déclarée par Nutanix, normalisée depuis les libellés bruts : `2022.x`…`2024.3.1` → 7.0 ; `2025.1`, `2025.2`, `7.3`, `pc.7.3` → 7.3 ; `pc.7.5`, `7.5.1` → 7.5 ; `master`/`Janus` (branches non publiées) → 7.6, **à vérifier**.
- Un PC sert aussi les versions d'API plus anciennes : un appel listé en v4.0 reste appelable en v4.0 sur 7.5 et 7.6.
- **Preview** : appels des versions beta/alpha plus récentes que la dernière GA, hors matrice, à ne pas utiliser en production.
- ⚠️ = opération marquée `deprecated` dans la spec.

## Vue d'ensemble : version d'API par namespace et par PC

| Namespace | Titre | PC 7.0 | PC 7.5 | PC 7.6 | Appels GA | Preview |
|---|---|---|---|---|---|---|
| [`aiops`](#aiops) | Nutanix AIOps APIs | v4.0 | v4.0 | v4.0 | 18 | v4.2.b1 |
| [`clustermgmt`](#clustermgmt) | Nutanix Cluster Management APIs | v4.0 | v4.2 | v4.4\* | 121 |  |
| [`datapolicies`](#datapolicies) | Nutanix Data Policies APIs | v4.0 | v4.3\* | v4.3\* | 43 |  |
| [`dataprotection`](#dataprotection) | Nutanix Data Protection APIs | v4.0 | v4.3\* | v4.4 | 29 |  |
| [`files`](#files) | Nutanix Files APIs | v4.0 | v4.0 | v4.0 | 102 | v4.0.a2 |
| [`iam`](#iam) | Nutanix Identity and Access Management APIs | v4.0 | v4.0 | v4.0 | 54 | v4.1.b3 |
| [`licensing`](#licensing) | Nutanix Licensing APIs | v4.0 | v4.3 | v4.4 | 22 |  |
| [`lifecycle`](#lifecycle) | Nutanix Lifecycle Management APIs | v4.0 | v4.2 | v4.3 | 72 |  |
| [`microseg`](#microseg) | Nutanix Flow Management APIs | v4.0 | v4.3\* | v4.3\* | 33 |  |
| [`monitoring`](#monitoring) | Nutanix Monitoring APIs | v4.0 | v4.3\* | v4.3\* | 23 |  |
| [`multidomain`](#multidomain) | Nutanix Multidomain Versioned APIs | — | v4.3\* | v4.3\* | 14 | v4.4.b1 |
| [`networking`](#networking) | Nutanix Networking APIs | v4.0 | v4.3\* | v4.4 | 123 |  |
| [`objects`](#objects) | Nutanix Objects Storage Management APIs | v4.0 | v4.0 | v4.1 | 17 |  |
| [`opsmgmt`](#opsmgmt) | Nutanix Cloud Management Platform APIs | v4.0 | v4.0 | v4.0 | 17 | v4.1.b1 |
| [`prism`](#prism) | Nutanix Prism APIs | v4.0 | v4.3\* | v4.4 | 41 |  |
| [`security`](#security) | Nutanix Security APIs | — | v4.1 | v4.2 | 27 |  |
| [`storage`](#storage) | Nutanix Storage APIs | — | — | — | 0 | v4.0.a3 |
| [`tenancy`](#tenancy) | SP Central Tenant Management | — | — | — | 0 | v4.0.a1 |
| [`vmm`](#vmm) | Nutanix Virtual Machine Management APIs | v4.0 | v4.2 | v4.3 | 192 |  |
| [`volumes`](#volumes) | Nutanix Volumes APIs | v4.0 | v4.3\* | v4.3\* | 30 |  |

## aiops

**Nutanix AIOps APIs** — versions GA : v4.0 ; pré-versions : v4.2.b1

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0)

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Metrics** | | | | | | |
| `GET` | `/aiops/{v}/config/sources` | getSourcesV4 | Get a list of available sources | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/sources/{sourceExtId}/entity-descriptors` | getEntityDescriptorsV4 | Get entity and metrics descriptors | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/sources/{sourceExtId}/entity-types` | getEntityTypesV4 | Get a list of available entity types for a given source | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/stats/sources/{sourceExtId}/entities/{extId}` | getEntityMetricsV4 | Get attribute/metric data for the selected entities | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Scenarios** | | | | | | |
| `GET` | `/aiops/{v}/config/scenarios` | listScenarios | Get a list of capacity planning scenarios | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/aiops/{v}/config/scenarios` | createScenario | Create a capacity planning scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/aiops/{v}/config/scenarios/{extId}` | deleteScenarioById | Delete a capacity planning scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/scenarios/{extId}` | getScenarioById | Get a single capacity planning scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/aiops/{v}/config/scenarios/{extId}` | updateScenarioById | Update a capacity planning scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/aiops/{v}/config/scenarios/{extId}/$actions/generate-recommendation` | generateRecommendation | Generate recommendation for a capacity planning scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/aiops/{v}/config/scenarios/{extId}/$actions/generate-report` | generateReport | Generate a report for a planned capacity scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/aiops/{v}/config/scenarios/{extId}/$actions/generate-runway` | generateRunway | Generate runway for a planned capacity scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/scenarios/{scenarioExtId}/reports` | getScenarioReport | Get the generated report for a planned capacity scenario | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/simulations` | listSimulations | Get a list of simulations | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/aiops/{v}/config/simulations` | createSimulation | Create a simulation | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/aiops/{v}/config/simulations/{extId}` | deleteSimulationById | Delete a simulation | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/aiops/{v}/config/simulations/{extId}` | getSimulationById | Get a simulation | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/aiops/{v}/config/simulations/{extId}` | updateSimulationById | Update a simulation | 7.0 | v4.0 | v4.0 | v4.0 |

## clustermgmt

**Nutanix Cluster Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5, v4.3 → pc.7.6, v4.4 → pc.7.6\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Bmc** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{extId}/bmc-info` | getBmcInfo | Get BMC details | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{extId}/bmc-info` | updateBmcInfo | Update BMC info summary | 7.0 | v4.0 | v4.2 | v4.4 |
| | **CertificateManager** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificate-authorities` | listCertificateAuthoritiesByClusterId | List of Certificate Authorities | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificate-authorities` | createCertificateAuthorityByClusterId | Add Certificate Authorities | 7.6 | — | — | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificate-authorities/{extId}` | deleteCertificateAuthorityById | Delete a Certificate Authority (CA) | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificate-authorities/{extId}` | getCertificateAuthorityById | Get details of a Certificate Authority (CA) | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificates` | listCertificatesByClusterId | List of Certificates on the cluster | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificates` | createCertificateByClusterId | Add Certificates to the cluster | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/certificates/{extId}` | getCertificateById | Get details of a Certificate | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/csrs` | listCsrsByClusterId | List of Certificate Signing Requests | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/csrs` | createCsrByClusterId | Generate a Certificate Signing Request (CSR) | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/csrs/{csrExtId}/file` | downloadCsrById | Download a Certificate Signing Request (CSR) | 7.6 | — | — | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/csrs/{extId}` | deleteCsrById | Delete a Certificate Signing Request (CSR) | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/csrs/{extId}` | getCsrById | Get details of a Certificate Signing Request (CSR) | 7.6 | — | — | v4.4 |
| | **ClusterProfiles** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/cluster-profiles` | listClusterProfiles | List cluster profiles | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/cluster-profiles` | createClusterProfile | Create a cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/cluster-profiles/{extId}` | deleteClusterProfileById | Delete cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/cluster-profiles/{extId}` | getClusterProfileById | Get cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/cluster-profiles/{extId}` | updateClusterProfileById | Update cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/cluster-profiles/{extId}/$actions/apply` | applyClusterProfile | Apply cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/cluster-profiles/{extId}/$actions/disassociate-cluster` | disassociateClusterFromClusterProfile | Disassociate cluster from a cluster profile | 7.0 | v4.0 | v4.2 | v4.4 |
| | **Clusters** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters` | listClusters | Get the list of clusters | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters` | createCluster | Create a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/associate-categories` | associateCategoriesToCluster | Associate categories to the cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/check-hypervisor-requirements` | checkHypervisorRequirements | Get hypervisor ISO upload information | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/compute-non-migratable-vms` | computeNonMigratableVms | Compute non-migratable VMs | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/disassociate-categories` | disassociateCategoriesFromCluster | Disassociate categories from the cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/discover-unconfigured-nodes` | discoverUnconfiguredNodes | Discover unconfigured nodes | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/expand-cluster` | expandCluster | Add node on a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/fetch-node-networking-details` | fetchNodeNetworkingDetails | Get network information of unconfigured nodes | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/remove-node` | removeNode | Remove nodes from the cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/validate-node` | validateNode | Validates hypervisor bundle and node uplinks | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/cvms` | listCvmsbyClusterId | Get a list of CVMs associated with a cluster | 7.5 | — | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/cvms/$actions/reconfigure` | reconfigureCvms | Reconfigure CVMs within a cluster | 7.5 | — | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/cvms/{extId}` | getCvmById | Get the details of a specific CVM associated with a cluster | 7.5 | — | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/cvms/{extId}` | updateCvmById | Update configuration of a specific CVM associated with a cluster | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts` | listHostsByClusterId | Get the list of hosts associated with a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{extId}` | getHostById | Get the details of host associated with the cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{hostExtId}/host-nics` | listHostNicsByHostId | Get the list of host NICs | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{hostExtId}/host-nics/{extId}` | getHostNicById | Get host NIC | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{hostExtId}/virtual-nics` | listVirtualNicsByHostId | Get the list of virtual NICs | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/hosts/{hostExtId}/virtual-nics/{extId}` | getVirtualNicById | Get virtual NIC | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ip-pools` | listIpPoolsByClusterId | Get IP Pool configurations of a cluster | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ip-pools` | createIpPoolByClusterId | Create IP Pool | 7.6 | — | — | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ip-pools/{extId}` | deleteIpPoolById | Delete IP Pool configuration | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ip-pools/{extId}` | getIpPoolById | Get IP Pool configuration | 7.6 | — | — | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ip-pools/{extId}` | updateIpPoolById | Update IP Pool configuration | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/network-segments` | listNetworkSegmentsByClusterId | Get Network Segment configuration of a cluster | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/network-segments` | createNetworkSegmentByClusterId | Create a new Network Segment configuration | 7.6 | — | — | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/network-segments/{extId}` | deleteNetworkSegmentById | Delete Network Segment configuration | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/network-segments/{extId}` | getNetworkSegmentById | Get Network Segment configuration | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/non-migratable-vms-result/{extId}` | getNonMigratableVmsResultById | Get the details of non-migratable VMs | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/physical-gpu-profiles` | listPhysicalGpuProfiles ⚠️ | List Physical GPU profiles. | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rackable-units` | listRackableUnitsByClusterId | Get the list of rackable units | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rackable-units/{extId}` | getRackableUnitById | Get the rackable unit details | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rsyslog-servers` | listRsyslogServersByClusterId | Get the list of RSYSLOG server configurations | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rsyslog-servers` | createRsyslogServer | Add RSYSLOG server configuration | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rsyslog-servers/{extId}` | deleteRsyslogServerById | Delete RSYSLOG server configuration | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rsyslog-servers/{extId}` | getRsyslogServerById | Get RSYSLOG server configuration | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/rsyslog-servers/{extId}` | updateRsyslogServerById | Update RSYSLOG server configuration | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp` | getSnmpConfigByClusterId | Get SNMP config details of a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/$actions/add-transports` | addSnmpTransport | Add SNMP transport ports and protocol details | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/$actions/remove-transports` | removeSnmpTransport | Remove SNMP transport ports and protocol details | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/$actions/update-status` | updateSnmpStatus | Update SNMP status | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/traps` | createSnmpTrap | Add SNMP trap | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/traps/{extId}` | deleteSnmpTrapById | Delete SNMP trap | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/traps/{extId}` | getSnmpTrapById | Get SNMP trap configuration details | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/traps/{extId}` | updateSnmpTrapById | Update SNMP trap | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/users` | createSnmpUser | Add SNMP user | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/users/{extId}` | deleteSnmpUserById | Delete SNMP user | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/users/{extId}` | getSnmpUserById | Get SNMP user information | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/snmp/users/{extId}` | updateSnmpUserById | Update SNMP user | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/virtual-gpu-profiles` | listVirtualGpuProfiles ⚠️ | List Virtual GPU profiles. | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/clusters/{extId}` | deleteClusterById | Delete a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{extId}` | getClusterById | Get details of a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{extId}` | updateClusterById | Update cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/host-nics` | listHostNics | Lists all host NICs | ? | — | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/hosts` | listHosts | Get the list of all host entities | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/task-response/{extId}` | fetchTaskResponse | Get task response based on the type of request | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/operations/clusters/{clusterExtId}/hosts/{extId}/$actions/enter-host-maintenance` | enterHostMaintenance | Enter host into maintenance mode | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/operations/clusters/{clusterExtId}/hosts/{extId}/$actions/exit-host-maintenance` | exitHostMaintenance | Exit host from maintenance mode | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/stats/clusters/{clusterExtId}/hosts/{extId}` | getHostStats | Get host statistics | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/stats/clusters/{extId}` | getClusterStats | Get cluster statistics | 7.0 | v4.0 | v4.2 | v4.4 |
| | **Disks** | | | | | | |
| `POST` | `/clustermgmt/{v}/config/clusters/{extId}/$actions/add-disk` | addDisk | Adds Disk to a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/disks` | listDisks | Get Disks for all the clusters | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/disks/{extId}` | deleteDiskById | Removes Disk from a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/disks/{extId}` | getDiskById | Get Disk by its external identifier | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/disks/{extId}/$actions/update-led-state` | updateDiskLEDState | Update LED state of a Disk | 7.3 | — | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/stats/disks/{extId}` | getDiskStats | Get stats for the existing Disk | 7.0 | v4.0 | v4.2 | v4.4 |
| | **Encryption** | | | | | | |
| `POST` | `/clustermgmt/{v}/config/clusters/$actions/prepare-encryption-keys-backup` | prepareEncryptionKeysBackup | Prepare encryption key backup for the specified cluster(s). | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/rotate-encryption-keys` | rotateEncryptionKeys | Rotate the encryption key on a cluster. | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/encryption-config` | getEncryptionConfig | Get the encryption configuration for a cluster. | 7.6 | — | — | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/encryption-config` | updateEncryptionConfig | Configure encryption on a cluster. | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/encryption-keys-backup/{extId}` | downloadEncryptionKeysBackup | Download encryption key backup for the cluster(s). | 7.6 | — | — | v4.4 |
| | **External Storages** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/external-storages` | listExternalStorages | List External Storages | 7.6 | — | — | v4.4 |
| `POST` | `/clustermgmt/{v}/config/external-storages` | createExternalStorage | Create an External Storage | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/config/external-storages/{extId}` | getExternalStorageById | Get External Storage by ID | 7.6 | — | — | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/external-storages/{extId}` | updateExternalStorageById | Update External Storage by ID | 7.6 | — | — | v4.4 |
| | **GpuProfiles** | | | | | | |
| `GET` | `/clustermgmt/{v}/ahv/config/physical-gpu-profiles` | listAhvPhysicalGpuProfiles | Get a list of physical GPU profiles | 7.6 | — | — | v4.4 |
| `GET` | `/clustermgmt/{v}/ahv/config/virtual-gpu-profiles` | listAhvVirtualGpuProfiles | Get a list of virtual GPU profiles | 7.6 | — | — | v4.4 |
| | **PasswordManager** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/system-user-passwords` | listSystemUserPasswords | List password status of system users | 7.3 | — | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/system-user-passwords/{extId}/$actions/change-password` | changeSystemUserPasswordById | Initiate password update for a system user | 7.3 | — | v4.2 | v4.4 |
| | **PcieDevices** | | | | | | |
| `GET` | `/clustermgmt/{v}/ahv/config/pcie-devices` | listPcieDevices | Fetch the PCIe devices | 7.0 | v4.0 | v4.2 | v4.4 |
| | **SSLCertificate** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ssl-certificate` | getSSLCertificate | Get SSL certificate details for a specified cluster | 7.3 | — | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/ssl-certificate` | updateSSLCertificate | Update the SSL certificate for a specific cluster | 7.3 | — | v4.2 | v4.4 |
| | **Storage Config** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/storage-config` | getStorageConfig | Get Storage Configuration | 7.6 | — | — | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/storage-config` | updateStorageConfig | Update Storage Configuration | 7.6 | — | — | v4.4 |
| | **StorageContainers** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/storage-containers/datastores` | listDataStoresByClusterId | List datastores of a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/storage-containers` | listStorageContainers | List Storage Containers | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/storage-containers` | createStorageContainer | Create a Storage Container | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/clustermgmt/{v}/config/storage-containers/{extId}` | deleteStorageContainerById | Delete a Storage Container | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/storage-containers/{extId}` | getStorageContainerById | Get Storage Container configuration | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/clustermgmt/{v}/config/storage-containers/{extId}` | updateStorageContainerById | Update a Storage Container | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/storage-containers/{extId}/$actions/clear-thick-provisioned-space` | clearThickProvisionedSpace | Clear thick provision for a Storage Container | 7.3 | — | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/storage-containers/{extId}/$actions/mount` | mountStorageContainer | Mount Storage Container on ESX datastore | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/storage-containers/{extId}/$actions/unmount` | unmountStorageContainer | Unmount Storage Container from ESX datastore | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/stats/storage-containers/{extId}` | getStorageContainerStats | Get Stats for a Storage Container | 7.0 | v4.0 | v4.2 | v4.4 |
| | **VcenterExtensions** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/vcenter-extensions` | listVcenterExtensions | List vCenter server extensions. | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/clustermgmt/{v}/config/vcenter-extensions/{extId}` | getVcenterExtensionById | Get vCenter server extension. | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/vcenter-extensions/{extId}/$actions/register` | registerVcenterExtension | Register vCenter server extension. | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/vcenter-extensions/{extId}/$actions/unregister` | unregisterVcenterExtension | Unregister vCenter server extension. | 7.0 | v4.0 | v4.2 | v4.4 |

## datapolicies

**Nutanix Data Policies APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5, v4.3 → pc.7.5\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **EntitySyncPolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/entity-sync-policies` | listEntitySyncPolicies | List entity sync policies | 7.3 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/entity-sync-policies/{extId}` | getEntitySyncPolicyById | Get an entity sync policy | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/entity-sync-policies/{extId}/$actions/sync-entity` | syncEntitySyncPolicyById | Sync entity identified by its identifier to a remote domain manager | 7.3 | — | v4.3 | v4.3 |
| | **ProtectionPolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/protection-policies` | listProtectionPolicies | List protection policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/protection-policies` | createProtectionPolicy | Create a protection policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/protection-policies/{extId}` | deleteProtectionPolicyById | Delete a protection policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{extId}` | getProtectionPolicyById | Get a protection policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/protection-policies/{extId}` | updateProtectionPolicyById | Update a protection policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules` | listConsistencyRulesByProtectionPolicyId | List consistency rules | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules` | createConsistencyRule | Create a consistency rule | 7.3 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | deleteConsistencyRuleById | Delete a consistency rule | 7.3 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | getConsistencyRuleById | Get details of a consistency rule | 7.3 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | updateConsistencyRuleById | Update a consistency rule | 7.3 | — | v4.3 | v4.3 |
| | **RecoveryPlans** | | | | | | |
| `GET` | `/datapolicies/{v}/config/recovery-plans` | listRecoveryPlans | List Recovery Plans | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans` | createRecoveryPlan | Create a Recovery Plan | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{extId}` | deleteRecoveryPlanById | Delete a Recovery Plan | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{extId}` | getRecoveryPlanById | Get a Recovery Plan | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{extId}` | updateRecoveryPlanById | Update a Recovery Plan | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings` | listDataServicesIpMappings | List Data Services IP Mappings | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings` | createDataServicesIpMapping | Create a Data Services IP Mapping | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | deleteDataServicesIpMappingById | Delete a Data Services IP Mapping | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | getDataServicesIpMappingById | Get a Data services IP mapping | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | updateDataServicesIpMappingById | Update a Data Services IP Mapping | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings` | listNetworkMappings | List Network Mappings | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings` | createNetworkMapping | Create a Network Mapping | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | deleteNetworkMappingById | Delete a Network Mapping | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | getNetworkMappingById | Get a Network Mapping | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | updateNetworkMappingById | Update a Network Mapping | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings` | listRecoverySettings | List custom recovery settings | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings` | createRecoverySetting | Create a custom recovery setting for VM or Volume Groups. | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | deleteRecoverySettingById | Delete recovery setting | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | getRecoverySettingById | Get the custom recovery setting | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | updateRecoverySettingById | Update recovery setting | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages` | listRecoveryStages | List Recovery stages | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages` | createRecoveryStage | Create a Recovery stage | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | deleteRecoveryStageById | Delete Recovery stage | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | getRecoveryStageById | Get a Recovery stage | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | updateRecoveryStageById | Update a Recovery stage | 7.5 | — | v4.3 | v4.3 |
| | **StoragePolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/storage-policies` | listStoragePolicies | Get a list of Storage Policies | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/datapolicies/{v}/config/storage-policies` | createStoragePolicy | Create a Storage Policy | 7.3 | — | v4.3 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/storage-policies/{extId}` | deleteStoragePolicyById | Delete an existing Storage Policy | 7.3 | — | v4.3 | v4.3 |
| `GET` | `/datapolicies/{v}/config/storage-policies/{extId}` | getStoragePolicyById | Get a Storage Policy based on external identifier | 7.3 | — | v4.3 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/storage-policies/{extId}` | updateStoragePolicyById | Update an existing Storage Policy | 7.3 | — | v4.3 | v4.3 |

## dataprotection

**Nutanix Data Protection APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3\*, v4.2 → pc.7.5, v4.3 → pc.7.5\*, v4.4 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **DataProtectionClusterCapabilities** | | | | | | |
| `GET` | `/dataprotection/{v}/config/cluster-capabilities` | listDataProtectionClusterCapabilities | Get data protection cluster capabilities | 7.5 | — | v4.3 | v4.4 |
| | **ProtectedResources** | | | | | | |
| `GET` | `/dataprotection/{v}/config/protected-resources/{extId}` | getProtectedResourceById | Get a protected resource | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/protected-resources/{extId}/$actions/promote` | promoteProtectedResource | Promote protected resource | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/protected-resources/{extId}/$actions/restore` | restoreProtectedResource | Restore protected resource | 7.0 | v4.0 | v4.3 | v4.4 |
| | **RecoveryPlanActions** | | | | | | |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/clean-up-resources` | cleanupRecoveryPlanResources | Cleanup resources on the last Recovery Plan execution | 7.5 | — | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/planned-failover` | plannedFailoverRecoveryPlan | Planned Failover Recovery Plan | 7.5 | — | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/resume-protection` | resumeProtection | Resume Protection on Recovery Plan | 7.6 | — | — | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/test-failover` | testFailoverRecoveryPlan | Test Failover Recovery Plan | 7.5 | — | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/unplanned-failover` | unplannedFailoverRecoveryPlan | Unplanned Failover Recovery Plan | 7.5 | — | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/validate` | validateRecoveryPlan | Validate Recovery Plan | 7.5 | — | v4.3 | v4.4 |
| | **RecoveryPlanJobs** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs` | listRecoveryPlanJobs | List Recovery Plan Jobs | 7.5 | — | v4.3 | v4.4 |
| `DELETE` | `/dataprotection/{v}/config/recovery-plan-jobs/{extId}` | deleteRecoveryPlanJobById | Delete Recovery Plan Job | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{extId}` | getRecoveryPlanJobById | Get Recovery Plan Job | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{recoveryPlanJobExtId}/execution-steps` | listExecutionStepsByRecoveryPlanJobId | List Recovery Plan Job Execution Steps | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{recoveryPlanJobExtId}/validation-errors` | listValidationErrorsByRecoveryPlanJobId | List Recovery Plan Job Validation Errors | 7.5 | — | v4.3 | v4.4 |
| | **RecoveryPointStores** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-point-stores` | listRecoveryPointStores | List recovery point stores | 7.6 | — | — | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-point-stores/{extId}` | getRecoveryPointStoreById | Get a recovery point store. | 7.6 | — | — | v4.4 |
| | **RecoveryPoints** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-points` | listRecoveryPoints | List recovery points | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points` | createRecoveryPoint | Create a recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/dataprotection/{v}/config/recovery-points/{extId}` | deleteRecoveryPointById | Delete a recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-points/{extId}` | getRecoveryPointById | Get a recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/discover-cluster` | discoverClusterForRecoveryPointId | Discover cluster info for a recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/replicate` | replicateRecoveryPoint | Replicate a recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/restore` | restoreRecoveryPoint | Restore recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/set-expiration-time` | setRecoveryPointExpirationTime | Set the expiration time of the recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-points/{recoveryPointExtId}/vm-recovery-points/{extId}` | getVmRecoveryPointById | Get a VM recovery point | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/vm-recovery-points/{vmRecoveryPointExtId}/disk-recovery-points/{extId}/$actions/compute-changed-regions` | vmRecoveryPointComputeChangedRegions | Compute VM recovery points changed regions | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/vm-recovery-points/{vmRecoveryPointExtId}/vss-metadata` | getVssMetadataByVmRecoveryPointId | Get VSS metadata by VM recovery point ID | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/volume-group-recovery-points/{volumeGroupRecoveryPointExtId}/disk-recovery-points/{extId}/$actions/compute-changed-regions` | volumeGroupRecoveryPointComputeChangedRegions | Compute Volume Group recovery points changed regions | 7.0 | v4.0 | v4.3 | v4.4 |

## files

**Nutanix Files APIs** — versions GA : v4.0 ; pré-versions : v4.0.a2

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0)

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Analytics** | | | | | | |
| `GET` | `/files/{v}/stats/file-servers/{extId}` | getFileServerStats | Get File server statistics | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/stats/file-servers/{fileServerExtId}/anti-virus-servers/{extId}` | getAntivirusServerStats | Get antivirus statistics | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/stats/file-servers/{fileServerExtId}/mount-targets/{extId}` | getMountTargetStats | Get mount target statistics | 7.0 | v4.0 | v4.0 | v4.0 |
| | **AntivirusServers** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers` | listAntivirusServers | List antivirus servers | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers` | createAntivirusServer | Create antivirus server | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers/{extId}` | deleteAntivirusServerById | Delete antivirus server | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers/{extId}` | getAntivirusServerById | Get antivirus server by external identifier | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers/{extId}` | updateAntivirusServerById | Update antivirus server | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/anti-virus-servers/{extId}/$actions/test-connection` | testConnectionAntivirusServer | Test antivirus server connection | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Dns** | | | | | | |
| `POST` | `/files/{v}/config/file-servers/{extId}/$actions/revise-dns-records` | reviseDnsRecords | Revise DNS records on DNS server | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{extId}/$actions/verify-dns-records` | verifyDnsRecords | Verify DNS records of file server on the DNS server | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/dns-records` | listDnsRecords | List DNS records | 7.0 | v4.0 | v4.0 | v4.0 |
| | **FileServers** | | | | | | |
| `GET` | `/files/{v}/config/file-servers` | listFileServers | List file servers | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{extId}` | getFileServerById | Get file server | 7.0 | v4.0 | v4.0 | v4.0 |
| | **InfectedFiles** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/infected-files` | listInfectedFiles | List infected files | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/infected-files/{extId}` | deleteInfectedFileById | Delete infected file | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/infected-files/{extId}` | getInfectedFileById | Get infected file | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/infected-files/{extId}/$actions/fix` | fixInfectedFile | Manage security of an infected file | 7.0 | v4.0 | v4.0 | v4.0 |
| | **MountTargets** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets` | listMountTargets | List mount targets | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets` | createMountTarget | Create mount target | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}` | deleteMountTargetById | Delete mount target | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}` | getMountTargetById | Get mount target | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}` | updateMountTargetById | Update mount target | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}/$actions/clone` | cloneMountTarget | Clone mount target | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}/$actions/disable-worm-legal-hold` | disableWormLegalHold | Disable WORM legal hold | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}/$actions/enable-worm-compliance` | enableWormCompliance | Enable WORM compliance | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{extId}/$actions/enable-worm-legal-hold` | enableWormLegalHold | Enable WORM legal hold | 7.0 | v4.0 | v4.0 | v4.0 |
| | **NotificationPolicies** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/notification-policies` | listNotificationPolicies | List notification policies | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/notification-policies` | createNotificationPolicy | Create notification policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/notification-policies/{extId}` | deleteNotificationPolicyById | Delete notification policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/notification-policies/{extId}` | getNotificationPolicyById | Get notification policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/notification-policies/{extId}` | updateNotificationPolicyById | Update notification policy | 7.0 | v4.0 | v4.0 | v4.0 |
| | **PartnerServers** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/partner-servers` | listPartnerServers | List partner servers | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/partner-servers` | createPartnerServer | Create partner server | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/partner-servers/{extId}` | deletePartnerServerById | Delete partner server | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/partner-servers/{extId}` | getPartnerServerById | Get partner server | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/partner-servers/{extId}` | updatePartnerServerById | Update partner server | 7.0 | v4.0 | v4.0 | v4.0 |
| | **QuotaPolicies** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/email-config` | getEmailConfig | Get email configuration for the quota policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/email-config` | updateEmailConfig | Update quota policy email configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/quota-policies` | listQuotaPolicies | List quota policies | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/quota-policies` | createQuotaPolicy | Create quota policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/quota-policies/{extId}` | deleteQuotaPolicyById | Delete quota policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/quota-policies/{extId}` | getQuotaPolicyById | Get quota policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/quota-policies/{extId}` | updateQuotaPolicyById | Update quota policy | 7.0 | v4.0 | v4.0 | v4.0 |
| | **RansomwareConfigs** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/ransomware-configs` | listRansomwareConfigs | List ransomware configurations | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/ransomware-configs` | createRansomwareConfig | Create ransomware configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/ransomware-configs/{extId}` | deleteRansomwareConfigById | Delete ransomware configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/ransomware-configs/{extId}` | getRansomwareConfigById | Get ransomware configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/ransomware-configs/{extId}` | updateRansomwareConfigById | Update ransomware configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Recommendations** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/recommendations` | listRecommendations | List recommendations | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/recommendations/{extId}` | deleteRecommendationById | Delete recommendation | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/recommendations/{extId}` | getRecommendationById | Get recommendation | 7.0 | v4.0 | v4.0 | v4.0 |
| | **ReplicationJobs** | | | | | | |
| `GET` | `/files/{v}/operations/replication-jobs` | listReplicationJobs | List data replication jobs | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/operations/replication-jobs/{extId}` | getReplicationJobById | Get data replication job | 7.0 | v4.0 | v4.0 | v4.0 |
| | **ReplicationPolicies** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/replication-policies/{replicationPolicyExtId}/vdi-user-sessions` | listVdiUserSessions | List VDI synchronization all user sessions | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/replication-policies/{replicationPolicyExtId}/vdi-user-sessions/{extId}` | getVdiUserSessionById | Get VDI synchronization user session | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/replication-policies/{replicationPolicyExtId}/vdi-user-sessions/{extId}` | updateVdiUserSessionById | Update VDI synchronization owner file server for the specified user | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/replication-policies` | listReplicationPolicies | List replication policies | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/replication-policies` | createReplicationPolicy | Create replication policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/replication-policies/{extId}` | deleteReplicationPolicyById | Delete replication policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/replication-policies/{extId}` | getReplicationPolicyById | Get replication policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/replication-policies/{extId}` | updateReplicationPolicyById | Update replication policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/operations/$actions/ad-dns-failover` | adDnsFailover | Perform an AD-DNS failover | ? | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/operations/$actions/failover` | failover | Perform data replication failover | ? | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/operations/$actions/resume-replication` | ResumeReplication | Perform resume replication | ? | v4.0 | v4.0 | v4.0 |
| | **SnapshotChangedContents** | | | | | | |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/$actions/compute-snapshot-change` | computeSnapshotChange | Create mount target snapshots changed content | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshot-changed-contents` | listSnapshotChangedContents | List mount target snapshots changed contents | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshot-changed-contents/{extId}` | getSnapshotChangedContentById | Get mount target snapshots changed content | 7.0 | v4.0 | v4.0 | v4.0 |
| | **SnapshotSchedules** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/snapshot-schedules` | listSnapshotSchedules | List snapshot schedules | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/snapshot-schedules` | createSnapshotSchedule | Create snapshot schedule | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/snapshot-schedules/{extId}` | deleteSnapshotScheduleById | Delete snapshot schedule | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/snapshot-schedules/{extId}` | getSnapshotScheduleById | Get snapshot schedule | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/snapshot-schedules/{extId}` | updateSnapshotScheduleById | Update snapshot schedule | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Snapshots** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshots` | listMountTargetSnapshots | List mount target snapshots | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshots` | createMountTargetSnapshot | Create mount target snapshot | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshots/{extId}` | deleteMountTargetSnapshotById | Delete mount target snapshot | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshots/{extId}` | getMountTargetSnapshotById | Get mount target snapshot | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/mount-targets/{mountTargetExtId}/snapshots/{extId}/$actions/restore` | restoreMountTarget | Restore mount target from snapshot | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Tier** | | | | | | |
| `POST` | `/files/{v}/config/file-servers/{extId}/$actions/recalculate-cold-data` | recalculateColdData | Recalculate cold data | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{extId}/$actions/recall-tiered-files` | recallTieredFiles | Recall one or more files | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{extId}/$actions/tier-data` | tierData | Initiate tiering data | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/object-store-profiles` | listObjectStoreProfiles | List object store profiles | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/object-store-profiles` | createObjectStoreProfile | Create object store profile | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/object-store-profiles/{extId}` | getObjectStoreProfileById | Get object store profile | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/object-store-profiles/{extId}` | updateObjectStoreProfileById | Update object store profile | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/tier-configurations` | listTieringConfigurations | List tiering configurations | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/tier-configurations` | createTieringConfiguration | Create tiering configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/tier-configurations/{extId}` | deleteTieringConfigurationById | Delete tiering configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/tier-configurations/{extId}` | getTieringConfigurationById | Get tiering configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/tier-configurations/{extId}` | updateTieringConfigurationById | Update tiering configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| | **UnifiedNamespaces** | | | | | | |
| `GET` | `/files/{v}/config/unified-namespaces` | listUnifiedNamespaces | List unified namespaces | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/unified-namespaces` | createUnifiedNamespace | Create unified namespace | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/unified-namespaces/{extId}` | deleteUnifiedNamespaceById | Delete unified namespace | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/unified-namespaces/{extId}` | getUnifiedNamespaceById | Get unified namespace | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/unified-namespaces/{extId}` | updateUnifiedNamespaceById | Update unified namespace | 7.0 | v4.0 | v4.0 | v4.0 |
| | **UserMappings** | | | | | | |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/$actions/upload-user-mappings` | uploadUserMappings | Upload user mappings | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/user-mappings` | downloadUserMappings | Download user mappings | 7.0 | v4.0 | v4.0 | v4.0 |
| | **VirusScanPolicies** | | | | | | |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/virus-scan-policies` | listVirusScanPolicies | List virus scan policies | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/files/{v}/config/file-servers/{fileServerExtId}/virus-scan-policies` | createVirusScanPolicy | Create virus scan policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/files/{v}/config/file-servers/{fileServerExtId}/virus-scan-policies/{extId}` | deleteVirusScanPolicyById | Delete virus scan policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/files/{v}/config/file-servers/{fileServerExtId}/virus-scan-policies/{extId}` | getVirusScanPolicyById | Get virus scan policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/files/{v}/config/file-servers/{fileServerExtId}/virus-scan-policies/{extId}` | updateVirusScanPolicyById | Update virus scan policy | 7.0 | v4.0 | v4.0 | v4.0 |

**Preview `v4.0.a2`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `GET` | `/files/{v}/config/file-server` | getFileServers | Get file server | ? |
| `PUT` | `/files/{v}/config/file-server` | updateFileServer | Update a file server | ? |
| `POST` | `/files/{v}/config/file-server/$actions/add-dns-entries` | addDnsServer | Add DNS server | ? |
| `POST` | `/files/{v}/config/file-server/$actions/configure-name-services` | configureNameServicesByFileServer | Configure file server name services | ? |
| `POST` | `/files/{v}/config/file-server/$actions/quarantine-infected-files` | quarantineInfectedFiles | Quarantine infected files | ? |
| `POST` | `/files/{v}/config/file-server/$actions/remove-dns-entries` | removeDnsServer | Remove DNS entries | ? |
| `POST` | `/files/{v}/config/file-server/$actions/remove-infected-files` | removeInfectedFiles | Remove infected files | ? |
| `POST` | `/files/{v}/config/file-server/$actions/rescan-infected-files` | rescanInfectedFiles | Rescan infected files | ? |
| `POST` | `/files/{v}/config/file-server/$actions/reset-infected-files` | resetInfectedFiles | Reset infected files | ? |
| `POST` | `/files/{v}/config/file-server/$actions/search-user-mapping` | searchUserMapping | Search a user mapping | ? |
| `POST` | `/files/{v}/config/file-server/$actions/tier-data` | tierData | Initiate tiering data. | ? |
| `POST` | `/files/{v}/config/file-server/$actions/unquarantine-infected-files` | unQuarantineInfectedFiles | Unquarantine infected files request. | ? |
| `POST` | `/files/{v}/config/file-server/$actions/verify-dns-entries` | verifyDnsServer | Verify DNS entries | ? |
| `GET` | `/files/{v}/config/file-server/admin-users` | getAdminUsers | List admin users | ? |
| `POST` | `/files/{v}/config/file-server/admin-users` | createAdminUser | Create admin user | ? |
| `DELETE` | `/files/{v}/config/file-server/admin-users/{adminUserExtId}` | deleteAdminUser | Delete admin user | ? |
| `GET` | `/files/{v}/config/file-server/admin-users/{adminUserExtId}` | getAdminUserByExtId | Get admin user by extId | ? |
| `PUT` | `/files/{v}/config/file-server/admin-users/{adminUserExtId}` | updateAdminUser | Update admin user | ? |
| `GET` | `/files/{v}/config/file-server/anti-virus-servers` | getAntivirusServers | List antivirus servers | ? |
| `POST` | `/files/{v}/config/file-server/anti-virus-servers` | createAntivirusServer | Create antivirus server | ? |
| `DELETE` | `/files/{v}/config/file-server/anti-virus-servers/{antivirusServerExtId}` | deleteAntivirusServer | Delete antivirus server | ? |
| `GET` | `/files/{v}/config/file-server/anti-virus-servers/{antivirusServerExtId}` | getAntivirusServerByExtId | Get antivirus server by extId | ? |
| `PUT` | `/files/{v}/config/file-server/anti-virus-servers/{antivirusServerExtId}` | updateAntivirusServer | Update antivirus server | ? |
| `POST` | `/files/{v}/config/file-server/anti-virus-servers/{antivirusServerExtId}/$actions/test-connection` | testConnectionAntivirusServer | Test antivirus server connection | ? |
| `GET` | `/files/{v}/config/file-server/dns-entries` | getDnsServers | List DNS entries | ? |
| `GET` | `/files/{v}/config/file-server/infected-files` | listInfectedFiles | List of infected files | ? |
| `GET` | `/files/{v}/config/file-server/infected-files/{infectedFileExtId}` | getInfectedFileByExtId | Get infected file by extId | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets` | getAllMountTargets | List all mount targets | ? |
| `POST` | `/files/{v}/config/file-server/mount-targets` | createMountTargets | Create a mount target | ? |
| `DELETE` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}` | deleteMountTargetById | Delete a mount target | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}` | getMountTargetByUuid | Get a mount target by extId | ? |
| `PUT` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}` | updateMountTargets | Update a mount target | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/files` | getFileByInodeGenId | Get the mimetype of files for the given inode genId pair. | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/quota-policies` | getQuotaPolicies | List all quota policies | ? |
| `POST` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/quota-policies` | createQuotaPolicy | Create a quota policy | ? |
| `DELETE` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/quota-policies/{quotaPolicyExtId}` | deleteQuotaPolicy | Delete a quota policy | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/quota-policies/{quotaPolicyExtId}` | getQuotaPolicyByExtId | Get a quota policy by extId | ? |
| `PUT` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/quota-policies/{quotaPolicyExtId}` | updateQuotaPolicy | Update a quota policy. | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/snapshots` | getMountTargetSnapshots | List mount target snapshots | ? |
| `DELETE` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/snapshots/{snapshotExtId}` | deleteMountTargetSnapshot | Delete mount target snapshot | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/snapshots/{snapshotExtId}` | getMountTargetSnapshotByExtId | Get mount target snapshot for the provided extId | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/virus-scan-policy` | listMountTargetVirusScanPolicy | List mount target virus scan policies | ? |
| `POST` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/virus-scan-policy` | createMountTargetVirusScanPolicy | Create a mount target virus scan policy | ? |
| `DELETE` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/virus-scan-policy/{virusScanPolicyExtId}` | deleteMountTargetVirusScanPolicy | Delete a mount target virus scan policy | ? |
| `GET` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/virus-scan-policy/{virusScanPolicyExtId}` | getMountTargetVirusScanPolicy | Get a mount target virus scan policy | ? |
| `PUT` | `/files/{v}/config/file-server/mount-targets/{mountTargetExtId}/virus-scan-policy/{virusScanPolicyExtId}` | updateMountTargetVirusScanPolicy | Update a mount target virus scan policy | ? |
| `GET` | `/files/{v}/config/file-server/name-services` | getNameServicesByFileServer | Name services by file server | ? |
| `GET` | `/files/{v}/config/file-server/networks` | getNetworks | Get networks | ? |
| `POST` | `/files/{v}/config/file-server/networks` | createNetwork | Create a network | ? |
| `DELETE` | `/files/{v}/config/file-server/networks/{extId}` | deleteNetwork | Delete a network | ? |
| `GET` | `/files/{v}/config/file-server/networks/{extId}` | getNetworkByExtId | Get network by extId | ? |
| `GET` | `/files/{v}/config/file-server/object-store/profiles/{profileExtId}` | getObjectStoreProfile | Get object store profile | ? |
| `PUT` | `/files/{v}/config/file-server/object-store/profiles/{profileExtId}` | UpdateObjectStoreProfile | Update object store profile | ? |
| `GET` | `/files/{v}/config/file-server/quota-email-config` | getQuotaEmailConfig | Get the quota policy email configuration | ? |
| `PUT` | `/files/{v}/config/file-server/quota-email-config` | updateQuotaEmailConfig | Update the quota policy email configuration | ? |
| `GET` | `/files/{v}/config/file-server/ssr-snapshot-schedules` | getSsrSnapshotSchedules | List SSR snapshot schedules | ? |
| `POST` | `/files/{v}/config/file-server/ssr-snapshot-schedules` | createSsrSnapshotSchedule | Create a SSR snapshot schedule | ? |
| `DELETE` | `/files/{v}/config/file-server/ssr-snapshot-schedules/{ssrSnapshotScheduleExtId}` | deleteSsrSnapshotSchedule | Delete SSR snapshot schedule | ? |
| `GET` | `/files/{v}/config/file-server/ssr-snapshot-schedules/{ssrSnapshotScheduleExtId}` | getSsrSnapshotScheduleByExtId | Get SSR snapshot schedule by extId | ? |
| `PUT` | `/files/{v}/config/file-server/ssr-snapshot-schedules/{ssrSnapshotScheduleExtId}` | updateSsrSnapshotSchedule | Update SSR snapshot schedule | ? |
| `GET` | `/files/{v}/config/file-server/tier-config` | getTieringConfigList | Get list of the tiering configuration. | ? |
| `POST` | `/files/{v}/config/file-server/tier-config` | createTieringConfig | Create the tiering configuration. | ? |
| `DELETE` | `/files/{v}/config/file-server/tier-config/{extId}` | deleteTieringConfig | Delete the tiering configuration. | ? |
| `GET` | `/files/{v}/config/file-server/tier-config/{extId}` | getTieringConfig | Get the tiering configuration. | ? |
| `PUT` | `/files/{v}/config/file-server/tier-config/{extId}` | updateTieringConfig | Update the tiering configuration. | ? |
| `GET` | `/files/{v}/config/file-server/tier-policies` | getTieringPolicies | List tiering policies | ? |
| `POST` | `/files/{v}/config/file-server/tier-policies` | createTieringPolicy | Create a tiering policy. | ? |
| `DELETE` | `/files/{v}/config/file-server/tier-policies/{extId}` | deleteTieringPolicy | Delete a tiering policy | ? |
| `GET` | `/files/{v}/config/file-server/tier-policies/{extId}` | getTieringPolicyById | Get a tiering policy by extId | ? |
| `PUT` | `/files/{v}/config/file-server/tier-policies/{extId}` | updateTieringPolicy | Update a tiering policy | ? |
| `GET` | `/files/{v}/config/file-server/user-mapping` | getUserMapping | Get a user mapping | ? |
| `POST` | `/files/{v}/config/file-server/user-mapping` | createUserMapping | Create a user mapping | ? |
| `PUT` | `/files/{v}/config/file-server/user-mapping` | updateUserMapping | Update a user mapping | ? |
| `GET` | `/files/{v}/config/file-server/users` | getFileServerUsers | List all the file server users | ? |
| `POST` | `/files/{v}/config/file-server/users` | createFileServerUser | Create a file server user | ? |
| `DELETE` | `/files/{v}/config/file-server/users/{fileServerUserExtId}` | deleteFileServerUser | Delete file server user | ? |
| `GET` | `/files/{v}/config/file-server/users/{fileServerUserExtId}` | getFileServerUserByExtId | Get file server user by extId | ? |
| `PUT` | `/files/{v}/config/file-server/users/{fileServerUserExtId}` | updateFileServerUser | Update file server user | ? |
| `GET` | `/files/{v}/config/file-server/virus-scan-policy` | listVirusScanPolicy | List virus scan policies | ? |
| `POST` | `/files/{v}/config/file-server/virus-scan-policy` | createVirusScanPolicy | Create a virus scan policy | ? |
| `GET` | `/files/{v}/config/file-server/virus-scan-policy/{virusScanPolicyExtId}` | getVirusScanPolicy | Get a virus scan policy | ? |
| `PUT` | `/files/{v}/config/file-server/virus-scan-policy/{virusScanPolicyExtId}` | updateVirusScanPolicy | Update a virus scan policy | ? |
| `GET` | `/files/{v}/stats/file-server` | getFileServerStats | Get File server stats | ? |
| `GET` | `/files/{v}/stats/file-server/anti-virus-servers/{antivirusServerExtId}` | getAntivirusServerStats | Get Antivirus Stats | ? |
| `GET` | `/files/{v}/stats/file-server/mount-targets/{mountTargetExtId}` | getMountTargetStats | Get Mount target stats | ? |

## iam

**Nutanix Identity and Access Management APIs** — versions GA : v4.0 ; pré-versions : v4.1.b3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0)

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **AuthorizationPolicies** | | | | | | |
| `GET` | `/iam/{v}/authz/authorization-policies` | listAuthorizationPolicies | Lists all the authorization policies | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authz/authorization-policies` | createAuthorizationPolicy | Create authorization policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authz/authorization-policies/{extId}` | deleteAuthorizationPolicyById | Delete authorization policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authz/authorization-policies/{extId}` | getAuthorizationPolicyById | Get authorization policy | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authz/authorization-policies/{extId}` | updateAuthorizationPolicyById | Update authorization policy | 7.0 | v4.0 | v4.0 | v4.0 |
| | **CertificateAuthenticationProviders** | | | | | | |
| `GET` | `/iam/{v}/authn/cert-auth-providers` | listCertAuthProviders | Lists all configured certificate-based authentication providers | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/cert-auth-providers` | createCertAuthProvider | Create certificate-based authentication provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/cert-auth-providers/{extId}` | deleteCertAuthProviderById | Delete certificate-based authentication provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/cert-auth-providers/{extId}` | getCertAuthProviderById | Get certificate-based authentication provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authn/cert-auth-providers/{extId}` | updateCertAuthProviderById | Update certificate-based authentication provider | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Clients** | | | | | | |
| `GET` | `/iam/{v}/authz/clients/{extId}` | getRegisteredClientById | Get client | 7.0 | v4.0 | v4.0 | v4.0 |
| | **DirectoryServices** | | | | | | |
| `GET` | `/iam/{v}/authn/directory-services` | listDirectoryServices | List directory services | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/directory-services` | createDirectoryService | Create directory service | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/directory-services/{extId}` | deleteDirectoryServiceById | Delete directory service | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/directory-services/{extId}` | getDirectoryServiceById | Get directory service | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authn/directory-services/{extId}` | updateDirectoryServiceById | Update directory service | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/directory-services/{extId}/$actions/search` | searchDirectoryService | Search user/group in directory service | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/directory-services/{extId}/$actions/verify-connection-status` | connectionStatusDirectoryService | Check directory service connection | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Entities** | | | | | | |
| `GET` | `/iam/{v}/authz/entities` | listEntities | List entities | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authz/entities/{extId}` | getEntityById | Get entity | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Operations** | | | | | | |
| `GET` | `/iam/{v}/authz/operations` | listOperations | List operation(s) | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authz/operations/{extId}` | getOperationById | Get operation | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Roles** | | | | | | |
| `GET` | `/iam/{v}/authz/roles` | listRoles | List role(s) | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authz/roles` | createRole | Create role | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authz/roles/{extId}` | deleteRoleById | Delete role | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authz/roles/{extId}` | getRoleById | Get role | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authz/roles/{extId}` | updateRoleById | Update role | 7.0 | v4.0 | v4.0 | v4.0 |
| | **SAMLIdentityProviders** | | | | | | |
| `GET` | `/iam/{v}/authn/saml-identity-providers` | listSamlIdentityProviders | List SAML identity providers | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/saml-identity-providers` | createSamlIdentityProvider | Create SAML identity provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/saml-identity-providers/{extId}` | deleteSamlIdentityProviderById | Delete SAML identity provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/saml-identity-providers/{extId}` | getSamlIdentityProviderById | Get SAML identity provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authn/saml-identity-providers/{extId}` | updateSamlIdentityProviderById | Update SAML identity provider | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/saml-sp-metadata` | getSamlSpMetadata | Get SP-Metadata for SAML identity provider | 7.0 | v4.0 | v4.0 | v4.0 |
| | **UserGroups** | | | | | | |
| `GET` | `/iam/{v}/authn/user-groups` | listUserGroups | List user groups | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/user-groups` | createUserGroup | Create user group | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/user-groups/{extId}` | deleteUserGroupById | Delete user group | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/user-groups/{extId}` | getUserGroupById | Get user group | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Users** | | | | | | |
| `GET` | `/iam/{v}/authn/users` | listUsers | List user(s) | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users` | createUser | Create user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/$actions/change-password` | changeUserPassword | Change password of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/users/{extId}` | getUserById | Get user | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/iam/{v}/authn/users/{extId}` | updateUserById | Update user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{extId}/$actions/change-state` | updateUserState | Update active state of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{extId}/$actions/reset-password` | resetUserPassword | Reset user password | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/users/{userExtId}/buckets-access-keys` | listUserBucketKeys ⚠️ | List bucket access keys of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{userExtId}/buckets-access-keys` | createBucketAccessKey ⚠️ | Create bucket access key for user | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/users/{userExtId}/buckets-access-keys/{extId}` | deleteUserBucketKeyById ⚠️ | Delete buckets access key of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/users/{userExtId}/buckets-access-keys/{extId}` | getUserBucketKeyById ⚠️ | Get bucket access key of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{userExtId}/buckets-access-keys/{extId}/$actions/revoke` | revokeUserBucketAccessKey ⚠️ | Revoke bucket access key of user | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/users/{userExtId}/keys` | listUserKeys | List keys for the user | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{userExtId}/keys` | createUserKey | Create a key of the requested key type for a user | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/iam/{v}/authn/users/{userExtId}/keys/{extId}` | deleteUserKeyById | Delete the requested key | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/iam/{v}/authn/users/{userExtId}/keys/{extId}` | getUserKeyById | Get the requested key | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/iam/{v}/authn/users/{userExtId}/keys/{extId}/$actions/revoke` | revokeUserKey | Revoke the requested key | 7.0 | v4.0 | v4.0 | v4.0 |

**Preview `v4.1.b3`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `POST` | `/iam/{v}/authn/config/directory-service/{extId}/$actions/share` | shareDirectoryService | Share directory service with projects | 7.6 |
| `POST` | `/iam/{v}/authn/config/directory-service/{extId}/$actions/share-all` | shareAllDirectoryService | Share directory service with all projects | 7.6 |
| `POST` | `/iam/{v}/authn/config/directory-service/{extId}/$actions/unshare` | unshareDirectoryService | Unshare directory service from a project | 7.6 |
| `POST` | `/iam/{v}/authn/config/directory-service/{extId}/$actions/unshare-all` | unshareAllDirectoryService | Unshare directory service from all projects | 7.6 |
| `POST` | `/iam/{v}/authn/config/saml-identity-provider/{extId}/$actions/share` | shareSamlIdentityProvider | Share SAML identity provider with projects | 7.6 |
| `POST` | `/iam/{v}/authn/config/saml-identity-provider/{extId}/$actions/share-all` | shareAllSamlIdentityProvider | Share SAML identity provider with all projects | 7.6 |
| `POST` | `/iam/{v}/authn/config/saml-identity-provider/{extId}/$actions/unshare` | unshareSamlIdentityProvider | Unshare SAML identity provider from a project | 7.6 |
| `POST` | `/iam/{v}/authn/config/saml-identity-provider/{extId}/$actions/unshare-all` | unshareAllSamlIdentityProvider | Unshare SAML identity provider from all projects | 7.6 |
| `GET` | `/iam/{v}/authn/login-providers` | listLoginProviders | List login providers | 7.0 |
| `GET` | `/iam/{v}/authn/saml-identity-providers/{extId}/sp-metadata` | getSamlIdpSpMetadataById | Downloads SP-Metadata for SAML identity provider. | 7.3 |
| `GET` | `/iam/{v}/authn/welcome-banner` | getWelcomeBanner | Get welcome banner | 7.5 |
| `PUT` | `/iam/{v}/authn/welcome-banner` | updateWelcomeBanner | Update welcome banner | 7.5 |
| `GET` | `/iam/{v}/authz/role-membership-summaries` | listRoleMembershipSummary | List role membership summary. | 7.6 |
| `GET` | `/iam/{v}/authz/role-memberships` | listRoleMemberships | List role membership(s). | 7.6 |
| `POST` | `/iam/{v}/authz/role-memberships` | createRoleMembership | Create role membership. | 7.6 |
| `DELETE` | `/iam/{v}/authz/role-memberships/{extId}` | deleteRoleMembershipById | Delete role membership. | 7.6 |
| `GET` | `/iam/{v}/authz/role-memberships/{extId}` | getRoleMembershipById | Get role membership. | 7.6 |

## licensing

**Nutanix Licensing APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3\*, v4.2 → pc.7.5\*, v4.3 → pc.7.5, v4.4 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **EndUserLicenseAgreement** | | | | | | |
| `GET` | `/licensing/{v}/agreements/eula` | getEula | Get End User License Agreement | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/licensing/{v}/agreements/eula/$actions/add-user` | addUser | Accept End User License Agreement | 7.0 | v4.0 | v4.3 | v4.4 |
| | **LicenseKeys** | | | | | | |
| `POST` | `/licensing/{v}/config/$actions/assign-license-keys` | assignLicenseKeys | Assign license keys to cluster | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/license-keys` | listLicenseKeys | Get license key | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/licensing/{v}/config/license-keys` | addLicenseKey | Add license key | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/licensing/{v}/config/license-keys/{extId}` | deleteLicenseKeyById | Delete license key | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/license-keys/{extId}` | getLicenseKeyById | Get license key detail | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/licensing/{v}/config/license-keys/{extId}/$actions/associate-license-keys` | associateLicenseKeys | Allows to link license keys together | 7.5 | — | v4.3 | v4.4 |
| `POST` | `/licensing/{v}/config/license-keys/{extId}/$actions/reclaim` | reclaimLicenseKey | Reclaim license key | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/reclaim-license-tokens` | listReclaimLicenseTokens | List reclaim license tokens. | 7.5 | — | v4.3 | v4.4 |
| | **Licenses** | | | | | | |
| `POST` | `/licensing/{v}/config/$actions/sync-license-state` | syncLicenseState | Seamless licensing action | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/licensing/{v}/config/$actions/upload-license-summary-file` | uploadLicenseSummaryFile | Upload license summary file | 7.6 | — | — | v4.4 |
| `GET` | `/licensing/{v}/config/allowances` | listAllowances | List allowances | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/cluster-summary-file` | downloadClusterSummaryFile | Get cluster summary file | 7.6 | — | — | v4.4 |
| `GET` | `/licensing/{v}/config/compliances` | listCompliances | List license compliances | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/entitlements` | listEntitlements | List license entitlements | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/features` | listFeatures | List license features | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/licenses` | listLicenses | List applied license inventory | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/recommendations` | listRecommendations | List cluster and license recommendations | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/settings` | listSettings | List license configurations | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/licensing/{v}/config/settings/{extId}` | getSettingById | Get setting | 7.6 | — | — | v4.4 |
| `GET` | `/licensing/{v}/config/violations` | listViolations | List license violations | 7.0 | v4.0 | v4.3 | v4.4 |

## lifecycle

**Nutanix Lifecycle Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5, v4.3 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Bundles** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/bundles` | listBundles | Get LCM bundles on the cluster | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/bundles` | createBundle | Create a new LCM bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/lifecycle/{v}/resources/bundles/{extId}` | deleteBundleById | Delete an LCM bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/bundles/{extId}` | getBundleById | Information about a bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| | **ClaimTokens** | | | | | | |
| `GET` | `/lifecycle/{v}/config/claim-tokens` | listClaimTokens | List claim tokens | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/claim-tokens` | createClaimToken | Create claim token | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/claim-tokens/{claimTokenExtId}/nodes` | listNodesByClaimTokenId | List nodes by claim token | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/claim-tokens/{claimTokenExtId}/nodes/{extId}` | getNodeByClaimTokenId | Get node by claim token | 7.6 | — | — | v4.3 |
| `DELETE` | `/lifecycle/{v}/config/claim-tokens/{extId}` | deleteClaimTokenById | Delete claim token | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/claim-tokens/{extId}` | getClaimTokenById | Get claim token | 7.6 | — | — | v4.3 |
| `PUT` | `/lifecycle/{v}/config/claim-tokens/{extId}` | updateClaimTokenById | Update claim token | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/claim-tokens/{extId}/secret` | getSecretByClaimTokenId | Get claim token secret | 7.6 | — | — | v4.3 |
| | **Config** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/config` | getConfig | Get the present LCM configuration. | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/lifecycle/{v}/resources/config` | updateConfig | Change the LCM configuration. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Entities** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/preload-artifacts` | preloadArtifacts | Preload artifacts on to the cluster. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/entities` | listEntities | Get details about all LCM entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/entities/$actions/export` | exportInventory | Export inventory information (the list of LCM entities) in the connected clusters. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/entities/{extId}` | getEntityById | Get details about an LCM entity. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **FoundationCentralConfig** | | | | | | |
| `GET` | `/lifecycle/{v}/mgmt/foundation-central-config` | getFoundationCentralConfig | Get Foundation Central configuration | 7.6 | — | — | v4.3 |
| `PUT` | `/lifecycle/{v}/mgmt/foundation-central-config` | updateFoundationCentralConfig | Update Foundation Central configuration | 7.6 | — | — | v4.3 |
| | **HardwareProviders** | | | | | | |
| `GET` | `/lifecycle/{v}/config/hardware-providers` | listHardwareProviders | List hardware providers | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{extId}` | getHardwareProviderById | Get hardware provider details | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections` | listConnectionsByHardwareProviderId | List connections | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections` | createConnectionByHardwareProviderId | Create connection | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/ip-pools` | listIpPoolsByConnectionId | List IP address pools | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/ip-pools/{extId}` | getIpPoolById | Get IP address pool details | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/mac-pools` | listMacPoolsByConnectionId | List MAC address pools | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/mac-pools/{extId}` | getMacPoolById | Get MAC address pool details | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/nodes` | listNodesByConnectionId | List discovered nodes | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/nodes/{extId}` | getConnectionNodeById | Get discovered node details | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/server-identity-pools` | listServerIdentityPoolsByConnectionId | List server identity pools | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{connectionExtId}/server-identity-pools/{extId}` | getServerIdentityPoolById | Get server identity pool details | 7.6 | — | — | v4.3 |
| `DELETE` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{extId}` | deleteConnectionById | Delete connection | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{extId}` | getConnectionById | Get connection details | 7.6 | — | — | v4.3 |
| `PUT` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{extId}` | updateConnectionById | Update connection | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/hardware-providers/{hardwareProviderExtId}/connections/{extId}/$actions/refresh` | refreshConnection | Refresh connection | 7.6 | — | — | v4.3 |
| | **Images** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/images` | listImages | Get the list of downloaded LCM images. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **InstallerImages** | | | | | | |
| `GET` | `/lifecycle/{v}/config/images` | listImages | List images | ? | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/images` | createImage | Create image | ? | — | — | v4.3 |
| `DELETE` | `/lifecycle/{v}/config/images/{extId}` | deleteImageById | Delete image | ? | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/images/{extId}` | getImageById | Get image details | ? | — | — | v4.3 |
| `PUT` | `/lifecycle/{v}/config/images/{extId}` | updateImageById | Update image details | ? | — | — | v4.3 |
| | **Inventory** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/inventory` | performInventory | Perform an inventory operation to identify/scan entities on the cluster that can be updated through LCM. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **LcmHistories** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/lcm-histories` | listLcmHistories | Summary of the queried LCM histories. | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/lcm-histories/$actions/export` | exportHistories | Export the history information of connected clusters. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/lcm-histories/{extId}` | getLcmHistoryById | Get details about an LCM history entry. | 7.5 | — | v4.2 | v4.3 |
| | **LcmSummaries** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/lcm-summaries` | listLcmSummaries | List the LCM summaries. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/lcm-summaries/{extId}` | getLcmSummaryById | Get the LCM summary. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Nodes** | | | | | | |
| `GET` | `/lifecycle/{v}/config/nodes` | listNodes | List nodes | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/nodes` | createNode | Onboard node | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/nodes/$actions/configure` | configureNode | Configure node | 7.6 | — | — | v4.3 |
| `DELETE` | `/lifecycle/{v}/config/nodes/{extId}` | deleteNodeById | Delete node | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/nodes/{extId}` | getNodeById | Get node information | 7.6 | — | — | v4.3 |
| `PUT` | `/lifecycle/{v}/config/nodes/{extId}` | updateNodeById | Update node information | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/nodes/{extId}/$actions/image` | imageNode | Image node | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/nodes/{extId}/$actions/refresh` | refreshNode | Refresh node | 7.6 | — | — | v4.3 |
| | **Notifications** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/compute-notifications` | ComputeNotifications | Compute LCM upgrade plan and notifications for a set of entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/notifications/{extId}` | GetNotificationById | Get LCM upgrade notification details for specified resource UUID. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **PatchedImages** | | | | | | |
| `GET` | `/lifecycle/{v}/config/patched-images` | listPatchedImages | List patched images | 7.6 | — | — | v4.3 |
| `POST` | `/lifecycle/{v}/config/patched-images` | createPatchedImage | Create patched image | 7.6 | — | — | v4.3 |
| `DELETE` | `/lifecycle/{v}/config/patched-images/{extId}` | deletePatchedImageById | Delete patched image | 7.6 | — | — | v4.3 |
| `GET` | `/lifecycle/{v}/config/patched-images/{extId}` | getPatchedImageById | Get patched image details | 7.6 | — | — | v4.3 |
| | **Prechecks** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/prechecks` | performPrechecks | Perform LCM prechecks operation. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Recommendations** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/compute-recommendations` | computeRecommendations | Compute LCM recommendations for a set of entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/recommendations/{extId}` | GetRecommendationById | Get a list of update recommendations from LCM. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Status** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/status` | getStatus | Get the LCM framework status. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **UpgradeSelections** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/upgrade-selections` | listUpgradeSelections | Get the LCM Upgrade Selections on the cluster | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/upgrade-selections` | createUpgradeSelection | Create a new LCM Upgrade Selection | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/lifecycle/{v}/resources/upgrade-selections/{extId}` | deleteUpgradeSelectionById | Delete LCM upgrade selection | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/upgrade-selections/{extId}` | getUpgradeSelectionById | Information about the upgrade selection made on the cluster | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/upgrade-selections/{extId}/$actions/export` | exportUpgradeSelection | Download the darksite upgrade orchestrator helper scripts which are packaged in the download_helper.zip file | 7.5 | — | v4.2 | v4.3 |
| | **Upgrades** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/upgrade` | performUpgrade | Perform an LCM upgrade operation. | 7.0 | v4.0 | v4.2 | v4.3 |

## microseg

**Nutanix Flow Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5\*, v4.3 → pc.7.5\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **AddressGroups** | | | | | | |
| `GET` | `/microseg/{v}/config/address-groups` | listAddressGroups | List all the Address Groups | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/address-groups` | createAddressGroup | Create an Address Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/address-groups/{extId}` | deleteAddressGroupById | Delete an Address Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/address-groups/{extId}` | getAddressGroupById | Get an Address Group by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/address-groups/{extId}` | updateAddressGroupById | Update an Address Group | 7.0 | v4.0 | v4.3 | v4.3 |
| | **DirectoryServerConfigs** | | | | | | |
| `GET` | `/microseg/{v}/config/category-mappings` | listCategoryMappings | List all the Directory Server Category Mappings | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/category-mappings` | createCategoryMapping | Create an AD Group and Category Mapping | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/category-mappings/{extId}` | deleteDsCategoryMappingById | Delete a Directory Config by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/category-mappings/{extId}` | getDsCategoryMappingById | Get a Category to Directory Config information by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/category-mappings/{extId}` | updateDsCategoryMappingById | Update a Category to Directory Config mapping by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/directory-server-configs` | listDirectoryServerConfigs | List all the Directory Servers | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/directory-server-configs` | createDirectoryServerConfig | Configure Directory Servers | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/directory-server-configs/{extId}` | deleteDirectoryServerConfigById | Delete a Directory Server by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/directory-server-configs/{extId}` | getDirectoryServerConfigById | Get details of Directory Server by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/directory-server-configs/{extId}` | updateDirectoryServerConfigById | Update a Directory Server by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| | **EntityGroups** | | | | | | |
| `GET` | `/microseg/{v}/config/entity-groups` | listEntityGroups | List Entity Groups | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/entity-groups` | createEntityGroup | Create an Entity Group | 7.3 | — | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/entity-groups/{extId}` | deleteEntityGroupById | Delete an Entity Group | 7.3 | — | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/entity-groups/{extId}` | getEntityGroupById | Get an Entity Group by external identifier | 7.3 | — | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/entity-groups/{extId}` | updateEntityGroupById | Update an Entity Group by external identifier | 7.3 | — | v4.3 | v4.3 |
| | **NetworkSecurityPolicies** | | | | | | |
| `GET` | `/microseg/{v}/config/policies` | listNetworkSecurityPolicies | List all the Network Security Policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/policies` | createNetworkSecurityPolicy | Create a Network Security Policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/policies/$actions/import` | applyNetworkSecurityPolicyImport | Import Network Security Policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/policies/$actions/prepare-export` | exportNetworkSecurityPolicy | Export Network Security Policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/policies/{extId}` | deleteNetworkSecurityPolicyById | Delete a Network Security Policy by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/policies/{extId}` | getNetworkSecurityPolicyById | Get a Network Security Policy by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/policies/{extId}` | updateNetworkSecurityPolicyById | Update a Network Security Policy by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/policies/{policyExtId}/rules` | listNetworkSecurityPolicyRules | List all the Network Security Policy rules by policy ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| | **ServiceGroups** | | | | | | |
| `GET` | `/microseg/{v}/config/service-groups` | listServiceGroups | List all the Service Groups | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/microseg/{v}/config/service-groups` | createServiceGroup | Create a Service Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/microseg/{v}/config/service-groups/{extId}` | deleteServiceGroupById | Delete a Service Group by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/microseg/{v}/config/service-groups/{extId}` | getServiceGroupById | Get a Service Group by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/microseg/{v}/config/service-groups/{extId}` | updateServiceGroupById | Update a Service Group by ExtID | 7.0 | v4.0 | v4.3 | v4.3 |

## monitoring

**Nutanix Monitoring APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5\*, v4.3 → pc.7.5\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Alerts** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/alerts` | listAlerts | List alerts | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/email-config` | getAlertEmailConfiguration | Get alert email configuration | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/monitoring/{v}/serviceability/alerts/email-config` | updateAlertEmailConfiguration | Update alert email configuration | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/{extId}` | getAlertById | Get alert details | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/monitoring/{v}/serviceability/alerts/{extId}/$actions/manage-alert` | manageAlert | Acknowledge or resolve the alert | 7.0 | v4.0 | v4.3 | v4.3 |
| | **Audits** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/audits` | listAudits | List audits | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/audits/{extId}` | getAuditById | Get audit details | 7.0 | v4.0 | v4.3 | v4.3 |
| | **ClusterLogs** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/clusters/{clusterExtId}/tags` | listTags | List tags | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/monitoring/{v}/serviceability/clusters/{extId}/$actions/collect-logs` | collectLogs | Collect logs | 7.0 | v4.0 | v4.3 | v4.3 |
| | **Events** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/events` | listEvents | List events | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/events/{extId}` | getEventById | Get event details | 7.0 | v4.0 | v4.3 | v4.3 |
| | **SystemDefinedPolicies** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/alerts/system-defined-policies` | listSdaPolicies | List System-Defined Alert Policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/system-defined-policies/{extId}` | getSdaPolicyById | Get System-Defined Alert Policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/system-defined-policies/{systemDefinedPolicyExtId}/cluster-configs` | listClusterConfigsBySdaId | List all cluster specific configurations associated with a System-Defined Alert Policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/system-defined-policies/{systemDefinedPolicyExtId}/cluster-configs/{extId}` | getClusterConfigById | Get cluster-specific configuration associated with a System-Defined Alert Policy for a cluster | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/monitoring/{v}/serviceability/alerts/system-defined-policies/{systemDefinedPolicyExtId}/cluster-configs/{extId}` | updateClusterConfigById | Update cluster-specific configuration associated with a System-Defined Alert Policy for a cluster | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/monitoring/{v}/serviceability/clusters/{clusterExtId}/$actions/run-system-defined-checks` | runSystemDefinedChecks | Run System-Defined Checks | 7.3 | — | v4.3 | v4.3 |
| | **UserDefinedPolicies** | | | | | | |
| `GET` | `/monitoring/{v}/serviceability/alerts/user-defined-policies` | listUdaPolicies | List User-Defined Alert policies | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/monitoring/{v}/serviceability/alerts/user-defined-policies` | createUdaPolicy | Create a User-Defined Alert policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/monitoring/{v}/serviceability/alerts/user-defined-policies/$actions/find-conflicts` | findConflictingUdaPolicies | Get existing policies with conflicting criteria | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/monitoring/{v}/serviceability/alerts/user-defined-policies/{extId}` | deleteUdaPolicyById | Delete a User-Defined Alert policy | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/monitoring/{v}/serviceability/alerts/user-defined-policies/{extId}` | getUdaPolicyById | Get User-Defined Alert policy details | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/monitoring/{v}/serviceability/alerts/user-defined-policies/{extId}` | updateUdaPolicyById | Update a User-Defined Alert policy | 7.0 | v4.0 | v4.3 | v4.3 |

## multidomain

**Nutanix Multidomain Versioned APIs** — versions GA : v4.2, v4.3 ; pré-versions : v4.4.b1

Release PC par version : v4.2 → pc.7.5, v4.3 → pc.7.5\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **ExternalRepositories** | | | | | | |
| `GET` | `/multidomain/{v}/config/external-repositories` | listExternalRepositories | List external repositories | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/multidomain/{v}/config/external-repositories` | createExternalRepository | Create an external repository | 7.5 | — | v4.3 | v4.3 |
| `DELETE` | `/multidomain/{v}/config/external-repositories/{extId}` | deleteExternalRepositoryById | Delete an external repository | 7.5 | — | v4.3 | v4.3 |
| `GET` | `/multidomain/{v}/config/external-repositories/{extId}` | getExternalRepositoryById | Get an external repository by ID | 7.5 | — | v4.3 | v4.3 |
| `PUT` | `/multidomain/{v}/config/external-repositories/{extId}` | updateExternalRepositoryById | Update an external repository | 7.5 | — | v4.3 | v4.3 |
| | **LocalDomain** | | | | | | |
| `GET` | `/multidomain/{v}/management/local-domain` | getLocalDomain | Get domain | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/multidomain/{v}/management/local-domain/$actions/register` | registerLocalDomain | Register a domain with Nutanix Central | 7.5 | — | v4.3 | v4.3 |
| `POST` | `/multidomain/{v}/management/local-domain/$actions/unregister` | unregisterLocalDomain | Unregister domain from Nutanix Central | 7.5 | — | v4.3 | v4.3 |
| | **Locations** | | | | | | |
| `GET` | `/multidomain/{v}/config/locations` | listLocations | List locations | ? | — | v4.3 | v4.3 |
| | **RegisteredDomains** | | | | | | |
| `GET` | `/multidomain/{v}/config/registered-domains` | listRegisteredDomains | List all registered domains | ? | — | v4.3 | v4.3 |
| `POST` | `/multidomain/{v}/config/registered-domains` | createRegisteredDomain | Create a registered domain | ? | — | v4.3 | v4.3 |
| `DELETE` | `/multidomain/{v}/config/registered-domains/{extId}` | deleteRegisteredDomainById | Delete a registered domain by its external identifier | ? | — | v4.3 | v4.3 |
| `GET` | `/multidomain/{v}/config/registered-domains/{extId}` | getRegisteredDomainById | Get a registered domain by its external identifier | ? | — | v4.3 | v4.3 |
| `PUT` | `/multidomain/{v}/config/registered-domains/{extId}` | updateRegisteredDomainById | Update a registered domain by its external identifier | ? | — | v4.3 | v4.3 |

**Preview `v4.4.b1`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `GET` | `/multidomain/{v}/config/projects` | listProjects | List projects | 7.6 |
| `POST` | `/multidomain/{v}/config/projects` | createProject | Create project | 7.6 |
| `DELETE` | `/multidomain/{v}/config/projects/{extId}` | deleteProjectById | Delete project | 7.6 |
| `GET` | `/multidomain/{v}/config/projects/{extId}` | getProjectById | Get project | 7.6 |
| `PUT` | `/multidomain/{v}/config/projects/{extId}` | updateProjectById | Update project | 7.6 |
| `POST` | `/multidomain/{v}/config/registered-domains/{extId}/$actions/refresh-api-credentials` | refreshApiCredentials | Refreshes the API credentials for the registered domain | ? |
| `GET` | `/multidomain/{v}/config/resource-groups` | listResourceGroups | Get list of Resource Groups | 7.6 |
| `POST` | `/multidomain/{v}/config/resource-groups` | createResourceGroup | Create a Resource Group | 7.6 |
| `DELETE` | `/multidomain/{v}/config/resource-groups/{extId}` | deleteResourceGroupById | Delete Resource Group | 7.6 |
| `GET` | `/multidomain/{v}/config/resource-groups/{extId}` | getResourceGroupById | Get Resource Group details | 7.6 |
| `PUT` | `/multidomain/{v}/config/resource-groups/{extId}` | updateResourceGroupById | Update Resource Group | 7.6 |
| `GET` | `/multidomain/{v}/content/content-repositories` | listContentRepositories | List Content Repositories | 7.6 |
| `POST` | `/multidomain/{v}/content/content-repositories` | createContentRepository | Create a Content Repository | 7.6 |
| `DELETE` | `/multidomain/{v}/content/content-repositories/{extId}` | deleteContentRepositoryById | Delete a Content Repository | 7.6 |
| `GET` | `/multidomain/{v}/content/content-repositories/{extId}` | getContentRepositoryById | Get Content Repository details | 7.6 |
| `PUT` | `/multidomain/{v}/content/content-repositories/{extId}` | updateContentRepositoryById | Update a Content Repository | 7.6 |
| `POST` | `/multidomain/{v}/content/content-repositories/{extId}/$actions/subscribe` | subscribeContentRepository | Subscribe to a source Content Repository | 7.6 |
| `POST` | `/multidomain/{v}/content/content-repositories/{extId}/$actions/sync` | syncContentRepository | Sync items of a subscribed Content Repository | 7.6 |
| `GET` | `/multidomain/{v}/content/content-repositories/{extId}/items` | listContentRepositoryItemsByContentRepositoryId | List Content Repository items | 7.6 |

## networking

**Nutanix Networking APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5\*, v4.3 → pc.7.5\*, v4.4 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **AwsSubnets** | | | | | | |
| `GET` | `/networking/{v}/aws/config/subnets` | listAwsSubnets | Get NC2A subnets. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **AwsVpcs** | | | | | | |
| `GET` | `/networking/{v}/aws/config/vpcs` | listAwsVpcs | Get NC2A VPCs. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **BgpRoutes** | | | | | | |
| `GET` | `/networking/{v}/config/bgp-sessions/{bgpSessionExtId}/bgp-routes` | listRoutesByBgpSessionId | List routes request | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/bgp-sessions/{bgpSessionExtId}/bgp-routes/{extId}` | getRouteForBgpSessionById | Fetches a BGP session route | 7.0 | v4.0 | v4.3 | v4.4 |
| | **BgpSessions** | | | | | | |
| `GET` | `/networking/{v}/config/bgp-sessions` | listBgpSessions | List BGP sessions request. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/bgp-sessions` | createBgpSession | Create BGP session. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/bgp-sessions/{extId}` | deleteBgpSessionById | Delete BGP session request. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/bgp-sessions/{extId}` | getBgpSessionById | Get BGP session request. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/bgp-sessions/{extId}` | updateBgpSessionById | Update BGP session request. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Capabilities** | | | | | | |
| `GET` | `/networking/{v}/aws/config/capabilities` | getCapabilities | Get NC2A capabilities | 7.0 | v4.0 | — | — |
| | **ClusterCapabilities** | | | | | | |
| `GET` | `/networking/{v}/config/capabilities` | listClusterCapabilities | Get cluster capabilities | 7.0 | v4.0 | v4.3 | v4.4 |
| | **FloatingIps** | | | | | | |
| `GET` | `/networking/{v}/config/floating-ips` | listFloatingIps | Get a list of floating IPs. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/floating-ips` | createFloatingIp | Create a floating IP. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/floating-ips/{extId}` | deleteFloatingIpById | Delete the floating IP corresponding to the extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/floating-ips/{extId}` | getFloatingIpById | Get the floating IP for this extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/floating-ips/{extId}` | updateFloatingIpById | Update the floating IP for this extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Gateways** | | | | | | |
| `GET` | `/networking/{v}/config/gateways` | listGateways | List network gateways. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/gateways` | createGateway | Create network gateway. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/gateways/{extId}` | deleteGatewayById | Delete network gateway. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/gateways/{extId}` | getGatewayById | Get network gateway. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/gateways/{extId}` | updateGatewayById | Update network gateway. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/gateways/{extId}/$actions/upgrade` | upgradeGatewayById | Upgrade network gateway. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **IPFIXExporters** | | | | | | |
| `GET` | `/networking/{v}/config/ipfix-exporters` | listIpfixExporters | Get the list of existing IPFIX Exporters. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/ipfix-exporters` | createIpfixExporter | Create an IPFIX Exporter. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/ipfix-exporters/{extId}` | deleteIpfixExporterById | Delete the specified IPFIX Exporter. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/ipfix-exporters/{extId}` | getIpfixExporterById | Get the specified IPFIX Exporter. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/ipfix-exporters/{extId}` | updateIpfixExporterById | Update the specified IPFIX Exporter. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Layer2Stretches** | | | | | | |
| `GET` | `/networking/{v}/config/layer2-stretches` | listLayer2Stretches | Get the list of existing Layer2Stretch configurations. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/layer2-stretches` | createLayer2Stretch | Create a Layer2Stretch configuration. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/layer2-stretches/{extId}` | deleteLayer2StretchById | Delete the specified Layer2Stretch configuration. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/layer2-stretches/{extId}` | getLayer2StretchById | Get the Layer2Stretch configuration with the specified UUID. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/layer2-stretches/{extId}` | updateLayer2StretchById | Update the specified Layer2Stretch configuration. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/stats/layer2-stretches/{extId}` | getLayer2StretchStats | Get Layer2Stretch statistics | 7.0 | v4.0 | v4.3 | v4.4 |
| | **LoadBalancerSessions** | | | | | | |
| `GET` | `/networking/{v}/config/load-balancer-sessions` | listLoadBalancerSessions | Get the list of existing load balancer sessions | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/load-balancer-sessions` | createLoadBalancerSession | Create a load balancer session | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/load-balancer-sessions/{extId}` | deleteLoadBalancerSessionById | Delete the specified load balancer session | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/load-balancer-sessions/{extId}` | getLoadBalancerSessionById | Get the load balancer session with the specified UUID | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/load-balancer-sessions/{extId}` | updateLoadBalancerSessionById | Update the specified load balancer session | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/stats/load-balancer-sessions/{extId}` | getLoadBalancerSessionStats | Get load balancer session listener and target statistics | 7.0 | v4.0 | v4.3 | v4.4 |
| | **MacAddresses** | | | | | | |
| `GET` | `/networking/{v}/config/layer2-stretches/{layer2StretchExtId}/learned-mac-addresses` | listLearnedMacAddressesByLayer2StretchId | Get stretch-related learned MAC Addresses. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/layer2-stretches/{layer2StretchExtId}/learned-mac-addresses/{extId}` | getLearnedMacAddressForLayer2StretchById | Get a specified stretch-related learned MAC Address. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **NetworkControllers** | | | | | | |
| `GET` | `/networking/{v}/config/controllers` | listNetworkControllers | Gets the list of existing network controllers | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/controllers` | createNetworkController | Create a network controller | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/controllers/{extId}` | deleteNetworkControllerById | Delete a network controller | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/controllers/{extId}` | getNetworkControllerById | Get the network controller with the specified UUID | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/controllers/{extId}` | updateNetworkControllerById | Update a network controller summary | 7.0 | v4.0 | v4.3 | v4.4 |
| | **NetworkFunctions** | | | | | | |
| `GET` | `/networking/{v}/config/network-functions` | listNetworkFunctions | Get the list of existing network functions. | 7.3 | — | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/network-functions` | createNetworkFunction | Create a network function. | 7.3 | — | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/network-functions/{extId}` | deleteNetworkFunctionById | Delete the specified network function. | 7.3 | — | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/network-functions/{extId}` | getNetworkFunctionById | Get the network function with the specified UUID. | 7.3 | — | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/network-functions/{extId}` | updateNetworkFunctionById | Update the specified network function. | 7.3 | — | v4.3 | v4.4 |
| | **NicProfiles** | | | | | | |
| `GET` | `/networking/{v}/config/nic-profiles` | listNicProfiles | Lists all NIC Profiles | 7.3 | — | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/nic-profiles` | createNicProfile | Create a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/nic-profiles/{extId}` | deleteNicProfileById | Delete a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/nic-profiles/{extId}` | getNicProfileById | Get a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/nic-profiles/{extId}` | updateNicProfileById | Update a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/nic-profiles/{extId}/$actions/associate-host-nic` | associateHostNicToNicProfile | Associate a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/nic-profiles/{extId}/$actions/disassociate-host-nic` | disassociateHostNicFromNicProfile | Disassociate a Host NIC from a NIC Profile | 7.3 | — | v4.3 | v4.4 |
| | **RemoteEntities** | | | | | | |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-subnets` | listRemoteSubnetsByClusterId | List remote subnets | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-subnets/{extId}` | getRemoteSubnetForClusterById | Get remote subnet | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-vpn-connections` | listRemoteVpnConnectionsByClusterId | List remote VPN connections | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-vpn-connections/{extId}` | getRemoteVpnConnectionForClusterById | Get a remote VPN connection | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-vtep-gateways` | listRemoteVtepGatewaysByClusterId | List remote VTEP gateways | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/clusters/{clusterExtId}/remote-vtep-gateways/{extId}` | getRemoteVtepGatewayForClusterById | Get a remote VTEP gateway | 7.0 | v4.0 | v4.3 | v4.4 |
| | **RouteTables** | | | | | | |
| `GET` | `/networking/{v}/config/route-tables` | listRouteTables | List route tables | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/route-tables/{extId}` | getRouteTableById | Get route table | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Routes** | | | | | | |
| `GET` | `/networking/{v}/config/route-tables/{routeTableExtId}/routes` | listRoutesByRouteTableId | Lists routes | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/route-tables/{routeTableExtId}/routes` | createRouteForRouteTable | Create route | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/route-tables/{routeTableExtId}/routes/{extId}` | deleteRouteForRouteTableById | Delete route | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/route-tables/{routeTableExtId}/routes/{extId}` | getRouteForRouteTableById | Fetches a route table route | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/route-tables/{routeTableExtId}/routes/{extId}` | updateRouteForRouteTableById | Update route | 7.0 | v4.0 | v4.3 | v4.4 |
| | **RoutingPolicies** | | | | | | |
| `GET` | `/networking/{v}/config/routing-policies` | listRoutingPolicies | Get a list of Routing Policies. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/routing-policies` | createRoutingPolicy | Create a Routing Policy. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/routing-policies/{extId}` | deleteRoutingPolicyById | Delete the Routing Policy corresponding to the extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/routing-policies/{extId}` | getRoutingPolicyById | Get a single Routing Policy corresponding to the extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/routing-policies/{extId}` | updateRoutingPolicyById | Update the Routing Policy corresponding to the extId. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/stats/routing-policies/$actions/clear` | clearRoutingPolicyCounters | Clear the value in packet and byte counters of all Routing Policies in the chosen VPC or particular routing policy. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **SubnetMigrations** | | | | | | |
| `POST` | `/networking/{v}/config/$actions/migrate-subnets` | migrateSubnets | Migrate VLAN subnets from VLAN basic to VLAN advanced. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/vnics/{extId}/$actions/migrate` | migrateVnicById | Migrate vNICs from Acropolis to Atlas or vice-versa. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Subnets** | | | | | | |
| `GET` | `/networking/{v}/config/subnets` | listSubnets | Get the list of existing subnets. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/subnets` | createSubnet | Create a subnet. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/subnets/{extId}` | deleteSubnetById | Delete the specified subnet. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/subnets/{extId}` | getSubnetById | Get the subnet with the specified UUID. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/subnets/{extId}` | updateSubnetById | Update the specified subnet. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/subnets/{extId}/addresses/$actions/reserve` | reserveIpsBySubnetId | Reserve IP addresses on a subnet | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/subnets/{extId}/addresses/$actions/unreserve` | unreserveIpsBySubnetId | Unreserve IP addresses on a subnet | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/subnets/{subnetExtId}/$actions/share` | shareSubnetById | Share the specified subnet with a project. | 7.6 | — | — | v4.4 |
| `POST` | `/networking/{v}/config/subnets/{subnetExtId}/$actions/unshare` | unshareSubnetById | Stop sharing the specified subnet with a project. | 7.6 | — | — | v4.4 |
| `GET` | `/networking/{v}/config/subnets/{subnetExtId}/reserved-ips` | listReservedIpsBySubnetId | List reserved IPs of a managed subnet | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/subnets/{subnetExtId}/vnics` | listVnicsBySubnetId | List virtual NICs on a subnet. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **TrafficMirrors** | | | | | | |
| `GET` | `/networking/{v}/config/traffic-mirrors` | listTrafficMirrors | List Traffic mirror sessions. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/traffic-mirrors` | createTrafficMirror | Create Traffic mirror session. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/traffic-mirrors/{extId}` | deleteTrafficMirrorById | Delete Traffic mirror session. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/traffic-mirrors/{extId}` | getTrafficMirrorById | Get Traffic mirror session. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/traffic-mirrors/{extId}` | updateTrafficMirrorById | Update a Traffic mirror session for the provided UUID. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/stats/traffic-mirrors/{extId}` | getTrafficMirrorStats | Get Traffic mirror session statistics. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **UplinkBonds** | | | | | | |
| `GET` | `/networking/{v}/config/uplink-bonds` | listUplinkBonds | List uplink bonds | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/uplink-bonds/{extId}` | getUplinkBondById | Get uplink bond | 7.0 | v4.0 | v4.3 | v4.4 |
| | **VirtualSwitches** | | | | | | |
| `GET` | `/networking/{v}/config/node-schedulable-statuses` | listNodeSchedulableStatus | Check whether a node in a cluster is a storage-only node or not | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/virtual-switches` | listVirtualSwitches | Get list of Virtual Switches | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/virtual-switches` | createVirtualSwitch | Create a Virtual Switch | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/virtual-switches/$actions/migrate` | migrateBridge | Create a Virtual Switch from an existing bridge | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/virtual-switches/{extId}` | deleteVirtualSwitchById | Delete a Virtual Switch | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/virtual-switches/{extId}` | getVirtualSwitchById | Get single Virtual Switch given its UUID | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/virtual-switches/{extId}` | updateVirtualSwitchById | Update a Virtual Switch | 7.0 | v4.0 | v4.3 | v4.4 |
| | **VpcVirtualSwitchMappings** | | | | | | |
| `GET` | `/networking/{v}/config/vpc-virtual-switch-mappings` | listVpcVirtualSwitchMappings | Get the VPC for virtual switch mappings config. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/vpc-virtual-switch-mappings` | createVpcVirtualSwitchMapping | Set VPC for virtual switch mappings traffic config. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Vpcs** | | | | | | |
| `GET` | `/networking/{v}/config/vpcs` | listVpcs | Get the list of existing VPCs. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/vpcs` | createVpc | Create a VPC. | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/vpcs/{extId}` | deleteVpcById | Delete the specified VPC. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/vpcs/{extId}` | getVpcById | Get the VPC with the specified UUID. | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/vpcs/{extId}` | updateVpcById | Update the specified VPC. | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/vpcs/{extId}/$actions/share` | shareVpcById | Share the specified VPC with a project. | 7.6 | — | — | v4.4 |
| `POST` | `/networking/{v}/config/vpcs/{extId}/$actions/unshare` | unshareVpcById | Stop sharing the specified VPC with a project. | 7.6 | — | — | v4.4 |
| `GET` | `/networking/{v}/stats/vpc/{vpcExtId}/external-subnets/{extId}` | getVpcNsStats | Get VPC North-South statistics. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **VpnConnections** | | | | | | |
| `GET` | `/networking/{v}/config/vpn-connections` | listVpnConnections | List the VPN connections | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/networking/{v}/config/vpn-connections` | createVpnConnection | Create a VPN connection | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/networking/{v}/config/vpn-connections/{extId}` | deleteVpnConnectionById | Delete VPN connection | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/vpn-connections/{extId}` | getVpnConnectionById | Get VPN connection | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/networking/{v}/config/vpn-connections/{extId}` | updateVpnConnectionById | Update VPN connection | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/vpn-connections/{vpnConnectionExtId}/vpn-vendor-configs` | listVpnAppliancesByVpnConnectionId | List of third-party VPN appliances for which configurations are available to download. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/config/vpn-connections/{vpnConnectionExtId}/vpn-vendor-configs/{extId}` | getVpnApplianceForVpnConnectionById | Get third-party VPN appliance configuration. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/networking/{v}/stats/vpn-connections/{extId}` | getVpnConnectionStats | Get VPN connection statistics | 7.0 | v4.0 | v4.3 | v4.4 |

## objects

**Nutanix Objects Storage Management APIs** — versions GA : v4.0, v4.1

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Buckets** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/buckets` | listBucketsByObjectstoreId | Get a list of the buckets in an Object store | 7.6 | — | — | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/buckets/{bucketName}` | getBucketByName | Get details of a specific bucket | 7.6 | — | — | v4.1 |
| | **DataMovementTargets** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets` | listDataMovementTargets | Get a list of the data movement targets configured in an Object store | 7.6 | — | — | v4.1 |
| `POST` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets` | createDataMovementTarget | Create a new data movement target for the specified Object store | 7.6 | — | — | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets/{extId}` | getDataMovementTargetById | Get details of a data movement target | 7.6 | — | — | v4.1 |
| | **ObjectStores** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores` | listObjectstores | Get a list of the Object stores | 7.0 | v4.0 | v4.0 | v4.1 |
| `POST` | `/objects/{v}/config/object-stores` | createObjectstore | Create an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `DELETE` | `/objects/{v}/config/object-stores/{extId}` | deleteObjectstoreById | Delete an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{extId}` | getObjectstoreById | Get an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `PUT` | `/objects/{v}/config/object-stores/{extId}` | updateObjectstoreById | Update an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates` | listCertificatesByObjectstoreId | Get a list of the SSL certificates of an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `POST` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates` | createCertificate | Create a SSL certificate for an Object store | 7.0 | v4.0 | v4.0 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates/{certificateExtId}/certificate-authority` | getCaByCertificateId | Download the certificate authority | 7.0 | v4.0 | v4.0 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates/{extId}` | getCertificateById | Get the details of an Object store certificate | 7.0 | v4.0 | v4.0 | v4.1 |
| | **Stats** | | | | | | |
| `GET` | `/objects/{v}/stats/object-stores/{extId}` | getObjectstoreStatsById | Get the Object store stats | 7.0 | v4.0 | v4.0 | v4.1 |
| | **StorageBackends** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/storage-backends` | listStorageBackends | Get a list of the storage backends configured in an Object store | 7.6 | — | — | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/storage-backends/{extId}` | getStorageBackendById | Get the details of a storage backend | 7.6 | — | — | v4.1 |

## opsmgmt

**Nutanix Cloud Management Platform APIs** — versions GA : v4.0 ; pré-versions : v4.1.b1

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0)

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **GlobalReportSetting** | | | | | | |
| `GET` | `/opsmgmt/{v}/config/user/{userExtId}/global-report-setting` | getGlobalReportSetting | Get a report setting | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/opsmgmt/{v}/config/user/{userExtId}/global-report-setting` | updateGlobalReportSetting | Update report setting | 7.0 | v4.0 | v4.0 | v4.0 |
| | **ReportArtifacts** | | | | | | |
| `GET` | `/opsmgmt/{v}/content/report-artifacts` | listReportArtifacts | Get a list of report artifacts | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/opsmgmt/{v}/content/report-artifacts` | createReportArtifact | Create a report artifact | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/opsmgmt/{v}/content/report-artifacts/{reportArtifactExtId}/$actions/upload` | uploadArtifactFile | Upload an artifact file | ? | v4.0 | v4.0 | v4.0 |
| `GET` | `/opsmgmt/{v}/content/report-artifacts/{reportArtifactExtId}/file` | downloadArtifactFile | Download an artifact file | ? | v4.0 | v4.0 | v4.0 |
| | **ReportConfig** | | | | | | |
| `GET` | `/opsmgmt/{v}/config/report-configs` | listReportConfigs | Get the list of report configurations | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/opsmgmt/{v}/config/report-configs` | createReportConfig | Create report configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/opsmgmt/{v}/config/report-configs/{extId}` | deleteReportConfigById | Delete a report configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/opsmgmt/{v}/config/report-configs/{extId}` | getReportConfigById | Get report configuration information | 7.0 | v4.0 | v4.0 | v4.0 |
| `PUT` | `/opsmgmt/{v}/config/report-configs/{extId}` | updateReportConfigById | Update report configuration | 7.0 | v4.0 | v4.0 | v4.0 |
| | **Reports** | | | | | | |
| `GET` | `/opsmgmt/{v}/config/reports` | listReports | Get the list of reports | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/opsmgmt/{v}/config/reports` | createReport | Generate a report instance | 7.0 | v4.0 | v4.0 | v4.0 |
| `DELETE` | `/opsmgmt/{v}/config/reports/{extId}` | deleteReportById | Delete a report | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/opsmgmt/{v}/config/reports/{extId}` | getReportById | Get a report | 7.0 | v4.0 | v4.0 | v4.0 |
| `POST` | `/opsmgmt/{v}/config/reports/{extId}/$actions/notify-recipients` | notifyReport | Notify user with a report | 7.0 | v4.0 | v4.0 | v4.0 |
| `GET` | `/opsmgmt/{v}/content/reports/{reportExtId}/file` | downloadReport | Download a report | 7.0 | v4.0 | v4.0 | v4.0 |

**Preview `v4.1.b1`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `GET` | `/opsmgmt/{v}/config/dashboard-settings` | getDashboardSettings | Get global dashboard settings. | ? |
| `POST` | `/opsmgmt/{v}/config/dashboard-settings/$actions/upload-geoconfigurations` | uploadDashboardGeoconfiguration | Upload a dashboard geoconfiguration file. | ? |
| `GET` | `/opsmgmt/{v}/config/dashboards` | listDashboards | List all dashboards. | ? |
| `POST` | `/opsmgmt/{v}/config/dashboards` | createDashboard | Create a new dashboard. | ? |
| `DELETE` | `/opsmgmt/{v}/config/dashboards/{extId}` | deleteDashboardById | Delete an existing dashboard. | ? |
| `GET` | `/opsmgmt/{v}/config/dashboards/{extId}` | getDashboardById | Get a dashboard by ID. | ? |
| `PUT` | `/opsmgmt/{v}/config/dashboards/{extId}` | updateDashboardById | Update an existing dashboard. | ? |

## prism

**Nutanix Prism APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3\*, v4.2 → pc.7.5, v4.3 → pc.7.5\*, v4.4 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Batches** | | | | | | |
| `POST` | `/prism/{v}/operations/$actions/batch` | submitBatch | Submit a batch operation. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/operations/batches` | listBatches | Get a list of all the Batches. | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/operations/batches/{extId}` | getBatchById | Get a Batch identified by {extId}. | 7.0 | v4.0 | v4.3 | v4.4 |
| | **Categories** | | | | | | |
| `GET` | `/prism/{v}/config/categories` | listCategories | List categories | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/config/categories` | createCategory | Create a category | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/config/categories/{categoryExtId}/$actions/share` | shareCategory | Share a category with project | 7.6 | — | — | v4.4 |
| `POST` | `/prism/{v}/config/categories/{categoryExtId}/$actions/unshare` | unshareCategory | Unshare a category with project | 7.6 | — | — | v4.4 |
| `DELETE` | `/prism/{v}/config/categories/{extId}` | deleteCategoryById | Delete a category | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/categories/{extId}` | getCategoryById | Fetch a category | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/prism/{v}/config/categories/{extId}` | updateCategoryById | Update a category | 7.0 | v4.0 | v4.3 | v4.4 |
| | **DomainManager** | | | | | | |
| `GET` | `/prism/{v}/config/domain-managers` | listDomainManagers | List domain manager (Prism Central) configuration details | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/config/domain-managers` | createDomainManager | Deploy a Prism Central | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/domain-managers/{extId}` | getDomainManagerById | Get the requested domain manager (Prism Central) entity | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/prism/{v}/config/domain-managers/{extId}` | updateDomainManagerById | Update the requested domain manager (Prism Central) entity. | ? | — | — | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets` | listBackupTargets | List backup targets | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets` | createBackupTarget | Create backup target | 7.0 | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets/{extId}` | deleteBackupTargetById | Delete backup target | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets/{extId}` | getBackupTargetById | Fetch backup target | 7.0 | v4.0 | v4.3 | v4.4 |
| `PUT` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets/{extId}` | updateBackupTargetById | Update backup target | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/products` | listProducts | List products | ? | — | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/products/{extId}` | getProductById | Get product details | ? | — | v4.3 | v4.4 |
| `PUT` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/products/{extId}` | updateProductById | Update the status of a product | ? | — | v4.3 | v4.4 |
| `POST` | `/prism/{v}/management/domain-managers/{extId}/$actions/register` | register | Register a domain manager (Prism Central) to a cluster | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/management/domain-managers/{extId}/$actions/scale-up` | scaleUpDomainManagerById | Scale up a Domain Manager cluster to a higher configuration. | 7.6 | — | — | v4.4 |
| `POST` | `/prism/{v}/management/domain-managers/{extId}/$actions/unregister` | unregister | Unregister a registered remote cluster from the local cluster | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/management/restore-sources` | createRestoreSource | Create restore source | ? | v4.0 | v4.3 | v4.4 |
| `DELETE` | `/prism/{v}/management/restore-sources/{extId}` | deleteRestoreSourceById | Delete restore source | ? | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{extId}` | getRestoreSourceById | Fetch restore source | ? | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers` | listRestorableDomainManagers | List restorable domain managers | ? | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points` | listRestorePoints | List restore points | ? | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points/{extId}` | getRestorePointById | Get restore point details | ? | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points/{extId}/$actions/restore` | restore | Restore domain manager | ? | v4.0 | v4.3 | v4.4 |
| | **ExternalStorages** | | | | | | |
| `GET` | `/prism/{v}/config/external-storages/{extId}` | getExternalStorageById ⚠️ | Get external storage by ID | 7.5 | — | v4.3 | v4.4 |
| | **Registration** | | | | | | |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/registrations` | listRegistrations | List of registered clusters | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/registrations/{extId}` | getRegistrationById | Specifications for the specified registration | 7.5 | — | v4.3 | v4.4 |
| | **Tasks** | | | | | | |
| `GET` | `/prism/{v}/config/tasks` | listTasks | List tasks | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/tasks/{extId}` | getTaskById | Fetch a task | 7.0 | v4.0 | v4.3 | v4.4 |
| `POST` | `/prism/{v}/config/tasks/{taskExtId}/$actions/cancel` | cancelTask | Cancel an ongoing task | 7.0 | v4.0 | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/tasks/{taskExtId}/affected-entities` | listTaskEntities | List entities associated with a task | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/tasks/{taskExtId}/jobs` | listTaskJobs | List jobs associated with a task | 7.5 | — | v4.3 | v4.4 |
| `GET` | `/prism/{v}/config/tasks/{taskExtId}/jobs/{extId}` | getTaskJobById | Fetch a job associated with a task | 7.5 | — | v4.3 | v4.4 |

## security

**Nutanix Security APIs** — versions GA : v4.0, v4.1, v4.2

Release PC par version : v4.0 → pc.7.3, v4.1 → pc.7.5, v4.2 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **ApprovalPolicies** | | | | | | |
| `GET` | `/security/{v}/management/approval-policies` | listApprovalPolicies | List approval policies | 7.0 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/management/approval-policies` | createApprovalPolicy | Create an approval policy | 7.0 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/management/approval-policies/{extId}` | getApprovalPolicyByExtId | Get an approval policy details | 7.0 | — | v4.1 | v4.2 |
| `PUT` | `/security/{v}/management/approval-policies/{extId}` | updateApprovalPolicyByExtId | Update the details of a specific approval policy | 7.0 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/management/approval-policies/{extId}/$actions/associate-policies` | associatePolicies | Update list of secured policies | 7.0 | — | v4.1 | v4.2 |
| | **Credentials** | | | | | | |
| `GET` | `/security/{v}/config/credentials` | listCredentials | List Credentials that match the filter provided. | 7.3 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/config/credentials` | createCredential | Create a credential with the provided fields. | 7.3 | — | v4.1 | v4.2 |
| `DELETE` | `/security/{v}/config/credentials/{extId}` | deleteCredentialById | Deletes a Credential with the given ExtId. | 7.3 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/config/credentials/{extId}` | getCredentialById | Retrieves a credential with the given ExtId. | 7.3 | — | v4.1 | v4.2 |
| `PUT` | `/security/{v}/config/credentials/{extId}` | updateCredentialById | Updates a credential with the given ExtId. | 7.3 | — | v4.1 | v4.2 |
| | **KeyManagementServers** | | | | | | |
| `GET` | `/security/{v}/config/key-management-servers` | listKeyManagementServers | List key management servers | 7.3 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/config/key-management-servers` | createKeyManagementServer | Create a key management server | 7.3 | — | v4.1 | v4.2 |
| `DELETE` | `/security/{v}/config/key-management-servers/{extId}` | deleteKeyManagementServerById | Delete a key management server | 7.3 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/config/key-management-servers/{extId}` | getKeyManagementServerById | Get details of a key management server | 7.3 | — | v4.1 | v4.2 |
| `PUT` | `/security/{v}/config/key-management-servers/{extId}` | updateKeyManagementServerById | Update a key management server | 7.3 | — | v4.1 | v4.2 |
| | **STIGs** | | | | | | |
| `GET` | `/security/{v}/report/stig-summaries` | listStigSummaries ⚠️ | Fetch the aggregate report of STIG scan | 7.0 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/report/stigs` | listStigs | Get the STIG controls details | 7.0 | — | v4.1 | v4.2 |
| | **SecurityConfigsVisibility** | | | | | | |
| `GET` | `/security/{v}/config/security-configs-visibility-setting` | getSecurityConfigsVisibilitySetting | Fetch the security configurations visibility setting | 7.3 | — | — | v4.2 |
| `PUT` | `/security/{v}/config/security-configs-visibility-setting` | updateSecurityConfigsVisibilitySetting | Update the security configurations visibility setting | 7.3 | — | — | v4.2 |
| | **SecurityProfiles** | | | | | | |
| `GET` | `/security/{v}/config/security-profiles` | listSecurityProfiles | Fetch the list of active security profiles on cluster | 7.6 | — | — | v4.2 |
| `GET` | `/security/{v}/config/security-profiles/{extId}` | getSecurityProfileById | Fetch the active security profile on cluster | 7.6 | — | — | v4.2 |
| `PUT` | `/security/{v}/config/security-profiles/{extId}` | updateSecurityProfileById | Update the security profile for cluster | 7.6 | — | — | v4.2 |
| `GET` | `/security/{v}/config/security-profiles/{securityProfileExtId}/advanced-config` | getAdvancedConfig | Fetch advanced configs for cluster | 7.6 | — | — | v4.2 |
| `PUT` | `/security/{v}/config/security-profiles/{securityProfileExtId}/advanced-config` | updateAdvancedConfig | Update advanced configs for cluster | 7.6 | — | — | v4.2 |
| | **SecuritySummaries** | | | | | | |
| `GET` | `/security/{v}/report/security-summaries` | listSecuritySummaries | Get the overall security status of the ecosystem | 7.5 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/report/security-summaries/$actions/refresh` | RefreshSecuritySummaries | Initiates a refresh operation | 7.5 | — | v4.1 | v4.2 |
| | **Vulnerabilities** | | | | | | |
| `GET` | `/security/{v}/report/vulnerabilities` | listVulnerabilities | Get the vulnerability information | 7.5 | — | v4.1 | v4.2 |

## storage

**Nutanix Storage APIs** — versions GA : aucune ; pré-versions : v4.0.a3

**Preview `v4.0.a3`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `GET` | `/storage/{v}/config/iscsi-clients` | getIscsiClients | Get a list of all the iSCSI clients. | ? |
| `GET` | `/storage/{v}/config/iscsi-clients/{clientId}` | getIscsiClientById | Get an iSCSI client identified by {clientId}. | ? |
| `PATCH` | `/storage/{v}/config/iscsi-clients/{clientId}` | updateIscsiClientById | Update an iSCSI client identified by {clientId}. | ? |
| `GET` | `/storage/{v}/config/storage-containers` | getAllStorageContainers | Get Storage containers for the cluster. | ? |
| `POST` | `/storage/{v}/config/storage-containers` | addStorageContainerForCluster | Add Storage container to the cluster. | ? |
| `GET` | `/storage/{v}/config/storage-containers/datastores` | getDataStores | Get the Data Stores. | ? |
| `DELETE` | `/storage/{v}/config/storage-containers/{containerExtId}` | deleteStorageContainerByExtId | Delete an existing Storage container. | ? |
| `GET` | `/storage/{v}/config/storage-containers/{containerExtId}` | getStorageContainerByExtId | Get existing Storage container. | ? |
| `PUT` | `/storage/{v}/config/storage-containers/{containerExtId}` | updateStorageContainer | Update existing Storage container. | ? |
| `POST` | `/storage/{v}/config/storage-containers/{containerExtId}/$actions/mount` | addDataStoreForCluster | Add a Data Store instance to the cluster. | ? |
| `POST` | `/storage/{v}/config/storage-containers/{containerExtId}/$actions/unmount` | deleteDataStoreForCluster | Delete a Data Store instance in the cluster. | ? |
| `GET` | `/storage/{v}/config/volume-groups` | getVolumeGroups | Get a list of all the Volume Groups. | ? |
| `POST` | `/storage/{v}/config/volume-groups` | createVolumeGroup | Create a new Volume Group. | ? |
| `DELETE` | `/storage/{v}/config/volume-groups/{extId}` | deleteVolumeGroupById | Delete the Volume Group identified by {extId}. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{extId}` | getVolumeGroupById | Get a Volume Group identified by {extId}. | ? |
| `PATCH` | `/storage/{v}/config/volume-groups/{extId}` | updateVolumeGroupById | Update details of a specified Volume Group identified by {extId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/associate-category` | associateCategory | Associate category to a Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/attach-iscsi-client` | attachIscsiClient | Attach an iSCSI client to the given Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/attach-vm` | attachVm | Attach a Vm to the given Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/detach-iscsi-client/{clientId}` | detachIscsiClient | Detach an iSCSi client from the given Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/detach-vm/{vmExtId}` | detachVm | Detach a Vm from the given Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/disassociate-category` | disassociateCategory | Disassociate category from a Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/migrate` | migrateVolumeGroup | Migrate Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/pause-synchronous-replication` | pauseVolumeGroupSynchronousReplication | Pauses replication for a given protected Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/resume-synchronous-replication` | resumeVolumeGroupSynchronousReplication | Resumes replication for a given protected Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/revert` | revertVolumeGroup | Revert a Volume Group identified by {volumeGroupExtId}. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/$actions/update-metadata-info` | updateVolumeGroupMetadataInfo | Updates metadata information associated with a Volume Group. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/category-associations` | getCategoryAssociations | Get a list of all category details that are associated with the Volume Group identified by {volumeGroupExtId}. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/disks` | getVolumeDisks | Get a list of all the Volume Disks. | ? |
| `POST` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/disks` | createVolumeDisk | Create a new Volume Disk. | ? |
| `DELETE` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/disks/{diskExtId}` | deleteVolumeDisk | Delete a Volume Disk identified by {diskExtId}. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/disks/{diskExtId}` | getVolumeDiskById | Get a Volume Disk identified by {diskExtId}. | ? |
| `PATCH` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/disks/{diskExtId}` | updateVolumeDisk | Update a specified Volume Disk identified by {diskExtId}. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/iscsi-client-attachments` | getExternalAttachments | Get a list of all the external attachments associated with the given Volume Group identified by {volumeGroupExtId}. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/metadata-info` | getVolumeGroupMetadataInfo | Fetches metadata information associated with a Volume Group. | ? |
| `GET` | `/storage/{v}/config/volume-groups/{volumeGroupExtId}/vm-attachments` | getVmAttachments | Get a list of all the VM attachments for a Volume Group identified by {volumeGroupExtId}. | ? |

## tenancy

**SP Central Tenant Management** — versions GA : aucune ; pré-versions : v4.0.a1

**Preview `v4.0.a1`** : appels absents des versions GA

| Méthode | Chemin | operationId | Résumé | Min PC |
|---|---|---|---|---|
| `GET` | `/tenancy/{v}/config/domain-memberships` | listDomainMemberships | List memberships | ? |
| `POST` | `/tenancy/{v}/config/domain-memberships` | createDomainMembership | Create membership | ? |
| `DELETE` | `/tenancy/{v}/config/domain-memberships/{extId}` | deleteDomainMembershipById | Delete membership | ? |
| `GET` | `/tenancy/{v}/config/domain-memberships/{extId}` | getDomainMembershipById | Get membership | ? |
| `GET` | `/tenancy/{v}/config/domains` | listDomains | List domains | ? |
| `POST` | `/tenancy/{v}/config/domains` | addDomain | Add domain | ? |
| `GET` | `/tenancy/{v}/config/tenants` | listTenants | List tenants | ? |
| `POST` | `/tenancy/{v}/config/tenants` | createTenant | Create tenant | ? |
| `DELETE` | `/tenancy/{v}/config/tenants/{extId}` | deleteTenantById | Delete tenant | ? |
| `GET` | `/tenancy/{v}/config/tenants/{extId}` | getTenantById | Get tenant | ? |
| `GET` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations` | listTenantDomainAllocations | List tenant domain allocations | ? |
| `POST` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations` | createTenantDomainAllocation | Create tenant domain allocation | ? |
| `GET` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations/{domainAllocationExtId}/external-network-connection` | getTenantExternalNetworkConnection | Get external network connection settings | ? |
| `PUT` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations/{domainAllocationExtId}/external-network-connection` | updateTenantExternalNetworkConnection | Update external network connection settings | ? |
| `DELETE` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations/{extId}` | deleteTenantDomainAllocationById | Delete tenant domain allocation | ? |
| `GET` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations/{extId}` | getTenantDomainAllocationById | Get tenant domain allocation | ? |
| `PUT` | `/tenancy/{v}/config/tenants/{tenantExtId}/domain-allocations/{extId}` | updateTenantDomainAllocationById | Update tenant domain allocation | ? |

## vmm

**Nutanix Virtual Machine Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5, v4.3 → pc.7.6

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **EsxiStats** | | | | | | |
| `GET` | `/vmm/{v}/esxi/stats/vms` | listVmStats | List VM stats for all VMs | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/esxi/stats/vms/{extId}` | getVmStatsById | Get VM stats for a given VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/esxi/stats/vms/{vmExtId}/disks/{extId}` | getDiskStatsById | Get the stats for the specified VM disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/esxi/stats/vms/{vmExtId}/nics/{extId}` | getNicStatsById | Get the stats for the specified VM NIC | 7.0 | v4.0 | v4.2 | v4.3 |
| | **EsxiVm** | | | | | | |
| `GET` | `/vmm/{v}/esxi/config/vms` | listVms | List VMs | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/esxi/config/vms/{extId}` | getVmById | Get VM configuration details | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/assign-owner` | assignVmOwner | Assign owner of a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/associate-categories` | associateCategories | Associate categories to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/disassociate-categories` | disassociateCategories | Disassociate categories from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/guest-reboot` | rebootGuestVm | Issue an ESXi guest OS reboot command | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/guest-shutdown` | shutdownGuestVm | Shut down services on ESXi guest OS | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/power-off` | powerOffVm | Force power off a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/power-on` | powerOnVm | Power on or resume a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/reset` | resetVm | Reset an ESXi VM by sequentially powering it off and on | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/revert` | revertVm | Revert the ESXi VM. | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/$actions/suspend` | suspendVm | Pause/Suspend virtual machine execution | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools` | getNutanixGuestToolsById | Get VM NGT configuration | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools` | updateNutanixGuestToolsById | Update NGT configuration for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools/$actions/insert-iso` | insertNutanixGuestTools | Insert NGT ISO into an available CD-ROM for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools/$actions/install` | installNutanixGuestTools | Install NGT in a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools/$actions/uninstall` | uninstallNutanixGuestTools | Uninstall NGT from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/esxi/config/vms/{extId}/nutanix-guest-tools/$actions/upgrade` | upgradeNutanixGuestTools | Upgrade NGT inside a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| | **GuestRebootPolicies** | | | | | | |
| `GET` | `/vmm/{v}/ahv/policies/guest-reboot-policies` | listGuestRebootPolicies | List Guest Reboot Policies. | 7.6 | — | — | v4.3 |
| `POST` | `/vmm/{v}/ahv/policies/guest-reboot-policies` | createGuestRebootPolicy | Create Guest Reboot Policy. | 7.6 | — | — | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/policies/guest-reboot-policies/{extId}` | deleteGuestRebootPolicyById | Delete Guest Reboot Policy. | 7.6 | — | — | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/guest-reboot-policies/{extId}` | getGuestRebootPolicyById | Get the Guest Reboot Policy configuration based on the provided external identifier. | 7.6 | — | — | v4.3 |
| `PUT` | `/vmm/{v}/ahv/policies/guest-reboot-policies/{extId}` | updateGuestRebootPolicyById | Update Guest Reboot Policy. | 7.6 | — | — | v4.3 |
| | **ImagePlacementPolicies** | | | | | | |
| `GET` | `/vmm/{v}/images/config/placement-policies` | listPlacementPolicies | List image placement policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/images/config/placement-policies` | createPlacementPolicy | Create an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/images/config/placement-policies/{extId}` | deletePlacementPolicyById | Delete an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/images/config/placement-policies/{extId}` | getPlacementPolicyById | Get an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/images/config/placement-policies/{extId}` | updatePlacementPolicyById | Update an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/images/config/placement-policies/{extId}/$actions/resume` | resumePlacementPolicy | Resume an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/images/config/placement-policies/{extId}/$actions/suspend` | suspendPlacementPolicy | Suspend an image placement policy | 7.0 | v4.0 | v4.2 | v4.3 |
| | **ImageRateLimitPolicies** | | | | | | |
| `GET` | `/vmm/{v}/images/config/effective-rate-limit-policies` | listEffectiveRateLimitPolicies | Resolve the effective rate limit for Prism Elements | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/images/config/rate-limit-policies` | listRateLimitPolicies | List image rate limit policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/images/config/rate-limit-policies` | createRateLimitPolicy | Create an image rate limit policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/images/config/rate-limit-policies/{extId}` | deleteRateLimitPolicyById | Delete an image rate limit policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/images/config/rate-limit-policies/{extId}` | getRateLimitPolicyById | Get an image rate limit policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/images/config/rate-limit-policies/{extId}` | updateRateLimitPolicyById | Update the image rate limit policy | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Images** | | | | | | |
| `GET` | `/vmm/{v}/content/images` | listImages | List images | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/images` | createImage | Create an image | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/images/$actions/import` | importImage | Import images from Prism Element | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/content/images/{extId}` | deleteImageById | Delete an image | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/images/{extId}` | getImageById | Get an image | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/content/images/{extId}` | updateImageById | Update an image | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/images/{extId}/$actions/migrate` | migrateImage | Migrate an image to a Content Repository. | 7.6 | — | — | v4.3 |
| `GET` | `/vmm/{v}/content/images/{imageExtId}/file` | getFileByImageId | Download an image | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Ovas** | | | | | | |
| `GET` | `/vmm/{v}/content/ovas` | listOvas | List OVAs | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/ovas` | createOva | Create OVA | 7.3 | — | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/content/ovas/{extId}` | deleteOvaById | Delete an OVA | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/ovas/{extId}` | getOvaById | Get an OVA | 7.3 | — | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/content/ovas/{extId}` | updateOvaById | Update an OVA | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/ovas/{extId}/$actions/deploy` | deployOva | Deploy VMs from an OVA | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/ovas/{ovaExtId}/file` | getFileByOvaId | Download an OVA | 7.3 | — | v4.2 | v4.3 |
| | **Stats** | | | | | | |
| `GET` | `/vmm/{v}/ahv/stats/vms` | listVmStats | List VM stats for all VMs | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/stats/vms/{extId}` | getVmStatsById | Get VM stats for a given VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/stats/vms/{vmExtId}/disks/{extId}` | getDiskStatsById | Get the stats for the specified VM disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/stats/vms/{vmExtId}/nics/{extId}` | getNicStatsById | Get the stats for the specified VM NIC | 7.0 | v4.0 | v4.2 | v4.3 |
| | **TemplatePlacementPolicies** | | | | | | |
| `GET` | `/vmm/{v}/config/template-placement-policies` | listTemplatePlacementPolicies | List template placement policies | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/config/template-placement-policies` | createTemplatePlacementPolicy | Create a template placement policy | 7.3 | — | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/config/template-placement-policies/{extId}` | deleteTemplatePlacementPolicyById | Delete a template placement policy | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/config/template-placement-policies/{extId}` | getTemplatePlacementPolicyById | Get a template placement policy | 7.3 | — | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/config/template-placement-policies/{extId}` | updateTemplatePlacementPolicyById | Update a template placement policy | 7.3 | — | v4.2 | v4.3 |
| | **Templates** | | | | | | |
| `GET` | `/vmm/{v}/content/templates` | listTemplates | List all templates | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates` | createTemplate | Create template from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/content/templates/{extId}` | deleteTemplateById | Delete a template and its associated versions | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/templates/{extId}` | getTemplateById | Get template details | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/content/templates/{extId}` | updateTemplateById | Update a template | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates/{extId}/$actions/cancel-guest-update` | cancelGuestUpdate | Cancel guest OS update | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates/{extId}/$actions/complete-guest-update` | completeGuestUpdate | Complete guest OS update | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates/{extId}/$actions/deploy` | deployTemplate | Deploy VMs from a template | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates/{extId}/$actions/initiate-guest-update` | initiateGuestUpdate | Initiate guest OS updates | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/templates/{extId}/$actions/publish` | publishTemplate | Set an active version | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/templates/{templateExtId}/versions` | listTemplateVersions | List all versions in a template | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/content/templates/{templateExtId}/versions/{extId}` | deleteTemplateVersionById | Delete a template version | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/content/templates/{templateExtId}/versions/{extId}` | getTemplateVersionById | Get the template version detail | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Vm** | | | | | | |
| `GET` | `/vmm/{v}/ahv/config/vms` | listVms | List VMs | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms` | createVm | Create a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{extId}` | deleteVmById | Delete a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{extId}` | getVmById | Get VM configuration details | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vms/{extId}` | updateVmById | Update configuration for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/add-custom-attributes` | addVmCustomAttributes | Add to the VM's custom attributes | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/assign-owner` | assignVmOwner | Assign owner of a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/associate-categories` | associateCategories | Associate categories to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/clone` | cloneVm | Clone a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/customize-guest` | customizeGuestVm | Stage guest customization configuration details | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/disassociate-categories` | disassociateCategories | Disassociate categories from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/generate-console-token` | generateConsoleTokenById | Generate VM console token | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/guest-reboot` | rebootGuestVm | Restart the VM using NGT | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/guest-shutdown` | shutdownGuestVm | Shutdown the VM using NGT | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/migrate` | crossClusterMigrateVm | Migrate a VM across clusters | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/migrate-to-host` | migrateVmToHost | Host to host VM migration | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/migrate-vm-disks` | migrateVmDisks | VmDisk migration between storage containers | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/power-cycle` | powerCycleVm | Force a power cycle for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/power-off` | powerOffVm | Force power off a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/power-on` | powerOnVm | Turn on a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/reboot` | rebootVm | Reboot a VM using ACPI | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/remove-custom-attributes` | removeVmCustomAttributes | Remove from the VM's custom attributes | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/reset` | resetVm | Reset a VM immediately | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/revert` | revertVm | Revert the AHV VM. | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/shutdown` | shutdownVm | Shutdown the VM using ACPI | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/$actions/transfer-files-to-guest` | transferFilesToGuest | Transfer files to the guest VM. | 7.6 | — | — | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools` | getGuestToolsById | Get VM NGT configuration | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools` | updateGuestToolsById | Update NGT configuration for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools/$actions/insert-iso` | insertVmGuestTools | Insert NGT ISO into an available CD-ROM for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools/$actions/install` | installVmGuestTools | Install NGT in a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools/$actions/uninstall` | uninstallVmGuestTools | Uninstall NGT from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{extId}/guest-tools/$actions/upgrade` | upgradeVmGuestTools | Upgrade NGT inside a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms` | listCdRomsByVmId | List CD-ROMs attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms` | createCdRom | Create a CD-ROM device for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}` | deleteCdRomById | Remove a CD-ROM device from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}` | getCdRomById | Get configuration details for the provided CD-ROM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}/$actions/disable-hydration` | disableVmCdRomHydration | Disable hydration for a VM CD-ROM | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}/$actions/eject` | ejectCdRomById | Ejects an ISO from the provided CD-ROM device | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}/$actions/enable-hydration` | enableVmCdRomHydration | Enable hydration for a VM CD-ROM | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/cd-roms/{extId}/$actions/insert` | insertCdRomById | Inserts an ISO in the provided CD-ROM device | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks` | listDisksByVmId | List disks attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks` | createDisk | Create a disk device for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}` | deleteDiskById | Removes the specified disk device from a virtual machine. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}` | getDiskById | Get configuration details for the provided disk device | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}` | updateDiskById | Update the configuration for the provided disk device | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}/$actions/add-custom-attributes` | addVmDiskCustomAttributes | Add to the VM disk's custom attributes | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}/$actions/disable-hydration` | disableVmDiskHydration | Disable hydration for a VM disk | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}/$actions/enable-hydration` | enableVmDiskHydration | Enable hydration for a VM disk | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/disks/{extId}/$actions/remove-custom-attributes` | removeVmDiskCustomAttributes | Remove from the VM disk's custom attributes | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/gpus` | listGpusByVmId | List GPUs attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/gpus` | createGpu | Attach a GPU device to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/gpus/{extId}` | deleteGpuById | Remove a GPU device from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/gpus/{extId}` | getGpuById | Get configuration details for the provided GPU device | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics` | listNicsByVmId | List network devices attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics` | createNic | Create a network device for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}` | deleteNicById | Remove a network device from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}` | getNicById | Get configuration details for the provided network device | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}` | updateNicById | Update the configuration for the provided network device | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}/$actions/assign-ip` | assignIpById | Assign an IP address to the provided network device | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}/$actions/migrate` | migrateNicById | Migrate a network device to another subnet | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/nics/{extId}/$actions/release-ip` | releaseIpById | Release an assigned IP address from the provided network device | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/pcie-devices` | listPcieDevicesByVmId | List PCIe devices attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/pcie-devices` | createPcieDevice | Create a PCIe device for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/pcie-devices/{extId}` | deletePcieDeviceById | Remove a PCIe device from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/pcie-devices/{extId}` | getPcieDeviceById | Get configuration details for the provided PCIe device | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/serial-ports` | listSerialPortsByVmId | List serial ports attached to a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vms/{vmExtId}/serial-ports` | createSerialPort | Create a serial port for a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vms/{vmExtId}/serial-ports/{extId}` | deleteSerialPortById | Remove a serial port from a VM | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vms/{vmExtId}/serial-ports/{extId}` | getSerialPortById | Get configuration details for the provided serial port | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vms/{vmExtId}/serial-ports/{extId}` | updateSerialPortById | Update the configuration for the provided serial port | 7.0 | v4.0 | v4.2 | v4.3 |
| | **VmAntiAffinityPolicies** | | | | | | |
| `GET` | `/vmm/{v}/ahv/policies/legacy-vm-anti-affinity-policies` | listLegacyVmAntiAffinityPolicies | List legacy VM-VM anti-affinity policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/policies/legacy-vm-anti-affinity-policies/{extId}` | deleteLegacyVmAntiAffinityPolicyById | Delete legacy VM-VM anti-affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies` | listVmAntiAffinityPolicies | List VM-VM anti-affinity policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies` | createVmAntiAffinityPolicy | Create VM-VM anti-affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies/{extId}` | deleteVmAntiAffinityPolicyById | Delete VM-VM anti-affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies/{extId}` | getVmAntiAffinityPolicyById | Get VM-VM anti-affinity policy based on the provided external identifier | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies/{extId}` | updateVmAntiAffinityPolicyById | Update VM-VM anti-affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-anti-affinity-policies/{vmAntiAffinityPolicyExtId}/vm-compliance-states` | listVmAntiAffinityPolicyVmComplianceStates | List compliance states of VMs in the VM-VM anti-affinity policy based on the provided external identifier | 7.0 | v4.0 | v4.2 | v4.3 |
| | **VmGuestCustomizationProfiles** | | | | | | |
| `GET` | `/vmm/{v}/ahv/config/vm-guest-customization-profiles` | listVmGuestCustomizationProfiles | List VM Guest Customization Profiles | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-guest-customization-profiles` | createVmGuestCustomizationProfile | Create a VM Guest Customization Profile | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vm-guest-customization-profiles/{extId}` | deleteVmGuestCustomizationProfileById | Delete VM Guest Customization Profile | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vm-guest-customization-profiles/{extId}` | getVmGuestCustomizationProfileById | Get the VM Guest Customization Profile configuration based on the provided external identifier | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vm-guest-customization-profiles/{extId}` | updateVmGuestCustomizationProfileById | Update VM Guest Customization Profile | 7.5 | — | v4.2 | v4.3 |
| | **VmHostAffinityPolicies** | | | | | | |
| `GET` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies` | listVmHostAffinityPolicies | List all the VM-Host Affinity policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies` | createVmHostAffinityPolicy | Create a new VM-host affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies/{extId}` | deleteVmHostAffinityPolicyById | Delete a VM-host affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies/{extId}` | getVmHostAffinityPolicyById | Get the VM-host affinity policy details | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies/{extId}` | updateVmHostAffinityPolicyById | Update the VM-host affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies/{extId}/$actions/re-enforce` | reEnforceVmHostAffinityPolicyById | Re-enforce the VM-host affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-host-affinity-policies/{vmHostAffinityPolicyExtId}/vm-compliance-states` | listVmHostAffinityPolicyVmComplianceStates | List the VM compliance states of the VM-host affinity policy | 7.0 | v4.0 | v4.2 | v4.3 |
| | **VmProfile** | | | | | | |
| `GET` | `/vmm/{v}/ahv/config/vm-profiles` | listVmProfiles | List VM Profiles | 7.6 | — | — | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vm-profiles/{extId}` | getVmProfileById | Get VM Profile configuration details | 7.6 | — | — | v4.3 |
| `PUT` | `/vmm/{v}/ahv/config/vm-profiles/{extId}` | updateVmProfileById | Update configuration for a VM Profile | 7.6 | — | — | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-profiles/{extId}/$actions/deploy` | deployVmFromVmProfile | Deploy VM from VM Profile | 7.6 | — | — | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-profiles/{extId}/$actions/share` | shareVmProfileWithProject | Share VM Profile with Project | 7.6 | — | — | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-profiles/{extId}/$actions/unshare` | unshareVmProfileFromProject | Unshare VM Profile from Project | 7.6 | — | — | v4.3 |
| | **VmRecoveryPoints** | | | | | | |
| `GET` | `/vmm/{v}/ahv/config/vm-recovery-points` | listVmRecoveryPoints | List AHV VM recovery points | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-recovery-points` | createVmRecoveryPoint | Create AHV VM recovery point | 7.3 | — | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/config/vm-recovery-points/{extId}` | deleteVmRecoveryPointByExtId | Delete AHV VM recovery point | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/config/vm-recovery-points/{extId}` | getVmRecoveryPointByExtId | Retrieve AHV VM recovery point details | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/config/vm-recovery-points/{extId}/$actions/restore` | restoreVmRecoveryPoint | Restore a new VM from an AHV VM recovery point. | 7.3 | — | v4.2 | v4.3 |
| | **VmStartupPolicies** | | | | | | |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies` | listVmStartupPolicies | List VM startup policies | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/ahv/policies/vm-startup-policies` | createVmStartupPolicy | Create VM startup policy | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/vmm/{v}/ahv/policies/vm-startup-policies/{extId}` | deleteVmStartupPolicyById | Delete VM startup policy | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{extId}` | getVmStartupPolicyById | Get the VM startup policy based on the provided external identifier | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/vmm/{v}/ahv/policies/vm-startup-policies/{extId}` | updateVmStartupPolicyById | Update VM startup policy | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/dependency-conflicts` | listVmStartupPolicyDependencyConflicts | List Dependency conflicts of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/dependency-conflicts/{dependencyConflictExtId}/dependee-vms` | listVmStartupPolicyDependencyConflictDependeeVms | List dependee VMs of a Dependency conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/dependency-conflicts/{dependencyConflictExtId}/dependent-vms` | listVmStartupPolicyDependencyConflictDependentVms | List dependent VMs of a Dependency conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/dependency-conflicts/{extId}` | getVmStartupPolicyDependencyConflictById | Get Dependency conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/start-condition-conflicts` | listVmStartupPolicyStartConditionConflicts | List Start condition conflicts of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/start-condition-conflicts/{extId}` | getVmStartupPolicyStartConditionConflictById | Get Start condition conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/start-condition-conflicts/{startConditionConflictExtId}/dependee-vms` | listVmStartupPolicyStartConditionConflictDependeeVms | List dependee VMs of a Start condition conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/start-condition-conflicts/{startConditionConflictExtId}/dependent-vms` | listVmStartupPolicyStartConditionConflictDependentVms | List dependent VMs of a Start condition conflict of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/vmm/{v}/ahv/policies/vm-startup-policies/{vmStartupPolicyExtId}/vm-compliance-states` | listVmStartupPolicyVmComplianceStates | List VM compliances of a VM startup policy. | 7.5 | — | v4.2 | v4.3 |

## volumes

**Nutanix Volumes APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release PC par version : v4.0 → pc.2024.3 (AOS 7.0), v4.1 → pc.7.3, v4.2 → pc.7.5\*, v4.3 → pc.7.5\*

| Méthode | Chemin | operationId | Résumé | Min PC | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **IscsiClients** | | | | | | |
| `GET` | `/volumes/{v}/config/iscsi-clients` | listIscsiClients | List all the iSCSI clients | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/iscsi-clients/{extId}` | getIscsiClientById | Fetch an iSCSI client details | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/volumes/{v}/config/iscsi-clients/{extId}` | updateIscsiClientById | Update an iSCSI client | 7.0 | v4.0 | v4.3 | v4.3 |
| | **NvmfClients** | | | | | | |
| `GET` | `/volumes/{v}/config/nvmf-clients` | listNvmfClients | List all NVMe-TCP clients | 7.3 | — | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/nvmf-clients/{extId}` | getNvmfClientById | Get a NVMe-TCP client details | 7.3 | — | v4.3 | v4.3 |
| | **VolumeGroups** | | | | | | |
| `GET` | `/volumes/{v}/config/volume-groups` | listVolumeGroups | List all the Volume Groups | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups` | createVolumeGroup | Creates a new Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/volumes/{v}/config/volume-groups/{extId}` | deleteVolumeGroupById | Delete the Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{extId}` | getVolumeGroupById | Get a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/volumes/{v}/config/volume-groups/{extId}` | updateVolumeGroupById | Update details of a specified Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/associate-category` | associateCategory | Associate category to a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-iscsi-client` | attachIscsiClient | Attach an iSCSI client to the given Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-nvmf-client` | attachNvmfClient | Attach an NVMe-TCP client to the given Volume Group | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-vm` | attachVm | Attach an AHV VM to the given Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-iscsi-client` | detachIscsiClient | Detach an iSCSi client from the given Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-nvmf-client` | detachNvmfClient | Detach a NVMe-TCP client from the given Volume Group | 7.3 | — | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-vm` | detachVm | Detach an AHV VM from the given Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/disassociate-category` | disassociateCategory | Disassociate category from a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/revert` | revertVolumeGroup | Revert a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/category-associations` | listCategoryAssociationsByVolumeGroupId ⚠️ | List all the category details that are associated with the Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks` | listVolumeDisksByVolumeGroupId | List all the Volume Disks attached to the Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks` | createVolumeDisk | Creates a new Volume Disk | 7.0 | v4.0 | v4.3 | v4.3 |
| `DELETE` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | deleteVolumeDiskById | Delete a Volume Disk | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | getVolumeDiskById | Get the details of a Volume Disk | 7.0 | v4.0 | v4.3 | v4.3 |
| `PUT` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | updateVolumeDiskById | Update a specified Volume Disk | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/external-iscsi-attachments` | listExternalIscsiAttachmentsByVolumeGroupId ⚠️ | List all the iSCSI attachments associated with the given Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/metadata` | getVolumeGroupMetadataById ⚠️ | Fetch metadata information associated with a Volume Group. | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/vm-attachments` | listVmAttachmentsByVolumeGroupId ⚠️ | List all the VM attachments for a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/stats/volume-groups/{extId}` | getVolumeGroupStats | Get statistics for a Volume Group | 7.0 | v4.0 | v4.3 | v4.3 |
| `GET` | `/volumes/{v}/stats/volume-groups/{volumeGroupExtId}/disks/{extId}` | getVolumeDiskStats | Get statistics for a Volume Disk | 7.0 | v4.0 | v4.3 | v4.3 |

