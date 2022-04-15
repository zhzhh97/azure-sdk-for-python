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
from ...operations._virtual_machine_scale_set_extensions_operations import build_create_or_update_request_initial, build_delete_request_initial, build_get_request, build_list_request, build_update_request_initial
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class VirtualMachineScaleSetExtensionsOperations:
    """VirtualMachineScaleSetExtensionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2020_12_01.models
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

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        extension_parameters: "_models.VirtualMachineScaleSetExtension",
        **kwargs: Any
    ) -> "_models.VirtualMachineScaleSetExtension":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtension"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(extension_parameters, 'VirtualMachineScaleSetExtension')

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore


    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        extension_parameters: "_models.VirtualMachineScaleSetExtension",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VirtualMachineScaleSetExtension"]:
        """The operation to create or update an extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set where the extension should be create or
         updated.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :param extension_parameters: Parameters supplied to the Create VM scale set Extension
         operation.
        :type extension_parameters:
         ~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtension
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineScaleSetExtension or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtension]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtension"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                vmss_extension_name=vmss_extension_name,
                extension_parameters=extension_parameters,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)
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

    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        extension_parameters: "_models.VirtualMachineScaleSetExtensionUpdate",
        **kwargs: Any
    ) -> "_models.VirtualMachineScaleSetExtension":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtension"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(extension_parameters, 'VirtualMachineScaleSetExtensionUpdate')

        request = build_update_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore


    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        extension_parameters: "_models.VirtualMachineScaleSetExtensionUpdate",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VirtualMachineScaleSetExtension"]:
        """The operation to update an extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set where the extension should be updated.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :param extension_parameters: Parameters supplied to the Update VM scale set Extension
         operation.
        :type extension_parameters:
         ~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtensionUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineScaleSetExtension or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtension]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtension"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                vmss_extension_name=vmss_extension_name,
                extension_parameters=extension_parameters,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)
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

    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore

    async def _delete_initial(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            subscription_id=self._config.subscription_id,
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

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore


    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """The operation to delete the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set where the extension should be deleted.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
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
                vm_scale_set_name=vm_scale_set_name,
                vmss_extension_name=vmss_extension_name,
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

    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        vmss_extension_name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.VirtualMachineScaleSetExtension":
        """The operation to get the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set containing the extension.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineScaleSetExtension, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtension
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtension"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.VirtualMachineScaleSetExtensionListResult"]:
        """Gets a list of all extensions in a VM scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set containing the extension.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either VirtualMachineScaleSetExtensionListResult or the
         result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2020_12_01.models.VirtualMachineScaleSetExtensionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineScaleSetExtensionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    vm_scale_set_name=vm_scale_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    vm_scale_set_name=vm_scale_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("VirtualMachineScaleSetExtensionListResult", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions'}  # type: ignore
