#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 15:47
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open('test3.png')

text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)