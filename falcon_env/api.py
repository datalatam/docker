#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon
import json
import os
 
class diHola:
    def on_get(self, req, resp):
        """Se encarga de solicitudes GET"""
        quote = {
            'mensaje': 'Hola Data Latam!',
            'version': '0.0.4',
            'variable ambiental': os.environ['MI_VARIABLE']
        }

        resp.body = json.dumps(quote)
 
demo = falcon.API()
demo.add_route('/', diHola())
