from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.option_base import OptionBase
from openapi_server import util

from openapi_server.models.option_base import OptionBase  # noqa: E501

class EnumValueOption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, path=None, values=None):  # noqa: E501
        """EnumValueOption - a model defined in OpenAPI

        :param type: The type of this EnumValueOption.  # noqa: E501
        :type type: str
        :param path: The path of this EnumValueOption.  # noqa: E501
        :type path: str
        :param values: The values of this EnumValueOption.  # noqa: E501
        :type values: List[str]
        """
        self.openapi_types = {
            'type': str,
            'path': str,
            'values': List[str]
        }

        self.attribute_map = {
            'type': 'type',
            'path': 'path',
            'values': 'values'
        }

        self._type = type
        self._path = path
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'EnumValueOption':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EnumValueOption of this EnumValueOption.  # noqa: E501
        :rtype: EnumValueOption
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this EnumValueOption.


        :return: The type of this EnumValueOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this EnumValueOption.


        :param type: The type of this EnumValueOption.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def path(self) -> str:
        """Gets the path of this EnumValueOption.

        The target path that the option applies to.   # noqa: E501

        :return: The path of this EnumValueOption.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this EnumValueOption.

        The target path that the option applies to.   # noqa: E501

        :param path: The path of this EnumValueOption.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def values(self) -> List[str]:
        """Gets the values of this EnumValueOption.

        The list of allowed values to use.   # noqa: E501

        :return: The values of this EnumValueOption.
        :rtype: List[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]):
        """Sets the values of this EnumValueOption.

        The list of allowed values to use.   # noqa: E501

        :param values: The values of this EnumValueOption.
        :type values: List[str]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values