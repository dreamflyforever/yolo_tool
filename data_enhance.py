# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os.path
import copy
from tqdm import tqdm
import xml.etree.ElementTree as ET

from PIL import Image


def trans_square(image, save_name):
    r"""Open the image using PIL."""
    image = image.convert('RGB')
    w, h = image.size
    background = Image.new('RGB', size=(max(w, h), max(w, h)), color=(255, 255, 255))  # 创建背景图，颜色值为127
    length = int(abs(w - h) // 2)  # 一侧需要填充的长度
    box = (length, 0) if w < h else (0, length)  # 粘贴的位置
    background.paste(image, box)
    print(save_name)
    background.save(save_name, quality=95)
    return background


def salt_and_pepper(src, percetage):
    """椒盐噪声"""
    SP_NoiseImg = src.copy()
    SP_NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(SP_NoiseNum):
        randR = np.random.randint(0, src.shape[0] - 1)
        randG = np.random.randint(0, src.shape[1] - 1)
        randB = np.random.randint(0, 3)
        if np.random.randint(0, 1) == 0:
            SP_NoiseImg[randR, randG, randB] = 0
        else:
            SP_NoiseImg[randR, randG, randB] = 255
    return SP_NoiseImg


def addGaussianNoise(image, percetage):
    """给图片增加高斯噪声"""
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum = int(percetage * image.shape[0] * image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0, h)
        temp_y = np.random.randint(0, w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg


def darker(image, percetage=0.3):
    """降低图片亮度"""
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get darker
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = int(image[xj, xi, 0] * percetage)
            image_copy[xj, xi, 1] = int(image[xj, xi, 1] * percetage)
            image_copy[xj, xi, 2] = int(image[xj, xi, 2] * percetage)
    return image_copy


def brighter(image, percetage=1.5):
    """增加图片亮度"""
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get brighter
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = np.clip(int(image[xj, xi, 0] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 1] = np.clip(int(image[xj, xi, 1] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 2] = np.clip(int(image[xj, xi, 2] * percetage), a_max=255, a_min=0)
    return image_copy


def rotate(image, angle, center=None, scale=1.0):
    """生成旋转图片"""
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the rotation center
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))
    return rotated


def flip(image):
    """生成翻转图片"""
    flipped_image = np.fliplr(image)
    return flipped_image


def run(file_dir):
    # # 图片文件夹路径
    # file_dir = '../data/meishigewen-img/'

    for img_name in tqdm(os.listdir(file_dir)):
        image = Image.open(file_dir + img_name)
        if image.size[0] != image.size[1]:
            trans_square(image, file_dir + img_name)

    #for img_name in tqdm(os.listdir(file_dir)):
    #    img_path = file_dir + img_name
    #    img = cv2.imread(img_path)
    #    rotated_90 = rotate(img, 90)
    #    cv2.imwrite(file_dir + img_name[0:-4] + '_r90.jpg', rotated_90)

    #    rotated_180 = rotate(img, 180)
    #    cv2.imwrite(file_dir + img_name[0:-4] + '_r180.jpg', rotated_180)

    #    flipped_img = flip(img)
    #    cv2.imwrite(file_dir + img_name[0:-4] + '_fli.jpg', flipped_img)

    for img_name in tqdm(os.listdir(file_dir)):
        img_path = file_dir + img_name
        img = cv2.imread(img_path)

        img_gauss = addGaussianNoise(img, 0.3)
        cv2.imwrite(file_dir + img_name[0:-4] + '_noise.jpg', img_gauss)

        img_darker = darker(img)
        cv2.imwrite(file_dir + img_name[0:-4] + '_darker.jpg', img_darker)

        img_brighter = brighter(img)
        cv2.imwrite(file_dir + img_name[0:-4] + '_brighter.jpg', img_brighter)

        blur = cv2.GaussianBlur(img, (7, 7), 1.5)
        cv2.imwrite(file_dir + img_name[0:-4] + '_blur.jpg', blur)


if __name__ == '__main__':
    run(file_dir='img/')


