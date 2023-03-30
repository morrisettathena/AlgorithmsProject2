from mergeSort import mergeSort
from linkedinsertion.LinkedList import LinkedList as LL
from InsertionSort import insertionSort

test = [
    [19, 99, 18, 23, 67, 63, 6, 63, 17, 47],
    [11, 20, 67, 51, 55, 56, 25, 31, 30, 29],
    [96, 64, 92, 89, 68, 7, 92, 17, 37, 35],
    [44, 11, 83, 46, 13, 6, 12, 63, 54, 93],
    [84, 17, 58, 78, 90, 93, 12, 7, 89, 86],
]

sorted_test = [
    [6, 17, 18, 19, 23, 47, 63, 63, 67, 99],
    [11, 20, 25, 29, 30, 31, 51, 55, 56, 67],
    [7, 17, 35, 37, 64, 68, 89, 92, 92, 96],
    [6, 11, 12, 13, 44, 46, 54, 63, 83, 93],
    [7, 12, 17, 58, 78, 84, 86, 89, 90, 93],
]

def testSorts():
    mergeSortCorrect = True
    for i in range(len(test)):
        x = test[i].copy()
        mergeSort(x)
        if x != sorted_test[i]:
            mergeSortCorrect = False
    print("Merge sort correct: " + str(mergeSortCorrect))

    linkedSortCorrect = True
    for i in range(len(test)):
        unsortedList = LL()
        for item in test[i]:
            unsortedList.append(item)

        sortedList = LL()
        for item in sorted_test[i]:
            sortedList.append(item)

        unsortedList.insertionSort()
        if str(unsortedList) != str(sortedList):
            linkedSortCorrect = False
    print("linked sort correct: " + str(linkedSortCorrect))

    iterativeSortCorrect = True
    for i in range(len(test)):
        x = test[i].copy()
        insertionSort(x)
        if x != sorted_test[i]:
            iterativeSortCorrect = False

    print("iterative insertion sort correct: " + str(iterativeSortCorrect))