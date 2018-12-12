# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class ResourceNameAvailabilityResponseResource(Resource):
    """Response for check name availability API. Resource provider will set
    availability as true | false.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id represents the complete path to the resource.
    :vartype id: str
    :ivar name: Resource name associated with the resource.
    :vartype name: str
    :ivar type: Resource type represents the complete path of the form
     Namespace/ResourceType/ResourceType/...
    :vartype type: str
    :param e_tag: Optional ETag.
    :type e_tag: str
    :param properties: ResourceNameAvailabilityResponseResource properties
    :type properties:
     ~azure.mgmt.recoveryservices.models.ResourceNameAvailabilityResponse
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ResourceNameAvailabilityResponse'},
    }

    def __init__(self, *, e_tag: str=None, properties=None, **kwargs) -> None:
        super(ResourceNameAvailabilityResponseResource, self).__init__(e_tag=e_tag, **kwargs)
        self.properties = properties
