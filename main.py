"""
This file contains code for combining all the modules and running the entire
framework
"""

from kg_query.main import RankedList


ranked_list = RankedList()

while True:
    img_path = input(f'Enter image path: ')
    image_list, uris_list = ranked_list.generate_img_results(img_path)
    print(uris_list)
