import bisect
from collections import deque

from .base import PriorityQueue


class PriorityQueueByList(PriorityQueue):
    def __init__(self, asc=True):
        super().__init__(asc)
        self.array = []

    def push(self, x):
        if not self.asc:
            x *= -1
        self.array.append(x)

    def pop(self):
        if len(self.array) == 0:
            raise IndexError

        x = min(self.array)

        self.array.remove(x)

        if not self.asc:
            x *= -1
        return x

    def top(self):
        x = min(self.array)

        if not self.asc:
            x *= -1

        return x

    def __len__(self):
        return len(self.array)


class PriorityQueueByOrderedList(PriorityQueue):

    def __init__(self, asc=True):
        super().__init__(asc)
        self.queue = deque()

    def push(self, x):
        if not self.asc:
            x *= -1

        index = bisect.bisect(self.queue, x)
        self.queue.insert(index, x)

    def pop(self):
        x = self.queue.popleft()

        if not self.asc:
            x *= -1

        return x

    def top(self):
        x = self.queue[0]

        if not self.asc:
            x *= -1

        return x

    def __len__(self):
        return len(self.queue)


class PriorityQueueByHeap(PriorityQueue):

    def __init__(self, asc=True, capacity=256):
        super().__init__(asc)
        self.count = 0
        self.capacity = capacity
        self.heap = [0] * capacity

    def push(self, x):
        if not self.asc:
            x *= -1

        if self.count == self.capacity:
            self._resize_heap()

        self.count += 1

        index = self.count - 1
        while index > 0:
            parent = self._parent(index)
            if parent == -1:
                break
            if self.heap[parent] <= x:
                break
            self.heap[index] = self.heap[parent]
            index = parent
        self.heap[index] = x

    def pop(self):
        if self.count == 0:
            raise IndexError

        x = self.heap[0]

        self.heap[0] = self.heap[self.count - 1]
        self.count -= 1

        self._percolate_down(0)

        if not self.asc:
            x *= -1

        return x

    def top(self):
        if self.count == 0:
            raise IndexError

        x = self.heap[0]

        if not self.asc:
            x *= -1

        return x

    def __len__(self):
        return self.count

    def _valid_index(self, index):
        return 0 <= index < self.count

    def _parent(self, index):
        parent = (index - 1) // 2

        if self._valid_index(parent):
            return parent
        else:
            return -1

    def _left_child(self, index):
        left = index * 2 + 1
        if self._valid_index(left):
            return left
        else:
            return -1

    def _right_child(self, index):
        right = index * 2 + 2
        if self._valid_index(right):
            return right
        else:
            return -1

    def _percolate_down(self, index):
        left = self._left_child(index)
        right = self._right_child(index)

        parent = index
        if left == -1 and right == -1:
            pass
        elif right == -1:
            if self.heap[left] < self.heap[index]:
                parent = left
        elif left == -1:
            if self.heap[right] < self.heap[index]:
                parent = right
        elif self.heap[left] <= self.heap[right] and self.heap[left] < self.heap[index]:
            parent = left
        elif self.heap[right] < self.heap[left] and self.heap[right] < self.heap[index]:
            parent = right

        if parent != index:
            tmp = self.heap[index]
            self.heap[index] = self.heap[parent]
            self.heap[parent] = tmp
            self._percolate_down(parent)

    def _resize_heap(self):
        self.heap.extend([0] * self.capacity)
        self.capacity *= 2
