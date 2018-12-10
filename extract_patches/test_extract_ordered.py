import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
'''
    测试顺序取patches的函数：
        将取的patches拼接起来进行显示
'''

img_patches = np.load("img_ordered_patches.npy")
mask_patches = np.load("mask_ordered_patches.npy")

# 测试代码用的图有14*11个patch块
img = np.zeros((256*14, 256*11, 3))
mask = np.zeros((256*14, 256*11))


plt.figure()
t = 0
for i in range(14):
    for j in range(11):
        img[256*i:256*i+256, 256*j:256*j+256, :] = img_patches[t]
        t = t + 1

plt.imshow(img, cmap='gray')
plt.show()


plt.figure()
t = 0
for i in range(14):
    for j in range(11):
        mask[256*i:256*i+256, 256*j:256*j+256] = mask_patches[t]
        t = t + 1

print(mask.shape)
plt.imshow(mask, cmap='gray')
plt.show()
