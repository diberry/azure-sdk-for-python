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

from .protection_policy import ProtectionPolicy


class MabProtectionPolicy(ProtectionPolicy):
    """Mab container-specific backup policy.

    All required parameters must be populated in order to send to Azure.

    :param protected_items_count: Number of items associated with this policy.
    :type protected_items_count: int
    :param backup_management_type: Required. Constant filled by server.
    :type backup_management_type: str
    :param schedule_policy: Backup schedule of backup policy.
    :type schedule_policy:
     ~azure.mgmt.recoveryservicesbackup.models.SchedulePolicy
    :param retention_policy: Retention policy details.
    :type retention_policy:
     ~azure.mgmt.recoveryservicesbackup.models.RetentionPolicy
    """

    _validation = {
        'backup_management_type': {'required': True},
    }

    _attribute_map = {
        'protected_items_count': {'key': 'protectedItemsCount', 'type': 'int'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'schedule_policy': {'key': 'schedulePolicy', 'type': 'SchedulePolicy'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(MabProtectionPolicy, self).__init__(**kwargs)
        self.schedule_policy = kwargs.get('schedule_policy', None)
        self.retention_policy = kwargs.get('retention_policy', None)
        self.backup_management_type = 'MAB'
