import os
import xml.etree.ElementTree as ET

# Define the classes for your objects
classes = ['LiquidCargoShip', 'PassengerShip', 'DryCargoShip', 'CargoTruck', 'SmallCar', 'DumpTruck', 'Van', 'Motorboat', 'Bridge', 'Intersection', 'Excavator', 'other-vehicle', 'Boeing737', 'A321', 'TennisCourt', 'BasketballCourt', 'Bus', 'A220', 'other-ship', 'other-airplane', 'Boeing787', 'FootballField', 'EngineeringShip', 'Warship', 'Tugboat', 'Tractor', 'Roundabout', 'ARJ21', 'FishingBoat', 'Boeing747', 'Trailer', 'TruckTractor', 'BaseballField', 'A330', 'A350', 'Boeing777', 'C919']

# Define the path to the directory containing the XML files
xml_dir1 = r'D:\TAI LIEU HOC\Nam5\ObjectDetection_CoHong\FAIR1M2.0\train\part1\labelXml'
xml_dir2 = r'D:\TAI LIEU HOC\Nam5\ObjectDetection_CoHong\FAIR1M2.0\train\part2\labelXml'
# Define the path to the directory where you want to save the YOLO label files
label_dir1 = r'D:\TAI LIEU HOC\Nam5\ObjectDetection_CoHong\FAIR1M2.0\train\part1\labels'
label_dir2 = r'D:\TAI LIEU HOC\Nam5\ObjectDetection_CoHong\FAIR1M2.0\train\part2\labels'
# Loop through all the XML files in the directory
for xml_file in os.listdir(xml_dir1):
    if xml_file.endswith('.xml'):
        # print(True)
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_dir1, xml_file))
        root = tree.getroot()
        # print(root)

        # Get the image size (if available)
        size = root.find('size')
        width_image = int(size.find('width').text)
        height_image = int(size.find('height').text)

        objects = root.find('objects')
        # Create a label file for this image
        label_file = os.path.join(label_dir1, os.path.splitext(xml_file)[0] + '.txt')

        # Open the label file for writing
        with open(label_file, 'w') as f:
            # Loop through all the objects in the XML file
            for obj in objects.findall('object'):
                    # Get the object class
                
                cls = obj.find('possibleresult/name').text
                print(cls)
                cls=cls.replace(' ','')
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
                objectPoints = obj.find('points')
                points = []
                for point in objectPoints.findall('point'):
                    points.append([float(point.text.split(',')[0]),float(point.text.split(',')[1])])
                x_center = (points[0][0]+points[1][0]+points[2][0]+points[3][0])/4
                y_center = (points[0][1]+points[1][1]+points[2][1]+points[3][1])/4
                heigh = max(points[0][1],points[1][1],points[2][1],points[3][1]) - min(points[0][1],points[1][1],points[2][1],points[3][1])
                width = max(points[0][0],points[1][0],points[2][0],points[3][0]) - min(points[0][0],points[1][0],points[2][0],points[3][0])
                f.write(f"{cls_id} {(x_center/width_image):.6f} {(y_center/height_image):.6f} {(width/width_image):.6f} {(heigh/height_image):.6f}\n")


for xml_file in os.listdir(xml_dir2):
    if xml_file.endswith('.xml'):
        # print(True)
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_dir2, xml_file))
        root = tree.getroot()
        # print(root)

        # Get the image size (if available)
        size = root.find('size')
        width_image = int(size.find('width').text)
        height_image = int(size.find('height').text)

        objects = root.find('objects')
        # Create a label file for this image
        label_file = os.path.join(label_dir2, os.path.splitext(xml_file)[0] + '.txt')

        # Open the label file for writing
        with open(label_file, 'w') as f:
            # Loop through all the objects in the XML file
            for obj in objects.findall('object'):
                    # Get the object class
                
                cls = obj.find('possibleresult/name').text
                print(cls)
                cls=cls.replace(' ','')
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
                objectPoints = obj.find('points')
                points = []
                for point in objectPoints.findall('point'):
                    points.append([float(point.text.split(',')[0]),float(point.text.split(',')[1])])
                x_center = points[0][0]+points[1][0]+points[2][0]+points[3][0]
                y_center = points[0][1]+points[1][1]+points[2][1]+points[3][1]
                heigh = max(points[0][1],points[1][1],points[2][1],points[3][1]) - min(points[0][1],points[1][1],points[2][1],points[3][1])
                width = max(points[0][0],points[1][0],points[2][0],points[3][0]) - min(points[0][0],points[1][0],points[2][0],points[3][0])
                f.write(f"{cls_id} {(x_center/width_image):.6f} {(y_center/height_image):.6f} {(width/width_image):.6f} {(heigh/height_image):.6f}\n")
