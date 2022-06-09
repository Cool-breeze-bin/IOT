from time import sleep
from turtle import color
import pymysql
import matplotlib.pyplot as plt
import numpy as np

# 读取数据库函数
def read(cur):
    # 数据库命令
    select = cur.execute("SELECT * FROM py_t_h")
    # print(select)#预览数据概况
    # 获取所有数据
    all = cur.fetchall()
    # 创建列表，存储作图所需要的数据
    date = []
    date1 = []
    temp = []
    humi = []
    # 判断是否有数据
    if len(all) > 0:
        for i in all:
            date.append(i[0])
            date1.append(i[1])
            temp.append(round(float(i[2]),2))
            humi.append(round(float(i[3]),2))
            
    else:
        print("数据库无数据！")
    # 返回作图所需的数据
    return [date,temp,humi,date1,select]

def pic(date,temp,humi):
    x = np.arange(len(date))  # 标签定位
    width = 0.6  # 柱状图宽度
    
    fig, ax = plt.subplots(1,1,figsize=(10,5)) #设置画布参数及尺寸
    # 设置温度图表y轴数据范围
    ax.set_ylim(min(temp)-0.1, max(temp)+0.1)
    # 温度数据作柱状图，颜色为红色
    ax.bar(date,temp,width,color='red',label = 'Temp')
    ax.set_ylabel('Temp')
    
    # 将湿度作为折线图
    ax1 = ax.twinx()
    
    # 设置湿度图表y轴数据范围
    ax1.set_ylim(min(humi)-0.1, max(humi)+0.1)
    # 湿度数据作折线图，颜色为蓝色
    ax1.plot(date,humi,width,color='blue',label='Humi')
    ax1.set_ylabel('Humi')
    # 设置数据标签
    ax.legend(loc=2)
    ax1.legend(loc=1)
    ax.set_xlabel("Data Id")
    plt.show()

if __name__ == '__main__':
    # 连接数据库
    con = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='py_t_h',
        charset='utf8'
    )
    cur = con.cursor()
    data = read(cur)
    # 调用作图函数
    pic(data[0],data[1],data[2])
