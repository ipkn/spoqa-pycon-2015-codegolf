from test import EXAMPLE as logo
import zlib
logo = open('pp2').read()

code = u"""#coding:L1\nimport zlib\nprint(zlib.decompress([bytes,lambda x,y:x][str==bytes]('!!!','L1')).decode())"""

f = open('./pupu.py', mode='wb')
f.write(bytes(code.split('!!!')[0], 'utf-8'))

data = zlib.compress(bytes(logo, 'utf-8'),9)
data=data.replace(b'\r',b'\\r')
data=data.replace(b'\n',b'\\n')

f.write(data)

f.write(bytes(code.split('!!!')[1], 'utf-8'))
f.close()
