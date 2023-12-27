"""
Sorts an array of N rational numbers in ascending order.

Implements Merge sortm quick sort, and bubble sort,
compares their performance and generate a graph.
"""

import random
import time
import matplotlib.pyplot as plt
from typing import List


def merge_sort(array: List[float]) -> None:
    """Sorts the array using merge sort algorithm.

    1- Base case: If the array has only one element, return.
    2- Split the array into two halves, recursively.
    3- Compare the first element of each half,
      and add the smallest to the merged array.
    4- Repeat step 3 until one of the halves is empty.
    5- Add the remaining elements.

    avg time complexity: O(n log n), best case: O(n log n), worst case: O(n log n)
    uses more memory than quick sort.
    """
    if len(array) > 1:
        mid: int = len(array) // 2
        left: List[float] = array[:mid]
        right: List[float] = array[mid:]

        merge_sort(left)
        merge_sort(right)

        # Merge the two sorted halves
        i: int = 0  # left half index
        j: int = 0  # right half index
        k: int = 0  # merged array index

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        # Check if any element was left
        # add them to the merged array
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

            while j < len(right):
                array[k] = right[j]
                j = j + 1
                k = k + 1


def quick_sort(array: List[float]) -> None:
    """Sorts the array using quick sort algorithm.

    1- Base case: If the array has only one element, return.
    2- Choose a pivot element. (mid element, in this implementation)
    3- Partition the array around the pivot. (one list of elements smaller
        than the pivot, one list of elements greater than the pivot)
    4- Recursively sort the two halves.

    avg time complexity: O(n log n), best case: O(n log n),worst case: O(n^2)
    """
    if len(array) > 1:
        mid: int = len(array) // 2
        pivot: float = array[mid]
        left: List[float] = [x for i, x in enumerate(array) if i != mid and x <= pivot]
        right: List[float] = [x for i, x in enumerate(array) if i != mid and x > pivot]

        quick_sort(left)
        quick_sort(right)

        array[:] = left + [pivot] + right


def bubble_sort(array: List[float]) -> None:
    """Sorts the array using bubble sort algorithm.

    1- Base case: If the array has only one element, return.
    2- Compare each element with its neighbor,
      swap if the element is greater than its neighbor.
    3- Repeat step 2 until the array is sorted.

    This implementation is optimized by checking if the array is already sorted.
    If the array is already sorted, the algorithm will stop. So in the best case,
    the time complexity will be O(n).

    avg time complexity: O(n^2), best case: O(n), worst case: O(n^2)

    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


def generate_random_array(size: int) -> List[float]:
    """Generate an array of random numbers.

    Args:
        size: The size of the array.

    Returns:
        An array of random numbers.

    """
    array: List[float] = []
    for _ in range(size):
        array.append(random.uniform(-10000, 10000))
        # array.append(random.randint(-10000, 10000))
    return array


def main() -> None:
    """Test the sorting algorithms and generate a graph."""
    # Generate random arrays
    sizes: List[int] = [1000, 10000, 100000, 1000000]
    # 10ˆ3, 10ˆ4, 10ˆ5, 10ˆ6 (10ˆ7 too slow for my computer)
    arrays: List[List[float]] = []
    for size in sizes:
        arrays.append(generate_random_array(size))

    # Merge sort
    merge_sort_times: List[float] = []
    for array in arrays:
        start: float = time.time()
        merge_sort(array)
        end: float = time.time()
        merge_sort_times.append(end - start)

    print("Merge sort times: ", merge_sort_times)

    # Quick sort
    quick_sort_times: List[float] = []
    for array in arrays:
        start: float = time.time()
        quick_sort(array)
        end: float = time.time()
        quick_sort_times.append(end - start)

    print("Quick sort times: ", quick_sort_times)

    # Bubble sort
    bubble_sort_times: List[float] = []
    for array in arrays:
        start: float = time.time()
        bubble_sort(array)
        end: float = time.time()
        bubble_sort_times.append(end - start)

    print("Bubble sort times: ", bubble_sort_times)

    # Plot the results
    plt.plot(sizes, merge_sort_times, label="Merge sort")
    plt.plot(sizes, quick_sort_times, label="Quick sort")
    plt.plot(sizes, bubble_sort_times, label="Bubble sort")

    # Set logarithmic scale for the x-axis
    plt.xscale('log')

    # Set the y-axis limit
    plt.ylim(0, 10)

    # Set labels and legend
    plt.ylabel("Time (s)")
    plt.xlabel("Array size (log scale)")
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
