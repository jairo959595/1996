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

from paapi5_python_sdk.models.offer_listing import OfferListing  # noqa: F401,E501
from paapi5_python_sdk.models.offer_summary import OfferSummary  # noqa: F401,E501


class Offers(object):
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
        'listings': 'list[OfferListing]',
        'summaries': 'list[OfferSummary]'
    }

    attribute_map = {
        'listings': 'Listings',
        'summaries': 'Summaries'
    }

    def __init__(self, listings=None, summaries=None):  # noqa: E501
        """Offers - a model defined in Swagger"""  # noqa: E501

        self._listings = None
        self._summaries = None
        self.discriminator = None

        if listings is not None:
            self.listings = listings
        if summaries is not None:
            self.summaries = summaries

    @property
    def listings(self):
        """Gets the listings of this Offers.  # noqa: E501


        :return: The listings of this Offers.  # noqa: E501
        :rtype: list[OfferListing]
        """
        return self._listings

    @listings.setter
    def listings(self, listings):
        """Sets the listings of this Offers.


        :param listings: The listings of this Offers.  # noqa: E501
        :type: list[OfferListing]
        """

        self._listings = listings

    @property
    def summaries(self):
        """Gets the summaries of this Offers.  # noqa: E501


        :return: The summaries of this Offers.  # noqa: E501
        :rtype: list[OfferSummary]
        """
        return self._summaries

    @summaries.setter
    def summaries(self, summaries):
        """Sets the summaries of this Offers.


        :param summaries: The summaries of this Offers.  # noqa: E501
        :type: list[OfferSummary]
        """

        self._summaries = summaries

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
        if issubclass(Offers, dict):
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
        if not isinstance(other, Offers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
