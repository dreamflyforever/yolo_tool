import  os
from tqdm import tqdm
import shutil
import cv2
from glob import glob

import numpy as np

 
def tuneinto_gray(path):
    # 遍历当前目录下所有文件及文件夹
    file_list = os.listdir(path)
 
    # 循环判断file_list中每个元素是文件还是文件夹,若是文件，传入list，若是文件夹，再递归
    for file in tqdm(file_list):
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
 
        # 判断是否是文件夹，若是重新递归
        if os.path.isdir(cur_path):
            tuneinto_gray(cur_path)
        else:
            print(cur_path) 
            """
            给每个文件重新修改后缀
            """
            #new_suf = cur_path.replace('.jpeg', '.jpg')
 
            # 改完后缀后，需要移动并覆盖源文件
            #shutil.move(cur_path, new_suf)

            img = cv2.imread(cur_path, cv2.IMREAD_GRAYSCALE)
            if not img is None:
                cv2.imwrite(cur_path, img)
 
tuneinto_gray("/Users/jim/workspace/sleepy/rv1103/ai_tool/test")
