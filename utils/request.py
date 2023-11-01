# Copyright 2023
# Author: Sergio Lopez Banos
import requests
import json
from requests.auth import HTTPBasicAuth
from planet import order_request

""" Module for handling request to planet API"""

def handy_order_request(request_name, item_type, item_ids, bundle, delivery, tools):
    """ Request the Order """

    product         = [order_request.product(item_ids, bundle, item_type)]

    request         = order_request.build_request(name     = request_name.replace('.json',''),
                                                 products  = product,
                                                 delivery  = delivery,
                                                 tools     = tools)

    return request

def handy_search_request(API_KEY, ITEM_TYPE, filter):
    search_request = {
            "item_types" : [ITEM_TYPE],
            "filter"     : filter   
            }

    search_result = requests.post('https://api.planet.com/data/v1/quick-search',
                                    auth=HTTPBasicAuth(API_KEY, ''),
                                    json=search_request)
    geojson = search_result.json()
    image_ids = [feature['id'] for feature in geojson['features']]


    # Take just the last two elements of a list in case it contains multiples ids
    if len(image_ids)>2:
        image_ids = _drop_ids(image_ids)
    return image_ids


def _drop_ids(ids):
    " Return the last two elements of a list "
    return ids[-2:]