import numpy as np
from PIL import Image
import os
import random


# 训练集patch顺序提取函数
def extract_ordered(N_patches_tot=10000, dataset_path="./dataset_path/", patch_h=256, patch_w=256):
    '''

    :param N_patches_tot: 设置一个patch容量(比较大的一个数)
    :param dataset_path: images和masks文件夹所在的路径
    :param patch_h: patch的高度
    :param patch_w: patch的宽度
    :return: 返回两个数组，分别为原图的patches和对应的mask的patches
    '''


    # 构建一个空数组来存储patches(原图和mask的patch)
    img_patches = np.empty((N_patches_tot, patch_h, patch_w, 3))
    mask_patches = np.empty((N_patches_tot, patch_h, patch_w))

    # 原始图像的路径
    imgs_path = dataset_path+"images/"
    path_list = os.listdir(imgs_path)


    # 总patch数的计数器
    iter_tot = 0
    for file in path_list:

        # 原图
        img = np.asarray(Image.open(imgs_path + file))
        img = img/255.

        # 原图对应的mask图
        file_path, file_name = os.path.splitext(file)
        mask_path = dataset_path + "masks/" + file_path + "_hemorrhage_binary.png" # mask图像的路径
        mask = np.asarray(Image.open(mask_path), 'f')

        # 注意mask图已经是二值图像了，不需要在进行二值化处理
        mask = mask/255. # reduce to 0-1 range

        # 输入图像的高度
        img_h = img.shape[0]
        # 输入图像的宽度
        img_w = img.shape[1]

        # 计算一张图在高度上能取的patch数
        N_patches_h = int(img_h/patch_h)
        if img_h % patch_h != 0:
            print("Warning:"+str(N_patches_h)+"patches in height, with about "+str(img_h%patch_h)+" pixels left over")

        # 计算一张图在宽度上能取到的patch数
        N_patches_w = int(img_w / patch_w)
        if img_w % patch_w != 0:
            print("Warning:"+str(N_patches_h)+"patches in width, with about "+str(img_w%patch_w)+" pixels left over")

        # 一张原始图像能取到的patch数为N_patches_h*N_patches_w
        print("number of patches per image:" + str(N_patches_h*N_patches_w))


        for h in range(N_patches_h):
            for w in range(N_patches_w):
                # 原图的patch
                patch1 = img[h*patch_h:(h*patch_h)+patch_h, w*patch_w:(w*patch_w)+patch_w, :]
                img_patches[iter_tot] = patch1
                # mask的patch
                patch2 = mask[h*patch_h:(h*patch_h)+patch_h, w*patch_w:(w*patch_w)+patch_w]
                mask_patches[iter_tot] = patch2

                iter_tot += 1

    img_patches = img_patches[0:iter_tot]
    mask_patches = mask_patches[0:iter_tot]

    # 将顺序生成的patches保存为.npy文件
    np.save(file="img_ordered_patches.npy", arr=img_patches)
    np.save(file="mask_ordered_patches.npy", arr=mask_patches)

    return img_patches, mask_patches



def extract_random(per_patches=20, dataset_path="./dataset_path/", patch_h=256, patch_w=256):
    '''

        :param N_patches: 每张图想要随机获取的patch数
        :param dataset_path: images和masks文件夹所在的路径
        :param patch_h: patch的高度
        :param patch_w: patch的宽度
        :return: 返回两个数组，分别为原图的patches和对应的mask的patches
        '''

    # 原始图像的路径
    imgs_path = dataset_path + "images/"
    path_list = os.listdir(imgs_path)

    # 所有图像总共要取的patch数
    N_patch = per_patches * len(path_list)
    # 构建一个空数组来存储patches(原图和mask的patch)
    img_patches = np.empty((N_patch, patch_h, patch_w, 3))
    mask_patches = np.empty((N_patch, patch_h, patch_w))


    # 图像子块总数计数器
    iter_tot = 0
    for file in path_list:

        # 原图
        img = np.asarray(Image.open(imgs_path + file))
        img = img / 255.

        # 原图对应的mask图
        file_path, file_name = os.path.splitext(file)
        mask_path = dataset_path + "masks/" + file_path + "_hemorrhage_binary.png"  # mask图像的路径
        mask = np.asarray(Image.open(mask_path), 'f')
        # 注意mask图已经是二值图像了，不需要在进行二值化处理
        mask = mask / 255.  # reduce to 0-1 range

        # 输入图像的高度
        img_h = img.shape[0]
        # 输入图像的宽度
        img_w = img.shape[1]

        k = 0  # 每张图像子块计数器
        while k < per_patches:
            # 确定patch块的中心点的范围
            x_center = random.randint(0 + int(patch_w / 2), img_w - int(patch_w / 2))  # 块的中心范围
            # print "x_center " +str(x_center)
            y_center = random.randint(0 + int(patch_h / 2), img_h - int(patch_h / 2))
            # print "y_center " +str(y_center)

            patch1 = img[y_center-int(patch_h/2):y_center+int(patch_h/2), x_center-int(patch_w/2):x_center+int(patch_w/2), :]
            patch2 = mask[y_center-int(patch_h/2):y_center+int(patch_h/2), x_center-int(patch_w/2):x_center+int(patch_w/2)]

            img_patches[iter_tot] = patch1
            mask_patches[iter_tot] = patch2

            k += 1 # 每张原图提取的patch数
            iter_tot += 1 # 总的patch数

    # 将随机生成的patches保存为.npy文件
    np.save(file="img_random_patches.npy", arr=img_patches)
    np.save(file="mask_random_patches.npy", arr=mask_patches)

    return img_patches, mask_patches


if __name__=="__main__":
    extract_ordered()
    extract_random()


