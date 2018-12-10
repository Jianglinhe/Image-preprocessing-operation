import numpy as np
import matplotlib.pyplot as plt
'''
    测试随机取patches的函数：
        将取的patches拼接起来进行显示
'''


img_patches = np.load("img_random_patches.npy")
mask_patches = np.load("mask_random_patches.npy")

# 测试代码用的图有40个patch块
img = np.zeros((256*5, 256*8, 3))
mask = np.zeros((256*5, 256*8))


plt.figure()
t = 0
for i in range(5):
    for j in range(8):
        img[256*i:256*i+256, 256*j:256*j+256, :] = img_patches[t]
        t = t + 1

print(img.shape)
plt.imshow(img, cmap='gray')
plt.show()


plt.figure()
t = 0
for i in range(5):
    for j in range(8):
        mask[256*i:256*i+256, 256*j:256*j+256] = mask_patches[t]
        t = t + 1

print(mask.shape)
plt.imshow(mask, cmap='gray')
plt.show()