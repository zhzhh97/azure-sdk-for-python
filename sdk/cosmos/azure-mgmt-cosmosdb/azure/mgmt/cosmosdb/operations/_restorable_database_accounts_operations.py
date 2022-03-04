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

def build_list_by_location_request(
    subscription_id: str,
    location: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-11-15-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "location": _SERIALIZER.url("location", location, 'str'),
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


def build_list_request(
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-11-15-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/restorableDatabaseAccounts')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
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


def build_get_by_location_request(
    subscription_id: str,
    location: str,
    instance_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-11-15-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "location": _SERIALIZER.url("location", location, 'str'),
        "instanceId": _SERIALIZER.url("instance_id", instance_id, 'str'),
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

class RestorableDatabaseAccountsOperations(object):
    """RestorableDatabaseAccountsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cosmosdb.models
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
    def list_by_location(
        self,
        location: str,
        **kwargs: Any
    ) -> Iterable["_models.RestorableDatabaseAccountsListResult"]:
        """Lists all the restorable Azure Cosmos DB database accounts available under the subscription and
        in a region.  This call requires
        'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.

        :param location: Cosmos DB region, with spaces between words and each word capitalized.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RestorableDatabaseAccountsListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.RestorableDatabaseAccountsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestorableDatabaseAccountsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_location_request(
                    subscription_id=self._config.subscription_id,
                    location=location,
                    template_url=self.list_by_location.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_location_request(
                    subscription_id=self._config.subscription_id,
                    location=location,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RestorableDatabaseAccountsListResult", pipeline_response)
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
    list_by_location.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts'}  # type: ignore

    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> Iterable["_models.RestorableDatabaseAccountsListResult"]:
        """Lists all the restorable Azure Cosmos DB database accounts available under the subscription.
        This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RestorableDatabaseAccountsListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.RestorableDatabaseAccountsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestorableDatabaseAccountsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RestorableDatabaseAccountsListResult", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/restorableDatabaseAccounts'}  # type: ignore

    @distributed_trace
    def get_by_location(
        self,
        location: str,
        instance_id: str,
        **kwargs: Any
    ) -> "_models.RestorableDatabaseAccountGetResult":
        """Retrieves the properties of an existing Azure Cosmos DB restorable database account.  This call
        requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission.

        :param location: Cosmos DB region, with spaces between words and each word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database account.
        :type instance_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RestorableDatabaseAccountGetResult, or the result of cls(response)
        :rtype: ~azure.mgmt.cosmosdb.models.RestorableDatabaseAccountGetResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestorableDatabaseAccountGetResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_by_location_request(
            subscription_id=self._config.subscription_id,
            location=location,
            instance_id=instance_id,
            template_url=self.get_by_location.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RestorableDatabaseAccountGetResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_location.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}'}  # type: ignore

