from mergeSort import main as MergeSort
from InsertionSort import main as IterativeInsertion
from linkedListRun import main as LinkedInsertion
from test import testSorts

RUN_TESTSORTS = True
RUN_MERGESORT = True
RUN_ITERATIVEINSERTION = True
RUN_LINKEDINSERTION = True

def main():
    if RUN_TESTSORTS:
        print("*"*40)
        print("testing sorts")
        testSorts()
        print("*"*40 + "\n")
    if RUN_MERGESORT:
        print("*"*40)
        print("Running merge sort")
        MergeSort()
        print("*"*40 + "\n")
    if RUN_ITERATIVEINSERTION:
        print("*"*40)
        print("Running iterative insertion")
        IterativeInsertion()
        print("*"*40 + "\n")
    if RUN_LINKEDINSERTION:
        print("*" * 40)
        print("Running linked insertion")
        LinkedInsertion()
        print("*" * 40 + "\n")

main()