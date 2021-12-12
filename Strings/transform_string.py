#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.

def transformSentence(sentence):
    # Write your code here
    values = sentence.split()
    result=""
    for i in values:
        result+=i[0]
        for j in range(1,len(i)):
            if i[j-1].lower()<i[j].lower():
                result+=i[j].upper()
            elif i[j-1].lower()>i[j].lower():
                result+=i[j].lower()
            else:
                result+=i[j]
        result+=" "
    return result[:-1:]
                
            
        
