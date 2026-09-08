#  Runtime Comparison Chart Data and Scalability Report

import math

class Solution:
    def solve(self, k, arr):
        print("Runtime Comparison Chart Data")
        print("InputSize LinearSearch BinarySearch BubbleSort InsertionSort")

        for n in arr:
            linear = n
            binary = int(math.log2(n)) + 1
            bubble = n * (n - 1) // 2
            insertion = n * (n - 1) // 2

            print(n, linear, binary, bubble, insertion)

        print("Scalability Summary")
        print("Algorithm Complexity Scalability")
        print("Linear Search O(n) Moderate")
        print("Binary Search O(log n) Excellent")
        print("Bubble Sort O(n^2) Poor")
        print("Insertion Sort O(n^2) Poor")

        print("Key Observations")
        print("Binary Search scales best with increasing input size.")
        print("Linear Search has moderate scalability.")
        print("Bubble Sort and Insertion Sort have poor scalability.")

        print("Conclusion")
        print("Binary Search is the most scalable algorithm, while Bubble Sort and Insertion Sort are least scalable.")