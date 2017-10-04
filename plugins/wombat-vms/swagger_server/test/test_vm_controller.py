# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.vm import VM
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVmController(BaseTestCase):
    """ VmController integration test stubs """

    def test_add_pet(self):
        """
        Test case for add_pet

        Creates a new VM
        """
        vm = VM()
        response = self.client.open('/v1/vm',
                                    method='POST',
                                    data=json.dumps(vm),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
