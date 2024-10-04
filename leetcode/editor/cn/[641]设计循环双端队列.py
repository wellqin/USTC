#设计实现双端队列。 
#你的实现需要支持以下操作： 
#
# 
# MyCircularDeque(k)：构造函数,双端队列的大小为k。 
# insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。 
# insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。 
# deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。 
# deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。 
# getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。 
# getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。 
# isEmpty()：检查双端队列是否为空。 
# isFull()：检查双端队列是否满了。 
# 
#
# 示例： 
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
#circularDeque.insertLast(1);			        // 返回 true
#circularDeque.insertLast(2);			        // 返回 true
#circularDeque.insertFront(3);			        // 返回 true
#circularDeque.insertFront(4);			        // 已经满了，返回 false
#circularDeque.getRear();  				// 返回 2
#circularDeque.isFull();				        // 返回 true
#circularDeque.deleteLast();			        // 返回 true
#circularDeque.insertFront(4);			        // 返回 true
#circularDeque.getFront();				// 返回 4
#  
#
# 
#
# 提示： 
#
# 
# 所有值的范围为 [1, 1000] 
# 操作次数的范围为 [1, 1000] 
# 请不要使用内置的双端队列库。 
# 
#


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = -1, -1
        self.vec = [None for _ in range(k)]

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.head -= 1
        if self.head < 0:
            self.head = len(self.vec) - 1
        self.vec[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.tail += 1
        if self.tail == len(self.vec):
            self.tail = 0
        self.vec[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.vec[self.head] = None
        self.head += 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.vec[self.tail] = None
        self.tail -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        print(self.head, len(self.vec))
        return self.vec[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.vec[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        for x in self.vec:
            if x != None:
                return False
        return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        for x in self.vec:
            if x == None:
                return False
        return True




class MyCircularDeque2:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.size = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.insert(0,value)
            return True
        else:
            return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return len(self.queue) == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return len(self.queue) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()