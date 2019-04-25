"""
ElementTree生来就是位处理xml,在Python标准库中有两种实现:
1.一种是纯Python实现,xml.etree.ElementTree
2.另一种速度快一点,xml.etree.cElementTree
注意：尽量使用层c语言实现的那种，速度更快，而且消耗的内存更少

常用方法：
    1.获取属性值时，用attrib方法
    2.获取节点值时，用txt方法
    3.获取节点名时，用tag方法

"""

import xml.etree.ElementTree as ET
import os

# 目标检测的xml文件转换
def annotation(xml_path="VOCdevkit/VOC2007/Annotations/", txt_path="train.txt"):
    '''

    :param xml_path:xml文件所在的目录
    :param txt_path:保存的txt文件
    :return:
    '''

    # 所有的类别
    classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat",
               "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person",
               "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    # 获取所有的xml文件的路径
    path_list = os.listdir(xml_path)

    # 打开txt文件
    txt_file = open(txt_path, 'w')

    # 获取当前文件坐在路径
    wd = os.getcwd()


    count = 0
    # 遍历所有的xml文件
    for path in path_list:

        # 获取img的id
        img_id = os.path.splitext(path)[0]
        # 将图像的id写入txt(要获取图片所在的位置)
        txt_file.write('%s/VOCdevkit/VOC2007/JPEGImages/%s.jpg' % (wd, img_id))

        # 调用parse()方法，返回解析树arse()方法，返回解析树
        tree = ET.parse(xml_path+path)

        # 获取根节点
        root = tree.getroot()
        # print(root)

        # iter遍历所有的'object'标签, find查找第一个匹配的子元素
        for obj in root.iter('object'):
            cls = obj.find('name').text     # 获取name节点的值
            difficult = obj.find('difficult').text   # 获取diffiuclt节点的值
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)     # 类别标签

            xml_box = obj.find('bndbox')    # 找到边界框的4个值
            b = (int(xml_box.find('xmin').text), int(xml_box.find('ymin').text), int(xml_box.find('xmax').text), int(xml_box.find('ymax').text))
            # 将边界框写入txt
            txt_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

        # 处理玩一个xml,换行
        txt_file.write('\n')

        count += 1
        print("finish %d xml" % count)

    txt_file.close()    # 关闭文件
    print("finish")

if __name__=="__main__":
    annotation()