# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
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

def build_list_service_providers_request(
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.BotService/listAuthServiceProviders')
    path_format_arguments = {
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


def build_list_with_secrets_request(
    resource_group_name: str,
    resource_name: str,
    connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}/listWithSecrets')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "connectionName": _SERIALIZER.url("connection_name", connection_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][\sa-zA-Z0-9_.-]*$'),
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


def build_create_request(
    resource_group_name: str,
    resource_name: str,
    connection_name: str,
    subscription_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "connectionName": _SERIALIZER.url("connection_name", connection_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][\sa-zA-Z0-9_.-]*$'),
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


def build_update_request(
    resource_group_name: str,
    resource_name: str,
    connection_name: str,
    subscription_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "connectionName": _SERIALIZER.url("connection_name", connection_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][\sa-zA-Z0-9_.-]*$'),
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
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    resource_name: str,
    connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "connectionName": _SERIALIZER.url("connection_name", connection_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][\sa-zA-Z0-9_.-]*$'),
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


def build_delete_request(
    resource_group_name: str,
    resource_name: str,
    connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "connectionName": _SERIALIZER.url("connection_name", connection_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][\sa-zA-Z0-9_.-]*$'),
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


def build_list_by_bot_service_request(
    resource_group_name: str,
    resource_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str', max_length=64, min_length=2, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
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

class BotConnectionOperations(object):
    """BotConnectionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.botservice.models
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
    def list_service_providers(
        self,
        **kwargs: Any
    ) -> "_models.ServiceProviderResponseList":
        """Lists the available Service Providers for creating Connection Settings.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceProviderResponseList, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.ServiceProviderResponseList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ServiceProviderResponseList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_service_providers_request(
            subscription_id=self._config.subscription_id,
            template_url=self.list_service_providers.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ServiceProviderResponseList', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_service_providers.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.BotService/listAuthServiceProviders'}  # type: ignore


    @distributed_trace
    def list_with_secrets(
        self,
        resource_group_name: str,
        resource_name: str,
        connection_name: str,
        **kwargs: Any
    ) -> "_models.ConnectionSetting":
        """Get a Connection Setting registration for a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param connection_name: The name of the Bot Service Connection Setting resource.
        :type connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectionSetting, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.ConnectionSetting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConnectionSetting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_with_secrets_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            connection_name=connection_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list_with_secrets.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_with_secrets.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}/listWithSecrets'}  # type: ignore


    @distributed_trace
    def create(
        self,
        resource_group_name: str,
        resource_name: str,
        connection_name: str,
        parameters: "_models.ConnectionSetting",
        **kwargs: Any
    ) -> "_models.ConnectionSetting":
        """Register a new Auth Connection for a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param connection_name: The name of the Bot Service Connection Setting resource.
        :type connection_name: str
        :param parameters: The parameters to provide for creating the Connection Setting.
        :type parameters: ~azure.mgmt.botservice.models.ConnectionSetting
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectionSetting, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.ConnectionSetting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConnectionSetting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ConnectionSetting')

        request = build_create_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            connection_name=connection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        connection_name: str,
        parameters: "_models.ConnectionSetting",
        **kwargs: Any
    ) -> "_models.ConnectionSetting":
        """Updates a Connection Setting registration for a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param connection_name: The name of the Bot Service Connection Setting resource.
        :type connection_name: str
        :param parameters: The parameters to provide for updating the Connection Setting.
        :type parameters: ~azure.mgmt.botservice.models.ConnectionSetting
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectionSetting, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.ConnectionSetting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConnectionSetting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ConnectionSetting')

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            connection_name=connection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        resource_name: str,
        connection_name: str,
        **kwargs: Any
    ) -> "_models.ConnectionSetting":
        """Get a Connection Setting registration for a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param connection_name: The name of the Bot Service Connection Setting resource.
        :type connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectionSetting, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.ConnectionSetting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConnectionSetting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            connection_name=connection_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConnectionSetting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        connection_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a Connection Setting registration for a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param connection_name: The name of the Bot Service Connection Setting resource.
        :type connection_name: str
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

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            connection_name=connection_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections/{connectionName}'}  # type: ignore


    @distributed_trace
    def list_by_bot_service(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> Iterable["_models.ConnectionSettingResponseList"]:
        """Returns all the Connection Settings registered to a particular BotService resource.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ConnectionSettingResponseList or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.botservice.models.ConnectionSettingResponseList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConnectionSettingResponseList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_bot_service_request(
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_bot_service.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_bot_service_request(
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ConnectionSettingResponseList", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_bot_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections'}  # type: ignore
