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
import itertools
import multiprocessing
from datetime import datetime
import sys
def md5crypt(ascii_password,ascii_salt= "4fTgjp6q"):
    try:
        target_hash = "NqD7sOItIT/5JfzqmQ.ki0"
        b64_crypt = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
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
        #rearrange 16 bytes in this order: 11 4 10 5 3 9 15 2 8 14 1 7 13 0 6 12
        new_hex = hex_list[11] + hex_list[4] + hex_list[10] + hex_list[5] + hex_list[3] + hex_list[9] + hex_list[15] + hex_list[2] + hex_list[8] + hex_list[14] + hex_list[1] + hex_list[7] + hex_list[13] + hex_list[0] + hex_list[6] + hex_list[12]
        binary_string=bin(int(new_hex,16))[2:].zfill(128)
        #create 6bit strings to index into b_64 crypt
        index_list = [binary_string[i:i+6] for i in range(-12,-129,-6)]
        index_list.insert(0,binary_string[-6:])
        final_hash = ""
        for i in index_list:
            final_hash = final_hash + b64_crypt[int(i,2)]
        if final_hash == target_hash:
            print(ascii_password)
            with open('answer.txt', 'w') as f:
                print(ascii_password, file=f)
            return ascii_password
    except:
        print("Error with this result ",ascii_password) 
        sys.exit()
    return

if __name__ == '__main__':
    old_first= ''  
    word_list=[]
    for i in range(5,7):
        for subsets in itertools.product('QRSTUVWXYZABCDEFGHIJKLMNOPqrstuvwxyzabcdefghijklmnop',repeat=i):
            print(''.join(subsets))
            #run a max of 7 before attempting to join
            target_word = ''.join(subsets)
            if(target_word[0:3] != old_first):
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Now on ",target_word[0:3], dt_string)
                old_first = target_word[0:3]
            word_list.append(target_word)
            if(len(word_list) == 8000):
                p = multiprocessing.Pool(multiprocessing.cpu_count())
                #distribute word_list as workload
                result = p.map(md5crypt,word_list)
                p.close()
                p.join()
                word_list=[]
            
