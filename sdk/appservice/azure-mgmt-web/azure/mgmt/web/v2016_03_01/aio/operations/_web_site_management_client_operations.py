# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._web_site_management_client_operations import build_check_name_availability_request, build_get_publishing_user_request, build_get_source_control_request, build_get_subscription_deployment_locations_request, build_list_geo_regions_request, build_list_premier_add_on_offers_request, build_list_site_identifiers_assigned_to_host_name_request, build_list_skus_request, build_list_source_controls_request, build_move_request, build_update_publishing_user_request, build_update_source_control_request, build_validate_move_request, build_validate_request, build_verify_hosting_environment_vnet_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WebSiteManagementClientOperationsMixin:

    @distributed_trace_async
    async def get_publishing_user(
        self,
        **kwargs: Any
    ) -> "_models.User":
        """Gets publishing user.

        Gets publishing user.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: User, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.User
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.User"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_publishing_user_request(
            template_url=self.get_publishing_user.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('User', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_publishing_user.metadata = {'url': '/providers/Microsoft.Web/publishingUsers/web'}  # type: ignore


    @distributed_trace_async
    async def update_publishing_user(
        self,
        user_details: "_models.User",
        **kwargs: Any
    ) -> "_models.User":
        """Updates publishing user.

        Updates publishing user.

        :param user_details: Details of publishing user.
        :type user_details: ~azure.mgmt.web.v2016_03_01.models.User
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: User, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.User
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.User"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(user_details, 'User')

        request = build_update_publishing_user_request(
            content_type=content_type,
            json=_json,
            template_url=self.update_publishing_user.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('User', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_publishing_user.metadata = {'url': '/providers/Microsoft.Web/publishingUsers/web'}  # type: ignore


    @distributed_trace
    def list_source_controls(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.SourceControlCollection"]:
        """Gets the source controls available for Azure websites.

        Gets the source controls available for Azure websites.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SourceControlCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2016_03_01.models.SourceControlCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SourceControlCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_source_controls_request(
                    template_url=self.list_source_controls.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_source_controls_request(
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SourceControlCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_source_controls.metadata = {'url': '/providers/Microsoft.Web/sourcecontrols'}  # type: ignore

    @distributed_trace_async
    async def get_source_control(
        self,
        source_control_type: str,
        **kwargs: Any
    ) -> "_models.SourceControl":
        """Gets source control token.

        Gets source control token.

        :param source_control_type: Type of source control.
        :type source_control_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControl, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.SourceControl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SourceControl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_source_control_request(
            source_control_type=source_control_type,
            template_url=self.get_source_control.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SourceControl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_source_control.metadata = {'url': '/providers/Microsoft.Web/sourcecontrols/{sourceControlType}'}  # type: ignore


    @distributed_trace_async
    async def update_source_control(
        self,
        source_control_type: str,
        request_message: "_models.SourceControl",
        **kwargs: Any
    ) -> "_models.SourceControl":
        """Updates source control token.

        Updates source control token.

        :param source_control_type: Type of source control.
        :type source_control_type: str
        :param request_message: Source control token information.
        :type request_message: ~azure.mgmt.web.v2016_03_01.models.SourceControl
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControl, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.SourceControl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SourceControl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(request_message, 'SourceControl')

        request = build_update_source_control_request(
            source_control_type=source_control_type,
            content_type=content_type,
            json=_json,
            template_url=self.update_source_control.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SourceControl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_source_control.metadata = {'url': '/providers/Microsoft.Web/sourcecontrols/{sourceControlType}'}  # type: ignore


    @distributed_trace_async
    async def check_name_availability(
        self,
        name: str,
        type: Union[str, "_models.CheckNameResourceTypes"],
        is_fqdn: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.ResourceNameAvailability":
        """Check if a resource name is available.

        Check if a resource name is available.

        :param name: Resource name to verify.
        :type name: str
        :param type: Resource type used for verification.
        :type type: str or ~azure.mgmt.web.v2016_03_01.models.CheckNameResourceTypes
        :param is_fqdn: Is fully qualified domain name.
        :type is_fqdn: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceNameAvailability, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.ResourceNameAvailability
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceNameAvailability"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _request = _models.ResourceNameAvailabilityRequest(name=name, type=type, is_fqdn=is_fqdn)
        _json = self._serialize.body(_request, 'ResourceNameAvailabilityRequest')

        request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.check_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ResourceNameAvailability', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/checknameavailability'}  # type: ignore


    @distributed_trace_async
    async def get_subscription_deployment_locations(
        self,
        **kwargs: Any
    ) -> "_models.DeploymentLocations":
        """Gets list of available geo regions plus ministamps.

        Gets list of available geo regions plus ministamps.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentLocations, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.DeploymentLocations
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentLocations"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_subscription_deployment_locations_request(
            subscription_id=self._config.subscription_id,
            template_url=self.get_subscription_deployment_locations.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentLocations', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_subscription_deployment_locations.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/deploymentLocations'}  # type: ignore


    @distributed_trace
    def list_geo_regions(
        self,
        sku: Optional[Union[str, "_models.SkuName"]] = None,
        linux_workers_enabled: Optional[bool] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.GeoRegionCollection"]:
        """Get a list of available geographical regions.

        Get a list of available geographical regions.

        :param sku: Name of SKU used to filter the regions.
        :type sku: str or ~azure.mgmt.web.v2016_03_01.models.SkuName
        :param linux_workers_enabled: Specify :code:`<code>true</code>` if you want to filter to only
         regions that support Linux workers.
        :type linux_workers_enabled: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GeoRegionCollection or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2016_03_01.models.GeoRegionCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GeoRegionCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_geo_regions_request(
                    subscription_id=self._config.subscription_id,
                    sku=sku,
                    linux_workers_enabled=linux_workers_enabled,
                    template_url=self.list_geo_regions.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_geo_regions_request(
                    subscription_id=self._config.subscription_id,
                    sku=sku,
                    linux_workers_enabled=linux_workers_enabled,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("GeoRegionCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_geo_regions.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/geoRegions'}  # type: ignore

    @distributed_trace
    def list_site_identifiers_assigned_to_host_name(
        self,
        name_identifier: "_models.NameIdentifier",
        **kwargs: Any
    ) -> AsyncIterable["_models.IdentifierCollection"]:
        """List all apps that are assigned to a hostname.

        List all apps that are assigned to a hostname.

        :param name_identifier: Hostname information.
        :type name_identifier: ~azure.mgmt.web.v2016_03_01.models.NameIdentifier
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either IdentifierCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2016_03_01.models.IdentifierCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.IdentifierCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _json = self._serialize.body(name_identifier, 'NameIdentifier')
                
                request = build_list_site_identifiers_assigned_to_host_name_request(
                    subscription_id=self._config.subscription_id,
                    content_type=content_type,
                    json=_json,
                    template_url=self.list_site_identifiers_assigned_to_host_name.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _json = self._serialize.body(name_identifier, 'NameIdentifier')
                
                request = build_list_site_identifiers_assigned_to_host_name_request(
                    subscription_id=self._config.subscription_id,
                    content_type=content_type,
                    json=_json,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("IdentifierCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_site_identifiers_assigned_to_host_name.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/listSitesAssignedToHostName'}  # type: ignore

    @distributed_trace
    def list_premier_add_on_offers(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.PremierAddOnOfferCollection"]:
        """List all premier add-on offers.

        List all premier add-on offers.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PremierAddOnOfferCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2016_03_01.models.PremierAddOnOfferCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PremierAddOnOfferCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_premier_add_on_offers_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_premier_add_on_offers.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_premier_add_on_offers_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PremierAddOnOfferCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_premier_add_on_offers.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/premieraddonoffers'}  # type: ignore

    @distributed_trace_async
    async def list_skus(
        self,
        **kwargs: Any
    ) -> "_models.SkuInfos":
        """List all SKUs.

        List all SKUs.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SkuInfos, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.SkuInfos
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SkuInfos"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_skus_request(
            subscription_id=self._config.subscription_id,
            template_url=self.list_skus.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SkuInfos', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_skus.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/skus'}  # type: ignore


    @distributed_trace_async
    async def verify_hosting_environment_vnet(
        self,
        parameters: "_models.VnetParameters",
        **kwargs: Any
    ) -> "_models.VnetValidationFailureDetails":
        """Verifies if this VNET is compatible with an App Service Environment by analyzing the Network
        Security Group rules.

        Verifies if this VNET is compatible with an App Service Environment by analyzing the Network
        Security Group rules.

        :param parameters: VNET information.
        :type parameters: ~azure.mgmt.web.v2016_03_01.models.VnetParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VnetValidationFailureDetails, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.VnetValidationFailureDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VnetValidationFailureDetails"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'VnetParameters')

        request = build_verify_hosting_environment_vnet_request(
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.verify_hosting_environment_vnet.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VnetValidationFailureDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    verify_hosting_environment_vnet.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/verifyHostingEnvironmentVnet'}  # type: ignore


    @distributed_trace_async
    async def move(
        self,
        resource_group_name: str,
        move_resource_envelope: "_models.CsmMoveResourceEnvelope",
        **kwargs: Any
    ) -> None:
        """Move resources between resource groups.

        Move resources between resource groups.

        :param resource_group_name: Name of the resource group to which the resource belongs.
        :type resource_group_name: str
        :param move_resource_envelope: Object that represents the resource to move.
        :type move_resource_envelope: ~azure.mgmt.web.v2016_03_01.models.CsmMoveResourceEnvelope
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(move_resource_envelope, 'CsmMoveResourceEnvelope')

        request = build_move_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.move.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    move.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources'}  # type: ignore


    @distributed_trace_async
    async def validate(
        self,
        resource_group_name: str,
        validate_request: "_models.ValidateRequest",
        **kwargs: Any
    ) -> "_models.ValidateResponse":
        """Validate if a resource can be created.

        Validate if a resource can be created.

        :param resource_group_name: Name of the resource group to which the resource belongs.
        :type resource_group_name: str
        :param validate_request: Request with the resources to validate.
        :type validate_request: ~azure.mgmt.web.v2016_03_01.models.ValidateRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidateResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2016_03_01.models.ValidateResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ValidateResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(validate_request, 'ValidateRequest')

        request = build_validate_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.validate.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ValidateResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validate.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/validate'}  # type: ignore


    @distributed_trace_async
    async def validate_move(
        self,
        resource_group_name: str,
        move_resource_envelope: "_models.CsmMoveResourceEnvelope",
        **kwargs: Any
    ) -> None:
        """Validate whether a resource can be moved.

        Validate whether a resource can be moved.

        :param resource_group_name: Name of the resource group to which the resource belongs.
        :type resource_group_name: str
        :param move_resource_envelope: Object that represents the resource to move.
        :type move_resource_envelope: ~azure.mgmt.web.v2016_03_01.models.CsmMoveResourceEnvelope
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(move_resource_envelope, 'CsmMoveResourceEnvelope')

        request = build_validate_move_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.validate_move.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    validate_move.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/validateMoveResources'}  # type: ignore

