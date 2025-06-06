# coding: utf-8

"""
  Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

      http://www.apache.org/licenses/LICENSE-2.0

  or in the "license" file accompanying this file. This file is distributed
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
  express or implied. See the License for the specific language governing
  permissions and limitations under the License.
"""


"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from paapi5_python_sdk.models.unit_based_attribute import UnitBasedAttribute  # noqa: F401,E501


class DimensionBasedAttribute(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'height': 'UnitBasedAttribute',
        'length': 'UnitBasedAttribute',
        'weight': 'UnitBasedAttribute',
        'width': 'UnitBasedAttribute'
    }

    attribute_map = {
        'height': 'Height',
        'length': 'Length',
        'weight': 'Weight',
        'width': 'Width'
    }

    def __init__(self, height=None, length=None, weight=None, width=None):  # noqa: E501
        """DimensionBasedAttribute - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._length = None
        self._weight = None
        self._width = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if weight is not None:
            self.weight = weight
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this DimensionBasedAttribute.  # noqa: E501


        :return: The height of this DimensionBasedAttribute.  # noqa: E501
        :rtype: UnitBasedAttribute
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DimensionBasedAttribute.


        :param height: The height of this DimensionBasedAttribute.  # noqa: E501
        :type: UnitBasedAttribute
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this DimensionBasedAttribute.  # noqa: E501


        :return: The length of this DimensionBasedAttribute.  # noqa: E501
        :rtype: UnitBasedAttribute
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this DimensionBasedAttribute.


        :param length: The length of this DimensionBasedAttribute.  # noqa: E501
        :type: UnitBasedAttribute
        """

        self._length = length

    @property
    def weight(self):
        """Gets the weight of this DimensionBasedAttribute.  # noqa: E501


        :return: The weight of this DimensionBasedAttribute.  # noqa: E501
        :rtype: UnitBasedAttribute
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DimensionBasedAttribute.


        :param weight: The weight of this DimensionBasedAttribute.  # noqa: E501
        :type: UnitBasedAttribute
        """

        self._weight = weight

    @property
    def width(self):
        """Gets the width of this DimensionBasedAttribute.  # noqa: E501


        :return: The width of this DimensionBasedAttribute.  # noqa: E501
        :rtype: UnitBasedAttribute
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DimensionBasedAttribute.


        :param width: The width of this DimensionBasedAttribute.  # noqa: E501
        :type: UnitBasedAttribute
        """

        self._width = width

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DimensionBasedAttribute, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DimensionBasedAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
