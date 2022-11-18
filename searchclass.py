from timeit import default_timer as timer


class Search:
    def __init__(self):
        self.pool = []  # class search object

    def sequentialSearch(self, pool, item):
        start = timer()
        try:  # implemented try finally feature to ensure time function is in range of function after val returned
            for i in range(len(pool)):  # iterate through pool
                if pool[i] == item:  # check if current is the target
                    return i  # return if found
            return -1  # otherwise not present
        finally:
            end = timer()
            time = end - start
            print("Elapsed time: ", time, "ms")

    def binarySearch(self, pool, item):
        start = timer()
        left = 0
        right = len(pool) - 1  # used for splitting the list
        found = False  # initial true value for unfound value
        try:
            while left <= right and not found:  # iterate while the target isn't found
                mid = (left + right) // 2  # split the list
                if pool[mid] == item:  # if the mid item is the target, return
                    found = True
                else:
                    if item < pool[mid]:  # otherwise dictate if the left or right side should be updated
                        right = mid - 1
                    else:
                        left = mid + 1
            return found
            # If we reach here the element is not found
        finally:
            end = timer()
            time = end - start
            print("Elapsed time: ", time, "ms")

    def maxValue(self, pool):
        start = timer()
        currentmax = 0
        try:
            for i in pool:  # iterate through the list
                if i > currentmax:  # if the current position is more than current value, replace it
                    currentmax = i
            return currentmax
        finally:
            end = timer()
            time = end - start
            print("Elapsed time: ", time, "ms")

    def minValue(self, pool):
        start = timer()
        currentmin = 0
        try:
            for i in pool:  # iterate through the list
                if i < currentmin:  # if the current position is less than current min value, replace it
                    currentmin = i
            return currentmin
        finally:
            end = timer()
            time = end - start
            print("Elapsed time: ", time, "ms")

    def distinctValues(self, pool):
        start = timer()
        try:
            if len(pool) == len(set(pool)):  # compares the len of a set of the list and len of list
                return True  # if the list is the same size, then the list is distinct
            else:
                return False  # otherwise the list is not distinct

        finally:
            end = timer()
            time = end - start
            print("Elapsed time: ", time, "ms")
