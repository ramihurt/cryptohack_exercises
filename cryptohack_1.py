import base64
from Crypto.Util.number import *

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("".join(chr(o) for o in ords))
# crypto{ASCII_pr1nt4bl3}

print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
# crypto{You_will_be_working_with_hex_strings_a_lot}

print(base64.b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))
# crypto/Base+64+Encoding+is+Web+Safe/