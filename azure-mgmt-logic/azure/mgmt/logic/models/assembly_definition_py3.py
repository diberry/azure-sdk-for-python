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


class AssemblyDefinition(Resource):
    """The assembly definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param properties: Required. The assembly properties.
    :type properties: ~azure.mgmt.logic.models.AssemblyProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'AssemblyProperties'},
    }

    def __init__(self, *, properties, location: str=None, tags=None, **kwargs) -> None:
        super(AssemblyDefinition, self).__init__(location=location, tags=tags, **kwargs)
        self.properties = properties
