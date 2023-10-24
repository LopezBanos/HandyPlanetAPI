# Copyright 2023
# Author: Sergio Lopez Banos

""" Custom Filter for eSubstation Project """
def custom_filter():
    data_range_filter = {
            "type"       : "RangeFilter",
            "field_name" : "adquired",
            "config"     :{
                "gte"    : "2018-01-01T00:00:00.000Z",
                "lte"    : "2022-12-31T00:00:00.000Z"
                }
            }

    cloud_cover_filter = {
            "type"       : "RangeFilter",
            "field_name" : "cloud_cover",
            "config"     : {
                "lte"    : 0.05
                }
            }

    off_nadir_angle_filter = {
            "type"          : "RangeFilter",
            "field_name"    : "view_angle",
            "config"        : {
                "gte"       : -0.2,
                "lte"       : 0.2
                }
            }

    standard_quality_filter = {
            "type"        : "StringInFilter",
            "filter_name" : "quality_category",
            "config"      : [
                "standard"
                ]
            }

    permission_filter = {
            "type"   : "PermissionFilter",
            "config" : ["assets:download"]

            }

    satellite_filter = {
            "type"         : "StringInFilter",
            "field_name"   : "satellite_id",
            "config"       : ["SkySatScene"]
            }

    return custom_filter_eSubstation
