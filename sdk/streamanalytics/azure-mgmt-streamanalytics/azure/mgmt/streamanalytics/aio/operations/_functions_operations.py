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
from ...operations._functions_operations import build_create_or_replace_request, build_delete_request, build_get_request, build_list_by_streaming_job_request, build_retrieve_default_definition_request, build_test_request_initial, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FunctionsOperations:
    """FunctionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~stream_analytics_management_client.models
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
    async def create_or_replace(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        function: "_models.Function",
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.Function":
        """Creates a function or replaces an already existing function under an existing streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
        :param function: The definition of the function that will be used to create a new function or
         replace the existing one under the streaming job.
        :type function: ~stream_analytics_management_client.models.Function
        :param if_match: The ETag of the function. Omit this value to always overwrite the current
         function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent
         changes.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new function to be created, but to prevent updating
         an existing function. Other values will result in a 412 Pre-condition Failed response.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Function, or the result of cls(response)
        :rtype: ~stream_analytics_management_client.models.Function
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Function"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(function, 'Function')

        request = build_create_or_replace_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            if_none_match=if_none_match,
            template_url=self.create_or_replace.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            
            deserialized = self._deserialize('Function', pipeline_response)

        if response.status_code == 201:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            
            deserialized = self._deserialize('Function', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create_or_replace.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        function: "_models.Function",
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.Function":
        """Updates an existing function under an existing streaming job. This can be used to partially
        update (ie. update one or two properties) a function without affecting the rest the job or
        function definition.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
        :param function: A function object. The properties specified here will overwrite the
         corresponding properties in the existing function (ie. Those properties will be updated). Any
         properties that are set to null here will mean that the corresponding property in the existing
         function will remain the same and not change as a result of this PATCH operation.
        :type function: ~stream_analytics_management_client.models.Function
        :param if_match: The ETag of the function. Omit this value to always overwrite the current
         function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent
         changes.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Function, or the result of cls(response)
        :rtype: ~stream_analytics_management_client.models.Function
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Function"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(function, 'Function')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))

        deserialized = self._deserialize('Function', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a function from the streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
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
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        **kwargs: Any
    ) -> "_models.Function":
        """Gets details about the specified function.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Function, or the result of cls(response)
        :rtype: ~stream_analytics_management_client.models.Function
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Function"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))

        deserialized = self._deserialize('Function', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}'}  # type: ignore


    @distributed_trace
    def list_by_streaming_job(
        self,
        resource_group_name: str,
        job_name: str,
        select: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.FunctionListResult"]:
        """Lists all of the functions under the specified streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param select: The $select OData query parameter. This is a comma-separated list of structural
         properties to include in the response, or "\ *" to include all properties. By default, all
         properties are returned except diagnostics. Currently only accepts '*\ ' as a valid value.
        :type select: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FunctionListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~stream_analytics_management_client.models.FunctionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FunctionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_streaming_job_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    job_name=job_name,
                    select=select,
                    template_url=self.list_by_streaming_job.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_streaming_job_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    job_name=job_name,
                    select=select,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FunctionListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_streaming_job.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions'}  # type: ignore

    async def _test_initial(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        function: Optional["_models.Function"] = None,
        **kwargs: Any
    ) -> Optional["_models.ResourceTestStatus"]:
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ResourceTestStatus"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if function is not None:
            _json = self._serialize.body(function, 'Function')
        else:
            _json = None

        request = build_test_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            content_type=content_type,
            json=_json,
            template_url=self._test_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ResourceTestStatus', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _test_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}/test'}  # type: ignore


    @distributed_trace_async
    async def begin_test(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        function: Optional["_models.Function"] = None,
        **kwargs: Any
    ) -> AsyncLROPoller["_models.ResourceTestStatus"]:
        """Tests if the information provided for a function is valid. This can range from testing the
        connection to the underlying web service behind the function or making sure the function code
        provided is syntactically correct.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
        :param function: If the function specified does not already exist, this parameter must contain
         the full function definition intended to be tested. If the function specified already exists,
         this parameter can be left null to test the existing function as is or if specified, the
         properties specified will overwrite the corresponding properties in the existing function
         (exactly like a PATCH operation) and the resulting function will be tested.
        :type function: ~stream_analytics_management_client.models.Function
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ResourceTestStatus or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~stream_analytics_management_client.models.ResourceTestStatus]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceTestStatus"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._test_initial(
                resource_group_name=resource_group_name,
                job_name=job_name,
                function_name=function_name,
                function=function,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('ResourceTestStatus', pipeline_response)
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

    begin_test.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}/test'}  # type: ignore

    @distributed_trace_async
    async def retrieve_default_definition(
        self,
        resource_group_name: str,
        job_name: str,
        function_name: str,
        function_retrieve_default_definition_parameters: Optional["_models.FunctionRetrieveDefaultDefinitionParameters"] = None,
        **kwargs: Any
    ) -> "_models.Function":
        """Retrieves the default definition of a function based on the parameters specified.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param function_name: The name of the function.
        :type function_name: str
        :param function_retrieve_default_definition_parameters: Parameters used to specify the type of
         function to retrieve the default definition for.
        :type function_retrieve_default_definition_parameters:
         ~stream_analytics_management_client.models.FunctionRetrieveDefaultDefinitionParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Function, or the result of cls(response)
        :rtype: ~stream_analytics_management_client.models.Function
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Function"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if function_retrieve_default_definition_parameters is not None:
            _json = self._serialize.body(function_retrieve_default_definition_parameters, 'FunctionRetrieveDefaultDefinitionParameters')
        else:
            _json = None

        request = build_retrieve_default_definition_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            job_name=job_name,
            function_name=function_name,
            content_type=content_type,
            json=_json,
            template_url=self.retrieve_default_definition.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Function', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    retrieve_default_definition.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/functions/{functionName}/retrieveDefaultDefinition'}  # type: ignore

