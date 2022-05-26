from pip import main

def test_1():
    print(type(1))
    # \xyy: 十六进制
    # \yyy: 八进制
    a = 5
    print(int('10',16))
    print(eval('1.9+1.1'))
    print(str(16))
    # 二进制类型是bytes类型，
    print(type(b'hello')) #二进制
    str_1 = b'hello'
    print(str_1)

    str_2 = str_1.decode('utf-8')
    print(str_2)
    #1字节 = 8bit
    # b'3F'表示的是两个字节
    # B'\x3F'表示的是一个字节，是一个16进制数据0x3f
    # hex（）函数，转化为16进制字符串
    str_3 = b'0x3F'.hex()
    print(str_3)
    
#使用Python连接串口11向端口10发送数据
import serial
import serial.tools.list_ports
# import matplotlib.pyplot as plt
import numpy as np
def test_2(serial_1):
    
    try:
        print(serial_1)
        print(serial_1.portstr)
        # 发送数据
        # serial_1.write(('hellofbb,succelly!'.encode('gbk')))#发送数据
        # serial_1.close()
        
        # 接收数据
        while True:
            read_msg = serial_1.read_all()
            if len(read_msg) != 0:
                print("\nbytes:",read_msg)
                print("hex:",read_msg.hex())
                # print("utf-8:",str(read_msg,encoding='utf-8'))
                # print("gbk:",str(read_msg,encoding='gbk'))
                print("16bit:",int(read_msg.hex(),16))
                # print("10bit:",int(read_msg,10))
                # print(read_msg.)
            if read_msg.hex() == '55':
                break
        serial_1.close()
    except:
        if serial_1.isOpen():
            print('serial.isOpend,now closed:')
            serial_1.close()
#task_3
def test_3(serial_1,list_msg):
    try:
        print(serial_1)
        print(serial_1.portstr)
        # recive data
        while True:
            read_msg = serial_1.read_all()
            if len(read_msg) !=0:
                print('str_16:',str(read_msg))
                # print("\nbytes:",read_msg)
                # print("hex:",read_msg.hex())
                # print("msg_len:",len(read_msg))
                # print("all_16bit:",int(read_msg.hex(),16))
                # print("low_16bit:",int(read_msg.hex()[4:],16))
                # print("low_last_16bit:",int(read_msg.hex()[-2:],16))
                
                # list_msg.append(read_msg[:4])
                # list_msg.append(read_msg[4:])
                # print(list_msg)
                # y = []
                # for i in list_msg:
                #     y.append(int(i.hex()[:],16))
                # print(y)
                # y = []
                # list_msg = []
            # stop recive
            if read_msg.hex() == '55':
                break
        # close
        serial_1.close()
    except:
        if serial_1.isOpen():
            print('serial.isOpend,now closed:')
            serial_1.close()
# matplotlib 

# def matplot():
    #make data
    
               
if __name__ == '__main__':
    serial_1 = serial.Serial('COM11',115200,timeout = 1)
    list_msg = []
    test_3(serial_1,list_msg)
    