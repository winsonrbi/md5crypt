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
    print(intermediate_0.digest())
    
    for i in range(1000):
    #compute the intermediate_i+1 b concatenating and hashing the following
      
    a = binascii.b2a_uu(intermediate_0.digest())
    print(a)
    #compute intermediate sum
    #Concatenate Password, Magic, Salt, Length in bytes of the alternate sum

md5crypt("test","1234")
