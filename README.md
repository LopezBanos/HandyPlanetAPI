# Introdution
## What is Planet Python API?
Planet Python API script to access data of Planet satellites given a custom filter up to some geometry files stored in .json downloaded from OpenStreetMap.

## Handy Script comes to save time
The reason to pusblish this script is simple, it saves a lot of time if you want to download a set of images given a filter up to some AOI (Area of Interest) stored in a `.json` file. Precisely, the `.json` files on the test case come from OpenStreetMap.

# Installation
To download the script just clone the repository 
```bash
git clone https://github.com/LopezBanos/HandyPlanetAPI.git
```
To install the required packages 
```bash
pip install -r requirements.txt
```
The **Planet Python API version is 2.1.1**
# Usage
Copy the files `__init__.py`, `planetapi.py` and `utils` folder into the folder where your `.json` are stored, **src** directory. The tree folder have to look similiar to
```bash
├── src
│   ├── utils
│   │   ├── authentication.py
│   │   ├── custom_filter.py
│   │   ├── directory.py
│   │   ├── geometry.py
│   │   └── request.py
│   ├── __init__.py
│   ├── planetapi.py
│   └── **.json
```
where `**.json` represents all the `.json` in the **src** folder. 
### Inserting Credentials
1. On your planet account you can find a token in the settings menu. <br> 
2. Open `planetapi.py`.
3. Copy and paste that token in `API_KEY ='INSERT YOUR API KEY HERE'` in the `planetapi.py` script.

### Modifying the custom filter
The `utils/custom_filter.py` use the new style of creating filters (`and_filter`. `range_filter`, `date_range_filter` and `string_in_filter`) with a geometry filter that is generated with the `.json` files that come from OpenStreetMap. <br><br>
**Warning:** *If your `.json` files do not come from OSM they might have other formatting and you must do some workaround it.*
### Handy Search and Order Request
Inside the `utils/request.py` there are two main functions. 
#### Handy Search Request
This function returns the *items_ids* that match our filter and AOI.
```python
handy_search_request(API_KEY, ITEM_TYPES, filter):
```
- **API_KEY:** Account Token from Planet Website.
- **ITEM_TYPE:** Collection or Scene from Planet where we want to get the images from. 
- **filter:** Custom filter created with `custom_filter.py`. <br>


#### Handy Order Request
This function activate and build the request. In other words it create a dictionary that keeps every *item_ids* we are interested in and the AOI of interest of that *item_id* image. 
```python
handy_order_request(request_name, 
                    item_type, 
                    item_ids, 
                    bundle, 
                    delivery, 
                    tools):
```

- **request_name:** The name which is going to appear in the Planet website.
- **item_ids:** The item_ids we got in the search request. 
- **bundle:** Choose among the bundle Planet offers.
- **delivery:** In case you want to download the assets automatically, you can modify the delivery dictionary. Currently the images are downloaded and stored as `.zip` files.
- **tools:** Clip to AOI tool so that we get just the area we are interested in. <br><br>
**Warning:** *The clipping tool gives a true output if the area intersect with our item_id image, in other words, you may get just a single pixel and not the whole area of coverage. The reason behind this is that is not implemented yet in the Python Planet API.*
### Issues and Ordered Folders
When downloading and requesting images in the Planet API, it is common to find an exception either because the image for that AOI is not available with the given filter or the `.json` geometry file is corrupted (having just a single point instead of an area). For large data pipelines this can be a problem since it will stop the workflow. One must use a `try` and `except` block to deal with the issues.  

The `utils/directory.py` move those files that produce issues to the `Issues` folder and the ones that are requested to the `Ordered` folder. In case the folder are not in the current directory it will create them. 

