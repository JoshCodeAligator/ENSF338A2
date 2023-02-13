import sys
from urllib.request import urlopen
import json
from matplotlib import pyplot as plt
from timeit import default_timer as timer


sys.setrecursionlimit(20000)
url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json'




json_file = urlopen(url)

data = json.loads(json_file.read())


def func2(array, start, end):
  if end - start <= 1:
    return start

  mid = (start + end) // 2
  if array[start] > array[end-1]:
    array[start], array[end-1] = array[end-1], array[start]
  if array[mid] > array[end-1]:
    array[mid], array[end-1] = array[end-1], array[mid]
  if array[start] > array[mid]:
    array[start], array[mid] = array[mid], array[start]

  pivot = array[mid]
  low = start + 1
  high = end - 2

  while low <= high:
    while low <= high and array[high] >= pivot:
      high = high - 1
    while low <= high and array[low] <= pivot:
      low = low + 1
    if low <= high:
      array[low], array[high] = array[high], array[low]
  
  array[mid], array[high+1] = array[high+1], array[mid]
  return high + 1


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    

frequency = []
time_results = []
i = 0

for arr in data:
     start_time = timer()
     time = func1(arr, 0, len(arr)-1)
     time_results.append(timer() - start_time)
     i += 1
     frequency.append(i)

print(frequency)
print(time_results)

plt.scatter(frequency, time_results)
plt.title("Quick Sort Time Plot")
plt.xlabel("Frequency")
plt.ylabel("Time Results")
plt.show()