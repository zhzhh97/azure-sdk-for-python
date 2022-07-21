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


class AssessmentDayOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Day of the week to run assessment.
    """

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class AutoBackupDaysOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class BackupScheduleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup schedule type.
    """

    MANUAL = "Manual"
    AUTOMATED = "Automated"

class ClusterConfiguration(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Cluster type.
    """

    DOMAINFUL = "Domainful"

class ClusterManagerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of
    the group and the OS type.
    """

    WSFC = "WSFC"

class Commit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Replica commit mode in availability group.
    """

    SYNCHRONOUS_COMMIT = "SYNCHRONOUS_COMMIT"
    ASYNCHRONOUS_COMMIT = "ASYNCHRONOUS_COMMIT"

class ConnectivityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL Server connectivity option.
    """

    LOCAL = "LOCAL"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DayOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Day of week to apply the patch on.
    """

    EVERYDAY = "Everyday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class DiskConfigurationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Disk configuration to apply to SQL Server.
    """

    NEW = "NEW"
    EXTEND = "EXTEND"
    ADD = "ADD"

class Failover(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Replica failover mode in availability group.
    """

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"

class FullBackupFrequencyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Frequency of full backups. In both cases, full backups begin during the next scheduled time
    window.
    """

    DAILY = "Daily"
    WEEKLY = "Weekly"

class IdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an
    Azure Active Directory principal for the resource.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"

class OperationOrigin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    USER = "user"
    SYSTEM = "system"

class ReadableSecondary(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Replica readable secondary mode in availability group.
    """

    NO = "NO"
    ALL = "ALL"
    READ_ONLY = "READ_ONLY"

class Role(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Replica Role in availability group.
    """

    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"

class ScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Scale type.
    """

    HA = "HA"

class SqlImageSku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL Server edition type.
    """

    DEVELOPER = "Developer"
    EXPRESS = "Express"
    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"
    WEB = "Web"

class SqlManagementMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL Server Management type.
    """

    FULL = "Full"
    LIGHT_WEIGHT = "LightWeight"
    NO_AGENT = "NoAgent"

class SqlServerLicenseType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL Server license type.
    """

    PAYG = "PAYG"
    AHUB = "AHUB"
    DR = "DR"

class SqlVmGroupImageSku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL image sku.
    """

    DEVELOPER = "Developer"
    ENTERPRISE = "Enterprise"

class SqlWorkloadType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL Server workload type.
    """

    GENERAL = "GENERAL"
    OLTP = "OLTP"
    DW = "DW"

class StorageWorkloadType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Storage workload type.
    """

    GENERAL = "GENERAL"
    OLTP = "OLTP"
    DW = "DW"
