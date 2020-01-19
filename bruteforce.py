#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:48:07 2020

@author: winson
CS165 Lab1 Bruteforce Attack
"""
import binascii
import hashlib
import base64

result= hashlib.md5(b'0HPDynDxq')
hexform=result.hexdigest()
print(base64.b64encode(result.digest()))

def md5crypt(ascii_password,ascii_salt):
    #compute alternate sum md5(password + salt + password)
    alternate = ascii_password + ascii_salt + ascii_password
    alternate_sum = hashlib.md5()
    alternate_sum.update(alternate.encode("utf-8"))

    intermediate_0_string = ascii_password + "$1$" + ascii_salt
    intermediate_0 = hashlib.md5(intermediate_0_string.encode("utf-8"))
    
    #Update digest
    pwlen = len(ascii_password) 
    i = pwlen
    while i > 0:
        intermediate_0.update(alternate_sum.digest() if i > 16 else alternate_sum.digest()[:i])
        i -= 16
    i = pwlen
    #For each bit in length(password) from low to high and stop after the most significant set bit
    while True:
      #if bit is set append a NUL byte
      if(i%2 == 1):
        intermediate_0.update('\0'.encode("utf-8"))
      #if bit is unset append the first byte of the password
      if(i%2 == 0):
        intermediate_0.update(ascii_password[0].encode("utf-8"))
      #shift everything to the right
      i = i//2
      if(i == 0):
        break
    print("Intermediate_0.digest() is")
    print(intermediate_0.hexdigest())
    
    old_digest = intermediate_0
    new_digest = hashlib.md5()
    for i in range(1000):
    #compute the intermediate_i+1 b concatenating and hashing the following
        if i % 2 == 0:
            new_digest.update(old_digest.digest())
        if i % 2 == 1:
            new_digest.update(ascii_password.encode("utf-8"))
        if i % 3 != 0:
            new_digest.update(ascii_salt.encode('utf-8'))
        if i % 7 != 0:
            new_digest.update(ascii_password.encode('utf-8'))
        if i % 2 == 0:
            new_digest.update(ascii_password.encode('utf-8'))
        if i % 2 == 1:
            new_digest.update(old_digest.digest())
        old_digest = new_digest
        if(i == 999):
            break
        new_digest = hashlib.md5()
    target_hexstring = old_digest.hexdigest()
    #create a list
    hex_list = [target_hexstring[i:i+2] for i in range(0,len(target_hexstring),2)]
    print(hex_list)
    #rearrange 16 bytes in this order: 11 4 10 5 3 9 15 2 8 14 1 7 13 0 6 12
    
    #compute intermediate sum
    #Concatenate Password, Magic, Salt, Length in bytes of the alternate sum

md5crypt("zhgnnd","hfT7jp2q")
