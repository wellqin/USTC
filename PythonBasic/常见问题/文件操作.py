# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        文件操作
Description :   
Author :          wellqin
date:             2019/7/27
Change Activity:  2019/7/27
-------------------------------------------------
"""


"""
读写文件比较简单，有一点特别注意就好了

windows下Python默认打开的文件以gbk解码，而一般我们的文件是utf-8编码的，所以如果文本含有中文，就会出现异常或者乱码。
此时手动添加encoding='utf-8'表示以utf-8的方式打开。

当然Python写入时候，也是默认以gbk的编码写入。
而文件通常是utf-8格式保存的，所以若不指定写入的编码方式，一写入中文就是乱码了
"""
# with open('C:\\Users\QWust\Desktop\\abc.txt', encoding='utf-8') as f:
    # print(f.read())  # 这样打开文件有中文也不怕, 一次性读取文件的所有内容放在一个大字符串中
    # print(f.readline())  # readline()逐行读取文本，结果是返回一个字符串
    # print(f.readlines())   # readlines()一次性读取文本的所有内容，结果是一个list
#
# # 当然Python写入时候，默认以gbk的编码写入。而文件是utf-8格式保存的，所以不指定写入的编码方式，一写入中文就是乱码了
#
# with open('C:\\Users\QWust\Desktop\\abc.txt', 'w', encoding='utf-8') as f:   # 去掉并没有乱
#    f.write('你好')


"""
Python的文本处理是经常碰到的一个问题，Python的文本文件的内容读取中，有三类方法：read()、readline()、readlines()
read()是最简单的一种方法，一次性读取文件的所有内容放在一个大字符串中，即存在内存中,但是文件过大的时候，占用内存会过大
readline()逐行读取文本，结果是返回一个字符串， 占用内存小，逐行读取， 由于是逐行读取，速度比较慢，
每行文本末尾都会带一个'\n'换行符 (可以使用L.rstrip('\n')去掉换行符）

readlines()一次性读取文本的所有内容，结果是一个list
"""


str_context = """The US media reports suggest Robert Mueller's inquiry has taken the first step towards possible criminal charges.
According to Reuters news agency, the jury has issued subpoenas over a June 2016 meeting between President Donald Trump's son and a Russian lawyer.
The president has poured scorn on any suggestion his team colluded with the Kremlin to beat Hillary Clinton.
In the US, grand juries are set up to consider whether evidence in any case is strong enough to issue indictments for a criminal trial. They do not decide the innocence or guilt of a potential defendant.
The panel of ordinary citizens also allows a prosecutor to issue subpoenas, a legal writ, to obtain documents or compel witness testimony under oath.
Trump: US-Russia relations are at 'dangerous low'
The Trump-Russia saga in 200 words
Russia: The 'cloud' over the White House
Now it's deadly serious
Anthony Zurcher, BBC North America reporter
Robert Mueller's special counsel investigation has always been a concern for the Trump administration. Now it's deadly serious business.
With the news that a grand jury has been convened in Washington DC, and that it is looking into the June 2016 meeting between Donald Trump Jr and Russian nationals, it's clear the investigation is focusing on the president's inner circle.
This news shouldn't come as a huge shock, given that Mr Mueller has been staffing up with veteran criminal prosecutors and investigators. It is, however, a necessary step that could eventually lead to criminal indictments. At the very least it's a sign that Mr Mueller could be on the trail of something big - expanding the scope beyond former National Security Adviser Michael Flynn and his questionable lobbying. It also indicates his investigation is not going to go away anytime soon.
In the past, when big news about the Russia investigation has been revealed, Mr Trump has escalated his rhetoric and taken dead aim at his perceived adversaries. The pressure is being applied to the president. How will he respond?
At a rally in Huntington, West Virginia, on Thursday evening, Mr Trump said the allegations were a "hoax" that were "demeaning to our country".
"The Russia story is a total fabrication," he said. "It's just an excuse for the greatest loss in the history of American politics, that's all it is."
The crowd went wild as he continued: "What the prosecutor should be looking at are Hillary Clinton's 33,000 deleted emails."
"Most people know there were no Russians in our campaign," he added. "There never were. We didn't win because of Russia, we won because of you, that I can tell you."
Mr Trump's high-powered legal team fielding questions on the Russia inquiry said there was no reason to believe the president himself is under investigation.
Ty Cobb, a lawyer appointed last month as White House special counsel, said in a statement: "The White House favours anything that accelerates the conclusion of his work fairly.
"The White House is committed to fully co-operating with Mr Mueller."
Earlier on Thursday, the US Senate introduced two separate cross-party bills designed to limit the Trump administration's ability to fire Mr Mueller.
The measures were submitted amid concern the president might dismiss Mr Mueller, as he fired former FBI director James Comey in May, citing the Russia inquiry in his decision."""

# # 词频统计
# # 打开要统计的文档
# with open('C:\\Users\QWust\Desktop\\abc.txt', encoding='utf-8') as f:
#     lines = f.read()
# cptj = {}
# #将词频统计的结果存放到一个字典中
# lines = lines.replace('\n', '').lower().split(" ")  # split以空格为分隔符，包含 \n
# for line in lines:
#     if line in cptj:
#         cptj[line] += 1
#     else:
#         cptj[line] = 1
# # 将字典转化为类表方便进行后续的处理
# lcptj = list(cptj.items())
# #对生成的结果进行排序，按照每个元祖下标为1的数进行排序
# lcptj.sort(key=lambda x: x[1], reverse=True)
# count=0
# #将结果进行输出
# for i in lcptj:
#     print(i,"\t",end='')
#     count+=1
#     #对结果输出做出美化，使其每行打印出五个元素
#     for j in range(int(len(lcptj)/5)+1):
#         if count== 5*j:
#             print()
#         else:
#             pass

print("========================================")

"""
由于字典是个无序的结构，所以最终返回的是一个列表，没有排序好的字典这一说法。其中
key=lambda x:x[1] 其中X表示某一迭代出来的元素，其实是个元组，而x[1] 表示元组的第二个元素，即单词的次数(词频)，若要按照单词排序则改成
key=lambda x:x[0]即可。

# 关于 string 的 replace 方法，需要注意 replace 不会改变原 string 的内容。
print str.replace("is", "was");   把str中的is换成was， str.replace(old, new[, max])


sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，
而不是在原来的基础上进行的操作。

sorted(iterable[, cmp[, key[, reverse]]])

可迭代对象：count_dict.items()
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse = True 降序 ， reverse = False 升序（默认）。
"""


def wordcount1():
    with open('C:\\Users\QWust\Desktop\\abc.txt', encoding='utf-8') as f:
        lines = f.read()

    strl_list = lines.replace('\n', '').lower().split(" ")
    print(strl_list)

    count_dict = {}
    for str in strl_list:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)  # 利用key
    return count_list


print(wordcount1())