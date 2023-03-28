import LinkedList as LL
import time;

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

FILES2 = [REV5K, REV10K, REV100K]

FILES1 = [RANDOM5K]

FILES3 = ["test.txt"]

def readIn(path: str):
    ls = LL.LinkedList()

    f = open(path, "r")
    
    item = f.readline()
    while item:
        ls.append(int(item))
        item = f.readline()

    f.close()
    return ls

def performSorts():
    results = {}

    for filename in FILES:
        ls = readIn(PATH + filename)

        start = time.time_ns()
        fileResults = ls.insertionSort()
        end = time.time_ns()
        results[filename] = fileResults
        print("time to complete: %s" % start-end)
        print("completed sort for %s" % filename)
        print(fileResults)

    print(results)

performSorts()
