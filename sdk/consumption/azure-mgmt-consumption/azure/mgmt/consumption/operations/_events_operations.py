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

def build_list_by_billing_profile_request(
    billing_account_id: str,
    billing_profile_id: str,
    *,
    start_date: str,
    end_date: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/events')
    path_format_arguments = {
        "billingAccountId": _SERIALIZER.url("billing_account_id", billing_account_id, 'str'),
        "billingProfileId": _SERIALIZER.url("billing_profile_id", billing_profile_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    query_parameters['startDate'] = _SERIALIZER.query("start_date", start_date, 'str')
    query_parameters['endDate'] = _SERIALIZER.query("end_date", end_date, 'str')

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


def build_list_by_billing_account_request(
    billing_account_id: str,
    *,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/events')
    path_format_arguments = {
        "billingAccountId": _SERIALIZER.url("billing_account_id", billing_account_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')

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

class EventsOperations(object):
    """EventsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.consumption.models
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
    def list_by_billing_profile(
        self,
        billing_account_id: str,
        billing_profile_id: str,
        start_date: str,
        end_date: str,
        **kwargs: Any
    ) -> Iterable["_models.Events"]:
        """Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a
        billing account or a billing profile for a given start and end date.

        :param billing_account_id: BillingAccount ID.
        :type billing_account_id: str
        :param billing_profile_id: Azure Billing Profile ID.
        :type billing_profile_id: str
        :param start_date: Start date.
        :type start_date: str
        :param end_date: End date.
        :type end_date: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Events or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.consumption.models.Events]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Events"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_billing_profile_request(
                    billing_account_id=billing_account_id,
                    billing_profile_id=billing_profile_id,
                    start_date=start_date,
                    end_date=end_date,
                    template_url=self.list_by_billing_profile.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_billing_profile_request(
                    billing_account_id=billing_account_id,
                    billing_profile_id=billing_profile_id,
                    start_date=start_date,
                    end_date=end_date,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("Events", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/events'}  # type: ignore

    @distributed_trace
    def list_by_billing_account(
        self,
        billing_account_id: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.Events"]:
        """Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a
        billing account or a billing profile for a given start and end date.

        :param billing_account_id: BillingAccount ID.
        :type billing_account_id: str
        :param filter: May be used to filter the events by lotId, lotSource etc. The filter supports
         'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
         Tag filter is a key value pair string where key and value is separated by a colon (:).
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Events or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.consumption.models.Events]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Events"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_billing_account_request(
                    billing_account_id=billing_account_id,
                    filter=filter,
                    template_url=self.list_by_billing_account.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_billing_account_request(
                    billing_account_id=billing_account_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("Events", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/events'}  # type: ignore
