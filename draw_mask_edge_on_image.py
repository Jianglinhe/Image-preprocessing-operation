#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-7-14 下午2:56
    @Author:      hezhiqiang
    @FileName:    draw_mask_edge_on_image.py
    @IDE:         PyCharm

    在原始图像上绘制mask的轮廓,注意原始图像要和mask图像大小相同
"""

import numpy as np
import cv2
from skimage import measure


# 单张mask的情况
def draw_mask_edge_on_image_skimage(image, mask, color=(0, 0, 255)):
    coef = 255 if np.max(image) < 3 else 1
    image = (image * coef).astype(np.float32)
    contours = measure.find_contours(mask, 0.5)
    # image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for c in contours:
        c = np.around(c).astype(np.int)
        image[c[:, 0], c[:, 1]] = np.array(color)
    cv2.imwrite('test.png', image)

# 多张mask的情况
def draw_multi_mask_edge_on_image_skimage(image, mask1, mask2, mask3, color1=(0, 0, 255), color2=(0, 255, 0), color3=(0, 255, 255)):

    """
    :param image:原始图像
    :param mask1:分割mask1
    :param mask2:分割mask2
    :param mask3:分割mask3
    :param color1:mask1对应的轮廓
    :param color2:mask2对应的轮廓
    :param color3:mask3对应的轮廓
    :return:
    """
    # coef = 255 if np.max(image) < 3 else 1
    # image = (image * coef).astype(np.float32)

    contours1 = measure.find_contours(mask1, 0.5)
    contours2 = measure.find_contours(mask2, 0.5)
    contours3 = measure.find_contours(mask3, 0.5)


    # image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for c in contours1:
        c = np.around(c).astype(np.int)
        image[c[:, 0], c[:, 1]] = np.array(color1)

    for c in contours2:
        c = np.around(c).astype(np.int)
        image[c[:, 0], c[:, 1]] = np.array(color2)

    for c in contours3:
        c = np.around(c).astype(np.int)
        image[c[:, 0], c[:, 1]] = np.array(color3)

    cv2.imwrite('test.png', image)


path1 = "./1.png"   # 原图
path2 = "./2.png"   # mask1
path3 = "./3.png"   # mask2
path4 = "./4.png"   # Ground Truth

image = cv2.imread(path1)
image = cv2.resize(image, (256, 256))

mask1 = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
mask2 = cv2.imread(path3, cv2.IMREAD_GRAYSCALE)
mask3 = cv2.imread(path4, cv2.IMREAD_GRAYSCALE)
mask3 = cv2.resize(mask3, (256, 256))

draw_multi_mask_edge_on_image_skimage(image, mask1, mask2, mask3)