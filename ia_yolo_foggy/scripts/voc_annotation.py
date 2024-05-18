import os
import sys
import argparse
import xml.etree.ElementTree as ET

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from os import listdir

def convert_voc_annotation(data_path, anno_path, use_difficult_bbox=False):

    classes = ['license_plate']
    image_inds = set()
    for file_name in listdir(data_path):
        image_inds.add(file_name[:len(file_name)-4])

    with open(anno_path, 'w') as f:
        for image_ind in image_inds:
            image_path = os.path.join(data_path, image_ind + '.jpg')
            annotation = image_path
            label_path = os.path.join(data_path, image_ind + '.xml')
            root = ET.parse(label_path).getroot()
            objects = root.findall('object')
            for obj in objects:
                difficult = obj.find('difficult').text.strip()
                if (not use_difficult_bbox) and(int(difficult) == 1):
                    continue
                bbox = obj.find('bndbox')
                xmin = bbox.find('xmin').text.strip()
                xmax = bbox.find('xmax').text.strip()
                ymin = bbox.find('ymin').text.strip()
                ymax = bbox.find('ymax').text.strip()
                annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, '0'])

            print(annotation)
            f.write(annotation + "\n")
    return len(image_inds)

if __name__ == '__main__':
    # for foggy conditions
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="../../datasets")
    parser.add_argument("--train_annotation", default="data/dataset_fog/voc_norm_train.txt")
    parser.add_argument("--test_annotation",  default="data/dataset_fog/voc_norm_test.txt")
    parser.add_argument("--val_annotation",  default="data/dataset_fog/voc_norm_val.txt")

    flags = parser.parse_args()

    num1 = convert_voc_annotation(os.path.join(flags.data_path, 'lptrain'), flags.train_annotation, False)
    num2 = convert_voc_annotation(os.path.join(flags.data_path, 'lpval'), flags.val_annotation, False)
    num3 = convert_voc_annotation(os.path.join(flags.data_path, 'lptest'), flags.test_annotation, False)
    print('=> The number of image for train is: %d\tThe number of image for val is:%d\tThe number of image for test is:%d' %(num1, num2, num3))



