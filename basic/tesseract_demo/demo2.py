#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:34
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import pytesseract
from PIL import Image
import time
from urllib import request


def main():
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    url = "https://passport.mingrisoft.com/captcha.html?0.7718547163502254"
    while True:
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)

if __name__ == '__main__':
    main()