# create objects rferencing lists to class
from timeit import default_timer as timer
import searchclass
import sortingclass
import random
import copy
import collections

# Generate at least 10000 random numbers and store those in a list (name the list as Pool
pool = []
for i in range(0, 10000):
    n = random.randint(0, 10000)
    pool.append(n)

print("Og Pool: ", pool)

# creating copies of the list to be used for sorting methods
pool2 = copy.deepcopy(pool)
pool3 = copy.deepcopy(pool)
pool4 = copy.deepcopy(pool)

# Generate a random number and call it as Target (use random.randint()).
target = random.randint(0, 10000)
print("Target: ", target)

''' Perform Linear Search and Binary Search to find Target in Pool. write each as a function.
Note: Binary search can be performed on sorted integers. Perform a sorting (call a 
sorting function) before calling binary search
'''
# sorted pool
spool = sorted(pool)
# feeding it to a search object
poolsearch = searchclass.Search()

# not wise to print a 50,000 long list
print("Sorted list: ", spool)


def linearsearch(l, t):
    print("\nLinear Search:")
    if poolsearch.sequentialSearch(l, t) == -1:
        print("element not found")
    else:
        print("Target:", target, "found")


def binsearch(l, t):
    print("\nBinary Search:")
    if not poolsearch.binarySearch(l, t):
        print("element not found")
    else:
        print("Target:", target, "found")


'''Perform Max/Min number search on the unsorted list. write each as a function.'''


def minval(lst):
    return poolsearch.minValue(lst)


def maxval(lst):
    return poolsearch.maxValue(lst)


'''
Find/Search whether the unsorted list have distinct numbers. If it have distinct numbers 
return true and return false otherwise.  If false, print the numbers which are not 
distinct. write it as a function
'''


def distinct(l):
    return poolsearch.distinctValues(l)


def is_distinct(l):
    if not poolsearch.distinctValues(l):
        print("Repeated Values: ", [item for item, count in collections.Counter(l).items() if count > 1])


# calls for the first set of problems
linearsearch(spool, target)
binsearch(spool, target)
print("\nMin: ", minval(pool))
print("\nMax: ", maxval(pool))
print("\nIs it distinct?", distinct(pool))
print(is_distinct(pool))

'''
Perform the following sorting on the Pool (write each as a function)
'''
sortingpool = sortingclass.SortingClass()


# selection sort
def selectionsort(l):
    sortingpool.selectionSort(l)


print("Selection sorted list: ")
selectionsort(pool)


# print("Selection sorted list: ", pool)


# insertion sort
def insersort(l):
    sortingpool.insertionSort(l)


print("Insertion sorted list: ")
insersort(pool2)


# print("Insertion sorted list: ", pool2)


# bubble sort
def bubblesort(l):
    sortingpool.bubbleSort(l)


print("Bubble sorted list: ")
bubblesort(pool3)


# print("Bubble sorted list: ", pool3)


# merge sort
def mergesort(l):
    start = timer()
    sortingpool.mergeSort(l)
    end = timer()
    time = end - start
    print("Elapsed time: ", time, "ms")


print("Merge sorted list: ")
mergesort(pool4)
# print("Merge sorted list: ", pool4)
