# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Response
from config.strings import RESPONSE_STRING

try:
    import ujson as json
except Exception as message:
    import json

def resp(error_code=0, results={}, meta={}, lang='en_us', resp_message=''):
    """
    http response code untuk referensi
    Informational 1xx
    Successful 2xx
    Redirection 3xx
    Client Error 4xx
    Server Error 5xx

    :results:       payload kembalian utama, umumnya untuk tempat object yang di-request client
    :meta:          payload tambahan yang diperlukan sebagai pelengkap payload utama
    :lang:          settingan bahasa dari user yang request
    :resp_message:  custom response messsage
    """

    if error_code:
        if error_code in RESPONSE_STRING[lang]:
            results = {}
            if not resp_message:
                resp_message = RESPONSE_STRING[lang][error_code]


        response_dict = {
            "error":{
                "code": error_code,
                "message": resp_message
            }
        }
    else:
        response_dict = {
            "results": results
        }

        if meta:
            response_dict.update({"meta": meta})

    response_data = json.dumps(response_dict)
    return Response(response_data, mimetype='application/json')
