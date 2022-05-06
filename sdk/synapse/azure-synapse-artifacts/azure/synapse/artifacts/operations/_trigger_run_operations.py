# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_rerun_trigger_instance_request(
    trigger_name: str,
    run_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/triggers/{triggerName}/triggerRuns/{runId}/rerun")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_cancel_trigger_instance_request(
    trigger_name: str,
    run_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/triggers/{triggerName}/triggerRuns/{runId}/cancel")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url("trigger_name", trigger_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_query_trigger_runs_by_workspace_request(
    *,
    json: Optional[_models.RunFilterParameters] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/queryTriggerRuns")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )

class TriggerRunOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.synapse.artifacts.ArtifactsClient`'s
        :attr:`trigger_run` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def rerun_trigger_instance(  # pylint: disable=inconsistent-return-statements
        self,
        trigger_name: str,
        run_id: str,
        **kwargs: Any
    ) -> None:
        """Rerun single trigger instance by runId.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword api_version: Api Version. Default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_rerun_trigger_instance_request(
            trigger_name=trigger_name,
            run_id=run_id,
            api_version=api_version,
            template_url=self.rerun_trigger_instance.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    rerun_trigger_instance.metadata = {'url': "/triggers/{triggerName}/triggerRuns/{runId}/rerun"}  # type: ignore


    @distributed_trace
    def cancel_trigger_instance(  # pylint: disable=inconsistent-return-statements
        self,
        trigger_name: str,
        run_id: str,
        **kwargs: Any
    ) -> None:
        """Cancel single trigger instance by runId.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword api_version: Api Version. Default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_cancel_trigger_instance_request(
            trigger_name=trigger_name,
            run_id=run_id,
            api_version=api_version,
            template_url=self.cancel_trigger_instance.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_trigger_instance.metadata = {'url': "/triggers/{triggerName}/triggerRuns/{runId}/cancel"}  # type: ignore


    @distributed_trace
    def query_trigger_runs_by_workspace(
        self,
        filter_parameters: _models.RunFilterParameters,
        **kwargs: Any
    ) -> _models.TriggerRunsQueryResponse:
        """Query trigger runs.

        :param filter_parameters: Parameters to filter the pipeline run.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword api_version: Api Version. Default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-12-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.TriggerRunsQueryResponse]

        _json = self._serialize.body(filter_parameters, 'RunFilterParameters')

        request = build_query_trigger_runs_by_workspace_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.query_trigger_runs_by_workspace.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TriggerRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_trigger_runs_by_workspace.metadata = {'url': "/queryTriggerRuns"}  # type: ignore

