# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDeleteController(BaseTestCase):
    """DeleteController integration test stubs"""

    def test_get_delete_path(self):
        """Test case for get_delete_path

        Delete
        """
        query_string = [('query', 'query_example')]
        response = self.client.open(
            '/delete',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
