# Copyright 2023
# Author: Sergio Lopez Banos

import json

""" Module to workaround geometry json"""
def get_geometry(item_name):
    """ Get the type and coordinates of a json file """
    # Open json
    json_file = open(item_name)

    # Return json object as a dictionary
    json_dict = json.load(json_file)

    geometry_filter = json_dict["geometry"]
    return geometry_filter

