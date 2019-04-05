max_predicate = lambda a, b: a > b


class MyTree:

    def push_heap(self, heap, value, predicate=max_predicate):
        heap.append(value)
        current = len(heap) - 1
        while current > 0:
            parent = (current - 1) // 2
            if predicate(heap[current], heap[parent]):
                self.heap_swap(heap, parent, current)
                current = parent
            else:
                break

    def heap_swap(self, heap, a, b):
        t = heap[a]
        heap[a] = heap[b]
        heap[b] = t

    def get_len(self, heap):
        print(len(heap))

    def heap_sort(self, heap):
        print(sorted(heap))

