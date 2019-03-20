import xml.etree.ElementTree as ET
import os

'''
    python解析xml文件
'''


# 用于给类定下标，从0开始
VOC_CLASSES = (
    'aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')

# 解析PASCAL　VOC数据集的xnl文件
def parse_rec(filename):

    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)       # 调用parse返回解析树
    objects = []
    for obj in tree.findall('object'):          # 找到所有的object
        obj_struct = {}                         # 创建一个空列表
        difficult = int(obj.find('difficult').text)
        if difficult == 1:
            # print(filename)
            continue
        obj_struct['name'] = obj.find('name').text      # 获取类别名
        bbox = obj.find('bndbox')                       # 找到边界框的信息
        obj_struct['bbox'] = [int(float(bbox.find('xmin').text)),
                              int(float(bbox.find('ymin').text)),
                              int(float(bbox.find('xmax').text)),
                              int(float(bbox.find('ymax').text))]
        objects.append(obj_struct)

    return objects



txt_file = open('my_voc2007.txt', 'w')
# test_file = open('voc07testimg.txt', 'r')
#
# lines = test_file.readlines()
# lines = [x[:-1] for x in lines]
# print(lines)



Annotations = '/mnt/sda1/hzq/VOC2007/Annotations/'
xml_files = os.listdir(Annotations)

count = 0       # 计数
for xml_file in xml_files:
    count += 1
    # if xml_file.split('.')[0] not in lines:     # 找在test_file里的
    #     # print(xml_file.split('.')[0])
    #     continue
    image_path = xml_file.split('.')[0] + '.jpg'
    results = parse_rec(Annotations + xml_file)

    if len(results) == 0:
        print(xml_file)
        continue
    txt_file.write(image_path)
    # num_obj = len(results)
    # txt_file.write(str(num_obj)+' ')
    for result in results:
        class_name = result['name']
        bbox = result['bbox']
        class_name = VOC_CLASSES.index(class_name)   # 返回类的下标
        txt_file.write(' '+str(bbox[0])+' '+str(bbox[1])+' '+str(bbox[2])+' '+str(bbox[3])+' '+str(class_name))
    txt_file.write('\n')

    #if count == 10:
    #    break

txt_file.close()
