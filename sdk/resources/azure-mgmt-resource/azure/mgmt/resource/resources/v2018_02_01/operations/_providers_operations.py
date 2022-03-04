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
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_unregister_request(
    resource_provider_namespace: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-02-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister')
    path_format_arguments = {
        "resourceProviderNamespace": _SERIALIZER.url("resource_provider_namespace", resource_provider_namespace, 'str'),
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
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_register_request(
    resource_provider_namespace: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-02-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register')
    path_format_arguments = {
        "resourceProviderNamespace": _SERIALIZER.url("resource_provider_namespace", resource_provider_namespace, 'str'),
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
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id: str,
    *,
    top: Optional[int] = None,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-02-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    if expand is not None:
        query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')
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


def build_get_request(
    resource_provider_namespace: str,
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-02-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}')
    path_format_arguments = {
        "resourceProviderNamespace": _SERIALIZER.url("resource_provider_namespace", resource_provider_namespace, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if expand is not None:
        query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')
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

class ProvidersOperations(object):
    """ProvidersOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.resources.v2018_02_01.models
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
    def unregister(
        self,
        resource_provider_namespace: str,
        **kwargs: Any
    ) -> "_models.Provider":
        """Unregisters a subscription from a resource provider.

        :param resource_provider_namespace: The namespace of the resource provider to unregister.
        :type resource_provider_namespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2018_02_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Provider"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_unregister_request(
            resource_provider_namespace=resource_provider_namespace,
            subscription_id=self._config.subscription_id,
            template_url=self.unregister.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    unregister.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister'}  # type: ignore


    @distributed_trace
    def register(
        self,
        resource_provider_namespace: str,
        **kwargs: Any
    ) -> "_models.Provider":
        """Registers a subscription with a resource provider.

        :param resource_provider_namespace: The namespace of the resource provider to register.
        :type resource_provider_namespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2018_02_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Provider"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_register_request(
            resource_provider_namespace=resource_provider_namespace,
            subscription_id=self._config.subscription_id,
            template_url=self.register.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    register.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register'}  # type: ignore


    @distributed_trace
    def list(
        self,
        top: Optional[int] = None,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.ProviderListResult"]:
        """Gets all resource providers for a subscription.

        :param top: The number of results to return. If null is passed returns all deployments.
        :type top: int
        :param expand: The properties to include in the results. For example, use &$expand=metadata in
         the query string to retrieve resource provider metadata. To include property aliases in
         response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProviderListResult or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.resources.v2018_02_01.models.ProviderListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProviderListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    top=top,
                    expand=expand,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    top=top,
                    expand=expand,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProviderListResult", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers'}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_provider_namespace: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.Provider":
        """Gets the specified resource provider.

        :param resource_provider_namespace: The namespace of the resource provider.
        :type resource_provider_namespace: str
        :param expand: The $expand query parameter. For example, to include property aliases in
         response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2018_02_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Provider"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_provider_namespace=resource_provider_namespace,
            subscription_id=self._config.subscription_id,
            expand=expand,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}'}  # type: ignore

