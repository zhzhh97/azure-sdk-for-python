# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_create_or_update_request(
    resource_group_name: str,
    availability_set_name: str,
    subscription_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("availability_set_name", availability_set_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    resource_group_name: str,
    availability_set_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("availability_set_name", availability_set_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    availability_set_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("availability_set_name", availability_set_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_by_subscription_request(
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/availabilitySets')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if expand is not None:
        query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    resource_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_available_sizes_request(
    resource_group_name: str,
    availability_set_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2017-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/vmSizes')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("availability_set_name", availability_set_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class AvailabilitySetsOperations(object):
    """AvailabilitySetsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2017_03_30.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        availability_set_name: str,
        parameters: "_models.AvailabilitySet",
        **kwargs: Any
    ) -> "_models.AvailabilitySet":
        """Create or update an availability set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param availability_set_name: The name of the availability set.
        :type availability_set_name: str
        :param parameters: Parameters supplied to the Create Availability Set operation.
        :type parameters: ~azure.mgmt.compute.v2017_03_30.models.AvailabilitySet
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AvailabilitySet, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_03_30.models.AvailabilitySet
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailabilitySet"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'AvailabilitySet')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            availability_set_name=availability_set_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AvailabilitySet', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        availability_set_name: str,
        **kwargs: Any
    ) -> Optional["_models.OperationStatusResponse"]:
        """Delete an availability set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param availability_set_name: The name of the availability set.
        :type availability_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationStatusResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_03_30.models.OperationStatusResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.OperationStatusResponse"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            availability_set_name=availability_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatusResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        availability_set_name: str,
        **kwargs: Any
    ) -> "_models.AvailabilitySet":
        """Retrieves information about an availability set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param availability_set_name: The name of the availability set.
        :type availability_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AvailabilitySet, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_03_30.models.AvailabilitySet
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailabilitySet"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            availability_set_name=availability_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AvailabilitySet', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}'}  # type: ignore


    @distributed_trace
    def list_by_subscription(
        self,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.AvailabilitySetListResult"]:
        """Lists all availability sets in a subscription.

        :param expand: The expand expression to apply to the operation. Allowed values are
         'instanceView'.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailabilitySetListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2017_03_30.models.AvailabilitySetListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailabilitySetListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    template_url=self.list_by_subscription.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilitySetListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/availabilitySets'}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> Iterable["_models.AvailabilitySetListResult"]:
        """Lists all availability sets in a resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailabilitySetListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2017_03_30.models.AvailabilitySetListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailabilitySetListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilitySetListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets'}  # type: ignore

    @distributed_trace
    def list_available_sizes(
        self,
        resource_group_name: str,
        availability_set_name: str,
        **kwargs: Any
    ) -> Iterable["_models.VirtualMachineSizeListResult"]:
        """Lists all available virtual machine sizes that can be used to create a new virtual machine in
        an existing availability set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param availability_set_name: The name of the availability set.
        :type availability_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either VirtualMachineSizeListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2017_03_30.models.VirtualMachineSizeListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineSizeListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_available_sizes_request(
                    resource_group_name=resource_group_name,
                    availability_set_name=availability_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_available_sizes.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_available_sizes_request(
                    resource_group_name=resource_group_name,
                    availability_set_name=availability_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("VirtualMachineSizeListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_available_sizes.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/vmSizes'}  # type: ignore
