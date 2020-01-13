#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:48:07 2020

@author: winson
CS165 Lab1 Bruteforce Attack
"""
import hashlib
import base64

result= hashlib.md5(b'0HPDynDxq')
hexform=result.hexdigest()
print(base64.b64encode(result.digest()))

def passwordHash(password):
    #compute alternate sum
    
    #compute intermediate sum
    #Concatenate Password, Magic, Salt, Length in bytes of the alternate sum