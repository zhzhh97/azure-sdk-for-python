# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._source_control_configuration_client_enums import *


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
        """
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ProxyResource, self).__init__(**kwargs)


class Extension(ProxyResource):
    """The Extension object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar identity: Identity of the Extension resource.
    :vartype identity: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Identity
    :ivar system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :vartype system_data: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.SystemData
    :ivar extension_type: Type of the Extension, of which this resource is an instance of.  It must
     be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the
     Extension publisher.
    :vartype extension_type: str
    :ivar auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade
     of minor version, or not.
    :vartype auto_upgrade_minor_version: bool
    :ivar release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable,
     Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :vartype release_train: str
    :ivar version: Version of the extension for this extension, if it is 'pinned' to a specific
     version. autoUpgradeMinorVersion must be 'false'.
    :vartype version: str
    :ivar scope: Scope at which the extension is installed.
    :vartype scope: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Scope
    :ivar configuration_settings: Configuration settings, as name-value pairs for configuring this
     extension.
    :vartype configuration_settings: dict[str, str]
    :ivar configuration_protected_settings: Configuration settings that are sensitive, as
     name-value pairs for configuring this extension.
    :vartype configuration_protected_settings: dict[str, str]
    :ivar provisioning_state: The provisioning state of the extension resource. Possible values
     include: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ProvisioningState
    :ivar statuses: Status from this extension.
    :vartype statuses: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionStatus]
    :ivar error_info: The error detail.
    :vartype error_info: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    :ivar custom_location_settings: Custom Location settings properties.
    :vartype custom_location_settings: dict[str, str]
    :ivar package_uri: Uri of the Helm package.
    :vartype package_uri: str
    :ivar aks_assigned_identity: Identity of the Extension resource in an AKS cluster.
    :vartype aks_assigned_identity:
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionPropertiesAksAssignedIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'custom_location_settings': {'readonly': True},
        'package_uri': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'statuses': {'key': 'properties.statuses', 'type': '[ExtensionStatus]'},
        'error_info': {'key': 'properties.errorInfo', 'type': 'ErrorDetail'},
        'custom_location_settings': {'key': 'properties.customLocationSettings', 'type': '{str}'},
        'package_uri': {'key': 'properties.packageUri', 'type': 'str'},
        'aks_assigned_identity': {'key': 'properties.aksAssignedIdentity', 'type': 'ExtensionPropertiesAksAssignedIdentity'},
    }

    def __init__(
        self,
        *,
        identity: Optional["Identity"] = None,
        extension_type: Optional[str] = None,
        auto_upgrade_minor_version: Optional[bool] = True,
        release_train: Optional[str] = "Stable",
        version: Optional[str] = None,
        scope: Optional["Scope"] = None,
        configuration_settings: Optional[Dict[str, str]] = None,
        configuration_protected_settings: Optional[Dict[str, str]] = None,
        statuses: Optional[List["ExtensionStatus"]] = None,
        error_info: Optional["ErrorDetail"] = None,
        aks_assigned_identity: Optional["ExtensionPropertiesAksAssignedIdentity"] = None,
        **kwargs
    ):
        """
        :keyword identity: Identity of the Extension resource.
        :paramtype identity: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Identity
        :keyword extension_type: Type of the Extension, of which this resource is an instance of.  It
         must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the
         Extension publisher.
        :paramtype extension_type: str
        :keyword auto_upgrade_minor_version: Flag to note if this extension participates in auto
         upgrade of minor version, or not.
        :paramtype auto_upgrade_minor_version: bool
        :keyword release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g.
         Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        :paramtype release_train: str
        :keyword version: Version of the extension for this extension, if it is 'pinned' to a specific
         version. autoUpgradeMinorVersion must be 'false'.
        :paramtype version: str
        :keyword scope: Scope at which the extension is installed.
        :paramtype scope: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Scope
        :keyword configuration_settings: Configuration settings, as name-value pairs for configuring
         this extension.
        :paramtype configuration_settings: dict[str, str]
        :keyword configuration_protected_settings: Configuration settings that are sensitive, as
         name-value pairs for configuring this extension.
        :paramtype configuration_protected_settings: dict[str, str]
        :keyword statuses: Status from this extension.
        :paramtype statuses:
         list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionStatus]
        :keyword error_info: The error detail.
        :paramtype error_info: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
        :keyword aks_assigned_identity: Identity of the Extension resource in an AKS cluster.
        :paramtype aks_assigned_identity:
         ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionPropertiesAksAssignedIdentity
        """
        super(Extension, self).__init__(**kwargs)
        self.identity = identity
        self.system_data = None
        self.extension_type = extension_type
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version
        self.scope = scope
        self.configuration_settings = configuration_settings
        self.configuration_protected_settings = configuration_protected_settings
        self.provisioning_state = None
        self.statuses = statuses
        self.error_info = error_info
        self.custom_location_settings = None
        self.package_uri = None
        self.aks_assigned_identity = aks_assigned_identity


class ExtensionPropertiesAksAssignedIdentity(msrest.serialization.Model):
    """Identity of the Extension resource in an AKS cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :ivar type: The identity type. The only acceptable values to pass in are None and
     "SystemAssigned". The default value is None.
    :vartype type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword type: The identity type. The only acceptable values to pass in are None and
         "SystemAssigned". The default value is None.
        :paramtype type: str
        """
        super(ExtensionPropertiesAksAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class ExtensionsList(msrest.serialization.Model):
    """Result of the request to list Extensions.  It contains a list of Extension objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Extensions within a Kubernetes cluster.
    :vartype value: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Extension]
    :ivar next_link: URL to get the next set of extension objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Extension]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ExtensionsList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class ExtensionStatus(msrest.serialization.Model):
    """Status from the extension.

    :ivar code: Status code provided by the Extension.
    :vartype code: str
    :ivar display_status: Short description of status of the extension.
    :vartype display_status: str
    :ivar level: Level of the status. Possible values include: "Error", "Warning", "Information".
     Default value: "Information".
    :vartype level: str or ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.LevelType
    :ivar message: Detailed message of the status from the Extension.
    :vartype message: str
    :ivar time: DateLiteral (per ISO8601) noting the time of installation status.
    :vartype time: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        display_status: Optional[str] = None,
        level: Optional[Union[str, "LevelType"]] = "Information",
        message: Optional[str] = None,
        time: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword code: Status code provided by the Extension.
        :paramtype code: str
        :keyword display_status: Short description of status of the extension.
        :paramtype display_status: str
        :keyword level: Level of the status. Possible values include: "Error", "Warning",
         "Information". Default value: "Information".
        :paramtype level: str or ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.LevelType
        :keyword message: Detailed message of the status from the Extension.
        :paramtype message: str
        :keyword time: DateLiteral (per ISO8601) noting the time of installation status.
        :paramtype time: str
        """
        super(ExtensionStatus, self).__init__(**kwargs)
        self.code = code
        self.display_status = display_status
        self.level = level
        self.message = message
        self.time = time


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :ivar type: The identity type. The only acceptable values to pass in are None and
     "SystemAssigned". The default value is None.
    :vartype type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword type: The identity type. The only acceptable values to pass in are None and
         "SystemAssigned". The default value is None.
        :paramtype type: str
        """
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class OperationStatusList(msrest.serialization.Model):
    """The async operations in progress, in the cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of async operations in progress, in the cluster.
    :vartype value:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.OperationStatusResult]
    :ivar next_link: URL to get the next set of Operation Result objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationStatusResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(OperationStatusList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class OperationStatusResult(msrest.serialization.Model):
    """The current status of an async operation.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified ID for the async operation.
    :vartype id: str
    :ivar name: Name of the async operation.
    :vartype name: str
    :ivar status: Required. Operation status.
    :vartype status: str
    :ivar properties: Additional information, if available.
    :vartype properties: dict[str, str]
    :ivar error: The error detail.
    :vartype error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    """

    _validation = {
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        status: str,
        id: Optional[str] = None,
        name: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        """
        :keyword id: Fully qualified ID for the async operation.
        :paramtype id: str
        :keyword name: Name of the async operation.
        :paramtype name: str
        :keyword status: Required. Operation status.
        :paramtype status: str
        :keyword properties: Additional information, if available.
        :paramtype properties: dict[str, str]
        :keyword error: The error detail.
        :paramtype error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
        """
        super(OperationStatusResult, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.status = status
        self.properties = properties
        self.error = error


class PatchExtension(msrest.serialization.Model):
    """The Extension Patch Request object.

    :ivar auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade
     of minor version, or not.
    :vartype auto_upgrade_minor_version: bool
    :ivar release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable,
     Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :vartype release_train: str
    :ivar version: Version of the extension for this extension, if it is 'pinned' to a specific
     version. autoUpgradeMinorVersion must be 'false'.
    :vartype version: str
    :ivar configuration_settings: Configuration settings, as name-value pairs for configuring this
     extension.
    :vartype configuration_settings: dict[str, str]
    :ivar configuration_protected_settings: Configuration settings that are sensitive, as
     name-value pairs for configuring this extension.
    :vartype configuration_protected_settings: dict[str, str]
    """

    _attribute_map = {
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        auto_upgrade_minor_version: Optional[bool] = True,
        release_train: Optional[str] = "Stable",
        version: Optional[str] = None,
        configuration_settings: Optional[Dict[str, str]] = None,
        configuration_protected_settings: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword auto_upgrade_minor_version: Flag to note if this extension participates in auto
         upgrade of minor version, or not.
        :paramtype auto_upgrade_minor_version: bool
        :keyword release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g.
         Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        :paramtype release_train: str
        :keyword version: Version of the extension for this extension, if it is 'pinned' to a specific
         version. autoUpgradeMinorVersion must be 'false'.
        :paramtype version: str
        :keyword configuration_settings: Configuration settings, as name-value pairs for configuring
         this extension.
        :paramtype configuration_settings: dict[str, str]
        :keyword configuration_protected_settings: Configuration settings that are sensitive, as
         name-value pairs for configuring this extension.
        :paramtype configuration_protected_settings: dict[str, str]
        """
        super(PatchExtension, self).__init__(**kwargs)
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version
        self.configuration_settings = configuration_settings
        self.configuration_protected_settings = configuration_protected_settings


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operation of this resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name, in format of {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: Display metadata associated with the operation.
    :vartype display:
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperationDisplay
    :ivar is_data_action: The flag that indicates whether the operation applies to data plane.
    :vartype is_data_action: bool
    :ivar origin: Origin of the operation.
    :vartype origin: str
    """

    _validation = {
        'is_data_action': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["ResourceProviderOperationDisplay"] = None,
        **kwargs
    ):
        """
        :keyword name: Operation name, in format of {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: Display metadata associated with the operation.
        :paramtype display:
         ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperationDisplay
        """
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.is_data_action = None
        self.origin = None


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :ivar provider: Resource provider: Microsoft KubernetesConfiguration.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed.
    :vartype resource: str
    :ivar operation: Type of operation: get, read, delete, etc.
    :vartype operation: str
    :ivar description: Description of this operation.
    :vartype description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword provider: Resource provider: Microsoft KubernetesConfiguration.
        :paramtype provider: str
        :keyword resource: Resource on which the operation is performed.
        :paramtype resource: str
        :keyword operation: Type of operation: get, read, delete, etc.
        :paramtype operation: str
        :keyword description: Description of this operation.
        :paramtype description: str
        """
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ResourceProviderOperationList(msrest.serialization.Model):
    """Result of the request to list operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by this resource provider.
    :vartype value:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperation]
    :ivar next_link: URL to the next set of results, if any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceProviderOperation"]] = None,
        **kwargs
    ):
        """
        :keyword value: List of operations supported by this resource provider.
        :paramtype value:
         list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperation]
        """
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class Scope(msrest.serialization.Model):
    """Scope of the extension. It can be either Cluster or Namespace; but not both.

    :ivar cluster: Specifies that the scope of the extension is Cluster.
    :vartype cluster: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeCluster
    :ivar namespace: Specifies that the scope of the extension is Namespace.
    :vartype namespace: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeNamespace
    """

    _attribute_map = {
        'cluster': {'key': 'cluster', 'type': 'ScopeCluster'},
        'namespace': {'key': 'namespace', 'type': 'ScopeNamespace'},
    }

    def __init__(
        self,
        *,
        cluster: Optional["ScopeCluster"] = None,
        namespace: Optional["ScopeNamespace"] = None,
        **kwargs
    ):
        """
        :keyword cluster: Specifies that the scope of the extension is Cluster.
        :paramtype cluster: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeCluster
        :keyword namespace: Specifies that the scope of the extension is Namespace.
        :paramtype namespace: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeNamespace
        """
        super(Scope, self).__init__(**kwargs)
        self.cluster = cluster
        self.namespace = namespace


class ScopeCluster(msrest.serialization.Model):
    """Specifies that the scope of the extension is Cluster.

    :ivar release_namespace: Namespace where the extension Release must be placed, for a Cluster
     scoped extension.  If this namespace does not exist, it will be created.
    :vartype release_namespace: str
    """

    _attribute_map = {
        'release_namespace': {'key': 'releaseNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        release_namespace: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword release_namespace: Namespace where the extension Release must be placed, for a Cluster
         scoped extension.  If this namespace does not exist, it will be created.
        :paramtype release_namespace: str
        """
        super(ScopeCluster, self).__init__(**kwargs)
        self.release_namespace = release_namespace


class ScopeNamespace(msrest.serialization.Model):
    """Specifies that the scope of the extension is Namespace.

    :ivar target_namespace: Namespace where the extension will be created for an Namespace scoped
     extension.  If this namespace does not exist, it will be created.
    :vartype target_namespace: str
    """

    _attribute_map = {
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        target_namespace: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword target_namespace: Namespace where the extension will be created for an Namespace
         scoped extension.  If this namespace does not exist, it will be created.
        :paramtype target_namespace: str
        """
        super(ScopeNamespace, self).__init__(**kwargs)
        self.target_namespace = target_namespace


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Possible values include:
     "User", "Application", "ManagedIdentity", "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Possible values
         include: "User", "Application", "ManagedIdentity", "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Possible
         values include: "User", "Application", "ManagedIdentity", "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
