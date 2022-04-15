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


class AccessLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    READ = "Read"
    WRITE = "Write"

class DiskCreateOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This enumerates the possible sources of a disk's creation.
    """

    #: Create an empty data disk of a size given by diskSizeGB.
    EMPTY = "Empty"
    #: Disk will be attached to a VM.
    ATTACH = "Attach"
    #: Create a new disk from a platform image specified by the given imageReference or
    #: galleryImageReference.
    FROM_IMAGE = "FromImage"
    #: Create a disk by importing from a blob specified by a sourceUri in a storage account specified
    #: by storageAccountId.
    IMPORT_ENUM = "Import"
    #: Create a new disk or snapshot by copying from a disk or snapshot specified by the given
    #: sourceResourceId.
    COPY = "Copy"
    #: Create a new disk by copying from a backup recovery point.
    RESTORE = "Restore"
    #: Create a new disk by obtaining a write token and using it to directly upload the contents of
    #: the disk.
    UPLOAD = "Upload"

class DiskEncryptionSetIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"

class DiskState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the disk.
    """

    #: The disk is not being used and can be attached to a VM.
    UNATTACHED = "Unattached"
    #: The disk is currently mounted to a running VM.
    ATTACHED = "Attached"
    #: The disk is mounted to a stopped-deallocated VM.
    RESERVED = "Reserved"
    #: The disk currently has an Active SAS Uri associated with it.
    ACTIVE_SAS = "ActiveSAS"
    #: A disk is ready to be created by upload by requesting a write token.
    READY_TO_UPLOAD = "ReadyToUpload"
    #: A disk is created for upload and a write token has been issued for uploading to it.
    ACTIVE_UPLOAD = "ActiveUpload"

class DiskStorageAccountTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    #: Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    STANDARD_LRS = "Standard_LRS"
    #: Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    PREMIUM_LRS = "Premium_LRS"
    #: Standard SSD locally redundant storage. Best for web servers, lightly used enterprise
    #: applications and dev/test.
    STANDARD_SSD_LRS = "StandardSSD_LRS"
    #: Ultra SSD locally redundant storage. Best for IO-intensive workloads such as SAP HANA, top tier
    #: databases (for example, SQL, Oracle), and other transaction-heavy workloads.
    ULTRA_SSD_LRS = "UltraSSD_LRS"

class EncryptionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of key used to encrypt the data of the disk.
    """

    #: Disk is encrypted with XStore managed key at rest. It is the default encryption type.
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    #: Disk is encrypted with Customer managed key at rest.
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"

class HyperVGeneration(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """

    V1 = "V1"
    V2 = "V2"

class OperatingSystemTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Operating System type.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class SnapshotStorageAccountTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    #: Standard HDD locally redundant storage.
    STANDARD_LRS = "Standard_LRS"
    #: Premium SSD locally redundant storage.
    PREMIUM_LRS = "Premium_LRS"
    #: Standard zone redundant storage.
    STANDARD_ZRS = "Standard_ZRS"
