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


class AccessKeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Which access key to regenerate.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class AofFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Sets the frequency at which data is written to disk.
    """

    ONE_S = "1s"
    ALWAYS = "always"

class ClusteringPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Clustering policy - default is OSSCluster. Specified at create time.
    """

    ENTERPRISE_CLUSTER = "EnterpriseCluster"
    OSS_CLUSTER = "OSSCluster"

class EvictionPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Redis eviction policy - default is VolatileLRU
    """

    ALL_KEYS_LFU = "AllKeysLFU"
    ALL_KEYS_LRU = "AllKeysLRU"
    ALL_KEYS_RANDOM = "AllKeysRandom"
    VOLATILE_LRU = "VolatileLRU"
    VOLATILE_LFU = "VolatileLFU"
    VOLATILE_TTL = "VolatileTTL"
    VOLATILE_RANDOM = "VolatileRandom"
    NO_EVICTION = "NoEviction"

class LinkState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the link between the database resources.
    """

    LINKED = "Linked"
    LINKING = "Linking"
    UNLINKING = "Unlinking"
    LINK_FAILED = "LinkFailed"
    UNLINK_FAILED = "UnlinkFailed"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class Protocol(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols.
    Default is TLS-encrypted.
    """

    ENCRYPTED = "Encrypted"
    PLAINTEXT = "Plaintext"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current provisioning status
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"

class RdbFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Sets the frequency at which a snapshot of the database is created.
    """

    ONE_H = "1h"
    SIX_H = "6h"
    TWELVE_H = "12h"

class ResourceState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current resource status
    """

    RUNNING = "Running"
    CREATING = "Creating"
    CREATE_FAILED = "CreateFailed"
    UPDATING = "Updating"
    UPDATE_FAILED = "UpdateFailed"
    DELETING = "Deleting"
    DELETE_FAILED = "DeleteFailed"
    ENABLING = "Enabling"
    ENABLE_FAILED = "EnableFailed"
    DISABLING = "Disabling"
    DISABLE_FAILED = "DisableFailed"
    DISABLED = "Disabled"

class SkuName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10,
    EnterpriseFlash_F300 etc.)
    """

    ENTERPRISE_E10 = "Enterprise_E10"
    ENTERPRISE_E20 = "Enterprise_E20"
    ENTERPRISE_E50 = "Enterprise_E50"
    ENTERPRISE_E100 = "Enterprise_E100"
    ENTERPRISE_FLASH_F300 = "EnterpriseFlash_F300"
    ENTERPRISE_FLASH_F700 = "EnterpriseFlash_F700"
    ENTERPRISE_FLASH_F1500 = "EnterpriseFlash_F1500"

class TlsVersion(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The minimum TLS version for the cluster to support, e.g. '1.2'
    """

    ONE0 = "1.0"
    ONE1 = "1.1"
    ONE2 = "1.2"
