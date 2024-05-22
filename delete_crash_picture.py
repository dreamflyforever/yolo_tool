import  os
from tqdm import tqdm
import cv2
from glob import glob
images = glob('*.jpg')
for image in tqdm(images):
	img = cv2.imread(image)
	if img is None:
		print(image) 
		os.remove(image)  # 删除有问题的图片	

