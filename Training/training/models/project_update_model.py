# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProjectUpdateModel(Model):
    """Project update model to be sent as JSON.

    :param name: Gets or sets the name database property
    :type name: str
    :param description: Gets or sets the description database property
    :type description: str
    :param settings: Gets or sets the project settings
    :type settings: :class:`ProjectSettings <training.models.ProjectSettings>`
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'settings': {'key': 'Settings', 'type': 'ProjectSettings'},
    }

    def __init__(self, name=None, description=None, settings=None):
        self.name = name
        self.description = description
        self.settings = settings
