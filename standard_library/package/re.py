"""
-------------------------------------------------
File Name:        re
Author :          wellqin
date:             2020/5/4
-------------------------------------------------
正则表达式(Regular Expression)是一种文本模式，包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为"元字符"）。
正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。
"""

# re模块操作
# 1. re模块的使用过程
"""
# 导入re模块
import re

# 使用match方法进行匹配操作,re.match() 能够匹配出以xxx开头的字符串
result = re.match(正则表达式, 要匹配的字符串)

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
result.group()
"""

# 2. re模块示例
result = re.match("life", "life is sort,you need python!")  # 匹配以life开头的语句
print(result.group())

# 匹配单个字符
"""
.   匹配任意1个字符（除了\n）
[] 	匹配[ ]中列举的字符
\d 	匹配数字，即0-9
\D 	匹配非数字，即不是数字
\s 	匹配空白，即 空格，tab键
\S 	匹配非空白
\w 	匹配单词字符，即a-z、A-Z、0-9、_
\W 	匹配非单词字符
"""

# 2.1: .示例
# .的使用
# 匹配单个字符
char = re.match('.', 'M')
print(char.group())  # M

# 匹配一段文字
resultString = re.match("s.ort", "short is long!")
print(resultString.group())  # short

# 2.2: []示例

ret = re.match("h", "hello Python")  # 如果hello的首字符小写，那么正则表达式需要小写的h
print(ret.group())

ret = re.match("H", "Hello Python")  # 如果hello的首字符大写，那么正则表达式需要大写的H
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到3，5到9这个区间的数字
ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
# print(ret.group())















# from types import MethodType
# import re
#
# date = re.compile(
#     '(?:(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)'
#     '?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august'
#     '|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|feb\.?|february|mar\.'
#     '?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.'
#     '?|november|dec\.?|december)\s+(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]'
#     '?\d[-\./][0-3]?\d[-\./]\d{2,4}',
#     re.IGNORECASE)
#
# time = re.compile('\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?', re.IGNORECASE)
#
# phone = re.compile(
#     '((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])'
#     '(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))')
#
# link = re.compile(
#     '(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|(?:construction)|(?:contractors)|'
#     '(?:enterprises)|(?:photography)|(?:immobilien)|(?:management)|(?:technology)|(?:directory)|(?:education)|'
#     '(?:equipment)|(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|(?:computer)|(?:democrat)|'
#     '(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|'
#     '(?:careers)|(?:company)|(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|'
#     '(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|(?:berlin)|(?:camera)|'
#     '(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|(?:monash)|(?:museum)|(?:photos)|(?:repair)'
#     '|(?:social)|(?:tattoo)|(?:travel)|(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|'
#     '(?:email)|(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|(?:arpa)|'
#     '(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|(?:guru)|(?:info)|(?:jobs)|'
#     '(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|'
#     '(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|'
#     '(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|(?:uno)|(?:xxx)|(?:ac)|'
#     '(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)'
#     '|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)'
#     '|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|(?:ck)|(?:cl)'
#     '|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)'
#     '|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)'
#     '|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)'
#     '|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)'
#     '|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)'
#     '|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)'
#     '|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)'
#     '|(?:mt)|(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)'
#     '|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)'
#     '|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)'
#     '|(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|(?:su)|(?:sv)|(?:sx)|(?:sy)'
#     '|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)'
#     '|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|(?:vn)'
#     '|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'".,<>'
#     '?\xab\xbb\u201c\u201d\u2018\u2019])?)',
#     re.IGNORECASE)
#
# email = re.compile(
#     "([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)",
#     re.IGNORECASE)
# ip = re.compile(
#     '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]'
#     '?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
#     re.IGNORECASE)
#
# ipv6 = re.compile(
#     '\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)'
#     '[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)'
#     '(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*',
#     re.VERBOSE | re.IGNORECASE | re.DOTALL)
#
# price = re.compile('[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?')
#
# hex_color = re.compile('(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b')
#
# credit_card = re.compile('((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])')
#
# btc_address = re.compile('(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])')
#
# street_address = re.compile(
#     '\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct'
#     '|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)',
#     re.IGNORECASE)
#
# regexes = {"dates": date,
#            "times": time,
#            "phones": phone,
#            "links": link,
#            "emails": email,
#            "ips": ip,
#            "ipv6s": ipv6,
#            "prices": price,
#            "hex_colors": hex_color,
#            "credit_cards": credit_card,
#            "btc_addresses": btc_address,
#            "street_addresses": street_address}
#
#
# class regex:
#
#     def __init__(self, obj, regex):
#         self.obj = obj
#         self.regex = regex
#
#     def __call__(self, *args):
#         def regex_method(text=None):
#             return [x.strip() for x in self.regex.findall(text or self.obj.text)]
#
#         return regex_method
#
#
# class CommonRegex(object):
#
#     def __init__(self, text=""):
#         self.text = text
#
#         for k, v in list(regexes.items()):
#             setattr(self, k, regex(self, v)(self))
#
#         if text:
#             for key in list(regexes.keys()):
#                 method = getattr(self, key)
#                 setattr(self, key, method())
#
#
#
# parsed_text = CommonRegex("""John, please get that article on www.linkedin.com to me by 5:00PM
#                                on Jan 9th 2012. 4:00 would be ideal, actually. If you have any
#                                questions, You can reach me at (519)-236-2723x341 or get in touch with
#                                my associate at harold.smith@gmail.com""")
#
#
# print(parsed_text.times)
# print(parsed_text.dates)
# print(parsed_text.links)
# print(parsed_text.phones)
# print(parsed_text.emails)

