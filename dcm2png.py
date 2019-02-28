import os
import pydicom
from scipy import misc

# 将dicom格式(.dcm)的数据转化为.png格式
def dcm2png(dcm_path, png_path):
    '''

    :param dcm_path: dcm格式图像所在文件夹目录
    :param png_path: 保存为png格式的文件目录
    :return:
    '''

    path_list = os.listdir(dcm_path)

    # 计数器，记录总共筛选的图像
    count = 0
    for file in path_list:

        # 文件名及后缀
        file_path, file_name = os.path.splitext(file)

        # dicom格式图像的路径
        dcm = dcm_path+file
        # 读取dcm格式图像
        ds = pydicom.read_file(dcm)
        # 提取图像信息
        img_dcm = ds.pixel_array

        # png格式图像的路径
        png = png_path+file_path+".png"
        # 将dcm格式图像保存为png格式
        misc.imsave(png, img_dcm)
        count+=1

    print("convert %d .dcm images to png"%count)



if __name__=="__main__":

    # 参数设置
    dcm_path = "/home/hezhiqiang/桌面/0A5D6760-1730-48DB-A988-FCE0FF1D6C43/"
    png_path = "/home/hezhiqiang/桌面/0A5D6760-1730-48DB-A988-FCE0FF1D6C43_png/"

    # 进行转换
    dcm2png(dcm_path, png_path)







