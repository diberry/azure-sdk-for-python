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


class DetectorAbnormalTimePeriod(Model):
    """Class representing Abnormal Time Period detected.

    :param start_time: Start time of the correlated event
    :type start_time: datetime
    :param end_time: End time of the correlated event
    :type end_time: datetime
    :param message: Message describing the event
    :type message: str
    :param source: Represents the name of the Detector
    :type source: str
    :param priority: Represents the rank of the Detector
    :type priority: float
    :param meta_data: Downtime metadata
    :type meta_data: list[list[~azure.mgmt.web.models.NameValuePair]]
    :param type: Represents the type of the Detector. Possible values include:
     'ServiceIncident', 'AppDeployment', 'AppCrash', 'RuntimeIssueDetected',
     'AseDeployment', 'UserIssue', 'PlatformIssue', 'Other'
    :type type: str or ~azure.mgmt.web.models.IssueType
    :param solutions: List of proposed solutions
    :type solutions: list[~azure.mgmt.web.models.Solution]
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'float'},
        'meta_data': {'key': 'metaData', 'type': '[[NameValuePair]]'},
        'type': {'key': 'type', 'type': 'IssueType'},
        'solutions': {'key': 'solutions', 'type': '[Solution]'},
    }

    def __init__(self, *, start_time=None, end_time=None, message: str=None, source: str=None, priority: float=None, meta_data=None, type=None, solutions=None, **kwargs) -> None:
        super(DetectorAbnormalTimePeriod, self).__init__(**kwargs)
        self.start_time = start_time
        self.end_time = end_time
        self.message = message
        self.source = source
        self.priority = priority
        self.meta_data = meta_data
        self.type = type
        self.solutions = solutions
