# Copyright 2023
# Author: Sergio Lopez Banos

import json

""" Module to workaround geometry json and planet filters"""
def get_geometry(item_name):
    """ Get the type and coordinates of a json file """
    # Open json
    json_file = open(item_name)

    # Return json object as a dictionary
    json_dict = json.load(json_file)

    json_geometry = json_dict["geometry"]
    geometry_filter = {
                        "type": "GeometryFilter",
                        "field_name": "geometry",
                        "config": json_geometry
                     }
    return geometry_filter

def get_rectangle_geometry(item_name):
    """ Get a square bounding a given json geometry"""
    # Open json
    json_file = open(item_name)

    # Return json object as a dictionary
    json_dict = json.load(json_file)

    json_geometry = json_dict["geometry"]

    # Get x coordinates
    x = _get_x_coordinates(json_geometry['coordinates'][0])

    # Get y coordinates 
    y = _get_y_coordinates(json_geometry['coordinates'][0])

    # Get maximum and minimum values to produce a rectangle
    x_min, x_max, y_min, y_max = min(x), max(x), min(y), max(y)

    # Modify the coordinates
    json_geometry['coordinates'] = [[[x_min, y_min], [x_min, y_max],
                                     [x_max, y_max], [x_max, y_min],
                                     [x_min, y_min]]] # End where you stated
                                     
    geometry_filter = {
                        "type": "GeometryFilter",
                        "field_name": "geometry",
                        "config": json_geometry
                     }
    return geometry_filter

def _get_x_coordinates(list_points):
    " Get the x-coordinates of a set of points"
    x = []
    for point in list_points:
        x.append(point[0])
    return x
    
def _get_y_coordinates(list_points):
    " Get the y-coordinates of a set of points"
    y = []
    for point in list_points:
        y.append(point[1])
    return y



