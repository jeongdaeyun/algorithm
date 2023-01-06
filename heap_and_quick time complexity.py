import random 
import time
	    
count_ary=[100,200,500,1000,2000,3000,4000,5000]
global key
key = 0

def quickSort(array, start, end):
    global key
    if start >= end: return # 원소가 1개인 경우
    #pivot = random.randint(0,len(array)-1)
    #pivot = start
    pivot = (start + end)//2
    
    left, right = start + 1, end
    
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            key += 1
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            key += 1
            right -= 1
        if left > right: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)
    return key
    
    

def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr):
    global key
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


arr=[random.randint(0,99999) for i in range(100)]
quick_arr = arr.copy()
heap_arr = arr.copy()

start = time.time()
print(heapSort(heap_arr))
end = time.time()
#print(f'heapsort time complexity = {end-start:5.8f}')


#start = time.time()
#print(quickSort(quick_arr, 0, len(quick_arr)-1))
#end = time.time()
#print(f'quicksort time complexity = {end-start:5.8f}')
