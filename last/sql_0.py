import datetime
from time import sleep
import pymysql
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
from pynput import keyboard
from pynput.keyboard import Controller, Key, Listener
# def connect():
kb = Controller()
# 监听按压
# def on_press(key):
#     try:
#         print("正在按压:", format(key.char))
#     except AttributeError:
#         print("正在按压:", format(key))


# # 监听释放
# def on_release(key):
#     print("已经释放:", format(key))

#     if key == Key.enter:
#         # break
#         # 停止监听
#         quit()
# def start_listen():
    

def insert(id, temp, humi, box_id,con):
    cur = con.cursor()
    curr_time = datetime.datetime.now()
    data_time = datetime.datetime.strftime(curr_time, '%Y/%m/%d %H:%M:%S')
    cur.executemany("INSERT py_t_h VALUE(%s,%s,%s,%s,%s)", [
                    (str(id), data_time, str(temp), str(humi), box_id)])
    con.commit()

def data_recive(data):
    list_msg = []  # 用于存储获取到的初始温湿度数据
    # read_msg = data.read_all()
    print("\nbytes:", data)
    print("hex:", data.hex())
    print("msg_len:", len(data))
    # 向初始数据列表中插入初始湿度数据
    list_msg.append(
        int(data.hex()[10:12], 16)+int(data.hex()[12:14], 16)*256)
    # 向初始数据列表中插入初始温度数据
    list_msg.append(
        int(data.hex()[14:16], 16)+int(data.hex()[16:18], 16)*256)
    print(list_msg)  # 预览初始数据
    # 计算真实数据所需参数
    c1 = -4.0
    c2 = 0.0405
    c3 = -0.0000028
    t1 = 0.01
    t2 = 0.00008
    d1 = -42
    d2 = 0.01
    # 使用公式分别计算真实温度和湿度
    rh0 = c1 + c2*list_msg[0] + c3*(list_msg[0]*list_msg[0])
    t = d1 + d2 * list_msg[1]
    rh1 = (t-25)*(t1 + t2*list_msg[0])+rh0
    print('temp:', t, "\thumi:", rh1)  # 输出真实温湿度
    # round函数保留得到数据的小数点后两位
    return [round(t,2), round(rh1,2)]

# def main():
#     serial_1 = serial.Serial('COM12',9600,timeout = 1)
#     con = pymysql.connect(
#         host='127.0.0.1',
#         port=3306,
#         user='root',
#         passwd='123456',
#         db='py_t_h',
#         charset='utf8'
#     )
#     box_id = 'W-2020-001'
#     id = 0
#     while True:
#         data = serial_1.read_all()
#         if len(data) == 10:
#             data_1 = data_recive(data)
#             insert(id,data_1[0],data_1[1],box_id,con)
#             id = id + 1
#             sleep(5)
#         if id == 100:
#             con.close()
#             serial_1.close
#             print('结束采集！')
#             break

if __name__ == '__main__':
    serial_1 = serial.Serial('COM12',9600,timeout = 1)
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
    box_id = 'W-2020-001'
    id = 0
    while True:
        data = serial_1.read_all()
        if len(data) == 10:
            data_1 = data_recive(data)
            insert(id,data_1[0],data_1[1],box_id)
            id = id + 1
            sleep(5)
        if id == 100:
            con.close()
            serial_1.close
            print('结束采集！')
            break
