# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._check_name_availability_operations import build_execute_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CheckNameAvailabilityOperations:
    """CheckNameAvailabilityOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.rdbms.mysql_flexibleservers.models
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
    async def execute(
        self,
        location_name: str,
        name_availability_request: "_models.NameAvailabilityRequest",
        **kwargs: Any
    ) -> "_models.NameAvailability":
        """Check the availability of name for server.

        :param location_name: The name of the location.
        :type location_name: str
        :param name_availability_request: The required parameters for checking if server name is
         available.
        :type name_availability_request:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailabilityRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability, or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.NameAvailability
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NameAvailability"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(name_availability_request, 'NameAvailabilityRequest')

        request = build_execute_request(
            subscription_id=self._config.subscription_id,
            location_name=location_name,
            content_type=content_type,
            json=_json,
            template_url=self.execute.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('NameAvailability', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    execute.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DBforMySQL/locations/{locationName}/checkNameAvailability'}  # type: ignore

