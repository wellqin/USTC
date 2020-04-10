# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        查找
Description :   
Author :          wellqin
date:             2019/8/11
Change Activity:  2019/8/11
-------------------------------------------------
"""

# import base64 as b64
#
# def xor_encrypt(tips,key):
#     ltips=len(tips)
#     lkey=len(key)
#     secret=[]
#     num=0
#     for each in tips:
#         if num>=lkey:
#             num=num%lkey
#         secret.append( chr( ord(each)^ord(key[num]) ) )
#         num+=1
#
#     return b64.b64encode( "".join( secret ).encode() ).decode()
#
#
# def xor_decrypt(secret,key):
#
#     tips = b64.b64decode(secret.encode()).decode()
#
#     ltips = len(tips)
#     lkey = len(key)
#     secret = []
#     num=0
#     for each in tips:
#         if num >= lkey:
#             num = num % lkey
#
#         secret.append(chr(ord(each) ^ ord(key[num])))
#         num += 1
#
#     return "".join(secret)
#
#
# tips= "1234567"
# key= "owen"
# secret = xor_encrypt(tips,key)
# print( "cipher_text:", secret )
#
# plaintxt = xor_decrypt( secret, key )
# print( "plain_text:",plaintxt )

#加密



key='A'   # 密钥
message='haoiphgaop'   # 明文
ml=len(message)  # 分别得到密钥和明文的长度
kl=len(key)

key=ml//kl*key + key[:ml%kl]  # 因为要一对一的异或，所以key要变化
pwd=[]  #通过取整，求余的方法重新得到key
for i in range(len(key)):
    pwd.append(chr(ord(key[i])^ord(message[i]))) #一对一异或操作，得到结果,其中,"ord(char)"得到该字符对应的ASCII码,"chr(int)"刚好相反
print(''.join(pwd))

#解密
result=[]
#pwd为密文
for j in range(len(key)):
    result.append(chr(ord(pwd[j]) ^ ord(key[j]))) #跟KEY异或回去就是原明文
result=''.join(result)
print(result)


"""
解密中跟KEY异或回去就是原明文…
举个例子吧：
10101^11100=01001
结果是01001
01001^10101=11100
01001^11100=01001
异或的结果再与原来的其中一个数异或运算就得到另外一个原来的数
"""


def encode(plaintext,key):
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]  # 取整数/余数
    ciphertext=[]
    for i in range(len(plaintext)):
        ciphertext.append(str(ord(plaintext[i])^ord(key[i])))
    return ','.join(ciphertext)
# 解密
def decode(ciphertext,key):
    ciphertext=ciphertext.split(',')
    key=key*(len(ciphertext)//len(key))+key[:len(ciphertext)%len(key)]  # 取整数/余数
    plaintext=[]
    for i in range(len(ciphertext)):
        plaintext.append(chr(int(ciphertext[i])^ord(key[i])))
    return ''.join(plaintext)

if __name__ == '__main__':
    functions=input('输入A加密，输入B解密，其它关闭>>>>')
    if functions=='A':
        plaintext=input('请输入加密文字明文>>>')
        key=input('请输入加密密钥>>>')
        print('密文',encode(plaintext,key))
    if functions=='B':
        ciphertext = input('请输入解密文字明文>>>')
        key = input('请输入解密密钥>>>')
        print('明文',decode(ciphertext,key))


