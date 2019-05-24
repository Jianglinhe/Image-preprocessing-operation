#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-5-24 上午10:44
    @Author:      hezhiqiang
    @FileName:    get_figure.py
    @IDE:         PyCharm
"""

import cv2

path = "/mnt/sda1/hzq/a.mp4"
save_path = "figures/"

def get_figure_from_video(path, save_path):

    """
    视频抽取图片
    :param path:视频文件的路径
    :param save_path:保存图像的路径
    :return:
    """

    cap = cv2.VideoCapture(path)
    success, frame = cap.read()

    index = 0   # 记录图片的张数
    while success:
        index += 1

        cv2.imwrite(save_path + str(index) + ".png", frame)

        # if index > 30:
        #     break

        success, frame = cap.read()

    cap.release()

    print("共%d张图像" % index)