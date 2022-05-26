import datetime
from time import sleep
import pymysql
import matplotlib.pyplot as plt
import numpy as np

def read(cur):
    select = cur.execute("SELECT * FROM py_t_h")
    print(select)
    
    all = cur.fetchall()
    date = []
    temp = []
    humi = []
    if len(all) > 0:
        for i in all:
            date.append(i[0])
            temp.append(round(float(i[2]),2))
            humi.append(round(float(i[3]),2))
            print(humi)
            print(i)
    return [date,temp,humi]

def pic(date,temp,humi):
    x = np.arange(len(date))  # the label locations
    width = 0.3  # the width of the bars
    
    fig, ax = plt.subplots(1,1,figsize=(17,5))
    rects1 = ax.bar(x+width/3, temp, width, label='Temp')
    rects2 = ax.bar(x-width/3, humi, width, label='Humi')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Num')
    ax.set_title('Temp/Humi')
    ax.set_xticks(x, date)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    # plt.figure(figsize=(500,400))
    plt.show()

if __name__ == '__main__':
    # serial_1 = serial.Serial('COM12',9600,timeout = 1)
    
    con = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='py_t_h',
        charset='utf8'
    )
    # print(con)
    cur = con.cursor()
    data = read(cur)
    pic(data[0],data[1],data[2])
