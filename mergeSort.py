"""
The following code allows the user to use mergesort to sort an array
it also incorporates the merge aspect of the code
"""
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

def merge(U, V, mainArr):
    #indexes of: 
    i = 0   #first subarray
    j = 0   #second subarray
    k = 1   #merged array

    #The actual merging process
    while i < len(U) and j < len(V):
        #compars += 3
        if(U[i] < V[j]):  #if the value at A1[i] is the smaller one, it gets added first
            mainArr[k] = U[i]
            i+=1
        else:               #Otherwise, A2[j] is added instead
            mainArr[k] = V[j]
            j+=1
        k+=1

    #double checks if there is ANY term that still needs to be added in
    while i < len(U):
        #compars += 1
        mainArr[k] = U[i]
        i += 1
        k += 1

    while j < len(V):
        #compars += 1
        mainArr[k] = V[j]
        j += 1
        k += 1

    #return compars
        
def mergeSort(mainArr: list):
   n = len(mainArr)
   #compars = 1

   if n > 1:
       mainArr.insert(0, None)
       
       h = n//2 
       U = mainArr[1:h+1].copy()
       V = mainArr[h+1:].copy()

       #sorts the first halves
       #compars += mergeSort(U)
       #compars += mergeSort(V)
       #compars += merge(U, V, mainArr)
       mergeSort(U)
       mergeSort(V)
       merge(U, V, mainArr)
       mainArr.pop(0)

   #return compars
    
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
        start = time.time_ns()
        compars = mergeSort(a)
        elapsed = time.time_ns() - start

        # inserts file results into results dictionary
        fileResults = {"compars": compars, "time": elapsed}
        results[filename] = fileResults

        print("completed sort for %s" % filename)
        print(fileResults)
        

    print(results)

