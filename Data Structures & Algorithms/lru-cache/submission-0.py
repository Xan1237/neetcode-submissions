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
        

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node == -1:
            return -1
        node.prev.next = node.next
        node.next.prev = node.prev
        value = node.val
        
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev = node
        node.prev.next = node

        
        return value



        

    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value, None, None)

        if self.cache.get(key, -1) == -1:
            self.capacity -= 1
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            node.prev.next = node
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            value = node.val
        
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            node.prev.next = node
        if self.capacity == -1:
            remove = self.tail.next
            self.tail.next = remove.next
            remove.next.prev = self.tail
            del self.cache[remove.key]
            del remove
            self.capacity += 1

            




            

        
