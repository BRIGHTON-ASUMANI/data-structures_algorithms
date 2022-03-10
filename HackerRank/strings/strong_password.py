'''
https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
'''


#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special = "!@#$%^&*()-+"
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = '0123456789'
    # Python program to check validation of password
    # Module of regular expression is used with search()
    count = 0
    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in special for i in password) == False:
        count += 1
    return max(count, 6-n)


def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case =  string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special_characters = "!@#$%^&*()-+"
    
    n_bool = 1
    l_bool = 1
    u_bool = 1
    s_bool = 1
    for c in password:
        if c in numbers: n_bool = 0
        elif c in lower_case: l_bool = 0
        elif c in upper_case: u_bool = 0
        elif c in special_characters: s_bool = 0
    return max(6-n, n_bool + l_bool + u_bool + s_bool)