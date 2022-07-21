# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AgentPool
from ._models_py3 import AgentPoolAvailableVersions
from ._models_py3 import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
from ._models_py3 import AgentPoolListResult
from ._models_py3 import AgentPoolUpgradeProfile
from ._models_py3 import AgentPoolUpgradeProfilePropertiesUpgradesItem
from ._models_py3 import AgentPoolUpgradeSettings
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerServiceDiagnosticsProfile
from ._models_py3 import ContainerServiceLinuxProfile
from ._models_py3 import ContainerServiceMasterProfile
from ._models_py3 import ContainerServiceNetworkProfile
from ._models_py3 import ContainerServiceSshConfiguration
from ._models_py3 import ContainerServiceSshPublicKey
from ._models_py3 import ContainerServiceVMDiagnostics
from ._models_py3 import CreationData
from ._models_py3 import CredentialResult
from ._models_py3 import CredentialResults
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import ExtendedLocation
from ._models_py3 import KubeletConfig
from ._models_py3 import LinuxOSConfig
from ._models_py3 import MaintenanceConfiguration
from ._models_py3 import MaintenanceConfigurationListResult
from ._models_py3 import ManagedCluster
from ._models_py3 import ManagedClusterAADProfile
from ._models_py3 import ManagedClusterAPIServerAccessProfile
from ._models_py3 import ManagedClusterAccessProfile
from ._models_py3 import ManagedClusterAddonProfile
from ._models_py3 import ManagedClusterAddonProfileIdentity
from ._models_py3 import ManagedClusterAgentPoolProfile
from ._models_py3 import ManagedClusterAgentPoolProfileProperties
from ._models_py3 import ManagedClusterAutoUpgradeProfile
from ._models_py3 import ManagedClusterHTTPProxyConfig
from ._models_py3 import ManagedClusterIdentity
from ._models_py3 import ManagedClusterListResult
from ._models_py3 import ManagedClusterLoadBalancerProfile
from ._models_py3 import ManagedClusterLoadBalancerProfileManagedOutboundIPs
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPPrefixes
from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPs
from ._models_py3 import ManagedClusterManagedOutboundIPProfile
from ._models_py3 import ManagedClusterNATGatewayProfile
from ._models_py3 import ManagedClusterOIDCIssuerProfile
from ._models_py3 import ManagedClusterPodIdentity
from ._models_py3 import ManagedClusterPodIdentityException
from ._models_py3 import ManagedClusterPodIdentityProfile
from ._models_py3 import ManagedClusterPodIdentityProvisioningError
from ._models_py3 import ManagedClusterPodIdentityProvisioningErrorBody
from ._models_py3 import ManagedClusterPodIdentityProvisioningInfo
from ._models_py3 import ManagedClusterPoolUpgradeProfile
from ._models_py3 import ManagedClusterPoolUpgradeProfileUpgradesItem
from ._models_py3 import ManagedClusterPropertiesAutoScalerProfile
from ._models_py3 import ManagedClusterSKU
from ._models_py3 import ManagedClusterSecurityProfile
from ._models_py3 import ManagedClusterSecurityProfileAzureDefender
from ._models_py3 import ManagedClusterServicePrincipalProfile
from ._models_py3 import ManagedClusterUpgradeProfile
from ._models_py3 import ManagedClusterWindowsProfile
from ._models_py3 import ManagedServiceIdentityUserAssignedIdentitiesValue
from ._models_py3 import OSOptionProfile
from ._models_py3 import OSOptionProperty
from ._models_py3 import OperationListResult
from ._models_py3 import OperationValue
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import OutboundEnvironmentEndpointCollection
from ._models_py3 import PowerState
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourcesListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceReference
from ._models_py3 import RunCommandRequest
from ._models_py3 import RunCommandResult
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotListResult
from ._models_py3 import SubResource
from ._models_py3 import SysctlConfig
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import TimeInWeek
from ._models_py3 import TimeSpan
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import WindowsGmsaProfile


from ._container_service_client_enums import (
    AgentPoolMode,
    AgentPoolType,
    Code,
    ConnectionStatus,
    ContainerServiceStorageProfileTypes,
    ContainerServiceVMSizeTypes,
    Count,
    CreatedByType,
    Expander,
    ExtendedLocationTypes,
    GPUInstanceProfile,
    IpFamily,
    KubeletDiskType,
    LicenseType,
    LoadBalancerSku,
    ManagedClusterPodIdentityProvisioningState,
    ManagedClusterSKUName,
    ManagedClusterSKUTier,
    NetworkMode,
    NetworkPlugin,
    NetworkPolicy,
    OSDiskType,
    OSSKU,
    OSType,
    OutboundType,
    PrivateEndpointConnectionProvisioningState,
    PublicNetworkAccess,
    ResourceIdentityType,
    ScaleDownMode,
    ScaleSetEvictionPolicy,
    ScaleSetPriority,
    SnapshotType,
    UpgradeChannel,
    WeekDay,
    WorkloadRuntime,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AgentPool',
    'AgentPoolAvailableVersions',
    'AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem',
    'AgentPoolListResult',
    'AgentPoolUpgradeProfile',
    'AgentPoolUpgradeProfilePropertiesUpgradesItem',
    'AgentPoolUpgradeSettings',
    'CloudErrorBody',
    'ContainerServiceDiagnosticsProfile',
    'ContainerServiceLinuxProfile',
    'ContainerServiceMasterProfile',
    'ContainerServiceNetworkProfile',
    'ContainerServiceSshConfiguration',
    'ContainerServiceSshPublicKey',
    'ContainerServiceVMDiagnostics',
    'CreationData',
    'CredentialResult',
    'CredentialResults',
    'EndpointDependency',
    'EndpointDetail',
    'ExtendedLocation',
    'KubeletConfig',
    'LinuxOSConfig',
    'MaintenanceConfiguration',
    'MaintenanceConfigurationListResult',
    'ManagedCluster',
    'ManagedClusterAADProfile',
    'ManagedClusterAPIServerAccessProfile',
    'ManagedClusterAccessProfile',
    'ManagedClusterAddonProfile',
    'ManagedClusterAddonProfileIdentity',
    'ManagedClusterAgentPoolProfile',
    'ManagedClusterAgentPoolProfileProperties',
    'ManagedClusterAutoUpgradeProfile',
    'ManagedClusterHTTPProxyConfig',
    'ManagedClusterIdentity',
    'ManagedClusterListResult',
    'ManagedClusterLoadBalancerProfile',
    'ManagedClusterLoadBalancerProfileManagedOutboundIPs',
    'ManagedClusterLoadBalancerProfileOutboundIPPrefixes',
    'ManagedClusterLoadBalancerProfileOutboundIPs',
    'ManagedClusterManagedOutboundIPProfile',
    'ManagedClusterNATGatewayProfile',
    'ManagedClusterOIDCIssuerProfile',
    'ManagedClusterPodIdentity',
    'ManagedClusterPodIdentityException',
    'ManagedClusterPodIdentityProfile',
    'ManagedClusterPodIdentityProvisioningError',
    'ManagedClusterPodIdentityProvisioningErrorBody',
    'ManagedClusterPodIdentityProvisioningInfo',
    'ManagedClusterPoolUpgradeProfile',
    'ManagedClusterPoolUpgradeProfileUpgradesItem',
    'ManagedClusterPropertiesAutoScalerProfile',
    'ManagedClusterSKU',
    'ManagedClusterSecurityProfile',
    'ManagedClusterSecurityProfileAzureDefender',
    'ManagedClusterServicePrincipalProfile',
    'ManagedClusterUpgradeProfile',
    'ManagedClusterWindowsProfile',
    'ManagedServiceIdentityUserAssignedIdentitiesValue',
    'OSOptionProfile',
    'OSOptionProperty',
    'OperationListResult',
    'OperationValue',
    'OutboundEnvironmentEndpoint',
    'OutboundEnvironmentEndpointCollection',
    'PowerState',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourcesListResult',
    'PrivateLinkServiceConnectionState',
    'Resource',
    'ResourceReference',
    'RunCommandRequest',
    'RunCommandResult',
    'Snapshot',
    'SnapshotListResult',
    'SubResource',
    'SysctlConfig',
    'SystemData',
    'TagsObject',
    'TimeInWeek',
    'TimeSpan',
    'UserAssignedIdentity',
    'WindowsGmsaProfile',
    'AgentPoolMode',
    'AgentPoolType',
    'Code',
    'ConnectionStatus',
    'ContainerServiceStorageProfileTypes',
    'ContainerServiceVMSizeTypes',
    'Count',
    'CreatedByType',
    'Expander',
    'ExtendedLocationTypes',
    'GPUInstanceProfile',
    'IpFamily',
    'KubeletDiskType',
    'LicenseType',
    'LoadBalancerSku',
    'ManagedClusterPodIdentityProvisioningState',
    'ManagedClusterSKUName',
    'ManagedClusterSKUTier',
    'NetworkMode',
    'NetworkPlugin',
    'NetworkPolicy',
    'OSDiskType',
    'OSSKU',
    'OSType',
    'OutboundType',
    'PrivateEndpointConnectionProvisioningState',
    'PublicNetworkAccess',
    'ResourceIdentityType',
    'ScaleDownMode',
    'ScaleSetEvictionPolicy',
    'ScaleSetPriority',
    'SnapshotType',
    'UpgradeChannel',
    'WeekDay',
    'WorkloadRuntime',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()