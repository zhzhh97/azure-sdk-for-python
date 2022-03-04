# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Alias
from ._models_py3 import AliasPath
from ._models_py3 import AliasPathMetadata
from ._models_py3 import AliasPattern
from ._models_py3 import ApiProfile
from ._models_py3 import BasicDependency
from ._models_py3 import DebugSetting
from ._models_py3 import Dependency
from ._models_py3 import Deployment
from ._models_py3 import DeploymentExportResult
from ._models_py3 import DeploymentExtended
from ._models_py3 import DeploymentExtendedFilter
from ._models_py3 import DeploymentListResult
from ._models_py3 import DeploymentOperation
from ._models_py3 import DeploymentOperationProperties
from ._models_py3 import DeploymentOperationsListResult
from ._models_py3 import DeploymentProperties
from ._models_py3 import DeploymentPropertiesExtended
from ._models_py3 import DeploymentValidateResult
from ._models_py3 import DeploymentWhatIf
from ._models_py3 import DeploymentWhatIfProperties
from ._models_py3 import DeploymentWhatIfSettings
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorResponse
from ._models_py3 import ExportTemplateRequest
from ._models_py3 import ExpressionEvaluationOptions
from ._models_py3 import ExtendedLocation
from ._models_py3 import GenericResource
from ._models_py3 import GenericResourceExpanded
from ._models_py3 import GenericResourceFilter
from ._models_py3 import HttpMessage
from ._models_py3 import Identity
from ._models_py3 import IdentityUserAssignedIdentitiesValue
from ._models_py3 import OnErrorDeployment
from ._models_py3 import OnErrorDeploymentExtended
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ParametersLink
from ._models_py3 import Plan
from ._models_py3 import Provider
from ._models_py3 import ProviderExtendedLocation
from ._models_py3 import ProviderListResult
from ._models_py3 import ProviderResourceType
from ._models_py3 import ProviderResourceTypeListResult
from ._models_py3 import Resource
from ._models_py3 import ResourceGroup
from ._models_py3 import ResourceGroupExportResult
from ._models_py3 import ResourceGroupFilter
from ._models_py3 import ResourceGroupListResult
from ._models_py3 import ResourceGroupPatchable
from ._models_py3 import ResourceGroupProperties
from ._models_py3 import ResourceListResult
from ._models_py3 import ResourceProviderOperationDisplayProperties
from ._models_py3 import ResourceReference
from ._models_py3 import ResourcesMoveInfo
from ._models_py3 import ScopedDeployment
from ._models_py3 import ScopedDeploymentWhatIf
from ._models_py3 import Sku
from ._models_py3 import StatusMessage
from ._models_py3 import SubResource
from ._models_py3 import TagCount
from ._models_py3 import TagDetails
from ._models_py3 import TagValue
from ._models_py3 import Tags
from ._models_py3 import TagsListResult
from ._models_py3 import TagsPatchResource
from ._models_py3 import TagsResource
from ._models_py3 import TargetResource
from ._models_py3 import TemplateHashResult
from ._models_py3 import TemplateLink
from ._models_py3 import WhatIfChange
from ._models_py3 import WhatIfOperationResult
from ._models_py3 import WhatIfPropertyChange
from ._models_py3 import ZoneMapping


from ._resource_management_client_enums import (
    AliasPathAttributes,
    AliasPathTokenType,
    AliasPatternType,
    AliasType,
    ChangeType,
    DeploymentMode,
    ExpressionEvaluationOptionsScopeType,
    ExtendedLocationType,
    OnErrorDeploymentType,
    PropertyChangeType,
    ProvisioningOperation,
    ProvisioningState,
    ResourceIdentityType,
    TagsPatchOperation,
    WhatIfResultFormat,
)

__all__ = [
    'Alias',
    'AliasPath',
    'AliasPathMetadata',
    'AliasPattern',
    'ApiProfile',
    'BasicDependency',
    'DebugSetting',
    'Dependency',
    'Deployment',
    'DeploymentExportResult',
    'DeploymentExtended',
    'DeploymentExtendedFilter',
    'DeploymentListResult',
    'DeploymentOperation',
    'DeploymentOperationProperties',
    'DeploymentOperationsListResult',
    'DeploymentProperties',
    'DeploymentPropertiesExtended',
    'DeploymentValidateResult',
    'DeploymentWhatIf',
    'DeploymentWhatIfProperties',
    'DeploymentWhatIfSettings',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ExportTemplateRequest',
    'ExpressionEvaluationOptions',
    'ExtendedLocation',
    'GenericResource',
    'GenericResourceExpanded',
    'GenericResourceFilter',
    'HttpMessage',
    'Identity',
    'IdentityUserAssignedIdentitiesValue',
    'OnErrorDeployment',
    'OnErrorDeploymentExtended',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'ParametersLink',
    'Plan',
    'Provider',
    'ProviderExtendedLocation',
    'ProviderListResult',
    'ProviderResourceType',
    'ProviderResourceTypeListResult',
    'Resource',
    'ResourceGroup',
    'ResourceGroupExportResult',
    'ResourceGroupFilter',
    'ResourceGroupListResult',
    'ResourceGroupPatchable',
    'ResourceGroupProperties',
    'ResourceListResult',
    'ResourceProviderOperationDisplayProperties',
    'ResourceReference',
    'ResourcesMoveInfo',
    'ScopedDeployment',
    'ScopedDeploymentWhatIf',
    'Sku',
    'StatusMessage',
    'SubResource',
    'TagCount',
    'TagDetails',
    'TagValue',
    'Tags',
    'TagsListResult',
    'TagsPatchResource',
    'TagsResource',
    'TargetResource',
    'TemplateHashResult',
    'TemplateLink',
    'WhatIfChange',
    'WhatIfOperationResult',
    'WhatIfPropertyChange',
    'ZoneMapping',
    'AliasPathAttributes',
    'AliasPathTokenType',
    'AliasPatternType',
    'AliasType',
    'ChangeType',
    'DeploymentMode',
    'ExpressionEvaluationOptionsScopeType',
    'ExtendedLocationType',
    'OnErrorDeploymentType',
    'PropertyChangeType',
    'ProvisioningOperation',
    'ProvisioningState',
    'ResourceIdentityType',
    'TagsPatchOperation',
    'WhatIfResultFormat',
]
