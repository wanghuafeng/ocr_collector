#!-*- coding:utf-8 -*-
import os
import codecs
import requests
import base64


class WebImgText(object):
    """
    网络图片文字识别
    """
    headers = {
        "Host": "cloud.baidu.com",
        "Origin": "https://cloud.baidu.com",
        "Referer": "https://cloud.baidu.com/product/ocr/webimage",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }

    def get_base64_data(self, filename):
        assert os.path.isfile(filename)
        content = codecs.open(filename).read()
        base64_data = base64.b64encode(content)
        return base64_data

    def verify_base_pic(self, base64_pic_content):
        url = 'https://cloud.baidu.com/aidemo'
        data={
            'type':'webimage',
            'image':'data:image/png;base64,' + base64_pic_content,
        }
        r = requests.post(url, data, headers=self.headers)
        return r.content


if __name__ == "__main__":
    wit = WebImgText()
    filename = ""
    pic_content = wit.get_base64_data(filename)
    char = wit.verify_base_pic(pic_content)
    print char
