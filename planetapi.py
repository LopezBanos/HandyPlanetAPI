# Copyright 2023
# Author: Sergio Lopez Banos
import os
import asyncio
from utils.authentication import get_credentials
from utils.directory      import get_item_names, move_item_to_folder
from utils.geometry       import get_rectangle_geometry
from utils.custom_filter  import custom_filter
from utils.request        import handy_order_request, handy_search_request
from planet import Session, OrdersClient, Auth, order_request, reporting

ARCHIVE_TYPE = 'zip'

CURRENT_DIRECTORY = os.getcwd()

# Downloads
DOWNLOAD_DIR = os.path.join(CURRENT_DIRECTORY, 'ZIP')
if not os.path.exists(DOWNLOAD_DIR):
   os.makedirs(DOWNLOAD_DIR)

# Issues
ISSUES  = 'Issues'

# Ordered
ORDERED  = 'Ordered'

# Item Type and Bundle of interest
ITEM_TYPE    = "SkySatScene"
BUNDLE       = "Visual"


# Insert Credentials
API_KEY ='INSERT YOUR API KEY HERE'

# Item Names
item_names = get_item_names()

# Initialize the dictionaries and list
item_ids         = {}
combined_filter  = {}
item_aoi         = {}
delivery_config  = {}
requests         = []

for item_name in item_names:
    try:
        # Set the combined filter for that item
        combined_filter[item_name.replace('.json','')] = custom_filter(item_name)

        # Search for item ids
        item_ids[item_name.replace('.json','')] = handy_search_request(API_KEY,
    	                                        ITEM_TYPE,
    	                                        combined_filter[item_name.replace('.json','')])
        # Drop None/Null ids
        if len(item_ids[item_name.replace('.json','')]) == 0:
            del item_ids[item_name.replace('.json','')]
            del combined_filter[item_name.replace('.json','')]
            # Move item to issues folder
            """ Issue in the order """
            print("Issue on item ", item_name, ". Moving to issues Folder")
            move_item_to_folder(ISSUES, item_name)
        else:
            # Create the area of interest
            item_aoi[item_name.replace('.json','')] = get_rectangle_geometry(item_name)['config']

            # Delivery Configuration
            delivery_config[item_name.replace('.json','')] = order_request.delivery(
                                                    archive_type     = ARCHIVE_TYPE,
                                                    single_archive   = True,
                                                    archive_filename = item_name.replace('.json','.zip'))
            # Activate the request
            requests.append(handy_order_request(
                                request_name = item_name.replace('.json',''),
                                item_type    = ITEM_TYPE,
                                item_ids     = item_ids[item_name.replace('.json','')], # Take just one
                                bundle       = BUNDLE, 
                                delivery     = delivery_config[item_name.replace('.json','')],
                                tools        = [order_request.clip_tool(aoi=item_aoi[item_name.replace('.json','')])]))

            # Move File to ordered folder
            print("Item ", item_name, " ordered. Moving file to ordered Folder" )
            move_item_to_folder(ORDERED, item_name)
    except:
        # Move item to issues folder
        """ Issue in the order """
        print("Issue on item ", item_name, ". Moving to issues Folder")
        move_item_to_folder(ISSUES, item_name)


# Create and download function
async def create_and_download(client, order_detail, directory):
    """Make an order, wait for completion, download files as a single task."""
    with reporting.StateBar(state='creating') as reporter:
        order = await client.create_order(order_detail)
        reporter.update(state='created', order_id=order['id'])
        await client.wait(order['id'], callback=reporter.update_state)

    await client.download_order(order['id'], directory, progress_bar=True)

async def main():
    async with Session(auth = Auth.from_key(API_KEY)) as sess:
        #client = sess.client('orders')
        client = OrdersClient(sess)

        # Create and download the order
        await asyncio.gather(*[
                create_and_download(client, request, DOWNLOAD_DIR)
                for request in requests
            ])



if __name__ == '__main__':
    asyncio.run(main())
