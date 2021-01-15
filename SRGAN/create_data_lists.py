#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :create_data_lists.py
@说明        :创建训练集和测试集列表文件
@时间        :2020/02/11 11:32:59
@版本        :1.0
"""

from SR.SRGAN.utils import create_data_lists

if __name__ == '__main__':
    create_data_lists(train_folders=['/home/zhaohoj/Desktop/videos/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages',
                                     # './data/COCO2014/val2014'
                                     ],
                      test_folders=[
                                    '/home/zhaohoj/Desktop/videos/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/test',
                                    # '../data/Set5',
                                    # '../data/Set14'
                                    ],
                      min_size=100,
                      output_folder='./data/')
