# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 14:32
# @Author  : lazerliu
# @File    : CocoForm_Learn.py
import sys
import json

# sys.path.append("/xxx/cocoapi/PythonAPI")#把cocoapi的绝对路径加上
from pycocotools.coco import COCO

ann_file = "coco/annotations/instances.json"# json文件的绝对路径
coco = COCO(annotation_file=ann_file)

print("coco\nimages.size [%05d]\tannotations.size [%05d]\t category.size [%05d]\ndone!"
      %(len(coco.imgs),len(coco.anns),len(coco.cats)))
