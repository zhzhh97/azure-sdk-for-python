# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    build_service_name: str,
    builder_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
        "buildServiceName": _SERIALIZER.url("build_service_name", build_service_name, 'str'),
        "builderName": _SERIALIZER.url("builder_name", builder_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_create_or_update_request_initial(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    build_service_name: str,
    builder_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-04-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
        "buildServiceName": _SERIALIZER.url("build_service_name", build_service_name, 'str'),
        "builderName": _SERIALIZER.url("builder_name", builder_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request_initial(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    build_service_name: str,
    builder_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
        "buildServiceName": _SERIALIZER.url("build_service_name", build_service_name, 'str'),
        "builderName": _SERIALIZER.url("builder_name", builder_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    build_service_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
        "buildServiceName": _SERIALIZER.url("build_service_name", build_service_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class BuildServiceBuilderOperations(object):
    """BuildServiceBuilderOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appplatform.v2022_04_01.models
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
    def get(
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        builder_name: str,
        **kwargs: Any
    ) -> "_models.BuilderResource":
        """Get a KPack builder.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param build_service_name: The name of the build service resource.
        :type build_service_name: str
        :param builder_name: The name of the builder resource.
        :type builder_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BuilderResource, or the result of cls(response)
        :rtype: ~azure.mgmt.appplatform.v2022_04_01.models.BuilderResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BuilderResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            build_service_name=build_service_name,
            builder_name=builder_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BuilderResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}"}  # type: ignore


    def _create_or_update_initial(
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        builder_name: str,
        builder_resource: "_models.BuilderResource",
        **kwargs: Any
    ) -> "_models.BuilderResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BuilderResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(builder_resource, 'BuilderResource')

        request = build_create_or_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            build_service_name=build_service_name,
            builder_name=builder_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('BuilderResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('BuilderResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}"}  # type: ignore


    @distributed_trace
    def begin_create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        builder_name: str,
        builder_resource: "_models.BuilderResource",
        **kwargs: Any
    ) -> LROPoller["_models.BuilderResource"]:
        """Create or update a KPack builder.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param build_service_name: The name of the build service resource.
        :type build_service_name: str
        :param builder_name: The name of the builder resource.
        :type builder_name: str
        :param builder_resource: The target builder for the create or update operation.
        :type builder_resource: ~azure.mgmt.appplatform.v2022_04_01.models.BuilderResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either BuilderResource or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.appplatform.v2022_04_01.models.BuilderResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BuilderResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                build_service_name=build_service_name,
                builder_name=builder_name,
                builder_resource=builder_resource,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('BuilderResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}"}  # type: ignore

    def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        builder_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            build_service_name=build_service_name,
            builder_name=builder_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}"}  # type: ignore


    @distributed_trace
    def begin_delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        builder_name: str,
        **kwargs: Any
    ) -> LROPoller[None]:
        """Delete a KPack builder.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param build_service_name: The name of the build service resource.
        :type build_service_name: str
        :param builder_name: The name of the builder resource.
        :type builder_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                build_service_name=build_service_name,
                builder_name=builder_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders/{builderName}"}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        service_name: str,
        build_service_name: str,
        **kwargs: Any
    ) -> Iterable["_models.BuilderResourceCollection"]:
        """List KPack builders result.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param build_service_name: The name of the build service resource.
        :type build_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BuilderResourceCollection or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.appplatform.v2022_04_01.models.BuilderResourceCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-04-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BuilderResourceCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    build_service_name=build_service_name,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    build_service_name=build_service_name,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BuilderResourceCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/buildServices/{buildServiceName}/builders"}  # type: ignore
