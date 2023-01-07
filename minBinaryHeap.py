class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None

        min_val = self.heap[0]
        
        # Allows the removal of the element to be done in O(log n) time
        self.heap[0] = self.heap[-1] 
        del self.heap[-1]
        self._bubble_down(0)

        return min_val
    
    def modify_key(self, i, new_val):
        self.heap[i] = new_val

        self._bubble_up(i)
        if self.heap[i] == new_val:
            self._bubble_down(i)
    
    def _bubble_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._bubble_up(parent)
    
    def _bubble_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        min_index = i

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._bubble_down(min_index)

if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(2)
    heap.insert(4)
    print(heap.extract_min())  # prints 2
    print(heap.extract_min())  # prints 3
    heap.insert(1)
    print(heap.extract_min())  # prints 1
    print(heap.extract_min())  # prints 4
    print(heap.extract_min())  # prints 5
    print(heap.extract_min())  # prints None