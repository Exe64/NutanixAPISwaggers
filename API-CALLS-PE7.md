# Référence des appels API Nutanix v4 servis par Prism Element, par version d'AOS

Généré par `gen_api_calls.py PE` depuis les specs OpenAPI de <https://developers.nutanix.com/api-reference> (dossier `specs/json/`), via l'extension `x-supported-versions` (product `PE`) de chaque opération. Version machine : `api-calls-pe7.json`. Pendant côté Prism Central : `API-CALLS-PC7.md`.

## Comment lire ce document

- Seules figurent les opérations que Nutanix déclare servies par le **Prism Element** (entrée `PE` dans `x-supported-versions`). Tout le reste n'existe que sur le Prism Central. Namespaces absents ici (aiops, files, iam, licensing, microseg, monitoring, opsmgmt, storage, tenancy) : PC uniquement.
- Colonnes **AOS 7.0 / 7.5 / 7.6** : version d'API à mettre à la place de `{v}`, `—` = appel absent. AOS 7.3 n'a pas de colonne mais apparaît dans *Min AOS*.
- Chemin complet : `https://<cvm-ou-vip>:9440/api` + chemin, ex. `/clustermgmt/{v}/config/clusters` → `https://<vip>:9440/api/clustermgmt/v4.0/config/clusters`.
- Correspondance version d'API → AOS déduite comme côté PC : release d'une version GA = max(Min AOS de ses opérations PE, release de la version précédente, plus petite release où un autre namespace a introduit des appels PE dans ce numéro de version). **\*** = version datée par ces deux dernières règles seulement : la tester sur l'AOS visé, ou retomber sur la version précédente.
- *Min AOS* normalisé : `6.1`…`7.0.1.6` → 7.0 (tout est servi par AOS 7.0) ; `Janus` (branche non publiée) → 7.6, **à vérifier**.
- Les API historiques du PE (`/PrismGateway/services/rest/v1`, `v2.0`, `/api/nutanix/v3`) ne sont pas publiées en OpenAPI sur ce portail et ne figurent pas ici.
- **Preview** : appels PE des versions beta/alpha plus récentes que la dernière GA, hors matrice.
- ⚠️ = opération marquée `deprecated` dans la spec.

## Vue d'ensemble : version d'API par namespace et par AOS

| Namespace | Titre | AOS 7.0 | AOS 7.5 | AOS 7.6 | Appels GA | Preview |
|---|---|---|---|---|---|---|
| [`clustermgmt`](#clustermgmt) | Nutanix Cluster Management APIs | v4.0 | v4.2 | v4.4\* | 109 |  |
| [`datapolicies`](#datapolicies) | Nutanix Data Policies APIs | v4.0 | v4.2 | v4.3\* | 43 |  |
| [`dataprotection`](#dataprotection) | Nutanix Data Protection APIs | v4.0 | v4.2 | v4.4 | 34 |  |
| [`lifecycle`](#lifecycle) | Nutanix Lifecycle Management APIs | v4.0 | v4.2 | v4.3\* | 29 |  |
| [`multidomain`](#multidomain) | Nutanix Multidomain Versioned APIs | — | v4.2 | v4.3\* | 5 | v4.4.b1 |
| [`networking`](#networking) | Nutanix Networking APIs | v4.0 | v4.2\* | v4.4\* | 15 |  |
| [`objects`](#objects) | Nutanix Objects Storage Management APIs | v4.0 | v4.1\* | v4.1\* | 17 |  |
| [`prism`](#prism) | Nutanix Prism APIs | v4.0 | v4.2\* | v4.4\* | 10 |  |
| [`security`](#security) | Nutanix Security APIs | — | v4.1 | v4.2 | 15 |  |
| [`vmm`](#vmm) | Nutanix Virtual Machine Management APIs | v4.0 | v4.2 | v4.3 | 156 |  |
| [`volumes`](#volumes) | Nutanix Volumes APIs | v4.0 | v4.2\* | v4.3\* | 30 |  |

## clustermgmt

**Nutanix Cluster Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3, v4.2 → AOS 7.5, v4.3 → AOS 7.6, v4.4 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
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
| | **Clusters** | | | | | | |
| `GET` | `/clustermgmt/{v}/config/clusters` | listClusters | Get the list of clusters | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters` | createCluster | Create a cluster | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/check-hypervisor-requirements` | checkHypervisorRequirements | Get hypervisor ISO upload information | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/$actions/compute-non-migratable-vms` | computeNonMigratableVms | Compute non-migratable VMs | 7.0 | — | — | v4.4 |
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
| `GET` | `/clustermgmt/{v}/config/clusters/{clusterExtId}/non-migratable-vms-result/{extId}` | getNonMigratableVmsResultById | Get the details of non-migratable VMs | 7.0 | — | — | v4.4 |
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

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3, v4.2 → AOS 7.5, v4.3 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **EntitySyncPolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/entity-sync-policies` | listEntitySyncPolicies | List entity sync policies | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/entity-sync-policies/{extId}` | getEntitySyncPolicyById | Get an entity sync policy | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/entity-sync-policies/{extId}/$actions/sync-entity` | syncEntitySyncPolicyById | Sync entity identified by its identifier to a remote domain manager | 7.3 | — | v4.2 | v4.3 |
| | **ProtectionPolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/protection-policies` | listProtectionPolicies | List protection policies | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/protection-policies` | createProtectionPolicy | Create a protection policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/protection-policies/{extId}` | deleteProtectionPolicyById | Delete a protection policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{extId}` | getProtectionPolicyById | Get a protection policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/protection-policies/{extId}` | updateProtectionPolicyById | Update a protection policy | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules` | listConsistencyRulesByProtectionPolicyId | List consistency rules | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules` | createConsistencyRule | Create a consistency rule | 7.3 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | deleteConsistencyRuleById | Delete a consistency rule | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | getConsistencyRuleById | Get details of a consistency rule | 7.3 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/protection-policies/{protectionPolicyExtId}/consistency-rules/{extId}` | updateConsistencyRuleById | Update a consistency rule | 7.3 | — | v4.2 | v4.3 |
| | **RecoveryPlans** | | | | | | |
| `GET` | `/datapolicies/{v}/config/recovery-plans` | listRecoveryPlans | List Recovery Plans | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans` | createRecoveryPlan | Create a Recovery Plan | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{extId}` | deleteRecoveryPlanById | Delete a Recovery Plan | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{extId}` | getRecoveryPlanById | Get a Recovery Plan | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{extId}` | updateRecoveryPlanById | Update a Recovery Plan | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings` | listDataServicesIpMappings | List Data Services IP Mappings | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings` | createDataServicesIpMapping | Create a Data Services IP Mapping | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | deleteDataServicesIpMappingById | Delete a Data Services IP Mapping | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | getDataServicesIpMappingById | Get a Data services IP mapping | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/data-services-ip-mappings/{extId}` | updateDataServicesIpMappingById | Update a Data Services IP Mapping | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings` | listNetworkMappings | List Network Mappings | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings` | createNetworkMapping | Create a Network Mapping | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | deleteNetworkMappingById | Delete a Network Mapping | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | getNetworkMappingById | Get a Network Mapping | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/network-mappings/{extId}` | updateNetworkMappingById | Update a Network Mapping | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings` | listRecoverySettings | List custom recovery settings | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings` | createRecoverySetting | Create a custom recovery setting for VM or Volume Groups. | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | deleteRecoverySettingById | Delete recovery setting | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | getRecoverySettingById | Get the custom recovery setting | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/recovery-settings/{extId}` | updateRecoverySettingById | Update recovery setting | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages` | listRecoveryStages | List Recovery stages | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages` | createRecoveryStage | Create a Recovery stage | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | deleteRecoveryStageById | Delete Recovery stage | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | getRecoveryStageById | Get a Recovery stage | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/recovery-plans/{recoveryPlanExtId}/stages/{extId}` | updateRecoveryStageById | Update a Recovery stage | 7.5 | — | v4.2 | v4.3 |
| | **StoragePolicies** | | | | | | |
| `GET` | `/datapolicies/{v}/config/storage-policies` | listStoragePolicies | Get a list of Storage Policies | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/datapolicies/{v}/config/storage-policies` | createStoragePolicy | Create a Storage Policy | 7.3 | — | v4.2 | v4.3 |
| `DELETE` | `/datapolicies/{v}/config/storage-policies/{extId}` | deleteStoragePolicyById | Delete an existing Storage Policy | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/datapolicies/{v}/config/storage-policies/{extId}` | getStoragePolicyById | Get a Storage Policy based on external identifier | 7.3 | — | v4.2 | v4.3 |
| `PUT` | `/datapolicies/{v}/config/storage-policies/{extId}` | updateStoragePolicyById | Update an existing Storage Policy | 7.3 | — | v4.2 | v4.3 |

## dataprotection

**Nutanix Data Protection APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3\*, v4.2 → AOS 7.5, v4.3 → AOS 7.6\*, v4.4 → AOS 7.6

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **ConsistencyGroups** | | | | | | |
| `GET` | `/dataprotection/{v}/config/consistency-groups` | listConsistencyGroups | List consistency groups | 7.0 | — | v4.2 | — |
| `POST` | `/dataprotection/{v}/config/consistency-groups` | createConsistencyGroup | Create a consistency group | 7.0 | — | v4.2 | — |
| `DELETE` | `/dataprotection/{v}/config/consistency-groups/{extId}` | deleteConsistencyGroupById | Delete a consistency group | 7.0 | — | v4.2 | — |
| `GET` | `/dataprotection/{v}/config/consistency-groups/{extId}` | getConsistencyGroupById | Get details of a consistency group | 7.0 | — | v4.2 | — |
| `PUT` | `/dataprotection/{v}/config/consistency-groups/{extId}` | updateConsistencyGroupById | Update a consistency group | 7.0 | — | v4.2 | — |
| | **DataProtectionClusterCapabilities** | | | | | | |
| `GET` | `/dataprotection/{v}/config/cluster-capabilities` | listDataProtectionClusterCapabilities | Get data protection cluster capabilities | 7.5 | — | v4.2 | v4.4 |
| | **ProtectedResources** | | | | | | |
| `GET` | `/dataprotection/{v}/config/protected-resources/{extId}` | getProtectedResourceById | Get a protected resource | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/protected-resources/{extId}/$actions/promote` | promoteProtectedResource | Promote protected resource | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/protected-resources/{extId}/$actions/restore` | restoreProtectedResource | Restore protected resource | 7.0 | v4.0 | v4.2 | v4.4 |
| | **RecoveryPlanActions** | | | | | | |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/clean-up-resources` | cleanupRecoveryPlanResources | Cleanup resources on the last Recovery Plan execution | 7.5 | — | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/planned-failover` | plannedFailoverRecoveryPlan | Planned Failover Recovery Plan | 7.5 | — | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/resume-protection` | resumeProtection | Resume Protection on Recovery Plan | 7.6 | — | — | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/test-failover` | testFailoverRecoveryPlan | Test Failover Recovery Plan | 7.5 | — | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/unplanned-failover` | unplannedFailoverRecoveryPlan | Unplanned Failover Recovery Plan | 7.5 | — | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/operations/recovery-plans/{recoveryPlanExtId}/$actions/validate` | validateRecoveryPlan | Validate Recovery Plan | 7.5 | — | v4.2 | v4.4 |
| | **RecoveryPlanJobs** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs` | listRecoveryPlanJobs | List Recovery Plan Jobs | 7.5 | — | v4.2 | v4.4 |
| `DELETE` | `/dataprotection/{v}/config/recovery-plan-jobs/{extId}` | deleteRecoveryPlanJobById | Delete Recovery Plan Job | 7.5 | — | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{extId}` | getRecoveryPlanJobById | Get Recovery Plan Job | 7.5 | — | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{recoveryPlanJobExtId}/execution-steps` | listExecutionStepsByRecoveryPlanJobId | List Recovery Plan Job Execution Steps | 7.5 | — | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-plan-jobs/{recoveryPlanJobExtId}/validation-errors` | listValidationErrorsByRecoveryPlanJobId | List Recovery Plan Job Validation Errors | 7.5 | — | v4.2 | v4.4 |
| | **RecoveryPointStores** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-point-stores` | listRecoveryPointStores | List recovery point stores | 7.6 | — | — | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-point-stores/{extId}` | getRecoveryPointStoreById | Get a recovery point store. | 7.6 | — | — | v4.4 |
| | **RecoveryPoints** | | | | | | |
| `GET` | `/dataprotection/{v}/config/recovery-points` | listRecoveryPoints | List recovery points | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points` | createRecoveryPoint | Create a recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/dataprotection/{v}/config/recovery-points/{extId}` | deleteRecoveryPointById | Delete a recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-points/{extId}` | getRecoveryPointById | Get a recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/discover-cluster` | discoverClusterForRecoveryPointId | Discover cluster info for a recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/replicate` | replicateRecoveryPoint | Replicate a recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/restore` | restoreRecoveryPoint | Restore recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/config/recovery-points/{extId}/$actions/set-expiration-time` | setRecoveryPointExpirationTime | Set the expiration time of the recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/config/recovery-points/{recoveryPointExtId}/vm-recovery-points/{extId}` | getVmRecoveryPointById | Get a VM recovery point | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/vm-recovery-points/{vmRecoveryPointExtId}/disk-recovery-points/{extId}/$actions/compute-changed-regions` | vmRecoveryPointComputeChangedRegions | Compute VM recovery points changed regions | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/vm-recovery-points/{vmRecoveryPointExtId}/vss-metadata` | getVssMetadataByVmRecoveryPointId | Get VSS metadata by VM recovery point ID | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/dataprotection/{v}/content/recovery-points/{recoveryPointExtId}/volume-group-recovery-points/{volumeGroupRecoveryPointExtId}/disk-recovery-points/{extId}/$actions/compute-changed-regions` | volumeGroupRecoveryPointComputeChangedRegions | Compute Volume Group recovery points changed regions | 7.0 | v4.0 | v4.2 | v4.4 |

## lifecycle

**Nutanix Lifecycle Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3\*, v4.2 → AOS 7.5, v4.3 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Bundles** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/bundles` | listBundles | Get LCM bundles on the cluster | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/bundles` | createBundle | Create a new LCM bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/lifecycle/{v}/resources/bundles/{extId}` | deleteBundleById | Delete an LCM bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/bundles/{extId}` | getBundleById | Information about a bundle | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Config** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/config` | getConfig | Get the present LCM configuration. | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/lifecycle/{v}/resources/config` | updateConfig | Change the LCM configuration. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Entities** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/preload-artifacts` | preloadArtifacts | Preload artifacts on to the cluster. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/entities` | listEntities | Get details about all LCM entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/entities/$actions/export` | exportInventory | Export inventory information (the list of LCM entities) in the connected clusters. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/entities/{extId}` | getEntityById | Get details about an LCM entity. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Images** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/images` | listImages | Get the list of downloaded LCM images. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Inventory** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/inventory` | performInventory | Perform an inventory operation to identify/scan entities on the cluster that can be updated through LCM. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **LcmHistories** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/lcm-histories` | listLcmHistories | Summary of the queried LCM histories. | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/lcm-histories/$actions/export` | exportHistories | Export the history information of connected clusters. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/lcm-histories/{extId}` | getLcmHistoryById | Get details about an LCM history entry. | 7.5 | — | v4.2 | v4.3 |
| | **LcmSummaries** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/lcm-summaries` | listLcmSummaries | List the LCM summaries. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/lcm-summaries/{extId}` | getLcmSummaryById | Get the LCM summary. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Notifications** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/compute-notifications` | ComputeNotifications | Compute LCM upgrade plan and notifications for a set of entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/notifications/{extId}` | GetNotificationById | Get LCM upgrade notification details for specified resource UUID. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Prechecks** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/prechecks` | performPrechecks | Perform LCM prechecks operation. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Recommendations** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/compute-recommendations` | computeRecommendations | Compute LCM recommendations for a set of entities. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/recommendations/{extId}` | GetRecommendationById | Get a list of update recommendations from LCM. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **Status** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/status` | getStatus | Get the LCM framework status. | 7.0 | v4.0 | v4.2 | v4.3 |
| | **UpgradeSelections** | | | | | | |
| `GET` | `/lifecycle/{v}/resources/upgrade-selections` | listUpgradeSelections | Get the LCM Upgrade Selections on the cluster | 7.0 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/upgrade-selections` | createUpgradeSelection | Create a new LCM Upgrade Selection | 7.0 | — | v4.2 | v4.3 |
| `DELETE` | `/lifecycle/{v}/resources/upgrade-selections/{extId}` | deleteUpgradeSelectionById | Delete LCM upgrade selection | 7.0 | — | v4.2 | v4.3 |
| `GET` | `/lifecycle/{v}/resources/upgrade-selections/{extId}` | getUpgradeSelectionById | Information about the upgrade selection made on the cluster | 7.0 | — | v4.2 | v4.3 |
| `POST` | `/lifecycle/{v}/resources/upgrade-selections/{extId}/$actions/export` | exportUpgradeSelection | Download the darksite upgrade orchestrator helper scripts which are packaged in the download_helper.zip file | 7.0 | — | v4.2 | v4.3 |
| | **Upgrades** | | | | | | |
| `POST` | `/lifecycle/{v}/operations/$actions/upgrade` | performUpgrade | Perform an LCM upgrade operation. | 7.0 | v4.0 | v4.2 | v4.3 |

## multidomain

**Nutanix Multidomain Versioned APIs** — versions GA : v4.2, v4.3 ; pré-versions : v4.4.b1

Release AOS par version : v4.2 → AOS 7.5, v4.3 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **ExternalRepositories** | | | | | | |
| `GET` | `/multidomain/{v}/config/external-repositories` | listExternalRepositories | List External repositories. | 7.5 | — | v4.2 | v4.3 |
| `POST` | `/multidomain/{v}/config/external-repositories` | createExternalRepository | Create an External repository. | 7.5 | — | v4.2 | v4.3 |
| `DELETE` | `/multidomain/{v}/config/external-repositories/{extId}` | deleteExternalRepositoryById | Delete an External repository. | 7.5 | — | v4.2 | v4.3 |
| `GET` | `/multidomain/{v}/config/external-repositories/{extId}` | getExternalRepositoryById | Get an External repository by id. | 7.5 | — | v4.2 | v4.3 |
| `PUT` | `/multidomain/{v}/config/external-repositories/{extId}` | updateExternalRepositoryById | Update an External repository. | 7.5 | — | v4.2 | v4.3 |

## networking

**Nutanix Networking APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3\*, v4.2 → AOS 7.5\*, v4.3 → AOS 7.6\*, v4.4 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **AwsSubnets** | | | | | | |
| `GET` | `/networking/{v}/aws/config/subnets` | listAwsSubnets | Get NC2A subnets. | 7.0 | v4.0 | v4.2 | v4.4 |
| | **AwsVpcs** | | | | | | |
| `GET` | `/networking/{v}/aws/config/vpcs` | listAwsVpcs | Get NC2A VPCs. | 7.0 | v4.0 | v4.2 | v4.4 |
| | **Capabilities** | | | | | | |
| `GET` | `/networking/{v}/aws/config/capabilities` | getCapabilities | Get NC2A capabilities | 7.0 | v4.0 | — | — |
| | **Subnets** | | | | | | |
| `GET` | `/networking/{v}/config/subnets` | listSubnets | Get the list of existing subnets. | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/networking/{v}/config/subnets` | createSubnet | Create a subnet. | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/networking/{v}/config/subnets/{extId}` | deleteSubnetById | Delete the specified subnet. | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/networking/{v}/config/subnets/{extId}` | getSubnetById | Get the subnet with the specified UUID. | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/networking/{v}/config/subnets/{extId}` | updateSubnetById | Update the specified subnet. | 7.0 | v4.0 | v4.2 | v4.4 |
| | **VirtualSwitches** | | | | | | |
| `GET` | `/networking/{v}/config/node-schedulable-statuses` | listNodeSchedulableStatus | Check whether a node in a cluster is a storage-only node or not | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/networking/{v}/config/virtual-switches` | listVirtualSwitches | Get list of Virtual Switches | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/networking/{v}/config/virtual-switches` | createVirtualSwitch | Create a Virtual Switch | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/networking/{v}/config/virtual-switches/$actions/migrate` | migrateBridge | Create a Virtual Switch from an existing bridge | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/networking/{v}/config/virtual-switches/{extId}` | deleteVirtualSwitchById | Delete a Virtual Switch | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/networking/{v}/config/virtual-switches/{extId}` | getVirtualSwitchById | Get single Virtual Switch given its UUID | 7.0 | v4.0 | v4.2 | v4.4 |
| `PUT` | `/networking/{v}/config/virtual-switches/{extId}` | updateVirtualSwitchById | Update a Virtual Switch | 7.0 | v4.0 | v4.2 | v4.4 |

## objects

**Nutanix Objects Storage Management APIs** — versions GA : v4.0, v4.1

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **Buckets** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/buckets` | listBucketsByObjectstoreId | Get a list of the buckets in an Object store | 7.0 | — | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/buckets/{bucketName}` | getBucketByName | Get details of a specific bucket | 7.0 | — | v4.1 | v4.1 |
| | **DataMovementTargets** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets` | listDataMovementTargets | Get a list of the data movement targets configured in an Object store | 7.0 | — | v4.1 | v4.1 |
| `POST` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets` | createDataMovementTarget | Create a new data movement target for the specified Object store | 7.0 | — | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/data-movement-targets/{extId}` | getDataMovementTargetById | Get details of a data movement target | 7.0 | — | v4.1 | v4.1 |
| | **ObjectStores** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores` | listObjectstores | Get a list of the Object stores | 7.0 | v4.0 | v4.1 | v4.1 |
| `POST` | `/objects/{v}/config/object-stores` | createObjectstore | Create an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `DELETE` | `/objects/{v}/config/object-stores/{extId}` | deleteObjectstoreById | Delete an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{extId}` | getObjectstoreById | Get an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `PUT` | `/objects/{v}/config/object-stores/{extId}` | updateObjectstoreById | Update an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates` | listCertificatesByObjectstoreId | Get a list of the SSL certificates of an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `POST` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates` | createCertificate | Create a SSL certificate for an Object store | 7.0 | v4.0 | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates/{certificateExtId}/certificate-authority` | getCaByCertificateId | Download the certificate authority | 7.0 | v4.0 | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/certificates/{extId}` | getCertificateById | Get the details of an Object store certificate | 7.0 | v4.0 | v4.1 | v4.1 |
| | **Stats** | | | | | | |
| `GET` | `/objects/{v}/stats/object-stores/{extId}` | getObjectstoreStatsById | Get the Object store stats | 7.0 | v4.0 | v4.1 | v4.1 |
| | **StorageBackends** | | | | | | |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/storage-backends` | listStorageBackends | Get a list of the storage backends configured in an Object store | 7.0 | — | v4.1 | v4.1 |
| `GET` | `/objects/{v}/config/object-stores/{objectStoreExtId}/storage-backends/{extId}` | getStorageBackendById | Get the details of a storage backend | 7.0 | — | v4.1 | v4.1 |

## prism

**Nutanix Prism APIs** — versions GA : v4.0, v4.1, v4.2, v4.3, v4.4

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3\*, v4.2 → AOS 7.5\*, v4.3 → AOS 7.6\*, v4.4 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **DomainManager** | | | | | | |
| `POST` | `/prism/{v}/config/domain-managers` | createDomainManager | Deploy a Prism Central | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets` | listBackupTargets | List backup targets | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/domain-managers/{domainManagerExtId}/backup-targets/{extId}` | getBackupTargetById | Fetch backup target | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/prism/{v}/management/restore-sources` | createRestoreSource | Create restore source | 7.0 | v4.0 | v4.2 | v4.4 |
| `DELETE` | `/prism/{v}/management/restore-sources/{extId}` | deleteRestoreSourceById | Delete restore source | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{extId}` | getRestoreSourceById | Fetch restore source | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers` | listRestorableDomainManagers | List restorable domain managers | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points` | listRestorePoints | List restore points | 7.0 | v4.0 | v4.2 | v4.4 |
| `GET` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points/{extId}` | getRestorePointById | Get restore point details | 7.0 | v4.0 | v4.2 | v4.4 |
| `POST` | `/prism/{v}/management/restore-sources/{restoreSourceExtId}/restorable-domain-managers/{restorableDomainManagerExtId}/restore-points/{extId}/$actions/restore` | restore | Restore domain manager | 7.0 | v4.0 | v4.2 | v4.4 |

## security

**Nutanix Security APIs** — versions GA : v4.0, v4.1, v4.2

Release AOS par version : v4.0 → AOS 7.3, v4.1 → AOS 7.5, v4.2 → AOS 7.6

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **KeyManagementServers** | | | | | | |
| `GET` | `/security/{v}/config/key-management-servers` | listKeyManagementServers | List key management servers | 7.3 | — | v4.1 | v4.2 |
| `POST` | `/security/{v}/config/key-management-servers` | createKeyManagementServer | Create a key management server | 7.3 | — | v4.1 | v4.2 |
| `DELETE` | `/security/{v}/config/key-management-servers/{extId}` | deleteKeyManagementServerById | Delete a key management server | 7.3 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/config/key-management-servers/{extId}` | getKeyManagementServerById | Get details of a key management server | 7.3 | — | v4.1 | v4.2 |
| `PUT` | `/security/{v}/config/key-management-servers/{extId}` | updateKeyManagementServerById | Update a key management server | 7.3 | — | v4.1 | v4.2 |
| | **STIGs** | | | | | | |
| `GET` | `/security/{v}/report/stig-summaries` | listStigSummaries ⚠️ | Fetch the aggregate report of STIG scan | 7.0 | — | v4.1 | v4.2 |
| `GET` | `/security/{v}/report/stigs` | listStigs | Get the STIG controls details | 7.0 | — | v4.1 | v4.2 |
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

## vmm

**Nutanix Virtual Machine Management APIs** — versions GA : v4.0, v4.1, v4.2, v4.3

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3, v4.2 → AOS 7.5, v4.3 → AOS 7.6

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
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
| | **Images** | | | | | | |
| `POST` | `/vmm/{v}/content/images` | createImage | Create an image | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/vmm/{v}/content/images/{extId}/$actions/migrate` | migrateImage | Migrate an image to a Content Repository. | 7.0 | — | — | v4.3 |
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

Release AOS par version : v4.0 → AOS 7.0, v4.1 → AOS 7.3, v4.2 → AOS 7.5\*, v4.3 → AOS 7.6\*

| Méthode | Chemin | operationId | Résumé | Min AOS | 7.0 | 7.5 | 7.6 |
|---|---|---|---|---|---|---|---|
| | **IscsiClients** | | | | | | |
| `GET` | `/volumes/{v}/config/iscsi-clients` | listIscsiClients | List all the iSCSI clients | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/iscsi-clients/{extId}` | getIscsiClientById | Fetch an iSCSI client details | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/volumes/{v}/config/iscsi-clients/{extId}` | updateIscsiClientById | Update an iSCSI client | 7.0 | v4.0 | v4.2 | v4.3 |
| | **NvmfClients** | | | | | | |
| `GET` | `/volumes/{v}/config/nvmf-clients` | listNvmfClients | List all NVMe-TCP clients | 7.3 | — | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/nvmf-clients/{extId}` | getNvmfClientById | Get a NVMe-TCP client details | 7.3 | — | v4.2 | v4.3 |
| | **VolumeGroups** | | | | | | |
| `GET` | `/volumes/{v}/config/volume-groups` | listVolumeGroups | List all the Volume Groups | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups` | createVolumeGroup | Creates a new Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/volumes/{v}/config/volume-groups/{extId}` | deleteVolumeGroupById | Delete the Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{extId}` | getVolumeGroupById | Get a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/volumes/{v}/config/volume-groups/{extId}` | updateVolumeGroupById | Update details of a specified Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/associate-category` | associateCategory | Associate category to a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-iscsi-client` | attachIscsiClient | Attach an iSCSI client to the given Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-nvmf-client` | attachNvmfClient | Attach an NVMe-TCP client to the given Volume Group | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/attach-vm` | attachVm | Attach an AHV VM to the given Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-iscsi-client` | detachIscsiClient | Detach an iSCSi client from the given Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-nvmf-client` | detachNvmfClient | Detach a NVMe-TCP client from the given Volume Group | 7.3 | — | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/detach-vm` | detachVm | Detach an AHV VM from the given Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/disassociate-category` | disassociateCategory | Disassociate category from a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{extId}/$actions/revert` | revertVolumeGroup | Revert a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/category-associations` | listCategoryAssociationsByVolumeGroupId ⚠️ | List all the category details that are associated with the Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks` | listVolumeDisksByVolumeGroupId | List all the Volume Disks attached to the Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `POST` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks` | createVolumeDisk | Creates a new Volume Disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `DELETE` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | deleteVolumeDiskById | Delete a Volume Disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | getVolumeDiskById | Get the details of a Volume Disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `PUT` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/disks/{extId}` | updateVolumeDiskById | Update a specified Volume Disk | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/external-iscsi-attachments` | listExternalIscsiAttachmentsByVolumeGroupId ⚠️ | List all the iSCSI attachments associated with the given Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/metadata` | getVolumeGroupMetadataById ⚠️ | Fetch metadata information associated with a Volume Group. | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/config/volume-groups/{volumeGroupExtId}/vm-attachments` | listVmAttachmentsByVolumeGroupId ⚠️ | List all the VM attachments for a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/stats/volume-groups/{extId}` | getVolumeGroupStats | Get statistics for a Volume Group | 7.0 | v4.0 | v4.2 | v4.3 |
| `GET` | `/volumes/{v}/stats/volume-groups/{volumeGroupExtId}/disks/{extId}` | getVolumeDiskStats | Get statistics for a Volume Disk | 7.0 | v4.0 | v4.2 | v4.3 |

