# -*- coding: utf-8 -*-
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
import json

from odoo.tests.common import HttpCase, PORT
from bravado_core.spec import Spec
from swagger_spec_validator.common import SwaggerValidationError


class TestJsonSpec(HttpCase):
    at_install = True
    post_install = True

    # def setUp(self):
    #     super(TestJsonSpec, self).setUp()
    #     self.opener.addheaders.append(("content-type", "application/json"))

    def test_json_base(self):

        resp = self.url_open("http://localhost:%d/api/v1/demo/swagger.json?token=demo_token&download" % PORT,
                             timeout=30)
        self.assertEqual(resp.getcode(), 200, 'Cannot get json spec')
        # TODO add checking  actual content of the json

    def test_OAS_scheme_for_demo_data_is_valid(self):
        resp = self.url_open("http://localhost:%d/api/v1/demo/swagger.json?token=demo_token&download" % PORT,
                             timeout=30)
        spec_dict = json.loads(resp.read())
        try:
            Spec.from_dict(spec_dict, config={'validate_swagger_spec': True})
        except SwaggerValidationError as e:
            self.fail('A JSON Schema for Swagger 2.0 is not valid:\n %s' % e)
