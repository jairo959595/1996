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

from paapi5_python_sdk.models.duration_price import DurationPrice  # noqa: F401,E501
from paapi5_python_sdk.models.offer_availability import OfferAvailability  # noqa: F401,E501
from paapi5_python_sdk.models.offer_condition import OfferCondition  # noqa: F401,E501
from paapi5_python_sdk.models.offer_delivery_info import OfferDeliveryInfo  # noqa: F401,E501
from paapi5_python_sdk.models.offer_merchant_info import OfferMerchantInfo  # noqa: F401,E501


class RentalOfferListing(object):
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
        'availability': 'OfferAvailability',
        'base_price': 'DurationPrice',
        'condition': 'OfferCondition',
        'delivery_info': 'OfferDeliveryInfo',
        'id': 'str',
        'merchant_info': 'OfferMerchantInfo'
    }

    attribute_map = {
        'availability': 'Availability',
        'base_price': 'BasePrice',
        'condition': 'Condition',
        'delivery_info': 'DeliveryInfo',
        'id': 'Id',
        'merchant_info': 'MerchantInfo'
    }

    def __init__(self, availability=None, base_price=None, condition=None, delivery_info=None, id=None, merchant_info=None):  # noqa: E501
        """RentalOfferListing - a model defined in Swagger"""  # noqa: E501

        self._availability = None
        self._base_price = None
        self._condition = None
        self._delivery_info = None
        self._id = None
        self._merchant_info = None
        self.discriminator = None

        if availability is not None:
            self.availability = availability
        if base_price is not None:
            self.base_price = base_price
        if condition is not None:
            self.condition = condition
        if delivery_info is not None:
            self.delivery_info = delivery_info
        if id is not None:
            self.id = id
        if merchant_info is not None:
            self.merchant_info = merchant_info

    @property
    def availability(self):
        """Gets the availability of this RentalOfferListing.  # noqa: E501


        :return: The availability of this RentalOfferListing.  # noqa: E501
        :rtype: OfferAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this RentalOfferListing.


        :param availability: The availability of this RentalOfferListing.  # noqa: E501
        :type: OfferAvailability
        """

        self._availability = availability

    @property
    def base_price(self):
        """Gets the base_price of this RentalOfferListing.  # noqa: E501


        :return: The base_price of this RentalOfferListing.  # noqa: E501
        :rtype: DurationPrice
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this RentalOfferListing.


        :param base_price: The base_price of this RentalOfferListing.  # noqa: E501
        :type: DurationPrice
        """

        self._base_price = base_price

    @property
    def condition(self):
        """Gets the condition of this RentalOfferListing.  # noqa: E501


        :return: The condition of this RentalOfferListing.  # noqa: E501
        :rtype: OfferCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this RentalOfferListing.


        :param condition: The condition of this RentalOfferListing.  # noqa: E501
        :type: OfferCondition
        """

        self._condition = condition

    @property
    def delivery_info(self):
        """Gets the delivery_info of this RentalOfferListing.  # noqa: E501


        :return: The delivery_info of this RentalOfferListing.  # noqa: E501
        :rtype: OfferDeliveryInfo
        """
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, delivery_info):
        """Sets the delivery_info of this RentalOfferListing.


        :param delivery_info: The delivery_info of this RentalOfferListing.  # noqa: E501
        :type: OfferDeliveryInfo
        """

        self._delivery_info = delivery_info

    @property
    def id(self):
        """Gets the id of this RentalOfferListing.  # noqa: E501


        :return: The id of this RentalOfferListing.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RentalOfferListing.


        :param id: The id of this RentalOfferListing.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def merchant_info(self):
        """Gets the merchant_info of this RentalOfferListing.  # noqa: E501


        :return: The merchant_info of this RentalOfferListing.  # noqa: E501
        :rtype: OfferMerchantInfo
        """
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, merchant_info):
        """Sets the merchant_info of this RentalOfferListing.


        :param merchant_info: The merchant_info of this RentalOfferListing.  # noqa: E501
        :type: OfferMerchantInfo
        """

        self._merchant_info = merchant_info

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
        if issubclass(RentalOfferListing, dict):
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
        if not isinstance(other, RentalOfferListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
