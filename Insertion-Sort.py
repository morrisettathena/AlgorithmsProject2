###############
#
# Liam Reynolds
# Insertion Sort
# 03/21/2023
# Professor Cates
#
# Description: This program uses intersion sort to sort arrays created from text files
#
###############

import random
import time

PATH = "./datafiles/"

INORDER5K   = "inorder5k.txt"
INORDER10K  = "inorder10k.txt"
INORDER100K = "inorder100k.txt"
RANDOM5K    = "random5k.txt"
RANDOM10K   = "random10k.txt"
RANDOM100K  = "random100k.txt"
REV5K       = "rev5k.txt"
REV10K      = "rev10k.txt"
REV100K     = "rev100k.txt"

FILES = [INORDER5K, INORDER10K, INORDER100K, RANDOM5K, RANDOM10K, RANDOM100K, 
         REV5K, REV10K, REV100K]

def insertionSort(a):

    # start tracking the algorithm run time
    start = time.time_ns()

    for i in range(1, len(a)):

        key = a[i]
        j = i -1

        while j > 0 and a[j] > key:
            a[j + 1] = a[j]
            j-1

        a[j + 1] = key

    # stop tracking the algorithm run time
    end = time.time_ns()

    # finding the total algorithm run time
    total = end - start

    # print(a)
    print('Time: ', total)

def main():

    results = {}

    for filename in FILES:

        # initializing empty list, opens file and stores first element in num variable
        a = []
        f = open(PATH+filename, "r")
        num = f.readline()

        # appending each number to the list
        while num:

            a.append(int(num))      # adds current element stored under num
            num = f.readline()      # reads next element in file

        # closing each file after every element has been added
        f.close()

        # storing output of insertionSort in variable
        fileResults = insertionSort(a)

        # inserts file results into results dictionary
        results[filename] = fileResults

        print("completed sort for %s" % filename)

    print(results)

#main()

a = [38, 1, 3, 9, 7]
print(insertionSort(a))
