import qrcode
import pyotp

# 生成密钥
sec = pyotp.random_base32()
# 创建一个otps对象
topt = pyotp.TOTP(sec)
# 生成二维码url
qr_url = pyotp.totp.TOTP(sec).provisioning_uri("http://www.baidu.com")
# 生成二维码
img = qrcode.make(qr_url)
print(img.get_image().show())
print(topt.verify(401524))
