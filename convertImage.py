from PIL import Image
import cv2
import os, glob
import shutil

def writeToTrain(path,textTrain):
    with open(textTrain, 'w') as f:
        for fileName in glob.glob(os.path.join(path,'*.tif')):
            # im = Image.open(fileName)
            fileName = fileName.split('.')[0].split('/')[-1]
            if int(fileName)>=0 and int(fileName)<=2000:
                f.write(fileName)
                f.write('\n')

def writeToValid(path,textValid):
    with open(textValid, 'w') as f:
        for fileName in glob.glob(os.path.join(path,'*.tif')):
            # im = Image.open(fileName)
            fileName = fileName.split('.')[0].split('/')[-1]
            if int(fileName)>2000 and int(fileName)<=2200:
                f.write(fileName)
                f.write('\n')
                    

def createImage(path, newPath, newLabelPath, labelPath):
   for fileName in glob.glob(os.path.join(path,'*.tif')):
        im = Image.open(fileName)
        print(fileName)
        fileName = fileName.split('.')[0].split('/')[-1]
        # if int(fileName)>=15000:
        #     with open(textValid, 'w') as f:
        #         f.write(fileName)
        #         f.write('\n')
        # else:
        #     with open(textTrain, 'w') as f:
        #         f.write(fileName)
        #         f.write('\n')
        if int(fileName)>=0 and int(fileName)<=2200:
            im.save(newPath+fileName+'_co.png')
            shutil.copy(labelPath+fileName+'.txt',newLabelPath+fileName+'.txt')
                
            # im = cv2.imread(newPath+fileName+'_co.png')
            # img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # cv2.imwrite(newPath+fileName+'_ir.png',img_gray)
    

createImage('/content/images/','/content/drive/MyDrive/superYoloData2/images/','/content/drive/MyDrive/superYoloData2/labels/','/content/ObjectDetection_CoHong/train/part1/labels/')
writeToTrain('/content/images/','/content/drive/MyDrive/superYoloData2/train.txt')
writeToValid('/content/images/','/content/drive/MyDrive/superYoloData2/valid.txt')