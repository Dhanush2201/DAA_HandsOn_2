import timeit
import random
import matplotlib.pyplot as plt

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection(arr):
    n = len(arr)
    for i in range(n):
        j = i
        for k in range(i + 1, n):
            if arr[k] < arr[j]:
                j = k
        arr[i], arr[j] = arr[j], arr[i]

def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def benchmark(algorithm, arr):
    return timeit.timeit(lambda: algorithm(arr.copy()), number=10)

def benchmarks(input_sizes):
    algorithms = [insertion, selection, bubble]
    algorithm_names = ["Insertion Sort", "Selection Sort", "Bubble Sort"]
    all_runtimes = [[] for _ in range(len(algorithms))]

    for size in input_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        for algorithm, name, runtimes in zip(algorithms, algorithm_names, all_runtimes):
            runtime = benchmark(algorithm, arr)
            runtimes.append(runtime)
            print(f"{name} for input size {size}: {runtime} s, Ram : 16GB, CPU: AMD Ryzen 7 7730U ")

    return all_runtimes

input_sizes = [5, 50, 100, 500, 1000, 2500, 5000] 
algorithm_runtimes = benchmarks(input_sizes)

plt.figure(figsize=(10, 6))
for runtimes, name in zip(algorithm_runtimes, ["Insertion Sort", "Selection Sort", "Bubble Sort"]):
    plt.plot(input_sizes, runtimes, label=name)

plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Sorting Algorithm Runtimes')
plt.legend()
plt.show()
