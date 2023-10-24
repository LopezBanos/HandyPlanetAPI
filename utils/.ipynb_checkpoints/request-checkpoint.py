# Copyright 2023
# Author: Sergio Lopez Banos

from planet import order_request

""" Module for handling request to planet API"""

def handy_order_request(request_name, item_type, item_ids, bundle, filters):
    """ Request the Order """
    product = [order_request.product(item_ids, bundle, item_type)]
    request  = order_request.build_request(name     = request_name,
                                          products  = product,
                                          tools     = filters)

    return request



