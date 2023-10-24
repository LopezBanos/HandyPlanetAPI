# Copyright 2023
# Author: Sergio Lopez Banos

""" Module for working with files and folder (copying/deleting files) """
import os
import shutil

def get_item_names(items=os.listdir):
    """ Get the item names of the current directory """
    item_names = []
    for item in items:
        if "json" in item:
            item_names.append(item)

    return item_names

def move_item_to_folder(new_folder_name, item_name):
    """ Move an item to a given folder """
    current_path   = os.getcwd() + '/' + item_name
    final_directory = os.getcwd() + '/' + new_folder_name

    # Create Folder in case it does not exist
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        
    shutil.move(current_path,
                final_directory + '/' + item_name)
    pass
