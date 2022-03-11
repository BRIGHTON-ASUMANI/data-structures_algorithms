'''
https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
'''
from re import compile, VERBOSE
# regex = r'^(?=[0-9a-zA-Z]{6,}$)(?=[0-9a-zA-Z]*[A-Z])(?=[0-9a-zA-Z]*[a-z])(?=[0-9a-zA-Z]*[0-9]).*'

# # 大佬鼠
# regex0 = (
#     '^'
#     '(?=.*\d)'
#     '(?=.*[a-z])'
#     '(?=.*[A-Z])'
#     '[a-zA-Z\d]'
#     '{6,}'
#     '$'
# )


# regex1 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"


regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)
