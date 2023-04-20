import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import torch
import torchvision
import seaborn as sns
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

sample_image = Image.open('/home/dongtran/Downloads/Fair1m2.0/train/part1/images-001/images/1.tif')
tree = ET.parse('/home/dongtran/LapTrinh/Python_projects/Do_An_Tot_Nghiep/ObjectDetection_CoHong/train/part1/labelXml/1.xml')
root = tree.getroot()
sample_annotations = []
for neighbor in root.iter('points'):
    sample_point = []
    for point in neighbor.findall('point'):
        x, y = point.text.split(',')
        x = float(x)
        y = float(y)
        sample_point.append(x)
        sample_point.append(y)
    point = [sample_point[0], sample_point[1], sample_point[2], sample_point[3], sample_point[4], sample_point[5], sample_point[6], sample_point[7]]
    sample_annotations.append(point)

print(sample_annotations)

sample_image_new = sample_image.copy()

img_bbox = ImageDraw.Draw(sample_image_new)

for bbox in sample_annotations:
    points = []
    points = [(bbox[0], bbox[1]), (bbox[2], bbox[3]), (bbox[4], bbox[5]), (bbox[6], bbox[7])]
    img_bbox.polygon(points, outline='green', width=2)

sample_image_new.show()