import os
import re
from PIL import Image

folder_image = '/content/image_yolo_test/image/'
folder_label = '/content/image_yolo_test/label/'
new_path_label = '/content/new_label/'

array_of_yolo_classes = ['LiquidCargoShip', 'PassengerShip', 'DryCargoShip', 'CargoTruck', 'SmallCar', 'DumpTruck', 'Van', 'Motorboat', 'Bridge', 'Intersection', 'Excavator', 'other-vehicle', 'Boeing737', 'A321', 'TennisCourt', 'BasketballCourt', 'Bus', 'A220', 'other-ship', 'other-airplane', 'Boeing787', 'FootballField', 'EngineeringShip', 'Warship', 'Tugboat', 'Tractor', 'Roundabout', 'ARJ21', 'FishingBoat', 'Boeing747', 'Trailer', 'TruckTractor', 'BaseballField', 'A330', 'A350', 'Boeing777', 'C919'];

for each_label in os.listdir(folder_label):
  if(each_label.endswith('txt')):
    the_file = open(folder_label+each_label, 'r')
    all_lines = the_file.readlines();
    image_name_file = each_label.replace('txt','tif')

    ori_image = Image.open(folder_image+image_name_file);
    image_width = ori_image.width
    image_height = ori_image.height
    print("height:",image_height)
    print('width:',image_width)

    with open(new_path_label+each_label.replace('txt','xml'), "w") as f:
      f.write('<annotation>\n')
      f.write('\t<folder>XML</folder>\n')
      f.write('\t<filename>' + image_name_file + '</filename>\n')
      f.write('\t<path>' + folder_image + image_name_file + '</path>\n')
      f.write('\t<source>\n')
      f.write('\t\t<database>Unknown</database>\n')
      f.write('\t</source>\n')
      f.write('\t<size>\n')
      f.write('\t\t<width>' + str(image_width) + '</width>\n')
      f.write('\t\t<height>' + str(image_height) + '</height>\n')
      f.write('\t\t<depth>3</depth>\n') # assuming a 3 channel color image (RGB)
      f.write('\t</size>\n')
      f.write('\t<segmented>0</segmented>\n')

      for each_line in all_lines:
          # regex to find the numbers in each line of the text file
        yolo_array = re.split("\s", each_line.rstrip()) # remove any extra space from the end of the line

          # initalize the variables
        class_number = 0
        x_yolo = 0.0
        y_yolo = 0.0
        yolo_width = 0.0
        yolo_height = 0.0
        yolo_array_contains_only_digits = True

          # make sure the array has the correct number of items
        if len(yolo_array) == 5:
          class_number = int(yolo_array[0])
          object_name = array_of_yolo_classes[class_number]
          x_yolo = float(yolo_array[1])
          y_yolo = float(yolo_array[2])
          yolo_width = float(yolo_array[3])
          yolo_height = float(yolo_array[4])

              # Convert Yolo Format to Pascal VOC format
          box_width = yolo_width * image_width
          box_height = yolo_height * image_height
          x_min = str(int(x_yolo * image_width - (box_width / 2)))
          y_min = str(int(y_yolo * image_height - (box_height / 2)))
          x_max = str(int(x_yolo * image_width + (box_width / 2)))
          y_max = str(int(y_yolo * image_height + (box_height / 2)))

              # write each object to the file
          f.write('\t<object>\n')
          f.write('\t\t<name>' + object_name + '</name>\n')
          f.write('\t\t<pose>Unspecified</pose>\n')
          f.write('\t\t<truncated>0</truncated>\n')
          f.write('\t\t<difficult>0</difficult>\n')
          f.write('\t\t<bndbox>\n')
          f.write('\t\t\t<xmin>' + x_min + '</xmin>\n')
          f.write('\t\t\t<ymin>' + y_min + '</ymin>\n')
          f.write('\t\t\t<xmax>' + x_max + '</xmax>\n')
          f.write('\t\t\t<ymax>' + y_max + '</ymax>\n')
          f.write('\t\t</bndbox>\n')
          f.write('\t</object>\n')
      f.write('</annotation>\n')
      f.close() # Close the file
          


