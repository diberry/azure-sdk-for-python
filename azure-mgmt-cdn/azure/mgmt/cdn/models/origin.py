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

from .tracked_resource import TrackedResource


class Origin(TrackedResource):
    """CDN origin is the source of the content being delivered via CDN. When the
    edge nodes represented by an endpoint do not have the requested content
    cached, they attempt to fetch it from one or more of the configured
    origins.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param host_name: Required. The address of the origin. Domain names, IPv4
     addresses, and IPv6 addresses are supported.
    :type host_name: str
    :param http_port: The value of the HTTP port. Must be between 1 and 65535.
    :type http_port: int
    :param https_port: The value of the https port. Must be between 1 and
     65535.
    :type https_port: int
    :ivar resource_state: Resource status of the origin. Possible values
     include: 'Creating', 'Active', 'Deleting'
    :vartype resource_state: str or ~azure.mgmt.cdn.models.OriginResourceState
    :ivar provisioning_state: Provisioning status of the origin.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'host_name': {'required': True},
        'http_port': {'maximum': 65535, 'minimum': 1},
        'https_port': {'maximum': 65535, 'minimum': 1},
        'resource_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'http_port': {'key': 'properties.httpPort', 'type': 'int'},
        'https_port': {'key': 'properties.httpsPort', 'type': 'int'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Origin, self).__init__(**kwargs)
        self.host_name = kwargs.get('host_name', None)
        self.http_port = kwargs.get('http_port', None)
        self.https_port = kwargs.get('https_port', None)
        self.resource_state = None
        self.provisioning_state = None
