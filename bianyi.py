
import re

# 关键字表
key = {
    'if': 1,
    '+': 9,
    '=': 13,
    '>': 14,
    'return': 15,
    ';': 16,
}

with open('bianyi.txt', 'r') as f:      # 读取文件
    data = f.read()
    data1 = re.split(' ''|\n',data)     # 分割字符串
    f.close()
    
def test(data1):
    rule = re.compile('^[a-zA-z]{1}.*$')
    for i in data1:
        if i in key:            # 如果是关键字，则输出关键字的编号
            print((key[i],i))
        elif i.isdecimal():     # 判断是否是数字
            print((11,int(i)))
        elif rule.match(i):     # 判断是否是标识符
            print((7,i))  
        else:                   # 其他情况，则输出其他情况的编号
            print(('不合法符号',i))
            
if __name__ == '__main__':      # 测试函数
    test(data1)
   
    
    
    
    