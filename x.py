
#!/bin/python3

import math

import os

import random

import re

import sys

# Complete the 'getMinProcessingTime' function below.

#

#The function is expected to return an INTEGER.

# The function accepts following parameters:

#1. INTEGER_ARRAY data

#2. INTEGER processTimeA

#3. INTEGER processTimeB

#

def getMinProcessingTime(data, processTimeA, processTimeB):

#Write your code here

if name =='main'

fptr= open(os.environ ['OUTPUT_PATH'], 'w')

data_count = int(input().strip())

data = []
for in range(data_count): data_item = int(input().strip()) data.append(data_item)

processTimeA = int(input().strip())

processTimeB = int(input().strip())

result = getMinProcessing Time (data, processTimeA, processTimeB)

fptr.write(str(result) + '\n')

fptr.close()