from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.delay_executable import DelayExecutable
from openapi_server.models.ping_executable import PingExecutable
from openapi_server import util


class AbstractExecutable(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, name=None, spec=None):  # noqa: E501
        """AbstractExecutable - a model defined in OpenAPI

        :param type: The type of this AbstractExecutable.  # noqa: E501
        :type type: str
        :param name: The name of this AbstractExecutable.  # noqa: E501
        :type name: str
        :param spec: The spec of this AbstractExecutable.  # noqa: E501
        :type spec: object
        """
        self.openapi_types = {
            'type': str,
            'name': str,
            'spec': object
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'spec': 'spec'
        }

        self._type = type
        self._name = name
        self._spec = spec

    @classmethod
    def from_dict(cls, dikt) -> 'AbstractExecutable':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AbstractExecutable of this AbstractExecutable.  # noqa: E501
        :rtype: AbstractExecutable
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this AbstractExecutable.


        :return: The type of this AbstractExecutable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this AbstractExecutable.


        :param type: The type of this AbstractExecutable.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self) -> str:
        """Gets the name of this AbstractExecutable.


        :return: The name of this AbstractExecutable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AbstractExecutable.


        :param name: The name of this AbstractExecutable.
        :type name: str
        """

        self._name = name

    @property
    def spec(self) -> object:
        """Gets the spec of this AbstractExecutable.


        :return: The spec of this AbstractExecutable.
        :rtype: object
        """
        return self._spec

    @spec.setter
    def spec(self, spec: object):
        """Sets the spec of this AbstractExecutable.


        :param spec: The spec of this AbstractExecutable.
        :type spec: object
        """

        self._spec = spec