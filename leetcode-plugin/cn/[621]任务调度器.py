#给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，
# 并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 
#
# 你需要计算完成所有任务所需要的最短时间。 
#
# 示例 1： 
#
# 
#输入: tasks = ["A","A","A","B","B","B"], n = 2
#输出: 8
#执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# 
#
# 注： 
#
# 
# 任务的总个数为 [1, 10000]。 
# n 的取值范围为 [0, 100]。 
# 
#

"""
完成所有任务的最短时间取决于出现次数最多的任务数量。

看下题目给出的例子

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
因为相同任务必须要有时间片为 n 的间隔，所以我们先把出现次数最多的任务 A 安排上（当然你也可以选择任务 B）。例子中 n = 2，那么任意两个任务 A 之间都必须间隔 2 个单位的时间：

A -> (单位时间) -> (单位时间) -> A -> (单位时间) -> (单位时间) -> A
中间间隔的单位时间可以用来安排别的任务，也可以处于“待命”状态。当然，为了使总任务时间最短，我们要尽可能地把单位时间分配给其他任务。现在把任务 B 安排上：

A -> B -> (单位时间) -> A -> B -> (单位时间) -> A -> B
很容易观察到，前面两个 A 任务一定会固定跟着 2 个单位时间的间隔。最后一个 A 之后是否还有任务跟随取决于是否存在与任务 A 出现次数相同的任务。

该例子的计算过程为：

(任务 A 出现的次数 - 1) * (n + 1) + (出现次数为 3 的任务个数)，即：

(3 - 1) * (2 + 1) + 2 = 8
所以整体的解题步骤如下：

计算每个任务出现的次数
找出出现次数最多的任务，假设出现次数为 x
计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
特殊情况
然而存在一种特殊情况，例如：

输入: tasks = ["A","A","A","B","B","B","C","C","D","D"], n = 2
输出: 10
执行顺序: A -> B -> C -> A -> B -> D -> A -> B -> C -> D
此时如果按照上述方法计算将得到结果为 8，比数组总长度 10 要小，应返回数组长度。

代码实现


"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1

        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

class Solution1:
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0

        count = 0
        while tasks:
            now = tasks.pop()
            for i in range(0, len(tasks)):
                if tasks[i] != now:
                    tasks.pop(i)
            count += 2

        return count

    def leastInterval1(self, tasks, n):
        length_tasks = len(tasks)
        sorted_tasks = sorted(tasks)
        sorted_num = []
        num = 1
        for i in range(1, len(sorted_tasks)):
            if (sorted_tasks[i] != sorted_tasks[i - 1]):
                sorted_num.append(num)
                num = 1
            if (sorted_tasks[i] == sorted_tasks[i - 1]):
                num += 1
        sorted_num.append(num)
        sorted_num.sort()

        last = sorted_num.pop()
        last_num = last
        same_max = 0
        while (last_num == last):
            same_max += 1
            if (sorted_num == []):
                break
            last = sorted_num.pop()
        same_max -= 1

        short_time = (last_num - 1) * n + last_num + same_max
        print(short_time)
        return max(short_time, length_tasks)

tasks = ["A","A","A","B","B","B"]
n = 2
# print(Solution().leastInterval(tasks, n))
print(Solution().leastInterval1(tasks, n))