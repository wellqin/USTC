# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        约瑟夫环
Description :   
Author :          wellqin
date:             2019/7/15
Change Activity:  2019/7/15
-------------------------------------------------
"""
"""
1、方法一：数组
在大一第一次遇到这个题的时候，我是用数组做的，我猜绝大多数人也都知道怎么做。方法是这样的：
用一个数组来存放 1，2，3 … n 这 n 个编号，如图（这里我们假设n = 6, m = 3）
然后不停着遍历数组，对于被选中的编号，我们就做一个标记，例如编号 arr[2] = 3 被选中了，
那么我们可以做一个标记，例如让 arr[2] = -1，来表示 arr[2] 存放的编号已经出局的了。
然后就按照这种方法，不停着遍历数组，不停着做标记，直到数组中只有一个元素是非 -1 的，这样，剩下的那个元素就是我们要找的元素了。

这种方法简单吗？思路简单，但是编码却没那么简单，临界条件特别多，每次遍历到数组最后一个元素的时候，还得重新设置下标为 0，
并且遍历的时候还得判断该元素时候是否是 -1。感兴趣的可以动手写一下代码，用这种数组的方式做，千万不要觉得很简单，
编码这个过程还是挺考验人的。

这种做法的时间复杂度是 O(n * m), 空间复杂度是 O(n);

 新环是由  (旧环中编号-最大报数值)%旧总人数  得到的，所以逆推时可以由 ( 新环中的数字 + 最大报数值 )% 旧总人数 取得。
 即 old_number = ( new_number + value ) % old_sum.
"""

def josephus(n,k):
    if n < 1:
        return -1

    index = 0
    people = list(range(1, n+1))
    while people:
        if len(people) == 1:
            break
        index = (index + (k-1)) % len(people)    # k-1 下标从0开始
        print('kill:', people[index])
        del people[index]                        # list del掉自动补位，其他语言估计要费力些
    print('survive:', people)

josephus(8,3)
josephus(10, 4)


def lastRemaining(n, m):
    if n < 1:
        return -1
    con = list(range(n))
    final = -1
    start = 0
    while con:
        k = (start + m - 1) % n
        final = con.pop(k)
        n -= 1
        start = k
    return final


res = lastRemaining(10, 4)
print("lastRemaining", res)  # 4

# 代码2:  一共有三十个人，从1-30依次编号。每次隔9个人就踢出去一个人。求踢出的前十五个人的号码：

a = [ x for x in range(1,31) ] # 生成编号
del_number = 8                 # 该删除的编号
for i in range(15):
   print("踢出的前十五个人的号码", a[del_number])
   del a[del_number]
   del_number = (del_number + 8) % len(a)

"""
2、方法二：环形链表
学过链表的人，估计都会用链表来处理约瑟夫环问题，用链表来处理其实和上面处理的思路差不多，只是用链表来处理的时候，
对于被选中的编号，不再是做标记，而是直接移除，因为从链表移除一个元素的时间复杂度很低，为 O(1)。当然，
上面数组的方法你也可以采用移除的方式，不过数组移除的时间复杂度为 O(n)。
"""

class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def createLinkList(total):
    head = LinkNode(1)
    prev = head
    index = 2

    while total - 1 > 0:
        cur = LinkNode(index)
        prev.next = cur
        prev = prev.next
        index += 1
        total -= 1

    cur.next = head
    return head


# 模拟从1开始计数
def run( total, m ):
    assert total >= 0, 'total should lq 0'
    assert m >= 0, 'm should lt 0'

    node = createLinkList(total)
    prev = None
    start = 1
    index = start
    while node and node.next:

        if index == m:
            print('pop:'+ str(node.val))
            prev.next = node.next
            node.next = None
            node = prev.next
            index = start
        else:
            prev = node
            node = node.next
            index += 1
    return prev.val
print("环形链表", run(10, 4))



def f(n, m):
    if(n == 1):
        return n;
    return (f(n - 1, m) + m - 1) % n + 1;

print("递归", f(10, 4))

































