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

from msrest.serialization import Model


class AlertRuleKind1(Model):
    """Describes an Azure resource with kind.

    :param kind: The kind of the alert rule. Possible values include:
     'Scheduled'
    :type kind: str or ~azure.mgmt.securityinsight.models.AlertRuleKind
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, *, kind=None, **kwargs) -> None:
        super(AlertRuleKind1, self).__init__(**kwargs)
        self.kind = kind
