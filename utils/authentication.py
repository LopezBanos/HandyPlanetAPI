# Copyright 2023 
# Author: Sergio Lopez Banos

""" Module for setting up the required credential from Planet """
from getpass import getpass


def get_credentials():

    """ Get the credential to access the planet API """
    API_KEY = getpass('Enter your API key:')
    return API_KEY

