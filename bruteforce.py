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
    print("HIIII")
    print(i)
    print(i >> 1)
    print(intermediate_0.digest())
    a = binascii.b2a_uu(intermediate_0.digest())
    print(a)
    #compute intermediate sum
    #Concatenate Password, Magic, Salt, Length in bytes of the alternate sum

md5crypt("test","1234")
