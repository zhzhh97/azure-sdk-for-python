# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdditionalCapabilities
from ._models_py3 import AdditionalUnattendContent
from ._models_py3 import ApiEntityReference
from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import ApplicationProfile
from ._models_py3 import AutomaticOSUpgradePolicy
from ._models_py3 import AutomaticOSUpgradeProperties
from ._models_py3 import AutomaticRepairsPolicy
from ._models_py3 import AvailabilitySet
from ._models_py3 import AvailabilitySetListResult
from ._models_py3 import AvailabilitySetUpdate
from ._models_py3 import AvailablePatchSummary
from ._models_py3 import BillingProfile
from ._models_py3 import BootDiagnostics
from ._models_py3 import BootDiagnosticsInstanceView
from ._models_py3 import CapacityReservation
from ._models_py3 import CapacityReservationGroup
from ._models_py3 import CapacityReservationGroupInstanceView
from ._models_py3 import CapacityReservationGroupListResult
from ._models_py3 import CapacityReservationGroupUpdate
from ._models_py3 import CapacityReservationInstanceView
from ._models_py3 import CapacityReservationInstanceViewWithName
from ._models_py3 import CapacityReservationListResult
from ._models_py3 import CapacityReservationProfile
from ._models_py3 import CapacityReservationUpdate
from ._models_py3 import CapacityReservationUtilization
from ._models_py3 import ComputeOperationListResult
from ._models_py3 import ComputeOperationValue
from ._models_py3 import DataDisk
from ._models_py3 import DataDiskImage
from ._models_py3 import DedicatedHost
from ._models_py3 import DedicatedHostAllocatableVM
from ._models_py3 import DedicatedHostAvailableCapacity
from ._models_py3 import DedicatedHostGroup
from ._models_py3 import DedicatedHostGroupInstanceView
from ._models_py3 import DedicatedHostGroupListResult
from ._models_py3 import DedicatedHostGroupUpdate
from ._models_py3 import DedicatedHostInstanceView
from ._models_py3 import DedicatedHostInstanceViewWithName
from ._models_py3 import DedicatedHostListResult
from ._models_py3 import DedicatedHostUpdate
from ._models_py3 import DiagnosticsProfile
from ._models_py3 import DiffDiskSettings
from ._models_py3 import DisallowedConfiguration
from ._models_py3 import DiskEncryptionSetParameters
from ._models_py3 import DiskEncryptionSettings
from ._models_py3 import DiskInstanceView
from ._models_py3 import DiskRestorePointInstanceView
from ._models_py3 import DiskRestorePointReplicationStatus
from ._models_py3 import ExtendedLocation
from ._models_py3 import HardwareProfile
from ._models_py3 import Image
from ._models_py3 import ImageDataDisk
from ._models_py3 import ImageDisk
from ._models_py3 import ImageListResult
from ._models_py3 import ImageOSDisk
from ._models_py3 import ImageReference
from ._models_py3 import ImageStorageProfile
from ._models_py3 import ImageUpdate
from ._models_py3 import InnerError
from ._models_py3 import InstanceViewStatus
from ._models_py3 import KeyVaultKeyReference
from ._models_py3 import KeyVaultSecretReference
from ._models_py3 import LastPatchInstallationSummary
from ._models_py3 import LinuxConfiguration
from ._models_py3 import LinuxParameters
from ._models_py3 import LinuxPatchSettings
from ._models_py3 import ListUsagesResult
from ._models_py3 import LogAnalyticsInputBase
from ._models_py3 import LogAnalyticsOperationResult
from ._models_py3 import LogAnalyticsOutput
from ._models_py3 import MaintenanceRedeployStatus
from ._models_py3 import ManagedDiskParameters
from ._models_py3 import NetworkInterfaceReference
from ._models_py3 import NetworkProfile
from ._models_py3 import OSDisk
from ._models_py3 import OSDiskImage
from ._models_py3 import OSProfile
from ._models_py3 import OrchestrationServiceStateInput
from ._models_py3 import OrchestrationServiceSummary
from ._models_py3 import PatchInstallationDetail
from ._models_py3 import PatchSettings
from ._models_py3 import Plan
from ._models_py3 import ProximityPlacementGroup
from ._models_py3 import ProximityPlacementGroupListResult
from ._models_py3 import ProximityPlacementGroupUpdate
from ._models_py3 import ProxyResource
from ._models_py3 import PublicIPAddressSku
from ._models_py3 import PurchasePlan
from ._models_py3 import RecoveryWalkResponse
from ._models_py3 import RequestRateByIntervalInput
from ._models_py3 import Resource
from ._models_py3 import RestorePoint
from ._models_py3 import RestorePointCollection
from ._models_py3 import RestorePointCollectionListResult
from ._models_py3 import RestorePointCollectionSourceProperties
from ._models_py3 import RestorePointCollectionUpdate
from ._models_py3 import RestorePointInstanceView
from ._models_py3 import RestorePointSourceMetadata
from ._models_py3 import RestorePointSourceVMDataDisk
from ._models_py3 import RestorePointSourceVMOSDisk
from ._models_py3 import RestorePointSourceVMStorageProfile
from ._models_py3 import RetrieveBootDiagnosticsDataResult
from ._models_py3 import RollbackStatusInfo
from ._models_py3 import RollingUpgradePolicy
from ._models_py3 import RollingUpgradeProgressInfo
from ._models_py3 import RollingUpgradeRunningStatus
from ._models_py3 import RollingUpgradeStatusInfo
from ._models_py3 import RunCommandDocument
from ._models_py3 import RunCommandDocumentBase
from ._models_py3 import RunCommandInput
from ._models_py3 import RunCommandInputParameter
from ._models_py3 import RunCommandListResult
from ._models_py3 import RunCommandParameterDefinition
from ._models_py3 import RunCommandResult
from ._models_py3 import ScaleInPolicy
from ._models_py3 import ScheduledEventsProfile
from ._models_py3 import SecurityProfile
from ._models_py3 import Sku
from ._models_py3 import SpotRestorePolicy
from ._models_py3 import SshConfiguration
from ._models_py3 import SshPublicKey
from ._models_py3 import SshPublicKeyGenerateKeyPairResult
from ._models_py3 import SshPublicKeyResource
from ._models_py3 import SshPublicKeyUpdateResource
from ._models_py3 import SshPublicKeysGroupListResult
from ._models_py3 import StorageProfile
from ._models_py3 import SubResource
from ._models_py3 import SubResourceReadOnly
from ._models_py3 import SubResourceWithColocationStatus
from ._models_py3 import TerminateNotificationProfile
from ._models_py3 import ThrottledRequestsInput
from ._models_py3 import UefiSettings
from ._models_py3 import UpdateResource
from ._models_py3 import UpgradeOperationHistoricalStatusInfo
from ._models_py3 import UpgradeOperationHistoricalStatusInfoProperties
from ._models_py3 import UpgradeOperationHistoryStatus
from ._models_py3 import UpgradePolicy
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import UserAssignedIdentitiesValue
from ._models_py3 import VMDiskSecurityProfile
from ._models_py3 import VMGalleryApplication
from ._models_py3 import VMScaleSetConvertToSinglePlacementGroupInput
from ._models_py3 import VMSizeProperties
from ._models_py3 import VaultCertificate
from ._models_py3 import VaultSecretGroup
from ._models_py3 import VirtualHardDisk
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineAgentInstanceView
from ._models_py3 import VirtualMachineAssessPatchesResult
from ._models_py3 import VirtualMachineCaptureParameters
from ._models_py3 import VirtualMachineCaptureResult
from ._models_py3 import VirtualMachineExtension
from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
from ._models_py3 import VirtualMachineExtensionImage
from ._models_py3 import VirtualMachineExtensionInstanceView
from ._models_py3 import VirtualMachineExtensionUpdate
from ._models_py3 import VirtualMachineExtensionsListResult
from ._models_py3 import VirtualMachineHealthStatus
from ._models_py3 import VirtualMachineIdentity
from ._models_py3 import VirtualMachineImage
from ._models_py3 import VirtualMachineImageFeature
from ._models_py3 import VirtualMachineImageResource
from ._models_py3 import VirtualMachineInstallPatchesParameters
from ._models_py3 import VirtualMachineInstallPatchesResult
from ._models_py3 import VirtualMachineInstanceView
from ._models_py3 import VirtualMachineIpTag
from ._models_py3 import VirtualMachineListResult
from ._models_py3 import VirtualMachineNetworkInterfaceConfiguration
from ._models_py3 import VirtualMachineNetworkInterfaceDnsSettingsConfiguration
from ._models_py3 import VirtualMachineNetworkInterfaceIPConfiguration
from ._models_py3 import VirtualMachinePatchStatus
from ._models_py3 import VirtualMachinePublicIPAddressConfiguration
from ._models_py3 import VirtualMachinePublicIPAddressDnsSettingsConfiguration
from ._models_py3 import VirtualMachineReimageParameters
from ._models_py3 import VirtualMachineRunCommand
from ._models_py3 import VirtualMachineRunCommandInstanceView
from ._models_py3 import VirtualMachineRunCommandScriptSource
from ._models_py3 import VirtualMachineRunCommandUpdate
from ._models_py3 import VirtualMachineRunCommandsListResult
from ._models_py3 import VirtualMachineScaleSet
from ._models_py3 import VirtualMachineScaleSetDataDisk
from ._models_py3 import VirtualMachineScaleSetExtension
from ._models_py3 import VirtualMachineScaleSetExtensionListResult
from ._models_py3 import VirtualMachineScaleSetExtensionProfile
from ._models_py3 import VirtualMachineScaleSetExtensionUpdate
from ._models_py3 import VirtualMachineScaleSetHardwareProfile
from ._models_py3 import VirtualMachineScaleSetIPConfiguration
from ._models_py3 import VirtualMachineScaleSetIdentity
from ._models_py3 import VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue
from ._models_py3 import VirtualMachineScaleSetInstanceView
from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
from ._models_py3 import VirtualMachineScaleSetIpTag
from ._models_py3 import VirtualMachineScaleSetListOSUpgradeHistory
from ._models_py3 import VirtualMachineScaleSetListResult
from ._models_py3 import VirtualMachineScaleSetListSkusResult
from ._models_py3 import VirtualMachineScaleSetListWithLinkResult
from ._models_py3 import VirtualMachineScaleSetManagedDiskParameters
from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetNetworkProfile
from ._models_py3 import VirtualMachineScaleSetOSDisk
from ._models_py3 import VirtualMachineScaleSetOSProfile
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetReimageParameters
from ._models_py3 import VirtualMachineScaleSetSku
from ._models_py3 import VirtualMachineScaleSetSkuCapacity
from ._models_py3 import VirtualMachineScaleSetStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdate
from ._models_py3 import VirtualMachineScaleSetUpdateIPConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkProfile
from ._models_py3 import VirtualMachineScaleSetUpdateOSDisk
from ._models_py3 import VirtualMachineScaleSetUpdateOSProfile
from ._models_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdateVMProfile
from ._models_py3 import VirtualMachineScaleSetVM
from ._models_py3 import VirtualMachineScaleSetVMExtension
from ._models_py3 import VirtualMachineScaleSetVMExtensionUpdate
from ._models_py3 import VirtualMachineScaleSetVMExtensionsListResult
from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceView
from ._models_py3 import VirtualMachineScaleSetVMListResult
from ._models_py3 import VirtualMachineScaleSetVMNetworkProfileConfiguration
from ._models_py3 import VirtualMachineScaleSetVMProfile
from ._models_py3 import VirtualMachineScaleSetVMProtectionPolicy
from ._models_py3 import VirtualMachineScaleSetVMReimageParameters
from ._models_py3 import VirtualMachineSize
from ._models_py3 import VirtualMachineSizeListResult
from ._models_py3 import VirtualMachineSoftwarePatchProperties
from ._models_py3 import VirtualMachineStatusCodeCount
from ._models_py3 import VirtualMachineUpdate
from ._models_py3 import WinRMConfiguration
from ._models_py3 import WinRMListener
from ._models_py3 import WindowsConfiguration
from ._models_py3 import WindowsParameters


from ._compute_management_client_enums import (
    ArchitectureTypes,
    AvailabilitySetSkuTypes,
    CachingTypes,
    CapacityReservationGroupInstanceViewTypes,
    CapacityReservationInstanceViewTypes,
    ConsistencyModeTypes,
    DedicatedHostLicenseTypes,
    DeleteOptions,
    DiffDiskOptions,
    DiffDiskPlacement,
    DiskCreateOptionTypes,
    DiskDeleteOptionTypes,
    DiskDetachOptionTypes,
    ExecutionState,
    ExpandTypesForGetCapacityReservationGroups,
    ExpandTypesForGetVMScaleSets,
    ExtendedLocationTypes,
    HyperVGenerationType,
    HyperVGenerationTypes,
    IPVersion,
    IPVersions,
    InstanceViewTypes,
    IntervalInMins,
    LinuxPatchAssessmentMode,
    LinuxVMGuestPatchMode,
    MaintenanceOperationResultCodeTypes,
    NetworkApiVersion,
    OperatingSystemStateTypes,
    OperatingSystemType,
    OperatingSystemTypes,
    OrchestrationMode,
    OrchestrationServiceNames,
    OrchestrationServiceState,
    OrchestrationServiceStateAction,
    PatchAssessmentState,
    PatchInstallationState,
    PatchOperationStatus,
    ProtocolTypes,
    ProximityPlacementGroupType,
    PublicIPAddressSkuName,
    PublicIPAddressSkuTier,
    PublicIPAllocationMethod,
    RepairAction,
    ResourceIdentityType,
    RestorePointCollectionExpandOptions,
    RestorePointExpandOptions,
    RollingUpgradeActionType,
    RollingUpgradeStatusCode,
    SecurityEncryptionTypes,
    SecurityTypes,
    SettingNames,
    StatusLevelTypes,
    StorageAccountTypes,
    UpgradeMode,
    UpgradeOperationInvoker,
    UpgradeState,
    VMGuestPatchClassificationLinux,
    VMGuestPatchClassificationWindows,
    VMGuestPatchRebootBehavior,
    VMGuestPatchRebootSetting,
    VMGuestPatchRebootStatus,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetScaleInRules,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
    VmDiskTypes,
    WindowsPatchAssessmentMode,
    WindowsVMGuestPatchMode,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AdditionalCapabilities',
    'AdditionalUnattendContent',
    'ApiEntityReference',
    'ApiError',
    'ApiErrorBase',
    'ApplicationProfile',
    'AutomaticOSUpgradePolicy',
    'AutomaticOSUpgradeProperties',
    'AutomaticRepairsPolicy',
    'AvailabilitySet',
    'AvailabilitySetListResult',
    'AvailabilitySetUpdate',
    'AvailablePatchSummary',
    'BillingProfile',
    'BootDiagnostics',
    'BootDiagnosticsInstanceView',
    'CapacityReservation',
    'CapacityReservationGroup',
    'CapacityReservationGroupInstanceView',
    'CapacityReservationGroupListResult',
    'CapacityReservationGroupUpdate',
    'CapacityReservationInstanceView',
    'CapacityReservationInstanceViewWithName',
    'CapacityReservationListResult',
    'CapacityReservationProfile',
    'CapacityReservationUpdate',
    'CapacityReservationUtilization',
    'ComputeOperationListResult',
    'ComputeOperationValue',
    'DataDisk',
    'DataDiskImage',
    'DedicatedHost',
    'DedicatedHostAllocatableVM',
    'DedicatedHostAvailableCapacity',
    'DedicatedHostGroup',
    'DedicatedHostGroupInstanceView',
    'DedicatedHostGroupListResult',
    'DedicatedHostGroupUpdate',
    'DedicatedHostInstanceView',
    'DedicatedHostInstanceViewWithName',
    'DedicatedHostListResult',
    'DedicatedHostUpdate',
    'DiagnosticsProfile',
    'DiffDiskSettings',
    'DisallowedConfiguration',
    'DiskEncryptionSetParameters',
    'DiskEncryptionSettings',
    'DiskInstanceView',
    'DiskRestorePointInstanceView',
    'DiskRestorePointReplicationStatus',
    'ExtendedLocation',
    'HardwareProfile',
    'Image',
    'ImageDataDisk',
    'ImageDisk',
    'ImageListResult',
    'ImageOSDisk',
    'ImageReference',
    'ImageStorageProfile',
    'ImageUpdate',
    'InnerError',
    'InstanceViewStatus',
    'KeyVaultKeyReference',
    'KeyVaultSecretReference',
    'LastPatchInstallationSummary',
    'LinuxConfiguration',
    'LinuxParameters',
    'LinuxPatchSettings',
    'ListUsagesResult',
    'LogAnalyticsInputBase',
    'LogAnalyticsOperationResult',
    'LogAnalyticsOutput',
    'MaintenanceRedeployStatus',
    'ManagedDiskParameters',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'OSDisk',
    'OSDiskImage',
    'OSProfile',
    'OrchestrationServiceStateInput',
    'OrchestrationServiceSummary',
    'PatchInstallationDetail',
    'PatchSettings',
    'Plan',
    'ProximityPlacementGroup',
    'ProximityPlacementGroupListResult',
    'ProximityPlacementGroupUpdate',
    'ProxyResource',
    'PublicIPAddressSku',
    'PurchasePlan',
    'RecoveryWalkResponse',
    'RequestRateByIntervalInput',
    'Resource',
    'RestorePoint',
    'RestorePointCollection',
    'RestorePointCollectionListResult',
    'RestorePointCollectionSourceProperties',
    'RestorePointCollectionUpdate',
    'RestorePointInstanceView',
    'RestorePointSourceMetadata',
    'RestorePointSourceVMDataDisk',
    'RestorePointSourceVMOSDisk',
    'RestorePointSourceVMStorageProfile',
    'RetrieveBootDiagnosticsDataResult',
    'RollbackStatusInfo',
    'RollingUpgradePolicy',
    'RollingUpgradeProgressInfo',
    'RollingUpgradeRunningStatus',
    'RollingUpgradeStatusInfo',
    'RunCommandDocument',
    'RunCommandDocumentBase',
    'RunCommandInput',
    'RunCommandInputParameter',
    'RunCommandListResult',
    'RunCommandParameterDefinition',
    'RunCommandResult',
    'ScaleInPolicy',
    'ScheduledEventsProfile',
    'SecurityProfile',
    'Sku',
    'SpotRestorePolicy',
    'SshConfiguration',
    'SshPublicKey',
    'SshPublicKeyGenerateKeyPairResult',
    'SshPublicKeyResource',
    'SshPublicKeyUpdateResource',
    'SshPublicKeysGroupListResult',
    'StorageProfile',
    'SubResource',
    'SubResourceReadOnly',
    'SubResourceWithColocationStatus',
    'TerminateNotificationProfile',
    'ThrottledRequestsInput',
    'UefiSettings',
    'UpdateResource',
    'UpgradeOperationHistoricalStatusInfo',
    'UpgradeOperationHistoricalStatusInfoProperties',
    'UpgradeOperationHistoryStatus',
    'UpgradePolicy',
    'Usage',
    'UsageName',
    'UserAssignedIdentitiesValue',
    'VMDiskSecurityProfile',
    'VMGalleryApplication',
    'VMScaleSetConvertToSinglePlacementGroupInput',
    'VMSizeProperties',
    'VaultCertificate',
    'VaultSecretGroup',
    'VirtualHardDisk',
    'VirtualMachine',
    'VirtualMachineAgentInstanceView',
    'VirtualMachineAssessPatchesResult',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'VirtualMachineExtension',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineExtensionImage',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtensionUpdate',
    'VirtualMachineExtensionsListResult',
    'VirtualMachineHealthStatus',
    'VirtualMachineIdentity',
    'VirtualMachineImage',
    'VirtualMachineImageFeature',
    'VirtualMachineImageResource',
    'VirtualMachineInstallPatchesParameters',
    'VirtualMachineInstallPatchesResult',
    'VirtualMachineInstanceView',
    'VirtualMachineIpTag',
    'VirtualMachineListResult',
    'VirtualMachineNetworkInterfaceConfiguration',
    'VirtualMachineNetworkInterfaceDnsSettingsConfiguration',
    'VirtualMachineNetworkInterfaceIPConfiguration',
    'VirtualMachinePatchStatus',
    'VirtualMachinePublicIPAddressConfiguration',
    'VirtualMachinePublicIPAddressDnsSettingsConfiguration',
    'VirtualMachineReimageParameters',
    'VirtualMachineRunCommand',
    'VirtualMachineRunCommandInstanceView',
    'VirtualMachineRunCommandScriptSource',
    'VirtualMachineRunCommandUpdate',
    'VirtualMachineRunCommandsListResult',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionListResult',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetExtensionUpdate',
    'VirtualMachineScaleSetHardwareProfile',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetIpTag',
    'VirtualMachineScaleSetListOSUpgradeHistory',
    'VirtualMachineScaleSetListResult',
    'VirtualMachineScaleSetListSkusResult',
    'VirtualMachineScaleSetListWithLinkResult',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetNetworkConfigurationDnsSettings',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetPublicIPAddressConfiguration',
    'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings',
    'VirtualMachineScaleSetReimageParameters',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetUpdate',
    'VirtualMachineScaleSetUpdateIPConfiguration',
    'VirtualMachineScaleSetUpdateNetworkConfiguration',
    'VirtualMachineScaleSetUpdateNetworkProfile',
    'VirtualMachineScaleSetUpdateOSDisk',
    'VirtualMachineScaleSetUpdateOSProfile',
    'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration',
    'VirtualMachineScaleSetUpdateStorageProfile',
    'VirtualMachineScaleSetUpdateVMProfile',
    'VirtualMachineScaleSetVM',
    'VirtualMachineScaleSetVMExtension',
    'VirtualMachineScaleSetVMExtensionUpdate',
    'VirtualMachineScaleSetVMExtensionsListResult',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineScaleSetVMInstanceView',
    'VirtualMachineScaleSetVMListResult',
    'VirtualMachineScaleSetVMNetworkProfileConfiguration',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineScaleSetVMProtectionPolicy',
    'VirtualMachineScaleSetVMReimageParameters',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineSoftwarePatchProperties',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineUpdate',
    'WinRMConfiguration',
    'WinRMListener',
    'WindowsConfiguration',
    'WindowsParameters',
    'ArchitectureTypes',
    'AvailabilitySetSkuTypes',
    'CachingTypes',
    'CapacityReservationGroupInstanceViewTypes',
    'CapacityReservationInstanceViewTypes',
    'ConsistencyModeTypes',
    'DedicatedHostLicenseTypes',
    'DeleteOptions',
    'DiffDiskOptions',
    'DiffDiskPlacement',
    'DiskCreateOptionTypes',
    'DiskDeleteOptionTypes',
    'DiskDetachOptionTypes',
    'ExecutionState',
    'ExpandTypesForGetCapacityReservationGroups',
    'ExpandTypesForGetVMScaleSets',
    'ExtendedLocationTypes',
    'HyperVGenerationType',
    'HyperVGenerationTypes',
    'IPVersion',
    'IPVersions',
    'InstanceViewTypes',
    'IntervalInMins',
    'LinuxPatchAssessmentMode',
    'LinuxVMGuestPatchMode',
    'MaintenanceOperationResultCodeTypes',
    'NetworkApiVersion',
    'OperatingSystemStateTypes',
    'OperatingSystemType',
    'OperatingSystemTypes',
    'OrchestrationMode',
    'OrchestrationServiceNames',
    'OrchestrationServiceState',
    'OrchestrationServiceStateAction',
    'PatchAssessmentState',
    'PatchInstallationState',
    'PatchOperationStatus',
    'ProtocolTypes',
    'ProximityPlacementGroupType',
    'PublicIPAddressSkuName',
    'PublicIPAddressSkuTier',
    'PublicIPAllocationMethod',
    'RepairAction',
    'ResourceIdentityType',
    'RestorePointCollectionExpandOptions',
    'RestorePointExpandOptions',
    'RollingUpgradeActionType',
    'RollingUpgradeStatusCode',
    'SecurityEncryptionTypes',
    'SecurityTypes',
    'SettingNames',
    'StatusLevelTypes',
    'StorageAccountTypes',
    'UpgradeMode',
    'UpgradeOperationInvoker',
    'UpgradeState',
    'VMGuestPatchClassificationLinux',
    'VMGuestPatchClassificationWindows',
    'VMGuestPatchRebootBehavior',
    'VMGuestPatchRebootSetting',
    'VMGuestPatchRebootStatus',
    'VirtualMachineEvictionPolicyTypes',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetScaleInRules',
    'VirtualMachineScaleSetSkuScaleType',
    'VirtualMachineSizeTypes',
    'VmDiskTypes',
    'WindowsPatchAssessmentMode',
    'WindowsVMGuestPatchMode',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()