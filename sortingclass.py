"""Selection Sort
 Insertion Sort
 Bubble Sort
 Merge Sort."""
from timeit import default_timer as timer


class SortingClass:

    def __init__(self):
        self.pool = []

    def selectionSort(self, pool):
        start = timer()  # function used to measure the time it takes for function to run
        # Iterate through the list
        for i in range(len(pool) - 1, 0, -1):
            currentmax = 0
            for location in range(1, i + 1):
                # find the smallest value in the list
                if pool[location] > pool[currentmax]:
                    currentmax = location  # switch it with the value in the first position
            # swap values
            temp = pool[i]
            pool[i] = pool[currentmax]
            pool[currentmax] = temp

        end = timer()
        time = end - start
        print("Elapsed time: ", time, "ms")

    def insertionSort(self, pool):
        start = timer()
        for i in range(1, len(pool)):  # traverse4 through the list
            current = pool[i]
            position = i
            # compare the current val with each element until something smaller is found
            while position > 0 and pool[position - 1] > current:
                pool[position] = pool[position - 1]
                position = position - 1
            # shift elements that are greater than the current position

            pool[position] = current
        end = timer()
        time = end - start
        print("Elapsed time: ", time, "ms")

    def bubbleSort(self, pool):
        start = timer()
        # scan the list
        for num in range(len(pool) - 1, 0, -1):
            # scan the list again, bubbling up the second highest value
            for i in range(num):
                # exchanging adjacent elements if they are not in relative order;

                # swap if the element found is greater than the next element
                if pool[i] > pool[i + 1]:
                    temp = pool[i]
                    pool[i] = pool[i + 1]
                    pool[i + 1] = temp
        end = timer()
        time = end - start
        print("Elapsed time: ", time, "ms")

    def mergeSort(self, pool):

        if len(pool) > 1:
            mid = len(pool) // 2
            left = pool[:mid]  # creating sub arrays
            right = pool[mid:]
            # divide the list into two roughly equal parts
            self.mergeSort(left)
            self.mergeSort(right)
            # recursively divide each part in half, continuing until a
            # part contains only one element
            i = 0  # initial index of sub arrays
            j = 0
            k = 0  # initial index of merged subarray
            # merge the two parts into one sorted list
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    pool[k] = left[i]
                    i = i + 1
                else:
                    pool[k] = right[j]
                    j = j + 1
                k = k + 1
            # copy remaining elements if any exist
            while i < len(left):
                pool[k] = left[i]
                i = i + 1
                k = k + 1
            # continue to merge parts as the recursion unfolds
            while j < len(right):
                pool[k] = right[j]
                j = j + 1
                k = k + 1
