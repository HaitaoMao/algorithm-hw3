import random
import time
import matplotlib.pyplot as plt

import seaborn as sns; sns.set()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


def time_sort(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]

def generate_partially_sorted_list(n, shuffle_percentage=0.1):
    sorted_list = list(range(n))
    shuffle_count = int(n * shuffle_percentage)
    elements_to_shuffle = random.sample(range(n), shuffle_count)
    for i in range(0, shuffle_count, 2):
        if i+1 < shuffle_count:  
            sorted_list[elements_to_shuffle[i]], sorted_list[elements_to_shuffle[i+1]] = sorted_list[elements_to_shuffle[i+1]], sorted_list[elements_to_shuffle[i]]
    return sorted_list

input_sizes = list(range(1, 10)) + list(range(10, 1001, 30))
shuffle_percentages = [i * 0.1 for i in range(11)]
colors = ['#1f77b4','#ff7f0e','#2ca02c','#9467bd','#d62728', '#d67e27'] + sns.color_palette("tab10")


for shuffle_percentage in shuffle_percentages:
    merge_sort_times_random = []
    insertion_sort_times_random = []
    merge_sort_times_partially_sorted = []
    insertion_sort_times_partially_sorted = []
    for n in input_sizes:
        random_list = generate_random_list(n)
        partially_sorted_list = generate_partially_sorted_list(n, shuffle_percentage=shuffle_percentage)  # Adjust shuffle_percentage as needed
        
        merge_sort_times_random.append(time_sort(merge_sort, random_list.copy()))
        insertion_sort_times_random.append(time_sort(insertion_sort, random_list.copy()))

        merge_sort_times_partially_sorted.append(time_sort(merge_sort, partially_sorted_list.copy()))
        insertion_sort_times_partially_sorted.append(time_sort(insertion_sort, partially_sorted_list.copy()))
        
    # import ipdb; ipdb.set_trace()

    plt.plot(input_sizes, merge_sort_times_random, label='Merge Sort on Random List', color=colors[0])
    plt.plot(input_sizes, insertion_sort_times_random, label='Insertion Sort on Random List', color=colors[1])
    plt.plot(input_sizes, merge_sort_times_partially_sorted, label='Merge Sort on Partially Sorted List', color=colors[2])
    plt.plot(input_sizes, insertion_sort_times_partially_sorted, label='Insertion Sort on Partially Sorted List', color=colors[3])
    plt.xlabel('Input Size n')
    plt.ylabel('Execution Time')
    plt.legend()
    plt.title('Sorting Algorithm Performance Comparison')
    # plt.show()
    plt.savefig(f"homework_{shuffle_percentage}.png")
    plt.clf()