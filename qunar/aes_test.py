"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/11 19:16
@Software : PyCharm
@File     : aes_test.py
"""
import base64
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

data_string = '{"openTime":1702021534202,"startTime":1702021535985,"endTime":1702021536303,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36","uid":"0000f800254059475ae0ab8d","track":["36040;58.00;273.00;1.00","36061;112.00;277.00;55.00","36085;222.00;291.00;165.00","36108;309.00;294.00;252.00","36128;385.00;294.00;328.00","36150;405.00;294.00;348.00","36172;421.00;294.00;364.00","36192;428.00;294.00;371.00","36212;433.00;294.00;376.00","36233;443.00;294.00;386.00","36256;457.00;294.00;400.00","36276;468.00;294.00;411.00","36296;486.00;297.00;429.00"],"acc":[],"ori":[],"deviceMotion":[{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true}]}'
# key = "227V2xYeHTARSh1R".encode('utf-8')
key_string = "32323756327859654854415253683152"
key = binascii.a2b_hex(key_string)

aes = AES.new(
    key=key,
    mode=AES.MODE_ECB
)
raw = pad(data_string.encode('utf-8'), 16)
aes_bytes = aes.encrypt(raw)
res = base64.b64encode(aes_bytes)
print(res)
