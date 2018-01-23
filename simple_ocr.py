#coding:utf-8
import os
import sys
import time
import codecs
import requests
import pytesseract
from PIL import Image

"""
ocr识别最简实现，无灰度转换及二值化处理过程
适用于比较简单的图片验证码
"""


def img2str(pic_file_path):
    """
    @:param pic_file_path: 图片文件路径
    """
    image = Image.open(pic_file_path)
    vcode = pytesseract.image_to_string(image)
    return vcode

def get_pic_content():
    url = 'https://persons.shgjj.com/VerifyImageServlet'
    content = requests.get(url).content
    return content

def test_pic_verify(count=1):
    for i in range(count):
        try:
            pic_content = get_pic_content()
            pic_pattern = r'./pic/fund_shanghai_%s_vcode.jpg'
            filename = pic_pattern % time.time()
            codecs.open(filename, mode='wb').write(pic_content)
            vcode = img2str(filename).replace(' ', '')
            os.rename(filename, filename.replace('vcode', vcode))
        except BaseException as e:
            print e

if __name__ == "__main__":
    pic_filename = r'D:\py_project\fi\pic\fund_shanghai.jpg'
    test_pic_verify()

