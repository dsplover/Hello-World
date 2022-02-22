import re
re_endnum = re.compile(r"(?P<mychar>\w+[^0-9]+)(?P<mynum>[0-9]*)$")
# re_endnum = re.compile(r"(?P<mychar>[a-zA-Z0-9_\u4e00-\u9fa5]+[^0-9]+)(?P<mynum>[0-9]*)$")
#匹配以数字结尾的字符串，返回非数字部分
#str_n:可能以数字结尾的字符串
#re_num:是否返回2个值，不带数字的字符串和数字字符串
def str_num(str_n='',re_num=False):
    str_group=re_endnum.match(str_n)
    if str_group:
        mystr,mynum=str_group.group('mychar'),str_group.group('mynum')
        mynum = int(mynum) if mynum else ''
    else:
        mystr,mynum = str_n,''
    if not re_num:
        return mystr
    else:
        return mystr,mynum