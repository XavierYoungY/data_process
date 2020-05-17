import os
import json
import cv2

img_folder = '/media/yy/datasets/jd/allpic/'

all_anns = {}
count=0
with open('convert/ann.txt', 'r') as f:
    anns = f.readlines()
    for ann in anns:
        count+=1
        print(count)
        ann = ann.split()
        file_name = ann[0]
        img_path = img_folder + file_name
        try:
            img = cv2.imread(img_path)
            height, width, _ = img.shape
            all_anns[file_name]={}
            all_anns[file_name]['img_size']={}
            all_anns[file_name]['img_size']['height']=height
            all_anns[file_name]['img_size']['width'] = width
            all_anns[file_name]['bboxes']=[]
            bboxes=ann[1:]
            for i in range(len(bboxes) // 5):
                box=bboxes[5*i:5*i+5]
                all_anns[file_name]['bboxes'].append(box)

        except:
            print(file_name+' does not exit!----------')

with open('ann.json','w') as f:
    json.dump(all_anns,f)
