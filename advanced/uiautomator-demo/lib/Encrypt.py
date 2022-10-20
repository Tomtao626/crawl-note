#!/usr/bin/env python
#coding:utf-8
"""
  Author:  xulei --<>
  Purpose: 加密模块
  Created: 09/03/18
"""

import sys
try:
    if sys.version_info.major<3:
        from urllib import quote, unquote
    else:
        from urllib.parse import quote, unquote
except:
    pass
import base64
# 用于auth加密与解密
# 密钥
authkey = "ulei"
# 异或算法
xorStr = lambda ss,cc: ''.join(chr(ord(s)^ord(cc)) for s in ss)
# 方法
def encrypt_auth(data,key=authkey):
    """数据加密"""
    enStr = data   
    for cc in key:
        enStr = xorStr(enStr,cc)
    if isinstance(enStr, str):
        enStr = enStr.encode("utf-8")     
    return quote(base64.b64encode(enStr))

def decrypt_auth(data,key=authkey):
    """数据解密"""
    data = unquote(unquote(data))
    deStr = base64.b64decode(unquote(data))
    deKey = key[::-1]
    if isinstance(deStr, bytes):
        deStr = deStr.decode("utf-8")    
    for cc in deKey:
        deStr = xorStr(deStr,cc)
    return deStr

if __name__ == "__main__":
    # data = "featureIds: [1093, 2843, 3642, 4284, 4374,"
    import json
    aa = encrypt_auth(json.dumps({'cid':'163154_06H_0'}), 'benz')
    print(aa)
    bb = decrypt_auth('fCVkaGNiJT0nJSV6', 'vwag')
    print (bb)
    #print (repr(bb))