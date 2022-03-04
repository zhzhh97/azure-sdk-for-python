# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AcquireStorageAccountLock(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether storage account lock is to be acquired for this container or not.
    """

    ACQUIRE = "Acquire"
    NOT_ACQUIRE = "NotAcquire"

class AzureFileShareType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """File Share type XSync or XSMB.
    """

    INVALID = "Invalid"
    XSMB = "XSMB"
    X_SYNC = "XSync"

class BackupEngineType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the backup engine.
    """

    INVALID = "Invalid"
    DPM_BACKUP_ENGINE = "DpmBackupEngine"
    AZURE_BACKUP_SERVER_ENGINE = "AzureBackupServerEngine"

class BackupItemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of backup items associated with this container.
    """

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"

class BackupManagementType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup management type to execute the current job.
    """

    INVALID = "Invalid"
    AZURE_IAAS_VM = "AzureIaasVM"
    MAB = "MAB"
    DPM = "DPM"
    AZURE_BACKUP_SERVER = "AzureBackupServer"
    AZURE_SQL = "AzureSql"
    AZURE_STORAGE = "AzureStorage"
    AZURE_WORKLOAD = "AzureWorkload"
    DEFAULT_BACKUP = "DefaultBackup"

class BackupType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of backup, viz. Full, Differential, Log or CopyOnlyFull
    """

    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"

class ContainerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of container for filter
    """

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"
    MICROSOFT_CLASSIC_COMPUTE_VIRTUAL_MACHINES = "Microsoft.ClassicCompute/virtualMachines"
    MICROSOFT_COMPUTE_VIRTUAL_MACHINES = "Microsoft.Compute/virtualMachines"
    AZURE_WORKLOAD_CONTAINER = "AzureWorkloadContainer"

class CopyOptions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Options to resolve copy conflicts.
    """

    INVALID = "Invalid"
    CREATE_COPY = "CreateCopy"
    SKIP = "Skip"
    OVERWRITE = "Overwrite"
    FAIL_ON_CONFLICT = "FailOnConflict"

class CreateMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Create mode to indicate recovery of existing soft deleted data source or creation of new data
    source.
    """

    INVALID = "Invalid"
    DEFAULT = "Default"
    RECOVER = "Recover"

class DataMoveLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """DataMove Level
    """

    INVALID = "Invalid"
    VAULT = "Vault"
    CONTAINER = "Container"

class DataSourceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of workload this item represents.
    """

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"

class DayOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class DedupState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Vault Dedup state
    """

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class EncryptionAtRestType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Encryption At Rest Type
    """

    INVALID = "Invalid"
    MICROSOFT_MANAGED = "MicrosoftManaged"
    CUSTOMER_MANAGED = "CustomerManaged"

class EnhancedSecurityState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enabled or Disabled.
    """

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class FabricName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the fabric name - Azure or AD
    """

    INVALID = "Invalid"
    AZURE = "Azure"

class HealthState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Health State for the backed up item.
    """

    PASSED = "Passed"
    ACTION_REQUIRED = "ActionRequired"
    ACTION_SUGGESTED = "ActionSuggested"
    INVALID = "Invalid"

class HealthStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Health status of protected item.
    """

    PASSED = "Passed"
    ACTION_REQUIRED = "ActionRequired"
    ACTION_SUGGESTED = "ActionSuggested"
    INVALID = "Invalid"

class HttpStatusCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """HTTP Status Code of the operation.
    """

    CONTINUE_ENUM = "Continue"
    SWITCHING_PROTOCOLS = "SwitchingProtocols"
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "NonAuthoritativeInformation"
    NO_CONTENT = "NoContent"
    RESET_CONTENT = "ResetContent"
    PARTIAL_CONTENT = "PartialContent"
    MULTIPLE_CHOICES = "MultipleChoices"
    AMBIGUOUS = "Ambiguous"
    MOVED_PERMANENTLY = "MovedPermanently"
    MOVED = "Moved"
    FOUND = "Found"
    REDIRECT = "Redirect"
    SEE_OTHER = "SeeOther"
    REDIRECT_METHOD = "RedirectMethod"
    NOT_MODIFIED = "NotModified"
    USE_PROXY = "UseProxy"
    UNUSED = "Unused"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    REDIRECT_KEEP_VERB = "RedirectKeepVerb"
    BAD_REQUEST = "BadRequest"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "PaymentRequired"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    METHOD_NOT_ALLOWED = "MethodNotAllowed"
    NOT_ACCEPTABLE = "NotAcceptable"
    PROXY_AUTHENTICATION_REQUIRED = "ProxyAuthenticationRequired"
    REQUEST_TIMEOUT = "RequestTimeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "LengthRequired"
    PRECONDITION_FAILED = "PreconditionFailed"
    REQUEST_ENTITY_TOO_LARGE = "RequestEntityTooLarge"
    REQUEST_URI_TOO_LONG = "RequestUriTooLong"
    UNSUPPORTED_MEDIA_TYPE = "UnsupportedMediaType"
    REQUESTED_RANGE_NOT_SATISFIABLE = "RequestedRangeNotSatisfiable"
    EXPECTATION_FAILED = "ExpectationFailed"
    UPGRADE_REQUIRED = "UpgradeRequired"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    NOT_IMPLEMENTED = "NotImplemented"
    BAD_GATEWAY = "BadGateway"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"
    GATEWAY_TIMEOUT = "GatewayTimeout"
    HTTP_VERSION_NOT_SUPPORTED = "HttpVersionNotSupported"

class IAASVMPolicyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "Invalid"
    V1 = "V1"
    V2 = "V2"

class InfrastructureEncryptionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "Invalid"
    DISABLED = "Disabled"
    ENABLED = "Enabled"

class InquiryStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of protectable item, i.e. InProgress,Succeeded,Failed
    """

    INVALID = "Invalid"
    SUCCESS = "Success"
    FAILED = "Failed"

class IntentItemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of workload this item represents
    """

    INVALID = "Invalid"
    SQL_INSTANCE = "SQLInstance"
    SQL_AVAILABILITY_GROUP_CONTAINER = "SQLAvailabilityGroupContainer"

class JobOperationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of operation.
    """

    INVALID = "Invalid"
    REGISTER = "Register"
    UN_REGISTER = "UnRegister"
    CONFIGURE_BACKUP = "ConfigureBackup"
    BACKUP = "Backup"
    RESTORE = "Restore"
    DISABLE_BACKUP = "DisableBackup"
    DELETE_BACKUP_DATA = "DeleteBackupData"
    CROSS_REGION_RESTORE = "CrossRegionRestore"
    UNDELETE = "Undelete"
    UPDATE_CUSTOMER_MANAGED_KEY = "UpdateCustomerManagedKey"

class JobStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the job.
    """

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"

class JobSupportedAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "Invalid"
    CANCELLABLE = "Cancellable"
    RETRIABLE = "Retriable"

class LastBackupStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Last backup operation status. Possible values: Healthy, Unhealthy.
    """

    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    IR_PENDING = "IRPending"

class LastUpdateStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "Invalid"
    NOT_ENABLED = "NotEnabled"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    PARTIALLY_FAILED = "PartiallyFailed"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    INITIALIZED = "Initialized"
    FIRST_INITIALIZATION = "FirstInitialization"

class MabServerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Server type of MAB container.
    """

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"

class MonthOfYear(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "Invalid"
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

class OperationStatusValues(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operation status.
    """

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class OperationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Re-Do Operation
    """

    INVALID = "Invalid"
    REGISTER = "Register"
    REREGISTER = "Reregister"

class OverwriteOptions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Can Overwrite if Target DataBase already exists
    """

    INVALID = "Invalid"
    FAIL_ON_CONFLICT = "FailOnConflict"
    OVERWRITE = "Overwrite"

class PolicyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of backup policy type
    """

    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"

class PrivateEndpointConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the status
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class ProtectedItemHealthStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Health status of the backup item, evaluated based on last heartbeat received
    """

    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NOT_REACHABLE = "NotReachable"
    IR_PENDING = "IRPending"

class ProtectedItemState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup state of the backed up item.
    """

    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"

class ProtectionIntentItemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """backup protectionIntent type.
    """

    INVALID = "Invalid"
    AZURE_RESOURCE_ITEM = "AzureResourceItem"
    RECOVERY_SERVICE_VAULT_ITEM = "RecoveryServiceVaultItem"
    AZURE_WORKLOAD_CONTAINER_AUTO_PROTECTION_INTENT = "AzureWorkloadContainerAutoProtectionIntent"
    AZURE_WORKLOAD_AUTO_PROTECTION_INTENT = "AzureWorkloadAutoProtectionIntent"
    AZURE_WORKLOAD_SQL_AUTO_PROTECTION_INTENT = "AzureWorkloadSQLAutoProtectionIntent"

class ProtectionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup state of this backup item.
    """

    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"

class ProtectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies whether the container is registered or not
    """

    INVALID = "Invalid"
    NOT_PROTECTED = "NotProtected"
    PROTECTING = "Protecting"
    PROTECTED = "Protected"
    PROTECTION_FAILED = "ProtectionFailed"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets provisioning state of the private endpoint connection
    """

    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    PENDING = "Pending"

class RecoveryMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Defines whether the current recovery mode is file restore or database restore
    """

    INVALID = "Invalid"
    FILE_RECOVERY = "FileRecovery"
    WORKLOAD_RECOVERY = "WorkloadRecovery"

class RecoveryPointTierStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Recovery point tier status.
    """

    INVALID = "Invalid"
    VALID = "Valid"
    DISABLED = "Disabled"
    DELETED = "Deleted"
    REHYDRATED = "Rehydrated"

class RecoveryPointTierType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Recovery point tier type.
    """

    INVALID = "Invalid"
    INSTANT_RP = "InstantRP"
    HARDENED_RP = "HardenedRP"
    ARCHIVED_RP = "ArchivedRP"

class RecoveryType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of this recovery.
    """

    INVALID = "Invalid"
    ORIGINAL_LOCATION = "OriginalLocation"
    ALTERNATE_LOCATION = "AlternateLocation"
    RESTORE_DISKS = "RestoreDisks"
    OFFLINE = "Offline"

class RehydrationPriority(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Rehydration Priority
    """

    STANDARD = "Standard"
    HIGH = "High"

class ResourceHealthStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource Health Status
    """

    HEALTHY = "Healthy"
    TRANSIENT_DEGRADED = "TransientDegraded"
    PERSISTENT_DEGRADED = "PersistentDegraded"
    TRANSIENT_UNHEALTHY = "TransientUnhealthy"
    PERSISTENT_UNHEALTHY = "PersistentUnhealthy"
    INVALID = "Invalid"

class RestorePointQueryType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """RestorePoint type
    """

    INVALID = "Invalid"
    FULL = "Full"
    LOG = "Log"
    DIFFERENTIAL = "Differential"
    FULL_AND_DIFFERENTIAL = "FullAndDifferential"
    ALL = "All"
    INCREMENTAL = "Incremental"

class RestorePointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of restore point
    """

    INVALID = "Invalid"
    FULL = "Full"
    LOG = "Log"
    DIFFERENTIAL = "Differential"
    INCREMENTAL = "Incremental"

class RestoreRequestType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Restore Type (FullShareRestore or ItemLevelRestore)
    """

    INVALID = "Invalid"
    FULL_SHARE_RESTORE = "FullShareRestore"
    ITEM_LEVEL_RESTORE = "ItemLevelRestore"

class RetentionDurationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Retention duration type of retention policy.
    """

    INVALID = "Invalid"
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEARS = "Years"

class RetentionScheduleFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Retention schedule format type for monthly retention policy.
    """

    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"

class ScheduleRunType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Frequency of the schedule operation of this policy.
    """

    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    HOURLY = "Hourly"

class SoftDeleteFeatureState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Soft Delete feature state
    """

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class SQLDataDirectoryType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of data directory mapping
    """

    INVALID = "Invalid"
    DATA = "Data"
    LOG = "Log"

class StorageType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Storage type
    """

    INVALID = "Invalid"
    GEO_REDUNDANT = "GeoRedundant"
    LOCALLY_REDUNDANT = "LocallyRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"
    READ_ACCESS_GEO_ZONE_REDUNDANT = "ReadAccessGeoZoneRedundant"

class StorageTypeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Locked or Unlocked. Once a machine is registered against a resource, the storageTypeState is
    always Locked.
    """

    INVALID = "Invalid"
    LOCKED = "Locked"
    UNLOCKED = "Unlocked"

class SupportStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Support status of feature
    """

    INVALID = "Invalid"
    SUPPORTED = "Supported"
    DEFAULT_OFF = "DefaultOFF"
    DEFAULT_ON = "DefaultON"
    NOT_SUPPORTED = "NotSupported"

class Type(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup management type for this container.
    """

    INVALID = "Invalid"
    BACKUP_PROTECTED_ITEM_COUNT_SUMMARY = "BackupProtectedItemCountSummary"
    BACKUP_PROTECTION_CONTAINER_COUNT_SUMMARY = "BackupProtectionContainerCountSummary"

class UsagesUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Unit of the usage.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"

class ValidationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Validation Status
    """

    INVALID = "Invalid"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class WeekOfMonth(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    LAST = "Last"
    INVALID = "Invalid"

class WorkloadItemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Workload item type of the item for which intent is to be set
    """

    INVALID = "Invalid"
    SQL_INSTANCE = "SQLInstance"
    SQL_DATA_BASE = "SQLDataBase"
    SAP_HANA_SYSTEM = "SAPHanaSystem"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_SYSTEM = "SAPAseSystem"
    SAP_ASE_DATABASE = "SAPAseDatabase"

class WorkloadType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of workload for the backup management
    """

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"

class XcoolState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Vault x-cool state
    """

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
