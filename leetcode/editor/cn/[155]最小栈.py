#设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。 
#
# 
# push(x) -- 将元素 x 推入栈中。 
# pop() -- 删除栈顶的元素。 
# top() -- 获取栈顶元素。 
# getMin() -- 检索栈中的最小元素。 
# 
#
# 示例: 
#
# MinStack minStack = new MinStack();
#minStack.push(-2);
#minStack.push(0);
#minStack.push(-3);
#minStack.getMin();   --> 返回 -3.
#minStack.pop();
#minStack.top();      --> 返回 0.
#minStack.getMin();   --> 返回 -2.
# 
# Related Topics 栈 设计



#leetcode submit region begin(Prohibit modification and deletion)


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        初始化的时候多定义了一个最小值self.minStack,在每次push和pop操作的时候就判断是否为最小值，保证self.minStack是最小的。
        """
        self.stack = []
        self.minStack = []    # 常数时间内检索到最小元素的栈需要用到辅助栈minStack
                              # 借助一个辅助栈，利用它来存储每次入栈的最小元素。如果只用一个栈，这样的时间复杂度是O(n)

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        存放每一次压入数据时，栈中的最小值（如果压入数据的值大于栈中的最小值就不需要重复压入最小值，小于或者等于栈中最小值则需要压入）
        """
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.isEmpty():
            if self.top() == self.minStack[-1]:   # 移除栈顶元素时，判断是否移除栈中最小值
                self.minStack.pop()
            self.stack.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.minStack[-1]

    def isEmpty(self):
        return len(self.stack) < 1


if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(2)
    minstack.push(0)
    minstack.push(3)
    minstack.push(0)
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#leetcode submit region end(Prohibit modification and deletion)
