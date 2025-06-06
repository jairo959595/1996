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

from paapi5_python_sdk.models.condition import Condition  # noqa: F401,E501
from paapi5_python_sdk.models.get_items_resource import GetItemsResource  # noqa: F401,E501
from paapi5_python_sdk.models.item_id_type import ItemIdType  # noqa: F401,E501
from paapi5_python_sdk.models.merchant import Merchant  # noqa: F401,E501
from paapi5_python_sdk.models.offer_count import OfferCount  # noqa: F401,E501
from paapi5_python_sdk.models.partner_type import PartnerType  # noqa: F401,E501
from paapi5_python_sdk.models.properties import Properties  # noqa: F401,E501


class GetItemsRequest(object):
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
        'condition': 'Condition',
        'currency_of_preference': 'str',
        'item_ids': 'list[str]',
        'item_id_type': 'ItemIdType',
        'languages_of_preference': 'list[str]',
        'marketplace': 'str',
        'merchant': 'Merchant',
        'offer_count': 'OfferCount',
        'partner_tag': 'str',
        'partner_type': 'PartnerType',
        'properties': 'Properties',
        'resources': 'list[GetItemsResource]'
    }

    attribute_map = {
        'condition': 'Condition',
        'currency_of_preference': 'CurrencyOfPreference',
        'item_ids': 'ItemIds',
        'item_id_type': 'ItemIdType',
        'languages_of_preference': 'LanguagesOfPreference',
        'marketplace': 'Marketplace',
        'merchant': 'Merchant',
        'offer_count': 'OfferCount',
        'partner_tag': 'PartnerTag',
        'partner_type': 'PartnerType',
        'properties': 'Properties',
        'resources': 'Resources'
    }

    def __init__(self, condition=None, currency_of_preference=None, item_ids=None, item_id_type=None, languages_of_preference=None, marketplace=None, merchant=None, offer_count=None, partner_tag=None, partner_type=None, properties=None, resources=None):  # noqa: E501
        """GetItemsRequest - a model defined in Swagger"""  # noqa: E501

        self._condition = None
        self._currency_of_preference = None
        self._item_ids = None
        self._item_id_type = None
        self._languages_of_preference = None
        self._marketplace = None
        self._merchant = None
        self._offer_count = None
        self._partner_tag = None
        self._partner_type = None
        self._properties = None
        self._resources = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if currency_of_preference is not None:
            self.currency_of_preference = currency_of_preference
        self.item_ids = item_ids
        if item_id_type is not None:
            self.item_id_type = item_id_type
        if languages_of_preference is not None:
            self.languages_of_preference = languages_of_preference
        if marketplace is not None:
            self.marketplace = marketplace
        if merchant is not None:
            self.merchant = merchant
        if offer_count is not None:
            self.offer_count = offer_count
        self.partner_tag = partner_tag
        self.partner_type = partner_type
        if properties is not None:
            self.properties = properties
        if resources is not None:
            self.resources = resources

    @property
    def condition(self):
        """Gets the condition of this GetItemsRequest.  # noqa: E501


        :return: The condition of this GetItemsRequest.  # noqa: E501
        :rtype: Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this GetItemsRequest.


        :param condition: The condition of this GetItemsRequest.  # noqa: E501
        :type: Condition
        """

        self._condition = condition

    @property
    def currency_of_preference(self):
        """Gets the currency_of_preference of this GetItemsRequest.  # noqa: E501


        :return: The currency_of_preference of this GetItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_of_preference

    @currency_of_preference.setter
    def currency_of_preference(self, currency_of_preference):
        """Sets the currency_of_preference of this GetItemsRequest.


        :param currency_of_preference: The currency_of_preference of this GetItemsRequest.  # noqa: E501
        :type: str
        """

        self._currency_of_preference = currency_of_preference

    @property
    def item_ids(self):
        """Gets the item_ids of this GetItemsRequest.  # noqa: E501


        :return: The item_ids of this GetItemsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this GetItemsRequest.


        :param item_ids: The item_ids of this GetItemsRequest.  # noqa: E501
        :type: list[str]
        """
        if item_ids is None:
            raise ValueError("Invalid value for `item_ids`, must not be `None`")  # noqa: E501

        self._item_ids = item_ids

    @property
    def item_id_type(self):
        """Gets the item_id_type of this GetItemsRequest.  # noqa: E501


        :return: The item_id_type of this GetItemsRequest.  # noqa: E501
        :rtype: ItemIdType
        """
        return self._item_id_type

    @item_id_type.setter
    def item_id_type(self, item_id_type):
        """Sets the item_id_type of this GetItemsRequest.


        :param item_id_type: The item_id_type of this GetItemsRequest.  # noqa: E501
        :type: ItemIdType
        """

        self._item_id_type = item_id_type

    @property
    def languages_of_preference(self):
        """Gets the languages_of_preference of this GetItemsRequest.  # noqa: E501


        :return: The languages_of_preference of this GetItemsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages_of_preference

    @languages_of_preference.setter
    def languages_of_preference(self, languages_of_preference):
        """Sets the languages_of_preference of this GetItemsRequest.


        :param languages_of_preference: The languages_of_preference of this GetItemsRequest.  # noqa: E501
        :type: list[str]
        """

        self._languages_of_preference = languages_of_preference

    @property
    def marketplace(self):
        """Gets the marketplace of this GetItemsRequest.  # noqa: E501


        :return: The marketplace of this GetItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._marketplace

    @marketplace.setter
    def marketplace(self, marketplace):
        """Sets the marketplace of this GetItemsRequest.


        :param marketplace: The marketplace of this GetItemsRequest.  # noqa: E501
        :type: str
        """

        self._marketplace = marketplace

    @property
    def merchant(self):
        """Gets the merchant of this GetItemsRequest.  # noqa: E501


        :return: The merchant of this GetItemsRequest.  # noqa: E501
        :rtype: Merchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this GetItemsRequest.


        :param merchant: The merchant of this GetItemsRequest.  # noqa: E501
        :type: Merchant
        """

        self._merchant = merchant

    @property
    def offer_count(self):
        """Gets the offer_count of this GetItemsRequest.  # noqa: E501


        :return: The offer_count of this GetItemsRequest.  # noqa: E501
        :rtype: OfferCount
        """
        return self._offer_count

    @offer_count.setter
    def offer_count(self, offer_count):
        """Sets the offer_count of this GetItemsRequest.


        :param offer_count: The offer_count of this GetItemsRequest.  # noqa: E501
        :type: OfferCount
        """

        self._offer_count = offer_count

    @property
    def partner_tag(self):
        """Gets the partner_tag of this GetItemsRequest.  # noqa: E501


        :return: The partner_tag of this GetItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._partner_tag

    @partner_tag.setter
    def partner_tag(self, partner_tag):
        """Sets the partner_tag of this GetItemsRequest.


        :param partner_tag: The partner_tag of this GetItemsRequest.  # noqa: E501
        :type: str
        """
        if partner_tag is None:
            raise ValueError("Invalid value for `partner_tag`, must not be `None`")  # noqa: E501

        self._partner_tag = partner_tag

    @property
    def partner_type(self):
        """Gets the partner_type of this GetItemsRequest.  # noqa: E501


        :return: The partner_type of this GetItemsRequest.  # noqa: E501
        :rtype: PartnerType
        """
        return self._partner_type

    @partner_type.setter
    def partner_type(self, partner_type):
        """Sets the partner_type of this GetItemsRequest.


        :param partner_type: The partner_type of this GetItemsRequest.  # noqa: E501
        :type: PartnerType
        """
        if partner_type is None:
            raise ValueError("Invalid value for `partner_type`, must not be `None`")  # noqa: E501

        self._partner_type = partner_type

    @property
    def properties(self):
        """Gets the properties of this GetItemsRequest.  # noqa: E501


        :return: The properties of this GetItemsRequest.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GetItemsRequest.


        :param properties: The properties of this GetItemsRequest.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def resources(self):
        """Gets the resources of this GetItemsRequest.  # noqa: E501


        :return: The resources of this GetItemsRequest.  # noqa: E501
        :rtype: list[GetItemsResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this GetItemsRequest.


        :param resources: The resources of this GetItemsRequest.  # noqa: E501
        :type: list[GetItemsResource]
        """

        self._resources = resources

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
        if issubclass(GetItemsRequest, dict):
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
        if not isinstance(other, GetItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
