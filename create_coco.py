import json
import numpy as np
import shutil
import cv2
import os

def select(json_path, outpath, image_path):
    json_file = open(json_path,'r')
    infos = json.load(json_file)
    images = infos["images"]
    annos = infos["annotations"]
    #assert len(images) == len(images)
    print("path:::::::::",os.getcwd())
    for i in range(len(images)):
        im_id = images[i]["id"]
        im_path = image_path + "/" + images[i]["file_path"]
        print(im_path)
        img = cv2.imread(im_path)
        #print(img)
        try:
            print("img_shape:",img.shape)
        except Exception as e:
            print("img_path:",im_path)
            continue
        for j in range(len(annos)):
            if annos[j]["image_id"] == im_id:
                try:
                    x, y, w, h = annos[j]["bbox"]
                except Exception as e:
                    print("error:",e)
                    continue
                x, y, w, h = int(x), int(y), int(w), int(h)
                x2, y2 = x + w, y + h
                print("x:",x,y,w,h)
                # object_name = annos[j][""]
                cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), thickness=2)
                #img_name = outpath + "/" + images[i]["file_path"]
                img_name = "{}/{}".format(outpath,images[i]["file_path"])
                print("img_name;",img_name)
                cv2.imwrite(img_name, img)
                #cv2.imshow("img",img)
                #cv2.waitKeyEx(0)
                # continue
        
        print('exit.',i)
        break
#         print(i)

if __name__ == "__main__":
    json_path = r"./validation.json"#放标注json的地址 #"../SD/dataset/images/validation.json"#
    out_path = r"./result"#结果放的地址
    image_path = r"./validation"#原图的地址
    select(json_path, out_path, image_path)
