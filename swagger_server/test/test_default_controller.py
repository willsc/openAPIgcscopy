# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_copy_path(self):
        """Test case for get_copy_path

        path
        """
        query_string = [('copy', 'copy_example')]
        response = self.client.open(
            '/copy',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_path(self):
        """Test case for get_list_path

        list
        """
        query_string = [('query', 'query_example')]
        response = self.client.open(
            '/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
