# -*- coding: utf-8 -*-
import scrapy
import requests
from urllib import request
from PIL import Image
from base64 import b64encode

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url = 'https://accounts.douban.com/login'
    profile_url = "https://www.douban.com/people/76735403/"
    edit_url = "https://www.douban.com/j/people/76735403/edit_signature"

    def parse(self, response):
        formdata = {
            'source':'None',
            'redir':'https://www.douban.com/',
            'form_email': 'xxxxxxx@xx.com',
            'form_password': 'xxxxxx',
            'remember': 'on',
            'login':'登录'
        }
        captcha_url = response.css("img#captcha_img::attr(src)").get()
        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url,formdata=formdata,callback=self.parse_after_login)

    def parse_after_login(self,response):
        if response.url == "https://www.douban.com":
            yield scrapy.Request(self.profile_url,callback=self.parse_profile)
            print("login success!")
        else:
            print("login failed!")

    def parse_profile(self,response):
        if response.url == self.profile_url:
            ck = response.xpath("//input[@name='ck']/@value").get()
            formdata = {
                'ck': ck,
                'signature': 'I am Robot!'
            }
            yield scrapy.FormRequest(self.edit_url,formdata=formdata,callback=self.parse_test)
        else:
            print("没有进入个人中心")

    def parse_test(self, response):
        pass

    # def regonize_captcha(self,image_url):
    #     request.urlretrieve(image_url,'captcha.png')
    #     image = Image.open('captcha.png')
    #     image.show()
    #     captcha = input("请输入验证码:")
    #     return captcha
    # aliyun识别验证码
    def regonize_captcha(self,image_url):
        captcha_url = image_url
        request.urlretrieve(captcha_url, 'captcha.png')

        recognize_url = "https://tongyongwe.market.alicloudapi.com/generalrecognition/recognize?type=en"

        formdata = {}
        with open('captcha.png', 'rb') as fp:
            data = fp.read()
            pic = b64encode(data)
            formdata['pic'] = pic
        # 从阿里云获取appcode
        appcode = 'xxxxxxxxxxxxxxxxxxxxxxx'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Authorization': 'APPCODE ' + appcode
        }

        response = requests.post(url=recognize_url, data=formdata, headers=headers)
        result = response.json()
        code = result['result']
        return code
