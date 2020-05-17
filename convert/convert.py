import os
import json

coco = dict()
coco['images'] = []
coco['type'] = 'instances'
coco['annotations'] = []
coco['categories'] = []

category_set = dict()
image_set = set()

category_item_id = -1
image_id = 20180000000
annotation_id = 0

with open('ann.txt','r') as f:
    anns=f.readlines()
    for ann in anns:
        ann=ann.split()
        file_name=ann[0]


        bndbox = dict()
        size = dict()
        current_image_id = None
        current_category_id = None
        size['width'] = None
        size['height'] = None
        size['depth'] = None
        pass
