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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._webhooks_operations import build_create_request_initial, build_delete_request_initial, build_get_callback_config_request, build_get_request, build_list_events_request, build_list_request, build_ping_request, build_update_request_initial
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WebhooksOperations:
    """WebhooksOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.containerregistry.v2019_12_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> "_models.Webhook":
        """Gets the properties of the specified webhook.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Webhook, or the result of cls(response)
        :rtype: ~azure.mgmt.containerregistry.v2019_12_01_preview.models.Webhook
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Webhook"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Webhook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore


    async def _create_initial(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        webhook_create_parameters: "_models.WebhookCreateParameters",
        **kwargs: Any
    ) -> "_models.Webhook":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Webhook"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(webhook_create_parameters, 'WebhookCreateParameters')

        request = build_create_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            content_type=content_type,
            json=_json,
            template_url=self._create_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Webhook', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Webhook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore


    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        webhook_create_parameters: "_models.WebhookCreateParameters",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.Webhook"]:
        """Creates a webhook for a container registry with the specified parameters.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :param webhook_create_parameters: The parameters for creating a webhook.
        :type webhook_create_parameters:
         ~azure.mgmt.containerregistry.v2019_12_01_preview.models.WebhookCreateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either Webhook or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerregistry.v2019_12_01_preview.models.Webhook]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Webhook"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                registry_name=registry_name,
                webhook_name=webhook_name,
                webhook_create_parameters=webhook_create_parameters,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('Webhook', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore

    async def _delete_initial(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore


    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes a webhook from a container registry.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                registry_name=registry_name,
                webhook_name=webhook_name,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        webhook_update_parameters: "_models.WebhookUpdateParameters",
        **kwargs: Any
    ) -> "_models.Webhook":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Webhook"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(webhook_update_parameters, 'WebhookUpdateParameters')

        request = build_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            content_type=content_type,
            json=_json,
            template_url=self._update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Webhook', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Webhook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore


    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        webhook_update_parameters: "_models.WebhookUpdateParameters",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.Webhook"]:
        """Updates a webhook with the specified parameters.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :param webhook_update_parameters: The parameters for updating a webhook.
        :type webhook_update_parameters:
         ~azure.mgmt.containerregistry.v2019_12_01_preview.models.WebhookUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either Webhook or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerregistry.v2019_12_01_preview.models.Webhook]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Webhook"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                registry_name=registry_name,
                webhook_name=webhook_name,
                webhook_update_parameters=webhook_update_parameters,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('Webhook', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}'}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        registry_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.WebhookListResult"]:
        """Lists all the webhooks for the specified container registry.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either WebhookListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.containerregistry.v2019_12_01_preview.models.WebhookListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.WebhookListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    registry_name=registry_name,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    registry_name=registry_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("WebhookListResult", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks'}  # type: ignore

    @distributed_trace_async
    async def ping(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> "_models.EventInfo":
        """Triggers a ping event to be sent to the webhook.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventInfo, or the result of cls(response)
        :rtype: ~azure.mgmt.containerregistry.v2019_12_01_preview.models.EventInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EventInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_ping_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            template_url=self.ping.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EventInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    ping.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}/ping'}  # type: ignore


    @distributed_trace_async
    async def get_callback_config(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> "_models.CallbackConfig":
        """Gets the configuration of service URI and custom headers for the webhook.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CallbackConfig, or the result of cls(response)
        :rtype: ~azure.mgmt.containerregistry.v2019_12_01_preview.models.CallbackConfig
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CallbackConfig"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_callback_config_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            webhook_name=webhook_name,
            template_url=self.get_callback_config.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CallbackConfig', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_callback_config.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}/getCallbackConfig'}  # type: ignore


    @distributed_trace
    def list_events(
        self,
        resource_group_name: str,
        registry_name: str,
        webhook_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.EventListResult"]:
        """Lists recent events for the specified webhook.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param webhook_name: The name of the webhook.
        :type webhook_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EventListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.containerregistry.v2019_12_01_preview.models.EventListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EventListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_events_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    registry_name=registry_name,
                    webhook_name=webhook_name,
                    template_url=self.list_events.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_events_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    registry_name=registry_name,
                    webhook_name=webhook_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("EventListResult", pipeline_response)
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
    list_events.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}/listEvents'}  # type: ignore
