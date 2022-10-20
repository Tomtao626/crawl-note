#encoding:utf-8
'''
Created on 2014-6-1

@author: qiuyan.zwp
'''

import hmac
import hashlib
import base64

def setMd5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def hmac_md5(key,args):
    myhmac = hmac.new(key,args, hashlib.md5)
    str_result = base64.b64encode(myhmac.digest())
    return str_result
