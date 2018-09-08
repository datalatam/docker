#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon
import json
 
class diHola:
    def on_get(self, req, resp):
        """Se encarga de solicitudes GET"""
        quote = {
            'mensaje': 'Hola Data Latam!',
            'version': '0.0.3'
        }

        resp.body = json.dumps(quote)
 
demo = falcon.API()
demo.add_route('/', diHola())
