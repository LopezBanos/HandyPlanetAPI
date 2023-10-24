# Copyright 2023
# Author: Sergio Lopez Banos
from datetime  import datetime
from planet    import data_filter
from .geometry import get_rectangle_geometry

""" Custom Filter for eSubstation Project """
def custom_filter(item_name):

    geometry_filter = get_rectangle_geometry(item_name)


    and_filter = data_filter.and_filter([data_filter.permission_filter(),
                                        data_filter.date_range_filter('acquired', gt=datetime(2018,1,1,0), lt=datetime(2022,12,31,0)),
                                        data_filter.range_filter('cloud_cover', lt=0.05),
                                        data_filter.range_filter('view_angle', gt=-30, lt=30),
                                        data_filter.string_in_filter('quality_category',['standard']),
                                        geometry_filter])
    return and_filter
