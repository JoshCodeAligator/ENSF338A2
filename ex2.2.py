import sys
import random
from urllib.request import urlopen
import json
from matplotlib import pyplot as plt
from timeit import default_timer as timer


sys.setrecursionlimit(20000)
url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json'


json_file = urlopen(url)

data = json.loads(json_file.read())

def func2(array, start, end):
        p = array[start]
        low = start + 1
        high = end
        while True:
            while low <= high and array[high] >= p:
                high = high - 1
            while low <= high and array[low] <= p:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        array[start], array[high] = array[high], array[start]
        return high

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    

frequency = []
time_results = []
random_arr = []
i = 0

for arr in data:
     random.shuffle(arr)
     random_arr.append(arr)
     start_time = timer()
     time = func1(arr, 0, len(arr)-1)
     time_results.append(timer() - start_time)
     i += 1
     frequency.append(i)


with open('ex2.5.json', 'w') as file:
     json.dump(random_arr, file)
    
print(frequency)
print(time_results)

plt.scatter(frequency, time_results)
plt.title("Quick Sort Time Plot")
plt.xlabel("Frequency")
plt.ylabel("Time Results")
plt.show()

