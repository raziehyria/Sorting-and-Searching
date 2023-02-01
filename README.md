# Sorting-and-Searching
Linear, binary search + selection, insertion, bubble and merge sort on randomly generayed 50k or 10k long, integer holding lists + time analysis
CMPSC-462 –Data Structures and Algorithms
PROJECT-2

# Goal
The goal of this project is to perform search and sorting algorithms on an array/list and 
perform Time Complexity analysis on each function.
Write a program to perform Search and Sorting on randomly generated 10,000 and 50,000 
integers. 
# Instructions
1. Generate at least 10000 random numbers and store those in a list (name the list as 
Pool). 
2. Generate a random number and call it as Target (use random.randint()).
3. Perform Linear Search and Binary Search to find Target in Pool. write each as a function.
Note: Binary search can be performed on sorted integers. Perform a sorting (call a 
sorting function) before calling binary search.
4. Perform Max/Min number search on the unsorted list. write each as a function.
5. Find/Search whether the unsorted list have distinct numbers. If it have distinct numbers 
return true and return false otherwise.  If false, print the numbers which are not 
distinct. write it as a function.
6. Calculate the time taken for each function to perform the search. Note: for binary 
search, do not include the time taken for sorting the list.  
7. Perform the following sorting on the Pool (write each as a function):
  * Selection Sort
  * Insertion Sort
  * Bubble Sort
  * Merge Sort.
  
     Note  (Very  Important):  perform  these  sorting  on  the  unsorted  list.  Once  you  perform  a 
sorting,  the  list  would  be  sorted/ordered.  Do  not  apply  another  sorting  on  the  same  list.  So, 
before  applying  a  sorting,  make  a  copy  of  the  unsorted  list  and  apply  sorting  on  this  unsorted 
list. You can write a simple for loop or use inbuilt function to create a copy of the list.

8. Calculate the time taken for each sorting functions. If you get zero as recorded time, you 
can increase the number of elements to be sorted.   
Note:
 Create a class file and call it as SearchClass. SearchClass should contain the search 
functions including max/min and distinct functions.
 Create another class file and call it as SortingClass. SortingClass should contain all the 
sorting functions. 
 Call these appropriate class in your main class/function to perform the operations.
 All the required algorithms are covered in your lecture notes.

9. Perform these operations 3 times i.e. apply these functions on randomly generated 
numbers 3 times.  Tabulate the results.

10. Continue the steps 1 – 9 for 50,000 random numbers. Tabulate the results.
Report:    The project report should contain the following:
