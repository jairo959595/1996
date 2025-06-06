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

from paapi5_python_sdk.models.single_string_valued_attribute import SingleStringValuedAttribute  # noqa: F401,E501


class Classifications(object):
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
        'binding': 'SingleStringValuedAttribute',
        'product_group': 'SingleStringValuedAttribute'
    }

    attribute_map = {
        'binding': 'Binding',
        'product_group': 'ProductGroup'
    }

    def __init__(self, binding=None, product_group=None):  # noqa: E501
        """Classifications - a model defined in Swagger"""  # noqa: E501

        self._binding = None
        self._product_group = None
        self.discriminator = None

        if binding is not None:
            self.binding = binding
        if product_group is not None:
            self.product_group = product_group

    @property
    def binding(self):
        """Gets the binding of this Classifications.  # noqa: E501


        :return: The binding of this Classifications.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this Classifications.


        :param binding: The binding of this Classifications.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._binding = binding

    @property
    def product_group(self):
        """Gets the product_group of this Classifications.  # noqa: E501


        :return: The product_group of this Classifications.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._product_group

    @product_group.setter
    def product_group(self, product_group):
        """Sets the product_group of this Classifications.


        :param product_group: The product_group of this Classifications.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._product_group = product_group

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
        if issubclass(Classifications, dict):
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
        if not isinstance(other, Classifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
