# Référence des appels API historiques du Prism Element (v1, v2.0, v3)

Généré par `gen_pe_legacy.py` depuis les specs servies par des clusters réels (AOS 7.5.1.13, 7.6.0.6), dossier `specs/pe-legacy/`. Version machine : `api-calls-pe-legacy.json`. Les API v4 sont dans `API-CALLS-PC7.md` et `API-CALLS-PE7.md`.

## Comment lire ce document

- Chemin complet : `https://<cvm-ou-vip>:9440` + chemin.
- Colonnes AOS : ✓ = opération publiée par ce cluster. Les specs ne couvrent que les versions d'AOS disponibles en lab ; AOS 7.0 n'a pas pu être relevé.
- **v3** : le PE publie la spec v3 complète (212 opérations, identique sur les deux AOS), mais v3 est d'abord l'API du Prism Central ; ce qui répond réellement sur un PE n'a pas été testé.
- ⚠️ = opération marquée `deprecated` dans la spec.

## Vue d'ensemble

| API | Base | Ressources | Opérations | Dépréciées |
|---|---|---|---|---|
| v1 | `/PrismGateway/services/rest/v1` | 27 | 402 | 4 |
| v2.0 | `/PrismGateway/services/rest/v2.0` | 29 | 311 | 20 |
| v3 | `/api/nutanix/v3` | 49 | 212 | 0 |

## v1

| Méthode | Chemin | operationId | Résumé | AOS 7.5.1.13 | AOS 7.6.0.6 |
|---|---|---|---|---|---|
| | **alerts** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/alerts/` | getAlerts | Get the list of Alerts. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/alerts/acknowledge` | acknowledgeAlerts | Acknowledge Alerts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/alerts/configuration` | getAlertConfig | Get the Alert configuration. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/alerts/configuration` | patchAlertConfig | Modify the Alert configuration. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/alerts/configuration` | updateAlertConfig | Update the Alert configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/alerts/hardware` | getHardwareAlerts | Get the list of hardware Alerts. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/alerts/resolve` | resolveAlerts | Resolve Alerts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/alerts/storage` | getStorageAlerts | Get the list of storage Alerts. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/alerts/{id}/acknowledge` | acknowledgeAlert | Acknowledge Alert. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/alerts/{id}/resolve` | resolveAlert | Resolve Alert. | ✓ | ✓ |
| | **authconfig** | | | | |
| `DELETE` | `/PrismGateway/services/rest/v1/authconfig/` | deleteAuthConfig | Delete Auth config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/authconfig/` | getAuthConfig | Get Auth configuration. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/authconfig/` | patchAuthConfig | Modify Auth configuration. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/authconfig/` | updateAuthConfig | Update Auth configuration. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/authconfig/add_auth_types` | addAuthTypes | Add Auth types. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/authconfig/auth_types` | getAuthTypes | Get Auth types. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/authconfig/auth_types` | setAuthTypes | Update Auth types. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/authconfig/client_auth/` | getClientAuth | Get client authentication status. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/authconfig/client_auth/` | setClientAuthState | Enable/disable client authentication. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/authconfig/client_auth/` | updateClientAuth | Update client authentication. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/authconfig/client_auth/{name}` | deleteClientAuthChain | Delete client chain certificate for authentication. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/authconfig/directories/` | getAllDirectoryConfigs | Get the list of Directories. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/authconfig/directories/` | patchDirectoryConfig | Modify Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/authconfig/directories/` | addDirectoryConfig | Add Directory. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/authconfig/directories/` | updateDirectoryConfig | Edit Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/authconfig/directories/connection_status` | testConnection | Test LDAP directory connection status | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/authconfig/directories/{name}` | deleteDirectoryConfig | Delete Directory. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/authconfig/directories/{name}` | getDirectoryConfig | Get Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/authconfig/remove_auth_types` | deleteAuthTypes | Remove Auth types. | ✓ | ✓ |
| | **cloud** | | | | |
| `DELETE` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/credentials` | removeAllCredentials | Remove all cloud credentials. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/credentials` | getCredentials | Get cloud credentials. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/credentials` | addCredentials | Add a cloud credential. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/credentials/{name}` | removeCredentials | Remove a cloud credential. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/credentials/{name}` | updateCredentials | Update a cloud credential. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/cvms` | getCvms | Get a list of CVMs. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/default-credentials` | setDefaultCredentials | Set a default cloud credential to use. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/deploy_remote_site` | deployRemoteSite | Deploy a cloud CVM and create a remote site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/images` | getCvmImages | Get a list of CVM images. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cloud/{cloudType}/subnets` | getSubnets | Get a list of subnets. | ✓ | ✓ |
| | **cluster** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/cluster/` | getClusterInfo | Get Cluster details. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/cluster/` | patchClusterParams | Modify Cluster params. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/cluster/` | editClusterParams | Update Cluster params. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/block_aware_fixer/start/` | cassandraBlockAwareFixerStart ⚠️ | Start block aware fixer | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/block_aware_fixer/stop/` | cassandraBlockAwareFixerStop ⚠️ | Stop block aware fixer. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/metro_witness` | addMAWitness | Add Witness VM details | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/metro_witness/` | getAllMAWitnesses | List All Metro Availability Witnesses | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/metro_witness/{uuid}` | removeWitnessSite | Delete a Metro Availability Witness | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/cluster/metro_witness/{uuid}` | updateWitnessSite | Update a Metro Availability Witness | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/name_servers` | getNameServers | Get the list of Name Servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/name_servers` | addNameServer | Add name server. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/name_servers/{nameServer}` | removeNameServer | Delete the specified Name Server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/nfs_whitelist` | getNfsSubnetWhitelist | Get NFS subnet whitelist. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/nfs_whitelist` | addNfsSubnetWhitelist | Add NFS subnet whitelist entry. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/nfs_whitelist/{name:.+}` | removeNfsSubnetWhitelist | Delete NFS the specified subnet whitelist entry. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/ntp_servers` | getNtpServers | Get the list of NTP servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/ntp_servers` | addNtpServer | Add NTP server. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/ntp_servers/{ntpServer}` | removeNtpServer | Delete an NTP server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/public_keys` | getPublicKeys | Get the list of Public Keys. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/cluster/public_keys/` | addPublicKey | Add a Public Key. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/public_keys/{name}` | deletePublicKey | Delete a Public Key. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/public_keys/{name}` | getPublicKey | Get a Public Key. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/rackable_units` | getRackableUnits | Get the list of Rackable Units. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/rackable_units/{id}` | deleteRackableUnit | Delete the specified Rackable Unit. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/rackable_units/{id}` | getRackableUnit | Get the specified Rackable Unit. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/remote_support` | getRemoteSupportStatus | Get Remote Support settings. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/cluster/remote_support` | editRemoteSupport | Update Remote Support settings. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/search/` | doSpotlightSearch | Get spotlight search results. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/cluster/smtp` | removeSmtpServer | Delete SMTP server config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/smtp` | getSmtpServer | Get the SMTP server config. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/cluster/smtp` | patchSmtpServer | Modify the SMTP server config. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/cluster/smtp` | updateSmtpServer | Update the SMTP server config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/smtp/security_modes` | getSmtpServerSecurityModeType | Get the SMTP security modes. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/cluster/stats/` | getClusterStats | Get the list of Cluster stats. | ✓ | ✓ |
| | **clusters** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/clusters/` | getClusters | Get the list of clusters. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/alerts` | getClusterAlerts | Get the list of alerts generated on any Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/events` | getClusterEvents | Get the list of events generated on any Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/{id}` | getCluster | Get a Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/{id}/alerts` | getAlertsForCluster | Get the list of alerts generated on a specified Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/{id}/events` | getEventsForClusters | Get the list of events generated on a specified Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/clusters/{id}/stats/` | getStatsForCluster | Get the stats for a specified Cluster. | ✓ | ✓ |
| | **containers** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/containers/` | getContainers | Get the list of Containers. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/containers/` | patchContainer | Modify a Container. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/containers/` | addContainer | Add a Container. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/containers/` | editContainer | Update a Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/alerts` | getContainerAlerts | Get the list of alerts generated on any Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/datastores` | getNfsDatastores | Get the list of NFS Datastores. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/containers/datastores/add_datastore` | createNfsDatastores | Add an NFS Datastore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/containers/datastores/remove_datastore` | deleteNfsDatastores | Remove an NFS Datastore. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/events` | getContainerEvents | Get the list of events generated on any Container. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/containers/{id}` | deleteContainer | Delete a Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/{id}` | getContainer | Get a Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/{id}/alerts` | getAlertsForContainer | Get the list of alerts generated on a specified Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/{id}/events` | getEventsForContainer | Get the list of events generated on a specified Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/{id}/stats/` | getContainerStats | Get the stats for a specified Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/containers/{id}/vdisks` | getVDisksInContainer | Get the list of VDisks. | ✓ | ✓ |
| | **data_at_rest_encryption** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/` | getEncryptionStatus | Get encryption status. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/download_encryption_key` | downloadEncryptionKey | Download encryption key. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/enable` | enableEncryption | Enable encryption. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/recent_certificate_test_results` | getRecentCertificateTestResults | Get recent certificate test results. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/rekey` | rekey | Sets new passwords for encryption capable disks. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption/test` | testEncryptionConfiguration | Test encryption configuration. | ✓ | ✓ |
| | **data_at_rest_encryption_certificates** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/ca_certificates/` | getCACertificates | Get all CA certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/ca_certificates/` | addCACertificate | Add trusted CA certificate. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/ca_certificates/{name}` | deleteCACertificate | Delete Certificate Authority. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/certification_information` | updateCertificationInformation | Update the Certification information. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/certification_information/` | getCertificationInformation | Get Certification information. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/csr_for_discovered_node` | downloadCSRFromDiscoveredNode | Download CSR files | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/csrs` | downloadCSRs | Download CSR files | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/svm_certificate/` | deleteCertificate | Delete certificate. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/svm_certificates/` | uploadCertificates | Add certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/svm_certificates/multi_file` | uploadCertificatesViaMultiFile | Add certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/data_at_rest_encryption_certificates/svm_certificates/replace` | replaceExpiredCertificate | Replace expired svm certificate. | ✓ | ✓ |
| | **disks** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/disks/` | getDisks | Get the list of Disks. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/alerts` | getDiskAlerts | Get the list of alerts generated on any Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/events` | getDiskEvents | Get the list of events generated on any Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/health_check_summary` | getHealthCheckSummaryForDisks | Get the health check summary for the Disks. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/disks/{id}` | beginRemoveDisk | Mark specified Disk for Removal. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/{id}` | getDisk | Get a Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/{id}/alerts` | getAlertsForDisk | Get the list of alerts generated on a specified Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/{id}/events` | getEventsForDisks | Get the list of events generated on a specified Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/disks/{id}/stats/` | getDiskStats | Get the stats for a specified Disk. | ✓ | ✓ |
| | **events** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/events/` | getEvents | Get the list of Events. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/events/acknowledge` | acknowledgeEvents ⚠️ | Acknowledge events. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/events/hardware` | getHardwareEvents | Get the list of hardware Events. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/events/storage` | getStorageEvents | Get the list of storage Events. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/events/{id}/acknowledge` | acknowledgeEvent ⚠️ | Acknowledge Event. | ✓ | ✓ |
| | **file_groups** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/file_groups/` | listFileGroups | List file groups. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/file_groups/{fileGroupUuid}/delete_files` | deleteFiles | Remove files for a specific file group. | ✓ | ✓ |
| | **health_checks** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/health_checks/` | getHealthChecks | Get the list of Health Checks. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/health_checks/` | patchHealthCheck | Modify Health Check details. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/health_checks/` | updateHealthCheck | Update Health Check details. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/health_checks/{id}` | getHealthCheck | Get Health Check details. | ✓ | ✓ |
| | **hosts** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/hosts/` | getHosts | Get the list of Physical Hosts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/alerts` | getHostAlerts | Get the list of alerts generated on any Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/events` | getHostEvents | Get the list of events generated on any Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/health_check_summary` | getHealthCheckSummaryForHosts | Get the health check summary for Hosts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/{id}` | getHost | Get a Physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/{id}/alerts` | getAlertsForHost | Get the list of alerts generated on a specified Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/{id}/events` | getEventsForHost | Get the list of events generated on a specified Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/hosts/{id}/stats/` | getHostStats | Get the stats for a specified Physical Host. | ✓ | ✓ |
| | **http_proxies** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/http_proxies/` | getHttpProxies | Get the list of HTTP Proxies. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/http_proxies/` | patchHttpProxy | Modify an HTTP Proxy. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/http_proxies/` | addHttpProxy | Add an HTTP Proxy. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/http_proxies/` | editHttpProxy | Update an HTTP Proxy. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/http_proxies/whitelist` | getHttpProxyWhitelist | Get HTTP Proxy whitelist. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/http_proxies/whitelist` | setHttpProxyWhitelist | Set HTTP Proxy whitelist. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/http_proxies/{name}` | deleteHttpProxy | Delete an HTTP Proxy. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/http_proxies/{name}` | getHttpProxy | Get an HTTP Proxy. | ✓ | ✓ |
| | **key_management_servers** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/key_management_servers/` | getKeyManagementServers | Get all Key Management Servers. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/key_management_servers/` | patchKeyManagementServer | Modify the KeyManagementServer. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/key_management_servers/` | addKeyManagementServer | Add a Key Management Server. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/key_management_servers/` | updateKeyManagementServer | Update the KeyManagementServer. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/key_management_servers/type` | getKeyManagementServerType | Get Key Management Server Type. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/key_management_servers/type` | selectKeyManagementServerType | Select Key Management Server Type. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/key_management_servers/{name}` | deleteKeyManagementServer | Delete the KeyManagementServer. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/key_management_servers/{name}` | getKeyManagementServer | Get Key Management Server. | ✓ | ✓ |
| | **license** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/license/` | getCurrentLicense | Show current license file | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/license/` | applyLicense | Apply license file | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/alerts` | getLicenseAlerts | Get the list of alerts generated for any License. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/allowances` | getAllowances | Show allowances for all features | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/allowances/{featureName}` | getAllowanceForFeature | Show allowances for a particular feature | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/cluster_info` | getClusterLicenseInfo | Get Cluster Info | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/cluster_summary_file` | getClusterInfoFile | Get Cluster Info as a file | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/license/events` | getLicenseEvents | Get the list of events generated for any License. | ✓ | ✓ |
| | **protection_domains** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/` | getProtectionDomains | Get the list of Protection Domains. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/` | addProtectionDomain | Add a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/alerts` | getProtectionDomainAlerts | Get the list of alerts generated on any Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/consistency_groups/` | getConsistencyGroups | Get list of Consistency groups. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/dr_snapshots/` | getAllProtectionDomainSnapshots | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/events` | getProtectionDomainEvents | Get the list of events generated on any Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/health_check_summary` | getHealthCheckSummaryForProtectionDomains | Get the health check summary for the Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/oob_schedules/` | getOutOfBandSchedules | Get the list of Out-Of-Band schedules in Protection Domains. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/pending_actions/` | getPendingActions | Get list of pending actions. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/pending_replications/` | getProtectionDomainPendingReplications | Get list of pending replications. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/replications/` | getReplications | Get list of replications. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/status` | getStatus | Get the Data Protection status for all Protection Domains. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/unprotected_vms/` | getUnprotectedVms | Get list of unprotected VMs in a cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{name}/stats/` | getProtectionDomainStats | Get the stats for a specified Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}` | markProtectionDomainForRemoval | Delete a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}` | getProtectionDomainByName | Get a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/activate` | markProtectionDomainActive | Activate a protection domain | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/alerts` | getAlertsForProtectionDomain | Get the list of alerts generated on a specified Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/break_replication_timeout` | updateStretchCluster | Updates Metro Availability timeout for a specific protection domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/consistency_groups/` | getConsistencyGroupsInPd | Get list of Consistency groups in a Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/consistency_groups/{cgName}` | updateConsistencyGroup | Updates Consistency Group for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/deactivate` | markProtectionDomainInactive | Deactivate a protection domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/dr_snapshots/` | getSnapshotsForPd | Get the list of Snapshots in a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/events` | getEventsForProtectionDomain | Get the list of events generated on a specified Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/failure_handling` | updateStretchFailureHandling | Change failure handling mode for a protection domain | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/metro_avail_disable` | stopStretchCluster | Disables Metro Availability for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/metro_avail_enable` | startStretchCluster | Enables Metro Availability for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/migrate` | migrateProtectionDomain | Migrate an active Protection Domain to a DR site. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/oob_schedules` | addOutOfBandSchedule | Add a out of band snapshot schedule in a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/oob_schedules/` | getOutOfBandSchedulesForPd | Get the list of Out-Of-Band schedules in a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/oob_schedules/{scheduleId}` | removeOutOfBandSchedule | Delete a Out-Of-Band schedule. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/pending_actions/` | getPendingActionsForPd | Get list of pending actions in the Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/pending_replications/` | getPendingReplicationsInPd | Get list of pending replications in the Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/promote` | promoteStretchCluster | Promotes to active Metro Availability role for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/protect_vms` | addVmsByNamesToProtectionDomain | Add Virtual Machines to a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/realize` | realizeSnapshot | Realize a snapshot for the given time. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/replications/` | getReplicationsForPd | Get list of replications in a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/restore_entities` | restoreEntities | Rollback Virtual Machines and/or NFS files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/rollback` | rollbackProtectionDomain | Rollback an active Protection domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules` | clearCronSchedules | Remove all snapshot schedules from a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules` | getCronSchedules | Retrieve all snapshot schedules from a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules` | addCronSchedule | Add a snapshot schedule to a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules/{id}` | removeCronSchedule | Remove a snapshot schedule from a Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules/{id}` | replaceCronSchedule | Replace a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules/{id}/retention_policies` | clearRetentionPolicy | Clear retention policies of a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/schedules/{id}/retention_policies` | setRetentionPolicy | Set retention policies of a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/snapshots/{snapshotId}/clone` | restoreSnapshot | Restore Virtual Machines and/or NFS files.Parallel restore requests on the same PD are not allowed.The API will fail with kConflictingOperationInProgress error ifone restore request is already pending for the given PD. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{pdName}/unprotect_vms` | removeVmsFromProtectionDomain | Remove Virtual Machines from a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{protectionDomainName}/dr_snapshots/{snapshotId}` | removeSnapshot | Delete a snapshot. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/protection_domains/{protectionDomainName}/dr_snapshots/{snapshotId}/retain` | modifySnapshot | Retain a snapshot. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/protection_domains/{protectionDomainName}/replications/{id}` | abortReplication | Abort a replication. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/protection_domains/{protectionDomainName}/replications/{id}` | updateReplication | Update the state of the replication. | ✓ | ✓ |
| | **remote_sites** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/` | getAllRemoteSites | Get the list of Remote Sites. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/remote_sites/` | patchRemoteSite | Modify a Remote Site. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/remote_sites/` | addRemoteSite | Add a Remote Site. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/remote_sites/` | updateRemoteSite | Update a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/alerts` | getRemoteSiteAlerts | Get the list of alerts generated on any Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/dr_snapshots/` | getAllRemoteSiteSnapshots | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/events` | getRemoteSiteEvents | Get the list of events generated on any Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/health_check_summary` | getHealthCheckSummaryForRemoteSites | Get the health check summary for the Remote Sites. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/pending_replications/` | getPendingReplications | Get all pending replications. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/remote_sites/{name}` | markRemoteSiteForRemoval | Delete a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}` | getRemoteSite | Get a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}/alerts` | getAlertsForRemoteSite | Get the list of alerts generated on a specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}/dr_snapshots/` | getSnapshotsForRemoteSite | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}/events` | getEventsForRemoteSite | Get the list of events generated on a specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}/pending_replications/` | getPendingReplicationsInRemote | Get all pending replications for the specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/remote_sites/{name}/stats/` | getRemoteSiteStats | Get the stats for a specified Remote Site. | ✓ | ✓ |
| | **rsyslog** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/` | getRSyslogConfig | Get RSyslog configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/disable-tls` | disableRSyslogTls | Disable TLS for RSyslog | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/servers` | getRSyslogServers | Get log servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/rsyslog/servers` | setRSyslogServer | Add log server to RSyslog configuration. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/rsyslog/servers` | updateRSyslogServer | Edit log server in RSyslog configuration | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/servers/{logServerName}/modules` | getRSyslogServerModules | Get modules for a log server. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/rsyslog/servers/{logServerName}/modules` | setRSyslogServerModule | Add module in RSyslog configuration. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/rsyslog/servers/{logServerName}/modules/{moduleName}` | deleteRSyslogServerModule | Delete log server module. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/rsyslog/servers/{name}` | deleteRSyslogServer | Delete log server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/status` | getRSyslogStatus | Get the RSyslog status. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/rsyslog/status` | setRSyslogStatus | Enable/Disable RSyslog configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/rsyslog/tls` | getRSyslogTlsConfig | Get TLS configuration for RSyslog | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/rsyslog/tls` | setRSyslogTlsConfig | Set TLS configuration for RSyslog | ✓ | ✓ |
| | **snmp** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/snmp/` | getSnmpInfo | Get SNMP configuration. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/snmp/add_transports` | addSnmpTransports | Add SNMP Transports. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/snmp/remove_transports` | deleteSnmpTransports | Remove SNMP Transports. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/status` | getSnmpStatus | Get the SNMP status. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/snmp/status` | setSnmpStatus | Enable/Disable SNMP configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/transports` | getSnmpTransports | Get the list of SNMP Transports. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/traps` | getSnmpTraps | Get the list of SNMP Traps. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/snmp/traps` | patchSnmpTrap | Modify SNMP Trap. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/snmp/traps` | addSnmpTrap | Add SNMP Trap. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/snmp/traps` | editSnmpTrap | Edit SNMP Trap. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/snmp/traps/{trapAddress}` | deleteSnmpTrap | Delete SNMP Trap. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/traps/{trapAddress}` | getSnmpTrap | Get SNMP Trap. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/users` | getSnmpUsers | Get the list of SNMP Users. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/snmp/users` | patchSnmpUser | Modify SNMP User. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/snmp/users` | addSnmpUser | Add SNMP User. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/snmp/users` | editSnmpUser | Edit SNMP User. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/snmp/users/{username}` | deleteSnmpUser | Delete SNMP User. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/snmp/users/{username}` | getSnmpUser | Get SNMP User. | ✓ | ✓ |
| | **storage_pools** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/` | getStoragePools | Get the list of Storage Pools. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/storage_pools/` | patchStoragePool | Update a Storage Pool. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/storage_pools/` | addStoragePool | Add a Storage Pool. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/storage_pools/` | editStoragePool | Update a Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/alerts/` | getStoragePoolAlerts | Get the list of alerts generated on any Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/events/` | getStoragePoolEvents | Get the list of events generated on any Storage Pool. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/storage_pools/{id}` | deleteStoragePool | Delete a Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/{id}` | getStoragePool | Get a Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/{id}/alerts/` | getAlertsForStoragePool | Get the list of alerts generated on a specified Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/{id}/events/` | getEventsForStoragePool | Get the list of events generated on a specified Storage Pool. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/storage_pools/{id}/stats/` | getStoragePoolStats | Get the stats for a specified Storage Pool. | ✓ | ✓ |
| | **users** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/users/logged_in_users` | getAllLoggedInUsersInfo | Get Logged In Users Details. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/users/logged_in_users/{userName}` | getLoggedInUserInfo | Get Logged In Details of a user. | ✓ | ✓ |
| | **vdisks** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/` | getAllVDisks | Get the list of VDisks. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/vdisks/` | patchVDisk | Update a VDisk. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vdisks/` | addVDisk | Add a VDisk. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vdisks/` | editVDisk | Update a VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/alerts` | getVDiskAlerts | Get the list of alerts generated on any VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/events` | getVDiskEvents | Get the list of events generated on any VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/snapshots/` | getAllSnapshots | Get the complete list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/snapshots/{name}/` | getSnapshotByName | Get a Snapshot. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vdisks/{name}` | deleteVDisk | Delete a VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/{name}` | getVDisk | Get a VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/{name}/alerts` | getAlertsForVDisk | Get the list of alerts generated on a specified VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/{name}/events` | getEventsForVDisk | Get the list of events generated on a specified VDisk. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vdisks/{name}/snapshots` | createSnapshot | Snapshot a VDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/{name}/snapshots/` | getVDiskSnapshots | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vdisks/{name}/stats/` | getVDiskStats | Get the stats for a specified VDisk. | ✓ | ✓ |
| | **vfilers** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/` | getFileServers | Get FileServers based on passed criteria. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/` | addFileServer | Create a FileServer | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/` | updateFileServer | Update file server configuration | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/fsm` | getFSM | Get FSM Information | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/pulse/` | getPulseConfigs | Get the pulse configs. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/shares/` | getAllFileServersShares | Get the list of Shares associated with all file servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/snapshot_info` | getFileServerSnapshotInfo | Get File server snapshot info | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/upgrade` | upgradeFileServer | Upgrade given list of file servers | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/upgradeFilesModule` | upgradeFilesModule | Upgrade files module | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/usage/` | getFileServersUsage | Get the file servers usage. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}` | deleteFileServer | Delete FileServer | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}` | getFileServer | Get a single FileServer's details. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/activate` | activateFileServer | Activate File Server | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/addDns` | AddDNS | Add Dns Entries | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/admin_users/` | getAdminUsers | Get the list of admin users. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/admin_users/` | addAdminUser | Add new admin user | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/admin_users/` | updateAdminUser | Update Admin User | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/admin_users/{adminUserUuid}` | deleteAdminUser | Delete Admin User | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/admin_users/{adminUserUuid}` | getAdminUser | Get a single admin user. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/builtin_groups` | getBuiltInGroups | Get built in groups per file server. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/clone` | cloneFileServer | Clone File Server | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/configureNameServices` | configureNameServices | Configure Name services | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/dnsEntries/` | getDnsEntries | Get the list of dns entries. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/` | getIcapServers | Get the list of icap servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/` | addIcapServer | Add new icap server | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/` | updateIcapServer | Update Icap Server | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/{icapServerUuid}` | deleteIcapServer | Delete icap server | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/{icapServerUuid}` | getIcapServer | Get a icap server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/{icapServerUuid}/stats` | getIcapServerStats | Get the stats for a specified Icap server. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/icap_servers/{icapServerUuid}/test_connection` | testIcapServerConnection | Test Icap Server Connection | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/` | getInfectedFiles | Get the list of infected files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/delete` | deleteInfectedFiles | Delete list of infected files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/quarantine` | quarantineInfectedFiles | Quarantine list of infected files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/rescan` | rescanInfectedFiles | Rescan list of infected files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/reset` | resetInfectedFiles | Reset list of infected files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/unquarantine` | unquarantineInfectedFiles | Unquarantine list of infected files. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/infected_files/{infectedFileUuid}` | getInfectedFile | Get infected file. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/joinDomain` | joinDomain | Join Domain | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/loadBalance` | loadBalanceFileServer | LoadBalance File Server | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/protect` | protectFileServer | Protect File Server | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/quotaEmailConfig` | getQuotaEmailConfig | Get a Quota Policy Email Config | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/quotaEmailConfig` | updateQuotaEmailConfig | Update a Quota Policy Email Config | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/removeDns` | removeDNS | Remove Dns Entries | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/searchUserMappings/` | searchUserMapping | Search User Mapping | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/security-info/` | getFileServerSecurityInfo | Get file server security details. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/security-info/` | editFileServerSecurityParams | Update FileServer security config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/` | getFileServersShares | Get the list of Shares. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/` | addFileServerShare | Add new Share | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/` | updateFileServerShare | Update file server share configuration | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}` | deleteFileServerShare | Delete File Server Share | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}` | getFileServerShare | Get the Share | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/get_principal_type/` | getPrincipalType | Get principal type from principal name | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/quota_policies/` | getQuotaPolicies | Get the list of quota policies. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/quota_policies/` | addQuotaPolicy | Add new Quota Policy | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/quota_policies/` | updateQuotaPolicy | Update Quota Policy | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/quota_policies/{quotaPolicyUuid}` | deleteQuotaPolicy | Delete Quota Policy | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/quota_policies/{quotaPolicyUuid}` | getQuotaPolicy | Get a single quota policy. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/stats/` | getFileServerShareStats | Get the stats for a specified share. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/shares/{shareUuid}/virus_scan_policy/` | deleteVirusScanPolicy | Delete Virus Scan Policy | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshot_policies/` | getSnapshotPolicies | Get the list of snapshot policies. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshot_policies/` | addSnapshotPolicy | Add new Snapshot Policy | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshot_policies/` | updateSnapshotPolicy | Update Snapshot Policy | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshot_policies/{snapshotPolicyUuid}` | deleteSnapshotPolicy | Delete Snapshot Policy | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshots/{shareUuid}` | getSnapshots | Get the list of snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/snapshots/{shareUuid}/{snapshotUuid}` | getSnapshot | Get a file server share snapshot. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/ssl_certificate` | getSslCertificate | Get the ssl certificate details of FileServer. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/ssl_certificate` | generateSslCertificate | ReGenerate Self Signed Certificate | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/stats/` | getStats | Get the stats for a specified FS. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/unjoinDomain` | unjoinDomain | Unjoin Domain | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/userMappings/` | getUserMapping | Get the user mapping. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/userMappings/` | addUserMapping | Add new User Mapping | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/userMappings/` | updateUserMapping | Update User Mapping | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/users/` | deleteUser | Delete FileServer User | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/users/` | getUsers | Get the list of users. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/users/` | addUser | Add new user | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/users/` | updateUser | Update User | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/verifyDns` | verifyDNS | Verify Dns Entries | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/virus_scan_policy` | getVirusScanPolicy | Get a virus scan policy. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/virus_scan_policy/` | addVirusScanPolicy | Add Virus Scan Policy | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vfilers/{uuid}/virus_scan_policy/` | updateVirusScanPolicy | Update Antivirus Server Scan Policy | ✓ | ✓ |
| | **virtual_disks** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/virtual_disks/` | getVirtualDisks | Get the list of VirtualDisks. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/virtual_disks/{id}` | getVirtualDisk | Get VirtualDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/virtual_disks/{id}/stats/` | getVirtualDiskStats | Get the stats for a specified VirtualDisk. | ✓ | ✓ |
| | **vms** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/vms/` | getVMs | Get the list of VMs. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/` | createVM | Create a Virtual Machine. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/alerts` | getVMAlerts | Get the list of alerts generated on any VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/events` | getVMEvents | Get the list of events generated on any VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/guest_tools/` | listNutanixGuestTools | List Nutanix Guest Tools. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/health_check_summary` | getHealthCheckSummaryForVMs | Get the health check summary for VMs. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}` | getVM | Get VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/alerts` | getAlertsForVM | Get the list of alerts generated on a specified VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/events` | getEventsForVM | Get the list of events generated on a specified VM. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmId}/fingerprint_on_write` | updatefingerPrintOnWriteInVM | Update fingerPrintOnWrite on all VDisks of a VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/` | getNutanixGuestTools | Get Nutanix Guest Tools. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/` | patchNutanixGuestTools | Update Nutanix Guest Tools. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/` | createNutanixGuestTools | Create Nutanix Guest Tools. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/` | updateNutanixGuestTools | Update Nutanix Guest Tools. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/mount` | mountNutanixGuestTools | Mount Nutanix Guest Tools. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmId}/guest_tools/unmount` | unmountNutanixGuestTools | Unmount Nutanix Guest Tools. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmId}/on_disk_dedup` | updateonDiskDedup | Update OnDiskDedup on all VDisks of a VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/snapshots` | getSnapshotsOfVM | Get all snapshots of a VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/snapshots/{snapId}` | getSnapshotOfVM | Get snapshot info for given snapshot of a VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/stats/` | getVMStats | Get the stats for a specified VM. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/vdisks` | getVDisksInVm | Get the list of VDisks. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vms/{vmId}/virtual_disks` | getVirtualDisksInVm | Get the list of VirtualDisks. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vms/{vmid}/clone` | cloneVM | Clone a Virtual Machine. | ✓ | ✓ |
| | **vstores** | | | | |
| `GET` | `/PrismGateway/services/rest/v1/vstores/` | getVStores | Get the list of VStores. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v1/vstores/{id}` | getVStoreByUuid | Get a VStore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vstores/{id}/protect` | protectVStore | Protect a VStore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v1/vstores/{id}/unprotect` | unProtectVStore | Unprotect a VStore. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v1/vstores/{id}/update_protection_mode` | updateProtection | Protect a VStore. | ✓ | ✓ |

## v2.0

| Méthode | Chemin | operationId | Résumé | AOS 7.5.1.13 | AOS 7.6.0.6 |
|---|---|---|---|---|---|
| | **alerts** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/alerts/` | getAlerts | Get the list of Alerts. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/alerts/acknowledge` | acknowledgeAlerts | Acknowledge Alerts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/alerts/configuration` | getAlertConfig | Get the Alert configuration. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/alerts/configuration` | patchAlertConfig | Modify the Alert configuration. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/alerts/configuration` | updateAlertConfig | Update the Alert configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/alerts/policies` | getAlertPolicies | Get all User Defined Alert Policies | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/alerts/policies` | createPolicy | Create a new User Defined Alert Policy | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/alerts/policies` | updatePolicy | Update a User Defined Alert Policy | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/alerts/policies/{policy_id}` | deleteAlertPolicy | Delete the specified User Defined Alert Policy | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/alerts/policies/{policy_id}` | getAlertPolicy | Get the User Defined Alert Policy | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/alerts/resolve` | resolveAlerts | Resolve Alerts. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/alerts/{id}/acknowledge` | acknowledgeAlert | Acknowledge Alert. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/alerts/{id}/resolve` | resolveAlert | Resolve Alert. | ✓ | ✓ |
| | **authconfig** | | | | |
| `DELETE` | `/PrismGateway/services/rest/v2.0/authconfig/` | deleteAuthConfig | Delete Auth config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/authconfig/` | getAuthConfig | Get Auth configuration. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/authconfig/` | patchAuthConfig | Modify Auth configuration. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/authconfig/` | updateAuthConfig | Update Auth configuration. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/authconfig/add_auth_types` | addAuthTypes | Add Auth types. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/authconfig/auth_types` | getAuthTypes | Get Auth types. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/authconfig/auth_types` | setAuthTypes | Update Auth types. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/authconfig/client_auth/` | getClientAuth | Get client authentication status. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/authconfig/client_auth/` | setClientAuthState | Enable/disable client authentication. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/authconfig/client_auth/` | updateClientAuth | Update client authentication. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/authconfig/client_auth/{name}` | deleteClientAuthChain | Delete client chain certificate for authentication. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/authconfig/directories/` | getAllDirectoryConfigs | Get the list of Directories. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/authconfig/directories/` | patchDirectoryConfig | Modify Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/authconfig/directories/` | addDirectoryConfig | Add Directory. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/authconfig/directories/` | updateDirectoryConfig | Edit Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/authconfig/directories/connection_status` | testConnection | Test LDAP directory connection status | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/authconfig/directories/{name}` | deleteDirectoryConfig | Delete Directory. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/authconfig/directories/{name}` | getDirectoryConfig | Get Directory. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/authconfig/remove_auth_types` | deleteAuthTypes | Remove Auth types. | ✓ | ✓ |
| | **cloud** | | | | |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/credentials` | removeAllCredentials | Remove all cloud credentials. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/credentials` | getCredentials | Get cloud credentials. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/credentials` | addCredentials | Add a cloud credential. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/credentials/{name}` | removeCredentials | Remove a cloud credential. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/cvms` | getCvms | Get a list of CVMs. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/default-credentials` | setDefaultCredentials | Set a default cloud credential to use. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/deploy_remote_site` | deployRemoteSite | Deploy a cloud CVM and create a remote site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/images` | getCvmImages | Get a list of CVM images. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cloud/{cloud_type}/subnets` | getSubnets | Get a list of subnets. | ✓ | ✓ |
| | **cluster** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/` | getClusterInfo | Get Cluster details. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/cluster/` | patchClusterParams | Modify Cluster params. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/cluster/` | editClusterParams | Update Cluster params. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/domain_fault_tolerance_status/` | getDomainFaultToleranceStatuses | List domain fault tolerance status for all the domains | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/domain_fault_tolerance_status/{domainType}` | getDomainFaultToleranceStatus | Get domain fault tolerance status for the specified domain | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cluster/metro_witness` | addMAWitness | Add Witness VM details | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/metro_witness/` | getAllMAWitnesses | List All Metro Availability Witnesses | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/metro_witness/{uuid}` | removeWitnessSite | Delete a Metro Availability Witness | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/cluster/metro_witness/{uuid}` | updateWitnessSite | Update a Metro Availability Witness | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/name_servers` | getNameServers | Get the list of Name Servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cluster/name_servers` | addNameServer | Add name server. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/name_servers/{nameServer}` | removeNameServer | Delete the specified Name Server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/nfs_whitelist` | getNfsSubnetWhitelist | Get NFS subnet whitelist. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cluster/nfs_whitelist` | addNfsSubnetWhitelist | Add NFS subnet whitelist entry. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/nfs_whitelist/{name:.+}` | removeNfsSubnetWhitelist | Delete NFS the specified subnet whitelist entry. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/ntp_servers` | getNtpServers | Get the list of NTP servers. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cluster/ntp_servers` | addNtpServer | Add NTP server. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/ntp_servers/{ntp_server}` | removeNtpServer | Delete an NTP server. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/public_keys` | getPublicKeys | Get the list of Public Keys. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/cluster/public_keys/` | addPublicKey | Add a Public Key. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/public_keys/{name}` | deletePublicKey | Delete a Public Key. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/public_keys/{name}` | getPublicKey | Get a Public Key. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/rackable_units` | getRackableUnits | Get the list of Rackable Units. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/rackable_units/{uuid}` | deleteRackableUnit | Delete the specified Rackable Unit. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/rackable_units/{uuid}` | getRackableUnit | Get the specified Rackable Unit. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/remote_support` | getRemoteSupportStatus | Get Remote Support settings. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/cluster/remote_support` | editRemoteSupport | Update Remote Support settings. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/search/` | doSpotlightSearch | Get spotlight search results. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/cluster/smtp` | removeSmtpServer | Delete SMTP server config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/smtp` | getSmtpServer | Get the SMTP server config. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/cluster/smtp` | patchSmtpServer | Modify the SMTP server config. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/cluster/smtp` | updateSmtpServer | Update the SMTP server config. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/smtp/security_modes` | getSmtpServerSecurityModeType | Get the SMTP security modes. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/cluster/stats/` | getClusterStats | Get the list of Cluster stats. | ✓ | ✓ |
| | **clusters** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/` | getClusters | Get the list of clusters. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/alerts` | getClusterAlerts | Get the list of alerts generated on any Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/events` | getClusterEvents | Get the list of events generated on any Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/{id}` | getCluster | Get a Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/{id}/alerts` | getAlertsForCluster | Get the list of alerts generated on a specified Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/{id}/events` | getEventsForClusters | Get the list of events generated on a specified Cluster. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/clusters/{id}/stats/` | getStatsForCluster | Get the stats for a specified Cluster. | ✓ | ✓ |
| | **data_at_rest_encryption** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/` | getEncryptionStatus | Get encryption status. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/download_encryption_key` | downloadEncryptionKey | Download encryption key. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/enable` | enableEncryption | Enable encryption. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/recent_certificate_test_results` | getRecentCertificateTestResults | Get recent certificate test results. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/rekey` | rekey | Sets new passwords for encryption capable disks. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption/test` | testEncryptionConfiguration | Test encryption configuration. | ✓ | ✓ |
| | **data_at_rest_encryption_certificates** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/ca_certificates/` | getCACertificates | Get all CA certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/ca_certificates/` | addCACertificate | Add trusted CA certificate. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/ca_certificates/{name}` | deleteCACertificate | Delete Certificate Authority. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/certification_information` | updateCertificationInformation | Update the Certification information. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/certification_information/` | getCertificationInformation | Get Certification information. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/csr_for_discovered_node` | downloadCSRFromDiscoveredNode | Download CSR files | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/csrs` | downloadCSRs | Download CSR files | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/svm_certificate/` | deleteCertificate | Delete certificate. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/svm_certificates/` | uploadCertificates | Add certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/svm_certificates/multi_file` | uploadCertificatesViaMultiFile | Add certificates. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/data_at_rest_encryption_certificates/svm_certificates/replace` | replaceExpiredCertificate | Replace expired svm certificate. | ✓ | ✓ |
| | **disks** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/` | getDisks | Get the list of Disks. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/alerts` | getDiskAlerts ⚠️ | Get the list of alerts generated on any Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/events` | getDiskEvents ⚠️ | Get the list of events generated on any Disk. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/disks/{uuid}` | beginRemoveDisk | Mark specified Disk for Removal. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/{uuid}` | getDisk | Get a Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/{uuid}/alerts` | getAlertsForDisk ⚠️ | Get the list of alerts generated on a specified Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/{uuid}/events` | getEventsForDisks ⚠️ | Get the list of events generated on a specified Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/disks/{uuid}/stats/` | getDiskStats | Get the stats for a specified Disk. | ✓ | ✓ |
| | **events** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/events/` | getEvents | Get the list of Events. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/events/acknowledge` | acknowledgeEvents | Acknowledge events. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/events/{id}/acknowledge` | acknowledgeEvent | Acknowledge Event. | ✓ | ✓ |
| | **file_groups** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/file_groups/` | listFileGroups | List file groups. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/file_groups/{uuid}/delete_files` | deleteFiles | Remove files for a specific file group. | ✓ | ✓ |
| | **ha** | | | | |
| `GET` | `/api/nutanix/v2.0/ha/` | getHaConfig | Get current HA configuration. | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/ha/` | updateHaConfig | Enable, disable or modify HA configuration. | ✓ | ✓ |
| | **health_checks** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/health_checks/` | getHealthChecks | Get the list of Health Checks. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/health_checks/` | patchHealthCheck | Modify Health Check details. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/health_checks/` | updateHealthCheck | Update Health Check details. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/health_checks/{id}` | getHealthCheck | Get Health Check details. | ✓ | ✓ |
| | **hosts** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/` | getHosts | Get the list of Physical Hosts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/alerts` | getHostAlerts ⚠️ | Get the list of alerts generated on any Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/events` | getHostEvents ⚠️ | Get the list of events generated on any Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/gpu_profiles` | getVirtualGpuProfiles | Get the list of virtual GPU profiles for all physical Hosts. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/host_gpus` | getHostGpus | Get the list of GPUs for all physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}` | getHost | Get a Physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/alerts` | getAlertsForHost ⚠️ | Get the list of alerts generated on a specified Host. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/enter_maintenance_mode` | enterMaintenanceMode | Put a host in maintenance mode. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/events` | getEventsForHost ⚠️ | Get the list of events generated on a specified Host. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/exit_maintenance_mode` | exitMaintenanceMode | Pull a host out of maintenance mode or abort a prior attempt. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/host_gpus` | getGpusforHost | Get the list of GPUs for a physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/host_gpus/{gpu_uuid}` | getGpuforHost | Get a particular GPU for a physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/host_gpus/{gpu_uuid}/stats/` | getHostGpuStats | Get stats for a particular GPU for a physical Host. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/hosts/{uuid}/stats/` | getHostStats | Get the stats for a specified Physical Host. | ✓ | ✓ |
| | **http_proxies** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/http_proxies/` | getHttpProxies | Get the list of HTTP Proxies. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/http_proxies/` | patchHttpProxy | Modify an HTTP Proxy. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/http_proxies/` | addHttpProxy | Add an HTTP Proxy. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/http_proxies/` | editHttpProxy | Update an HTTP Proxy. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/http_proxies/{name}` | deleteHttpProxy | Delete an HTTP Proxy. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/http_proxies/{name}` | getHttpProxy | Get an HTTP Proxy. | ✓ | ✓ |
| | **images** | | | | |
| `GET` | `/api/nutanix/v2.0/images/` | getImages | Get the list of Disk Images. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/images/` | createImage | Create a Disk Image. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/images/{uuid}/` | deleteImage | Delete a Disk Image. | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/images/{uuid}/` | getImage | Get details of a specific Image based on the given Id. | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/images/{uuid}/` | updateImage | Update a Disk Image. | ✓ | ✓ |
| | **iscsi_clients** | | | | |
| `GET` | `/api/nutanix/v2.0/iscsi_clients/` | getIscsiClients | Retrieve Iscsi Client configuration | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/iscsi_clients/{uuid}` | getIscsiClient | Retrieve Iscsi Client configuration | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/iscsi_clients/{uuid}` | updateVolumeGroup | Modify an existing Iscsi Client configuration | ✓ | ✓ |
| | **key_management_servers** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/key_management_servers/` | getKeyManagementServers | Get all Key Management Servers. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/key_management_servers/` | patchKeyManagementServer | Modify the KeyManagementServer. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/key_management_servers/` | addKeyManagementServer | Add a Key Management Server. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/key_management_servers/` | updateKeyManagementServer | Update the KeyManagementServer. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/key_management_servers/type` | getKeyManagementServerType | Get Key Management Server Type. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/key_management_servers/type` | selectKeyManagementServerType | Select Key Management Server Type. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/key_management_servers/{name}` | deleteKeyManagementServer | Delete the KeyManagementServer. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/key_management_servers/{name}` | getKeyManagementServer | Get Key Management Server. | ✓ | ✓ |
| | **networks** | | | | |
| `GET` | `/api/nutanix/v2.0/networks/` | getNetworks | Get list of networks. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/networks/` | createNetwork | Create a network. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/networks/{uuid}` | deleteNetwork | Delete a network. | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/networks/{uuid}` | getNetwork | Get info of a network. | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/networks/{uuid}` | updateNetwork | Update a network. | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/networks/{uuid}/addresses` | getNetworkAddressTable | Get IP addresses assigned in the specified managed network. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/networks/{uuid}/blacklist_ip/{ipaddress}` | unreserveIP | Remove an IP address from the managed network blacklist. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/networks/{uuid}/blacklist_ip_addresses` | reserveIP | Blacklist an IP address from managed network. | ✓ | ✓ |
| | **protection_domains** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/` | getProtectionDomains | Get the list of Protection Domains. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/` | addProtectionDomain | Add a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/alerts` | getProtectionDomainAlerts ⚠️ | Get the list of alerts generated on any Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/consistency_groups/` | getConsistencyGroups | Get list of Consistency groups. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/dr_snapshots/` | getAllProtectionDomainSnapshots | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/events` | getProtectionDomainEvents ⚠️ | Get the list of events generated on any Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/oob_schedules/` | getOutOfBandSchedules | Get the list of Out-Of-Band schedules in Protection Domains. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/pending_actions/` | getPendingActions | Get list of pending actions. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/pending_replications/` | getProtectionDomainPendingReplications | Get list of pending replications. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/replications/` | getReplications | Get list of replications. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/status` | getStatus | Get the Data Protection status for all Protection Domains. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/unprotected_vms/` | getUnprotectedVms | Get list of unprotected VMs in a cluster. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}` | markProtectionDomainForRemoval | Delete a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}` | getProtectionDomainByName | Get a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/activate` | markProtectionDomainActive | Activate a protection domain | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/alerts` | getAlertsForProtectionDomain ⚠️ | Get the list of alerts generated on a specified Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/consistency_groups/` | getConsistencyGroupsInPd | Get list of Consistency groups in a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/deactivate` | markProtectionDomainInactive | Deactivate a protection domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/dr_snapshots/` | getSnapshotsForPd | Get the list of Snapshots in a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/events` | getEventsForProtectionDomain ⚠️ | Get the list of events generated on a specified Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/migrate` | migrateProtectionDomain | Migrate an active Protection Domain to a DR site. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/oob_schedules` | addOutOfBandSchedule | Add a out of band snapshot schedule in a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/oob_schedules/` | getOutOfBandSchedulesForPd | Get the list of Out-Of-Band schedules in a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/oob_schedules/{schedule_id}` | removeOutOfBandSchedule | Delete a Out-Of-Band schedule. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/pending_actions/` | getPendingActionsForPd | Get list of pending actions in the Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/pending_replications/` | getPendingReplicationsInPd | Get list of pending replications in the Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/protect_vms` | addVmsByNamesToProtectionDomain | Add Virtual Machines to a Protection Domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/replications/` | getReplicationsForPd | Get list of replications in a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/restore_entities` | restoreEntities | Rollback Virtual Machines and/or NFS files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/rollback` | rollbackProtectionDomain | Rollback an active Protection domain. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/schedules` | getCronSchedules | Retrieve all snapshot schedules from a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/schedules` | addCronSchedule | Add a snapshot schedule to a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/snapshots/{snapshot_id}/clone` | restoreSnapshot | Restore Virtual Machines and/or NFS files. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/snapshots/{snapshot_id}/replicate` | replicateSnapshot | Replicate Snapshot. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/stats/` | getProtectionDomainStats | Get the stats for a specified Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{name}/unprotect_vms` | removeVmsFromProtectionDomain | Remove Virtual Machines from a Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/break_replication_timeout` | updateStretchCluster | Updates Metro Availability timeout for a specific protection domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/consistency_groups/{cg_name}` | updateConsistencyGroup | Updates Consistency Group for a specific protection domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/failure_handling` | updateStretchFailureHandling | Change failure handling mode for a protection domain | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/metro_avail_disable` | stopStretchCluster | Disables Metro Availability for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/metro_avail_enable` | startStretchCluster | Enables Metro Availability for a specific protection domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/promote` | promoteStretchCluster | Promotes to active Metro Availability role for a specific protection domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/schedules` | clearCronSchedules | Remove all snapshot schedules from a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/schedules/{id}` | removeCronSchedule | Remove a snapshot schedule from a Protection Domain. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/schedules/{id}` | replaceCronSchedule | Replace a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/schedules/{id}/retention_policies` | clearRetentionPolicy | Clear retention policies of a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{pd_name}/schedules/{id}/retention_policies` | setRetentionPolicy | Set retention policies of a snapshot schedule of a Protection Domain. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{protection_domain_name}/dr_snapshots/{snapshot_id}` | removeSnapshot | Delete a snapshot. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/protection_domains/{protection_domain_name}/dr_snapshots/{snapshot_id}/retain` | modifySnapshot | Retain a snapshot. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/protection_domains/{protection_domain_name}/replications/{id}` | abortReplication | Abort a replication. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/protection_domains/{protection_domain_name}/replications/{id}` | updateReplication | Update the state of the replication. | ✓ | ✓ |
| | **remote_sites** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/` | getAllRemoteSites | Get the list of Remote Sites. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/remote_sites/` | patchRemoteSite | Modify a Remote Site. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/remote_sites/` | addRemoteSite | Add a Remote Site. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/remote_sites/` | updateRemoteSite | Update a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/alerts` | getRemoteSiteAlerts ⚠️ | Get the list of alerts generated on any Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/dr_snapshots/` | getAllRemoteSiteSnapshots | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/events` | getRemoteSiteEvents ⚠️ | Get the list of events generated on any Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/pending_replications/` | getPendingReplications | Get all pending replications. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}` | markRemoteSiteForRemoval | Delete a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}` | getRemoteSite | Get a Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}/alerts` | getAlertsForRemoteSite ⚠️ | Get the list of alerts generated on a specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}/dr_snapshots/` | getSnapshotsForRemoteSite | Get the list of Snapshots. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}/events` | getEventsForRemoteSite ⚠️ | Get the list of events generated on a specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}/pending_replications/` | getPendingReplicationsInRemote | Get all pending replications for the specified Remote Site. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/remote_sites/{name}/stats/` | getRemoteSiteStats | Get the stats for a specified Remote Site. | ✓ | ✓ |
| | **snapshots** | | | | |
| `GET` | `/api/nutanix/v2.0/snapshots/` | getSnapshots | Get a list of snapshots in a cluster. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/snapshots/` | createSnapshot | Create Virtual Machine snapshots. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/snapshots/{uuid}` | deleteSnapshot | Delete a snapshot. | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/snapshots/{uuid}` | getSnapshot | Get details of a specified snapshot. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/snapshots/{uuid}/clone` | cloneSnapshot | Clone a Snapshot. | ✓ | ✓ |
| | **snmp** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/` | getSnmpInfo | Get SNMP configuration. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/snmp/add_transports` | addSnmpTransports | Add SNMP Transports. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/snmp/remove_transports` | deleteSnmpTransports | Remove SNMP Transports. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/status` | getSnmpStatus | Get the SNMP status. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/snmp/status` | setSnmpStatus | Enable/Disable SNMP configuration. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/transports` | getSnmpTransports | Get the list of SNMP Transports. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/traps` | getSnmpTraps | Get the list of SNMP Traps. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/snmp/traps` | patchSnmpTrap | Modify SNMP Trap. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/snmp/traps` | addSnmpTrap | Add SNMP Trap. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/snmp/traps` | editSnmpTrap | Edit SNMP Trap. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/snmp/traps/{trap_address}` | deleteSnmpTrap | Delete SNMP Trap. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/traps/{trap_address}` | getSnmpTrap | Get SNMP Trap. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/users` | getSnmpUsers | Get the list of SNMP Users. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/snmp/users` | patchSnmpUser | Modify SNMP User. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/snmp/users` | addSnmpUser | Add SNMP User. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/snmp/users` | editSnmpUser | Edit SNMP User. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/snmp/users/{username}` | deleteSnmpUser | Delete SNMP User. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/snmp/users/{username}` | getSnmpUser | Get SNMP User. | ✓ | ✓ |
| | **storage_containers** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/` | getContainers | Get the list of Storage Containers. | ✓ | ✓ |
| `PATCH` | `/PrismGateway/services/rest/v2.0/storage_containers/` | patchContainer | Modify a Storage Container. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/storage_containers/` | addContainer | Add a Storage Container. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/storage_containers/` | editContainer | Update a Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/alerts` | getContainerAlerts ⚠️ | Get the list of alerts generated on any Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/datastores` | getNfsDatastores | Get the list of NFS Datastores. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/storage_containers/datastores/add_datastore` | createNfsDatastores | Add an NFS Datastore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/storage_containers/datastores/remove_datastore` | deleteNfsDatastores | Remove an NFS Datastore. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/events` | getContainerEvents ⚠️ | Get the list of events generated on any Storage Container. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}` | deleteContainer | Delete a Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}` | getContainer | Get a Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}/alerts` | getAlertsForContainer ⚠️ | Get the list of alerts generated on a specified Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}/events` | getEventsForContainer ⚠️ | Get the list of events generated on a specified Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}/stats/` | getContainerStats | Get the stats for a specified Storage Container. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/storage_containers/{uuid}/vdisks` | getVDisksInContainer | Get the list of VDisks. | ✓ | ✓ |
| | **tasks** | | | | |
| `PUT` | `/PrismGateway/services/rest/v2.0/tasks/cancel` | cancelTasks | Cancel a task. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/tasks/list` | getTasks | Get a list of tasks. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/tasks/poll` | pollTask | Poll a task. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/tasks/{uuid}` | getTask | Get details of the specified task. | ✓ | ✓ |
| | **vdisks** | | | | |
| `GET` | `/api/nutanix/v2.0/vdisks/` | getVdisks | Get a list of vdisks in the cluster. | ✓ | ✓ |
| | **virtual_disks** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/virtual_disks/` | getVirtualDisks | Get the list of VirtualDisks. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/virtual_disks/` | updateVirtualDisk | Update virtual Disk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/virtual_disks/{uuid}` | getVirtualDisk | Get VirtualDisk. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/virtual_disks/{uuid}/stats/` | getVirtualDiskStats | Get the stats for a specified VirtualDisk. | ✓ | ✓ |
| | **vms** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/vms/` | getVMs | Get a list of Virtual Machines. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/` | createVM | Create a Virtual Machine. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/vms/{uuid}` | getVM | Get a list of Virtual Machines. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/` | deleteVM | Delete a Virtual Machine. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/` | updateVM | Update a Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/clone` | cloneVM | Clone a Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/disks/attach` | attachVMDisk | Attach disks to Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/disks/detach` | detachVMDisk | Detach disks from Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/manage_vm_guest_tools` | manageGuestTool | Mount and unmount guest tools on a given Virtual Machine. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/nics/` | getNics | Get list of NICs in a Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/nics/` | createNic | Add a NIC to a Virtual Machine. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/nics/{nic_id}` | updateNic | Update a NIC for a Virtual Machine. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/restore` | restoreVM | Restore a Virtual Machine to a snapshotted state. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vms/{uuid}/set_power_state/` | setPowerState | Set power state of a Virtual Machine. | ✓ | ✓ |
| `DELETE` | `/PrismGateway/services/rest/v2.0/vms/{vm_uuid}/nics/{nic_id}` | deleteNic | Delete a NIC from a Virtual Machine. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/vms/{vm_uuid}/nics/{nic_id}` | getNic | Details of a NIC in a Virtual Machine. | ✓ | ✓ |
| | **volume_groups** | | | | |
| `GET` | `/api/nutanix/v2.0/volume_groups/` | getVolumeGroups | Retrieve Volume Group configuration | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/` | createVolumeGroup | Create a new Volume Group configuration | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/volume_groups/health_check_summary` | getHealthCheckSummaryForVolumeGroups | Get the health check summary for the Volume Groups. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/volume_groups/{uuid}` | removeVolumeGroup | Remove an existing Volume Group configuration | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/volume_groups/{uuid}` | getVolumeGroup | Retrieve Volume Group configuration | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/volume_groups/{uuid}` | updateVolumeGroup | Modify an existing Volume Group configuration | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/attach` | attachVirtualMachine | Attach Volume Group to Virtual Machine. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/clone` | cloneVolumeGroup | Clone a new Volume Group | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/close` | closeVolumeGroup | Close Volume Group for iSCSI initiators | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/detach` | detachVirtualMachine | Detach Volume Group to Virtual Machine. | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/disks` | createVolumeDisk | Create a Volume Disk | ✓ | ✓ |
| `PUT` | `/api/nutanix/v2.0/volume_groups/{uuid}/disks` | updateVolumeDisk | Updates a Volume Disk | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v2.0/volume_groups/{uuid}/disks/{index}` | deleteVolumeDisk | Delete a Volume Disk | ✓ | ✓ |
| `POST` | `/api/nutanix/v2.0/volume_groups/{uuid}/open` | openVolumeGroup | Open Volume Group for iSCSI initiators | ✓ | ✓ |
| `GET` | `/api/nutanix/v2.0/volume_groups/{uuid}/stats/` | getVolumeGroupStats | Get the stats for a specified VolumeGroup. | ✓ | ✓ |
| | **vstores** | | | | |
| `GET` | `/PrismGateway/services/rest/v2.0/vstores/` | getVStores | Get the list of VStores. | ✓ | ✓ |
| `GET` | `/PrismGateway/services/rest/v2.0/vstores/{uuid}` | getVStoreByUuid | Get a VStore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vstores/{uuid}/protect` | protectVStore | Protect a VStore. | ✓ | ✓ |
| `POST` | `/PrismGateway/services/rest/v2.0/vstores/{uuid}/unprotect` | unProtectVStore | Unprotect a VStore. | ✓ | ✓ |
| `PUT` | `/PrismGateway/services/rest/v2.0/vstores/{uuid}/update_protection_mode` | updateProtection | Protect a VStore. | ✓ | ✓ |

## v3

| Méthode | Chemin | operationId | Résumé | AOS 7.5.1.13 | AOS 7.6.0.6 |
|---|---|---|---|---|---|
| | **access_control_policies** | | | | |
| `POST` | `/api/nutanix/v3/access_control_policies/list` |  | Get a list of existing Access Control Policies | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/access_control_policies/{uuid}` |  | Get a existing Access Control Policy | ✓ | ✓ |
| | **alerts** | | | | |
| `POST` | `/api/nutanix/v3/alerts/action/{action}` |  | Perform an action to acknowledge or resolve alerts. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/alerts/list` |  | Get a list of existing alert | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/alerts/notify` |  | Create a new alert | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/alerts/{uuid}` |  | Get a existing alert | ✓ | ✓ |
| | **app_blueprint** | | | | |
| `POST` | `/api/nutanix/v3/app_blueprints/render_info` |  | Render an AppBlueprint from the given input | ✓ | ✓ |
| | **batch** | | | | |
| `POST` | `/api/nutanix/v3/batch` |  | Submit a list of one or more intentful REST APIs to be processed | ✓ | ✓ |
| | **citrix_adapters** | | | | |
| `POST` | `/api/nutanix/v3/citrix_adapters` |  | Create a new citrix_adapter | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/citrix_adapters/list` |  | Get a list of existing citrix_adapters | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/citrix_adapters/{uuid}` |  | Delete a existing citrix_adapter | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/citrix_adapters/{uuid}` |  | Get a existing citrix_adapter | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/citrix_adapters/{uuid}` |  | Update a existing citrix_adapter | ✓ | ✓ |
| | **clusters** | | | | |
| `POST` | `/api/nutanix/v3/clusters/list` |  | Get a list of existing clusters | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/synchronous_replication_capable` |  | Get a list of existing clusters | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}` |  | Get a existing cluster | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/clusters/{uuid}` |  | Update a existing cluster | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/ahv_cluster_config/supported_cpu_models` |  | Get list of supported CPU models for given cluster | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/ahv_cluster_config/supported_cpu_models/{cpu_model_uuid}` |  | Get information for given CPU model | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/ca_certs` |  | Add a new CA certificate | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/certificates/ca_certs/{ca_name}` |  | Delete the CA certificate | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/certificates/client_auth` |  | Remove the CA chain for client authentication | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/client_auth` |  | Import CA chain for client authentication | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/clusters/{uuid}/certificates/client_auth` |  | Replace the CA chain for client authentication | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/certificates/csrs` |  | Download CSRs from cluster | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/certificates/csrs/{node_ip}` |  | Download CSR from a discovered node | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/pemkey` |  | Generate a 2048 bits cipher length RSA key | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/pemkey/import` |  | Import a new key | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/certificates/root` |  | Remove PC root certificates | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/certificates/root` |  | Retrieve PC root certificates | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/root` |  | Save a PC root certificate on a PC or a PE | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/certificates/svm_certs/{kms_uuid}` |  | Add one or more certificates to a service VM | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/certificates/svm_certs/{node_uuid}/{kms_uuid}` |  | Delete the certificate on a service VM | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/clusters/{uuid}/certificates/svm_certs/{node_uuid}/{kms_uuid}` |  | Replace the certificate on a service VM | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}` |  | Delete all cloud credentials | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}` |  | Add a cloud credential for accessing cloud sites | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}/list` |  | Get a list of existing cloud credentials | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}/{cloud_credentials_id}` |  | Delete a existing cloud credentials | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}/{cloud_credentials_id}` |  | Get a existing cloud credentials | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/clusters/{uuid}/cloud_credentials/{cloud_type}/{cloud_credentials_id}` |  | Update a existing cloud credentials | ✓ | ✓ |
| | **data** | | | | |
| `POST` | `/api/nutanix/v3/data/changed_regions` |  | Query changed regions metadata. | ✓ | ✓ |
| | **datasource** | | | | |
| `GET` | `/api/nutanix/v3/external_repositories/datasources/{uuid}` |  | Get a existing datasource | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/external_repositories/datasources/{uuid}` |  | Update a existing datasource | ✓ | ✓ |
| | **directory_services** | | | | |
| `POST` | `/api/nutanix/v3/directory_services/list` |  | Get a list of existing directory service configurations | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/directory_services/{uuid}` |  | Get a existing directory service configuration | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/directory_services/{uuid}/search` |  | Search user or group in the directory service. | ✓ | ✓ |
| | **disks** | | | | |
| `POST` | `/api/nutanix/v3/disks/list` |  | Get a list of existing Disks | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/disks/{uuid}` |  | Delete a existing Disk | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/disks/{uuid}` |  | Get a existing Disk | ✓ | ✓ |
| | **docker_registry** | | | | |
| `POST` | `/api/nutanix/v3/docker_registries` |  | Create a docker registry | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/docker_registries/list` |  | List all docker registries | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/docker_registries/{uuid}` |  | Deletes a Docker registry | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/docker_registries/{uuid}` |  | Retrieve a Docker registry | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/docker_registries/{uuid}` |  | Update a docker registry | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/docker_registries/{uuid}/search/list` |  | Searches docker containers for specified registry | ✓ | ✓ |
| | **external_repositories** | | | | |
| `POST` | `/api/nutanix/v3/external_repositories/datasources/list` |  | Get a list of existing datasources | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/external_repositories/list` |  | Get a list of existing external_repositories | ✓ | ✓ |
| | **external_repository** | | | | |
| `POST` | `/api/nutanix/v3/external_repositories` |  | Create a new external_repository | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/external_repositories/{uuid}` |  | Delete a existing external_repository | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/external_repositories/{uuid}` |  | Get a existing external_repository | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/external_repositories/{uuid}` |  | Update a existing external_repository | ✓ | ✓ |
| | **file_store** | | | | |
| `POST` | `/api/nutanix/v3/file_store` |  | Create a new file_item | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/file_store/list` |  | Get a list of existing file_items | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/file_store/{uuid}` |  | Delete a existing file_item | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/file_store/{uuid}` |  | Get a existing file_item | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/file_store/{uuid}` |  | Update a existing file_item | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/file_store/{uuid}/file` |  | Get file item contents | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/file_store/{uuid}/file` |  | Upload file item contents | ✓ | ✓ |
| | **groups** | | | | |
| `POST` | `/api/nutanix/v3/groups` |  | Get Entities. | ✓ | ✓ |
| | **hosts** | | | | |
| `POST` | `/api/nutanix/v3/hosts/list` |  | Get a list of existing Hosts | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/hosts/{uuid}` |  | Delete a existing Host | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/hosts/{uuid}` |  | Get a existing Host | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/hosts/{uuid}` |  | Update a existing Host | ✓ | ✓ |
| | **idempotence_identifiers** | | | | |
| `POST` | `/api/nutanix/v3/idempotence_identifiers` |  | Create an new idempotence_identifier " (UUID4)" | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/idempotence_identifiers/{client_identifier}` |  | Delete an existing idempotence_identifier | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/idempotence_identifiers/{client_identifier}` |  | Get an existing idempotence_identifier | ✓ | ✓ |
| | **images** | | | | |
| `POST` | `/api/nutanix/v3/images` |  | Create a new image | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/images/list` |  | Get a list of existing images | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/images/{uuid}` |  | Delete a existing image | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/images/{uuid}` |  | Get a existing image | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/images/{uuid}` |  | Update a existing image | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/images/{uuid}/file` |  | Get Image Contents | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/images/{uuid}/file` |  | Upload Image Contents | ✓ | ✓ |
| | **ipfix_exporters** | | | | |
| `POST` | `/api/nutanix/v3/ipfix_exporters` |  | Create a new IPFix Exporter | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/ipfix_exporters/{uuid}` |  | Delete a existing IPFix Exporter | ✓ | ✓ |
| | **mh_vms** | | | | |
| `POST` | `/api/nutanix/v3/mh_vms` |  | Create a new VM | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/mh_vms/{uuid}` |  | Update an existing VM | ✓ | ✓ |
| | **ncc** | | | | |
| `GET` | `/api/nutanix/v3/ncc/archives/{task_uuid}` |  | Download archive logs corresponding to the task | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/ncc/collect_logs` |  | Create a new log collection | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/ncc/tags/list` |  | Get a list of existing ncc tags | ✓ | ✓ |
| | **network_function_chains** | | | | |
| `POST` | `/api/nutanix/v3/network_function_chains` |  | Create a new Network Function Chain | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/network_function_chains/list` |  | Get a list of existing Network Function Chains | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/network_function_chains/{uuid}` |  | Delete a existing Network Function Chain | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/network_function_chains/{uuid}` |  | Get a existing Network Function Chain | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/network_function_chains/{uuid}` |  | Update a existing Network Function Chain | ✓ | ✓ |
| | **ngt** | | | | |
| `POST` | `/api/nutanix/v3/ngt/list` |  | Get a list of existing vms | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/ngt/{uuid}` |  | Get a existing ngt | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vms/{uuid}/ngt` |  | Get a existing ngt | ✓ | ✓ |
| | **oauth** | | | | |
| `GET` | `/api/nutanix/v3/oauth/adfs_login` |  | ADFS login url for idp | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/authorize` |  | Used to get authorization code from server | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/client` |  | This is used to register new oauth client | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/client/list` |  | Retrieves all oauth client | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/oauth/client/{client_id}` |  | Delete an existing Oauth client | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/oauth/client/{client_id}` |  | Used to fetch existing oauth client details | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/oauth/client/{client_id}` |  | Used to update existing client details | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/generate_token` |  | This is used when the user is already authenticated and would like to create bearer tokens for distribution | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/oauth/idp_callback` |  | Oauth2 callback from IDP to intent gateway | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/oauth/idp_login` |  | Oauth2 login to idp | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/revoke_token` |  | Revoke a token will cause the token to be removed from system Any subsequent authorization calls with the token will fail | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/oauth/token` |  | This callback is used to get token from Oauth2 provider | ✓ | ✓ |
| | **ovas** | | | | |
| `PUT` | `/api/nutanix/v3/ovas/{uuid}/chunks` |  | Upload file chunk of an OVA | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/ovas/{uuid}/file` |  | Get OVA Contents | ✓ | ✓ |
| | **permissions** | | | | |
| `POST` | `/api/nutanix/v3/permissions/list` |  | List the permissions. | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/permissions/{uuid}` |  | Get a permission. | ✓ | ✓ |
| | **portal_services** | | | | |
| `POST` | `/api/nutanix/v3/portal_services/software/{software_type}/list` |  | Get all available software on Nutanix Portal | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/portal_services/software/{software_type}/{version}` |  | Get specified software information | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/portal_services/support_cases/upload` |  | Upload attachements for a specific support case. | ✓ | ✓ |
| | **prism_central** | | | | |
| `POST` | `/api/nutanix/v3/prism_central` |  | Create a new Prism Central | ✓ | ✓ |
| | **projects** | | | | |
| `POST` | `/api/nutanix/v3/projects/list` |  | Get a list of existing Projects | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/projects/{uuid}` |  | Get a existing Project | ✓ | ✓ |
| | **rack** | | | | |
| `POST` | `/api/nutanix/v3/racks` |  | Create a rack instance | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/racks/list` |  | Retrieves all racks | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/racks/validate_rack_config` |  | Validates Specified Rack Configuration | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/racks/{uuid}` |  | Delete specified rack | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/racks/{uuid}` |  | Retrieves specified rack | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/racks/{uuid}` |  | Update rack | ✓ | ✓ |
| | **rackable_unit** | | | | |
| `POST` | `/api/nutanix/v3/rackable_units/list` |  | Retrieves all rackable units | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/rackable_units/{uuid}` |  | Retrieves specified rackable unit | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/rackable_units/{uuid}` |  | Update rackable unit | ✓ | ✓ |
| | **ratelimiter** | | | | |
| `GET` | `/api/nutanix/v3/ratelimit_config` |  | Configure ratelimiter for cluster | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/ratelimit_config` |  | Configure ratelimiter for cluster | ✓ | ✓ |
| | **remote_connections** | | | | |
| `POST` | `/api/nutanix/v3/fanout_proxy` |  | Proxies request to remote cluster | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/remote_connections` |  | Creates a remote connection | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/remote_connections/list` |  | Get list of remote connections | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/remote_connections/{uuid}` |  | Delete an existing remote connection | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/remote_connections/{uuid}` |  | Used to fetch remote connection details | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/remote_connections/{uuid}` |  | Used to update remote connection details | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/remote_rpc_request` |  | Execute Remote RPC | ✓ | ✓ |
| | **remote_syslog_modules** | | | | |
| `POST` | `/api/nutanix/v3/remote_syslog_modules` |  | Create a new Remote Syslog modules list | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/remote_syslog_modules/list` |  | Get a list of existing Remote Syslog modules | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/remote_syslog_modules/{uuid}` |  | Delete a existing Remote Syslog modules list | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/remote_syslog_modules/{uuid}` |  | Get a existing Remote Syslog modules list | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/remote_syslog_modules/{uuid}` |  | Update a existing Remote Syslog modules list | ✓ | ✓ |
| | **remote_syslog_servers** | | | | |
| `POST` | `/api/nutanix/v3/remote_syslog_servers` |  | Create a new Remote Syslog server | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/remote_syslog_servers/cluster_rsyslog_servers` |  | Remote Syslog servers configured on all PEs registered to PC. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/remote_syslog_servers/list` |  | Get a list of existing Remote Syslog servers | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/remote_syslog_servers/{uuid}` |  | Delete a existing Remote Syslog server | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/remote_syslog_servers/{uuid}` |  | Get a existing Remote Syslog server | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/remote_syslog_servers/{uuid}` |  | Update a existing Remote Syslog server | ✓ | ✓ |
| | **roles** | | | | |
| `POST` | `/api/nutanix/v3/roles/list` |  | List the roles. | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/roles/{uuid}` |  | Get a role. | ✓ | ✓ |
| | **ssh_user** | | | | |
| `POST` | `/api/nutanix/v3/ssh_user` |  | Add SSH User to the entity | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/ssh_user/list` |  | Retrieves all SSH Users on the cluster | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/ssh_user/{uuid}` |  | Unregister specified SSH User | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/ssh_user/{uuid}` |  | Retrieves specified SSH User | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/ssh_user/{uuid}` |  | Update SSH User entity | ✓ | ✓ |
| | **subnets** | | | | |
| `POST` | `/api/nutanix/v3/subnets` |  | Create a new subnet | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/subnets/list` |  | Get a list of existing subnets | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/subnets/{uuid}` |  | Delete a existing subnet | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/subnets/{uuid}` |  | Get a existing subnet | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/subnets/{uuid}` |  | Update a existing subnet | ✓ | ✓ |
| | **tasks** | | | | |
| `POST` | `/api/nutanix/v3/tasks/list` |  | Get a list of existing Tasks | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/tasks/poll` |  | Poll for completion of tasks | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/tasks/{uuid}` |  | Get a existing Task | ✓ | ✓ |
| | **tenants** | | | | |
| `POST` | `/api/nutanix/v3/tenant_clusters/config/tenants` |  | Create a new Tenant | ✓ | ✓ |
| | **user_groups** | | | | |
| `POST` | `/api/nutanix/v3/user_groups/list` |  | Get a list of existing User Groups | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/user_groups/{uuid}` |  | Get a existing User Group | ✓ | ✓ |
| | **users** | | | | |
| `GET` | `/api/nutanix/v3/logout` |  | Logs out the current user | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/users/info` |  | Retrieves the Access control policies and other user data for logged in user. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/users/list` |  | Get a list of existing Users | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/users/me` |  | Retrieves currently logged in user. | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/users/{uuid}` |  | Get a existing User | ✓ | ✓ |
| | **versions** | | | | |
| `GET` | `/api/nutanix/v3/versions` |  | Get details on the api version | ✓ | ✓ |
| | **vm_recovery_points** | | | | |
| `POST` | `/api/nutanix/v3/vm_recovery_points` |  | Create a new vm recovery point | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_recovery_points/list` |  | Get a list of existing vm recovery point | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_recovery_points/restore` |  | Restore a vm recovery point for the given time point. | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/vm_recovery_points/{uuid}` |  | Delete a existing vm recovery point | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vm_recovery_points/{uuid}` |  | Get a existing vm recovery point | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/vm_recovery_points/{uuid}` |  | Update a existing vm recovery point | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_recovery_points/{uuid}/promote` |  | Promote a vm recovery point. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_recovery_points/{uuid}/restore` |  | Restore a vm recovery point. | ✓ | ✓ |
| | **vm_snapshot** | | | | |
| `POST` | `/api/nutanix/v3/vm_snapshots` |  | Create VM snapshot | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_snapshots/list` |  | Get VM snapshots | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/vm_snapshots/{uuid}` |  | Delete VM snapshot | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vm_snapshots/{uuid}` |  | Get VM snapshot | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/vm_snapshots/{uuid}` |  | Update VM snapshot | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vm_snapshots/{uuid}/clone` |  | Create a clone of a VM | ✓ | ✓ |
| | **vms** | | | | |
| `POST` | `/api/nutanix/v3/vms` |  | Create a new VM | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vms/capabilities` |  | Capability information for VMs. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vms/list` |  | Get a list of existing VMs | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/vms/{uuid}` |  | Delete an existing VM | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vms/{uuid}` |  | Get an existing VM | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/vms/{uuid}` |  | Update an existing VM | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vms/{uuid}/revert` |  | Revert the vm to the given recovery point. | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/vms/{uuid}/snapshot` |  | Create a vm recovery point. | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/vms/{uuid}/vm_disk/{vm_disk_uuid}/data` |  | Read from a VM disk. | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/vms/{uuid}/vm_disk/{vm_disk_uuid}/data` |  | Write to a VM disk. | ✓ | ✓ |
| | **volume_group_snapshots** | | | | |
| `POST` | `/api/nutanix/v3/volume_group_snapshots` |  | Create a new volume_group_snapshot | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/volume_group_snapshots/list` |  | Get a list of existing volume_group_snapshots | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/volume_group_snapshots/{uuid}` |  | Delete a existing volume_group_snapshot | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/volume_group_snapshots/{uuid}` |  | Get a existing volume_group_snapshot | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/volume_group_snapshots/{uuid}` |  | Update a existing volume_group_snapshot | ✓ | ✓ |
| | **volume_groups** | | | | |
| `POST` | `/api/nutanix/v3/volume_groups` |  | Create a new volume_group | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/volume_groups/list` |  | Get a list of existing volume_groups | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/volume_groups/{uuid}` |  | Delete a existing volume_group | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/volume_groups/{uuid}` |  | Get a existing volume_group | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/volume_groups/{uuid}` |  | Update a existing volume_group | ✓ | ✓ |
| | **webhooks** | | | | |
| `POST` | `/api/nutanix/v3/webhooks` |  | Create a new Webhook | ✓ | ✓ |
| `POST` | `/api/nutanix/v3/webhooks/list` |  | Get a list of existing Webhooks | ✓ | ✓ |
| `DELETE` | `/api/nutanix/v3/webhooks/{uuid}` |  | Delete a existing Webhook | ✓ | ✓ |
| `GET` | `/api/nutanix/v3/webhooks/{uuid}` |  | Get a existing Webhook | ✓ | ✓ |
| `PUT` | `/api/nutanix/v3/webhooks/{uuid}` |  | Update a existing Webhook | ✓ | ✓ |

