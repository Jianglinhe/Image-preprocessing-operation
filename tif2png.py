#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-27 上午10:45
    @Author:      hezhiqiang
    @FileName:    tif2png.py
    @IDE:         PyCharm
    使用PIL库的Image实现图像格式之间的相互转化

"""

import os
import numpy as np
from PIL import Image

def tif2png(path):
    path_list = os.listdir(path)
    for file_name in path_list:
        img_array = np.array(Image.open(path+file_name))
        img = Image.fromarray(img_array)
        img.save(path+file_name.split('.')[0]+".png")

if __name__ == '__main__':
    path = "./DRIVE/val/1st_manual/"
    # path = "./DRIVE/val/images/"
    tif2png(path)





