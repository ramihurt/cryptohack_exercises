import base64
from Crypto.Util.number import *
from pwn import xor

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("".join(chr(o) for o in ords))
# crypto{ASCII_pr1nt4bl3}

print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
# crypto{You_will_be_working_with_hex_strings_a_lot}

print(base64.b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))
# crypto/Base+64+Encoding+is+Web+Safe/

print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
# crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}

print(xor(b'label', 13))
# aloha

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG = xor(bytes.fromhex(KEY2_KEY3), bytes.fromhex(KEY1), bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))
print(FLAG)
# crypto{x0r_i5_ass0c1at1v3}

init = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print(xor(init,16))
# crypto{0x10_15_my_f4v0ur173_by7e}

