import os
import xml.etree.ElementTree as ET

# Define the classes for your objects
# classes = ['LiquidCargoShip', 'PassengerShip', 'DryCargoShip', 'CargoTruck', 'SmallCar', 'DumpTruck', 'Van', 'Motorboat', 'Bridge', 'Intersection', 'Excavator', 'other-vehicle', 'Boeing737', 'A321', 'TennisCourt', 'BasketballCourt', 'Bus', 'A220', 'other-ship', 'other-airplane', 'Boeing787', 'FootballField', 'EngineeringShip', 'Warship', 'Tugboat', 'Tractor', 'Roundabout', 'ARJ21', 'FishingBoat', 'Boeing747', 'Trailer', 'TruckTractor', 'BaseballField', 'A330', 'A350', 'Boeing777', 'C919']

# Define the path to the directory containing the XML files
xml_dir1 = r'/home/dongtran/Downloads/Fair1m2.0/train/part1/labelXml_1'
xml_dir2 = r'/home/dongtran/Downloads/Fair1m2.0/train/part2/labelXml_2'
# Define the path to the directory where you want to save the YOLO label files
label_file = r'/home/dongtran/LapTrinh/Python_projects/Do_An_Tot_Nghiep/ObjectDetection_CoHong/names.txt'
label_file_part1 = r'/home/dongtran/LapTrinh/Python_projects/Do_An_Tot_Nghiep/ObjectDetection_CoHong/train/part1/names.txt'
label_file_part2 = r'/home/dongtran/LapTrinh/Python_projects/Do_An_Tot_Nghiep/ObjectDetection_CoHong/train/part2/names.txt'
names = []

# Loop through all the XML files in the directory
for xml_file in os.listdir(xml_dir1):
    if xml_file.endswith('.xml'):
        tree = ET.parse(os.path.join(xml_dir1, xml_file))
        # print(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        # Get the image size (if available)
        objects = root.find('objects')
        # print('do dai :',len(objects))

        # with open(label_file, 'w') as f:
        for obj in objects.findall('object'):
            # Get the object class
            # print('object:',str(obj))
            cls = obj.find('possibleresult/name').text
            cls = cls.replace(' ', '')
            if cls not in names:
                names.append(cls)
            # names.append(cls)
            # print(cls)

for xml_file in os.listdir(xml_dir2):
    if xml_file.endswith('.xml'):
        tree = ET.parse(os.path.join(xml_dir2, xml_file))
        # print(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        # Get the image size (if available)
        objects = root.find('objects')
        # print('do dai :',len(objects))

        # with open(label_file, 'w') as f:
        for obj in objects.findall('object'):
            # Get the object class
            # print('object:',str(obj))
            cls = obj.find('possibleresult/name').text
            cls = cls.replace(' ', '')
            if cls not in names:
                names.append(cls)

f = open(label_file, "a")
f.write(str(names))
f.close()
