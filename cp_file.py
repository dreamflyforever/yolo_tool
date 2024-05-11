import cv2
import time
import subprocess
import os
import time
from tqdm import tqdm

def main(file_dir):
    for img_name in tqdm(os.listdir(file_dir)):
        #subprocess.call("adb pull /oem/ws/" + img)
        os.system("cp " + file_dir + "/" +img_name + " " + file_dir + "/" +img_name[0:-4] + '_noise.txt')
        os.system("cp " + file_dir + "/" +img_name + " " + file_dir + "/" +img_name[0:-4] + '_darker.txt')
        os.system("cp " + file_dir + "/" +img_name + " " + file_dir + "/" +img_name[0:-4] + '_brighter.txt')
        os.system("cp " + file_dir + "/" +img_name + " " + file_dir + "/" +img_name[0:-4] + '_blur.txt')

if __name__ == '__main__':
    main(file_dir='labels')
