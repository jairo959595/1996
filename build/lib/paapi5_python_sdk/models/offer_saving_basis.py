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

from paapi5_python_sdk.models.money import Money  # noqa: F401,E501
from paapi5_python_sdk.models.saving_basis_type import SavingBasisType  # noqa: F401,E501


class OfferSavingBasis(object):
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
        'money': 'Money',
        'saving_basis_type': 'SavingBasisType',
        'saving_basis_type_label': 'str'
    }

    attribute_map = {
        'money': 'Money',
        'saving_basis_type': 'SavingBasisType',
        'saving_basis_type_label': 'SavingBasisTypeLabel'
    }

    def __init__(self, money=None, saving_basis_type=None, saving_basis_type_label=None):  # noqa: E501
        """OfferSavingBasis - a model defined in Swagger"""  # noqa: E501

        self._money = None
        self._saving_basis_type = None
        self._saving_basis_type_label = None
        self.discriminator = None

        if money is not None:
            self.money = money
        if saving_basis_type is not None:
            self.saving_basis_type = saving_basis_type
        if saving_basis_type_label is not None:
            self.saving_basis_type_label = saving_basis_type_label

    @property
    def money(self):
        """Gets the money of this OfferSavingBasis.  # noqa: E501


        :return: The money of this OfferSavingBasis.  # noqa: E501
        :rtype: Money
        """
        return self._money

    @money.setter
    def money(self, money):
        """Sets the money of this OfferSavingBasis.


        :param money: The money of this OfferSavingBasis.  # noqa: E501
        :type: Money
        """

        self._money = money

    @property
    def saving_basis_type(self):
        """Gets the saving_basis_type of this OfferSavingBasis.  # noqa: E501


        :return: The saving_basis_type of this OfferSavingBasis.  # noqa: E501
        :rtype: SavingBasisType
        """
        return self._saving_basis_type

    @saving_basis_type.setter
    def saving_basis_type(self, saving_basis_type):
        """Sets the saving_basis_type of this OfferSavingBasis.


        :param saving_basis_type: The saving_basis_type of this OfferSavingBasis.  # noqa: E501
        :type: SavingBasisType
        """

        self._saving_basis_type = saving_basis_type

    @property
    def saving_basis_type_label(self):
        """Gets the saving_basis_type_label of this OfferSavingBasis.  # noqa: E501


        :return: The saving_basis_type_label of this OfferSavingBasis.  # noqa: E501
        :rtype: str
        """
        return self._saving_basis_type_label

    @saving_basis_type_label.setter
    def saving_basis_type_label(self, saving_basis_type_label):
        """Sets the saving_basis_type_label of this OfferSavingBasis.


        :param saving_basis_type_label: The saving_basis_type_label of this OfferSavingBasis.  # noqa: E501
        :type: str
        """

        self._saving_basis_type_label = saving_basis_type_label

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
        if issubclass(OfferSavingBasis, dict):
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
        if not isinstance(other, OfferSavingBasis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
