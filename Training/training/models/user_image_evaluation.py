# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserImageEvaluation(Model):
    """UserImageEvaluation.

    :param image_id:
    :type image_id: str
    :param image_uri:
    :type image_uri: str
    :param image_thumbnail_uri:
    :type image_thumbnail_uri: str
    :param project:
    :type project: str
    :param iteration:
    :type iteration: str
    :param timestamp:
    :type timestamp: datetime
    :param classifications:
    :type classifications: list of :class:`ImageClassEvaluation
     <training.models.ImageClassEvaluation>`
    """

    _attribute_map = {
        'image_id': {'key': 'ImageId', 'type': 'str'},
        'image_uri': {'key': 'ImageUri', 'type': 'str'},
        'image_thumbnail_uri': {'key': 'ImageThumbnailUri', 'type': 'str'},
        'project': {'key': 'Project', 'type': 'str'},
        'iteration': {'key': 'Iteration', 'type': 'str'},
        'timestamp': {'key': 'Timestamp', 'type': 'iso-8601'},
        'classifications': {'key': 'Classifications', 'type': '[ImageClassEvaluation]'},
    }

    def __init__(self, image_id=None, image_uri=None, image_thumbnail_uri=None, project=None, iteration=None, timestamp=None, classifications=None):
        self.image_id = image_id
        self.image_uri = image_uri
        self.image_thumbnail_uri = image_thumbnail_uri
        self.project = project
        self.iteration = iteration
        self.timestamp = timestamp
        self.classifications = classifications
