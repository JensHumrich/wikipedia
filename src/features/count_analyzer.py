#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:39:48 2019

@author: jh186076
"""
from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]

word_freq = {}

with open(project_dir.joinpath( "data/processed/count-sorted-small-chunkaa")) as file1:
    line = file1.readline()
    while line:
        line = line.lstrip()
        cnt = line.split(" ")[0].strip()
        word = line.split(" ")[1]
        word_freq[word] = int(cnt)
        line = file1.readline()
    
cnter = 0
with  open(project_dir.joinpath( "data/processed/count-sorted-small-chunkab")) as file2:
    line = file2.readline()
    while line:
        line = line.lstrip()
        cnt = line.split(" ")[0].strip()
        word = line.split(" ")[1]
        if word not in word_freq.keys():
            print(line)
            cnter += 1
            if cnter > 100:
                break
        line = file2.readline()