class ListNode: 
    def __init__(self,key, val: int, next, prev):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail = ListNode(0, 0, None, None)
        self.head = ListNode(0, 0, None, self.tail)
        self.tail.next = self.head

    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.next = self.head
        node.prev = self.head.prev
        node.prev.next = node
        node.next.prev = node
        

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node == -1:
            return -1
        self._remove(node)
        value = node.val
        self._add(node)
        return value



        

    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value, None, None)

        if self.cache.get(key, -1) == -1:
            self._add(node)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            value = node.val
            self._add(node)
        if len(self.cache) > self.capacity:
            remove = self.tail.next
            self._remove(remove)
            del self.cache[remove.key]
            




            

        
