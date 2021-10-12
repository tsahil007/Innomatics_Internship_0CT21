#!/bin/python3

import math
import os
import random
import re
import sys

n = input()

if int(n)%2 == 1:
    print('Weird')
else :
    if int(n) >= 6 and int(n) <=20 :
        print('Weird')
    else :
        print('Not Weird')
        
        
        