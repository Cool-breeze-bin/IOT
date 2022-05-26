
#使用Python连接串口11向端口10发送数据
from turtle import color
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import numpy as np
#task_3
def test_3(serial_1,list_msg,ax,ax1,temp,humi,fig):
    list_msg = []   #用于存储获取到的初始温湿度数据
    temp_data = []  #用于存储每次得到的真实温度数据
    humi_data = []  #用于存储每次得到的真实湿度数据
    e = 0  #用于记录获取的数据条数
    try:
        print(serial_1)
        print(serial_1.portstr)
        ax.set_title('Temp')
        ax1.set_title('Humi')
        # recive data
        while True:
            read_msg = serial_1.read_all()
            if len(read_msg)==10:
                print("\nbytes:",read_msg)
                print("hex:",read_msg.hex())
                print("msg_len:",len(read_msg))
                #向初始数据列表中插入初始湿度数据
                list_msg.append(int(read_msg.hex()[10:12],16)+int(read_msg.hex()[12:14],16)*256)
                #向初始数据列表中插入初始温度数据
                list_msg.append(int(read_msg.hex()[14:16],16)+int(read_msg.hex()[16:18],16)*256)
                print(list_msg)  #预览初始数据
                #计算真实数据所需参数
                c1 = -4.0
                c2 = 0.0405
                c3 = -0.0000028
                t1 = 0.01
                t2 = 0.00008
                d1 = -42
                d2 = 0.01
                #使用公式分别计算真实温度和湿度
                rh0 = c1 + c2*list_msg[0] + c3*(list_msg[0]*list_msg[0])
                t = d1 + d2 * list_msg[1]
                rh1 = (t-25)*(t1 + t2*list_msg[0])+rh0
                print('temp:',t,"\thumi:",rh1) #输出真实温湿度
                #round函数保留得到数据的小数点后两位
                temp_data.append(round(t,2))
                humi_data.append(round(rh1,2))
                e = e+1 #记录数据条数
                
                #可视化代码
                
                temp.set_xdata(range(e))
                temp.set_ydata(temp_data)
                # ax[0].plot(range(int(e)),temp_data,color='blue',linestyle='--')
                humi.set_xdata(range(e))
                humi.set_ydata(humi_data)
                ax.relim()
                ax.autoscale_view()
                ax1.relim()
                ax1.autoscale_view()
                fig.canvas.draw()
                fig.canvas.flush_events()
                # ax[1].plot(range(int(e)),humi_data,color='red')
                # plt.show()
                # plt.clf()
                if e ==100: 
                    break
                list_msg = []
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
    serial_1 = serial.Serial('COM11',9600,timeout = 1)
    list_msg = []
    plt.ion()
    fig,(ax,ax1) = plt.subplots(2,1)
    fig.tight_layout(w_pad = 5,h_pad = 2)
        
    temp, = ax.plot([],[],color='blue',linestyle='--')
    humi, = ax1.plot([],[],color='red')
    # ax1.set_autoscaley_on(True)
    ax.grid()
    ax1.grid()
    test_3(serial_1,list_msg,ax,ax1,temp,humi,fig)