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


class ApplicationInsightsComponentFeatureCapabilities(Model):
    """An Application Insights component feature capabilities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar support_export_data: Whether allow to use continuous export feature.
    :vartype support_export_data: bool
    :ivar burst_throttle_policy: Reserved, not used now.
    :vartype burst_throttle_policy: str
    :ivar metadata_class: Reserved, not used now.
    :vartype metadata_class: str
    :ivar live_stream_metrics: Reserved, not used now.
    :vartype live_stream_metrics: bool
    :ivar application_map: Reserved, not used now.
    :vartype application_map: bool
    :ivar work_item_integration: Whether allow to use work item integration
     feature.
    :vartype work_item_integration: bool
    :ivar power_bi_integration: Reserved, not used now.
    :vartype power_bi_integration: bool
    :ivar open_schema: Reserved, not used now.
    :vartype open_schema: bool
    :ivar proactive_detection: Reserved, not used now.
    :vartype proactive_detection: bool
    :ivar analytics_integration: Reserved, not used now.
    :vartype analytics_integration: bool
    :ivar multiple_step_web_test: Whether allow to use multiple steps web test
     feature.
    :vartype multiple_step_web_test: bool
    :ivar api_access_level: Reserved, not used now.
    :vartype api_access_level: str
    :ivar tracking_type: The application insights component used tracking
     type.
    :vartype tracking_type: str
    :ivar daily_cap: Daily data volume cap in GB.
    :vartype daily_cap: float
    :ivar daily_cap_reset_time: Daily data volume cap UTC reset hour.
    :vartype daily_cap_reset_time: float
    :ivar throttle_rate: Reserved, not used now.
    :vartype throttle_rate: float
    """

    _validation = {
        'support_export_data': {'readonly': True},
        'burst_throttle_policy': {'readonly': True},
        'metadata_class': {'readonly': True},
        'live_stream_metrics': {'readonly': True},
        'application_map': {'readonly': True},
        'work_item_integration': {'readonly': True},
        'power_bi_integration': {'readonly': True},
        'open_schema': {'readonly': True},
        'proactive_detection': {'readonly': True},
        'analytics_integration': {'readonly': True},
        'multiple_step_web_test': {'readonly': True},
        'api_access_level': {'readonly': True},
        'tracking_type': {'readonly': True},
        'daily_cap': {'readonly': True},
        'daily_cap_reset_time': {'readonly': True},
        'throttle_rate': {'readonly': True},
    }

    _attribute_map = {
        'support_export_data': {'key': 'SupportExportData', 'type': 'bool'},
        'burst_throttle_policy': {'key': 'BurstThrottlePolicy', 'type': 'str'},
        'metadata_class': {'key': 'MetadataClass', 'type': 'str'},
        'live_stream_metrics': {'key': 'LiveStreamMetrics', 'type': 'bool'},
        'application_map': {'key': 'ApplicationMap', 'type': 'bool'},
        'work_item_integration': {'key': 'WorkItemIntegration', 'type': 'bool'},
        'power_bi_integration': {'key': 'PowerBIIntegration', 'type': 'bool'},
        'open_schema': {'key': 'OpenSchema', 'type': 'bool'},
        'proactive_detection': {'key': 'ProactiveDetection', 'type': 'bool'},
        'analytics_integration': {'key': 'AnalyticsIntegration', 'type': 'bool'},
        'multiple_step_web_test': {'key': 'MultipleStepWebTest', 'type': 'bool'},
        'api_access_level': {'key': 'ApiAccessLevel', 'type': 'str'},
        'tracking_type': {'key': 'TrackingType', 'type': 'str'},
        'daily_cap': {'key': 'DailyCap', 'type': 'float'},
        'daily_cap_reset_time': {'key': 'DailyCapResetTime', 'type': 'float'},
        'throttle_rate': {'key': 'ThrottleRate', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ApplicationInsightsComponentFeatureCapabilities, self).__init__(**kwargs)
        self.support_export_data = None
        self.burst_throttle_policy = None
        self.metadata_class = None
        self.live_stream_metrics = None
        self.application_map = None
        self.work_item_integration = None
        self.power_bi_integration = None
        self.open_schema = None
        self.proactive_detection = None
        self.analytics_integration = None
        self.multiple_step_web_test = None
        self.api_access_level = None
        self.tracking_type = None
        self.daily_cap = None
        self.daily_cap_reset_time = None
        self.throttle_rate = None
