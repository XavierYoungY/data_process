
import os
import json
import copy
import random

def pick_ann(anns,ids):
    ann_id=copy.deepcopy(anns)
    # 先清除名字‘images’
    images=ann_id['images']
    images_copy=copy.deepcopy(images)
    for img in images_copy:
        id_=img['id']
        if id_ not in ids:
            images.remove(img)
    ann_id['images']=images
    
    #delete annotations
    annotations=ann_id['annotations']
    annotations_copy=copy.deepcopy(annotations)
    for ann in annotations_copy:
        id_=ann['image_id']
        if id_ not in ids:
            annotations.remove(ann)
    ann_id['annotations']=annotations
            
    return ann_id

        

with open('jd.json','r') as f:
    anns=json.load(f)
    all_images=anns['images']
    all_ids=[]
    for img in all_images:
        all_ids.append(img['id'])
        
    val_ids=random.sample(all_ids,int(len(all_ids)*0.1))
    train_ids=list(set(all_ids)-set(val_ids))

    
    val=pick_ann(anns,val_ids)
    train=pick_ann(anns,train_ids)
    test=copy.deepcopy(val)
    
    with open('val.json','w') as f: 
        json.dump(val,f)
        
    with open('train.json','w') as f: 
        json.dump(train,f)
        
    with open('test.json','w') as f: 
        json.dump(test,f)
    pass