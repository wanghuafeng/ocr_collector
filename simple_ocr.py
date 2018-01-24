#coding:utf-8
import os
import codecs
import requests
import pytesseract
from PIL import Image


class OnlyTesserAct(object):
    """
    ocr识别最简实现，无灰度转换及二值化处理过程
    适用于比较简单的图片验证码
    """
    def __init__(self, filename):
        self.filename = filename

    def img2str(self):
        assert os.path.isfile(self.filename)
        image = Image.open(self.filename)
        vcode = pytesseract.image_to_string(image)
        return vcode

    def get_pic_content_by_url(self, url):
        content = requests.get(url).content
        return content

    def main(self):
        pic_filename = r'./fund_shanghai.jpg'
        url = 'https://persons.shgjj.com/VerifyImageServlet'
        ta = OnlyTesserAct(pic_filename)
        pic_content = ta.get_pic_content_by_url(url)
        codecs.open(pic_filename, mode='wb').write(pic_content)
        print ta.img2str()


class GrayConvert(object):
    """
    PIL可以对图像的颜色进行转换，并支持诸如24位彩色、8位灰度图和二值图等模式，
    简单的转换可以通过Image.convert(mode)函数完 成，其中mode表示输出的颜色模式，
    例如''L''表示灰度，''1''表示二值图模式等。
    但是利用convert函数将灰度图转换为二值图时，是采用 固定的阈 值127来实现的，
    即灰度高于127的像素值为1，而灰度低于127的像素值为0。
    """
    def __init__(self, filename):
        self.filename = filename
        self.image = self._image_load()

    def _image_load(self):
        assert os.path.isfile(self.filename)
        return Image.open(self.filename)

    def image_grayed(self):
        """图片灰度处理"""
        imgry = self.image.convert('L')
        return imgry

    def image_binarize_reset_threshold(self, threshold):
        """
        :argument
            threshold 降噪阈值, 灰度处理结果默认为127
        """
        gray_img = self.image_grayed()
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        binarized_image = gray_img.point(table, '1')
        # binarized_image.show()
        # binarized_image.save()
        return binarized_image

    def img2str(self, image):
        vcode = pytesseract.image_to_string(image)
        return vcode

if __name__ == "__main__":
    pass