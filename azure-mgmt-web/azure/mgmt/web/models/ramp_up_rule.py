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


class RampUpRule(Model):
    """Routing rules for ramp up testing. This rule allows to redirect static
    traffic % to a slot or to gradually change routing % based on performance.

    :param action_host_name: Hostname of a slot to which the traffic will be
     redirected if decided to. E.g. myapp-stage.azurewebsites.net.
    :type action_host_name: str
    :param reroute_percentage: Percentage of the traffic which will be
     redirected to <code>ActionHostName</code>.
    :type reroute_percentage: float
    :param change_step: In auto ramp up scenario this is the step to
     add/remove from <code>ReroutePercentage</code> until it reaches
     <code>MinReroutePercentage</code> or <code>MaxReroutePercentage</code>.
     Site metrics are checked every N minutes specified in
     <code>ChangeIntervalInMinutes</code>.
     Custom decision algorithm can be provided in TiPCallback site extension
     which URL can be specified in <code>ChangeDecisionCallbackUrl</code>.
    :type change_step: float
    :param change_interval_in_minutes: Specifies interval in minutes to
     reevaluate ReroutePercentage.
    :type change_interval_in_minutes: int
    :param min_reroute_percentage: Specifies lower boundary above which
     ReroutePercentage will stay.
    :type min_reroute_percentage: float
    :param max_reroute_percentage: Specifies upper boundary below which
     ReroutePercentage will stay.
    :type max_reroute_percentage: float
    :param change_decision_callback_url: Custom decision algorithm can be
     provided in TiPCallback site extension which URL can be specified. See
     TiPCallback site extension for the scaffold and contracts.
     https://www.siteextensions.net/packages/TiPCallback/
    :type change_decision_callback_url: str
    :param name: Name of the routing rule. The recommended name would be to
     point to the slot which will receive the traffic in the experiment.
    :type name: str
    """

    _attribute_map = {
        'action_host_name': {'key': 'actionHostName', 'type': 'str'},
        'reroute_percentage': {'key': 'reroutePercentage', 'type': 'float'},
        'change_step': {'key': 'changeStep', 'type': 'float'},
        'change_interval_in_minutes': {'key': 'changeIntervalInMinutes', 'type': 'int'},
        'min_reroute_percentage': {'key': 'minReroutePercentage', 'type': 'float'},
        'max_reroute_percentage': {'key': 'maxReroutePercentage', 'type': 'float'},
        'change_decision_callback_url': {'key': 'changeDecisionCallbackUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RampUpRule, self).__init__(**kwargs)
        self.action_host_name = kwargs.get('action_host_name', None)
        self.reroute_percentage = kwargs.get('reroute_percentage', None)
        self.change_step = kwargs.get('change_step', None)
        self.change_interval_in_minutes = kwargs.get('change_interval_in_minutes', None)
        self.min_reroute_percentage = kwargs.get('min_reroute_percentage', None)
        self.max_reroute_percentage = kwargs.get('max_reroute_percentage', None)
        self.change_decision_callback_url = kwargs.get('change_decision_callback_url', None)
        self.name = kwargs.get('name', None)
