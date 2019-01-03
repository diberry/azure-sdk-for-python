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

from .execution_activity_py3 import ExecutionActivity


class ExecuteSSISPackageActivity(ExecutionActivity):
    """Execute SSIS package activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param package_location: Required. SSIS package location.
    :type package_location: ~azure.mgmt.datafactory.models.SSISPackageLocation
    :param runtime: Specifies the runtime to execute SSIS package. The value
     should be "x86" or "x64". Type: string (or Expression with resultType
     string).
    :type runtime: object
    :param logging_level: The logging level of SSIS package execution. Type:
     string (or Expression with resultType string).
    :type logging_level: object
    :param environment_path: The environment path to execute the SSIS package.
     Type: string (or Expression with resultType string).
    :type environment_path: object
    :param connect_via: Required. The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param project_parameters: The project level parameters to execute the
     SSIS package.
    :type project_parameters: dict[str,
     ~azure.mgmt.datafactory.models.SSISExecutionParameter]
    :param package_parameters: The package level parameters to execute the
     SSIS package.
    :type package_parameters: dict[str,
     ~azure.mgmt.datafactory.models.SSISExecutionParameter]
    :param project_connection_managers: The project level connection managers
     to execute the SSIS package.
    :type project_connection_managers: dict[str, dict[str,
     ~azure.mgmt.datafactory.models.SSISExecutionParameter]]
    :param package_connection_managers: The package level connection managers
     to execute the SSIS package.
    :type package_connection_managers: dict[str, dict[str,
     ~azure.mgmt.datafactory.models.SSISExecutionParameter]]
    :param property_overrides: The property overrides to execute the SSIS
     package.
    :type property_overrides: dict[str,
     ~azure.mgmt.datafactory.models.SSISPropertyOverride]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'package_location': {'required': True},
        'connect_via': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'package_location': {'key': 'typeProperties.packageLocation', 'type': 'SSISPackageLocation'},
        'runtime': {'key': 'typeProperties.runtime', 'type': 'object'},
        'logging_level': {'key': 'typeProperties.loggingLevel', 'type': 'object'},
        'environment_path': {'key': 'typeProperties.environmentPath', 'type': 'object'},
        'connect_via': {'key': 'typeProperties.connectVia', 'type': 'IntegrationRuntimeReference'},
        'project_parameters': {'key': 'typeProperties.projectParameters', 'type': '{SSISExecutionParameter}'},
        'package_parameters': {'key': 'typeProperties.packageParameters', 'type': '{SSISExecutionParameter}'},
        'project_connection_managers': {'key': 'typeProperties.projectConnectionManagers', 'type': '{{SSISExecutionParameter}}'},
        'package_connection_managers': {'key': 'typeProperties.packageConnectionManagers', 'type': '{{SSISExecutionParameter}}'},
        'property_overrides': {'key': 'typeProperties.propertyOverrides', 'type': '{SSISPropertyOverride}'},
    }

    def __init__(self, *, name: str, package_location, connect_via, additional_properties=None, description: str=None, depends_on=None, user_properties=None, linked_service_name=None, policy=None, runtime=None, logging_level=None, environment_path=None, project_parameters=None, package_parameters=None, project_connection_managers=None, package_connection_managers=None, property_overrides=None, **kwargs) -> None:
        super(ExecuteSSISPackageActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.package_location = package_location
        self.runtime = runtime
        self.logging_level = logging_level
        self.environment_path = environment_path
        self.connect_via = connect_via
        self.project_parameters = project_parameters
        self.package_parameters = package_parameters
        self.project_connection_managers = project_connection_managers
        self.package_connection_managers = package_connection_managers
        self.property_overrides = property_overrides
        self.type = 'ExecuteSSISPackage'
