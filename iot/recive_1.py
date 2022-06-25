from paho.mqtt import client as mqtt_client
import random
import sql_0
broker = '180.76.231.63' #云服务器公网IP,与发送端一致
port = 1883   #MQTT 协议端口
topic = "fangbinbin"  #与发送端一致

# 调用 Python random.randint 函数随机生成 MQTT 客户端 id
client_id = f'python-mqtt-{random.randint(0, 1000)}'

#  建立 MQTT 客户端
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):     # 创建 MQTT 客户端
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)   # 建立连接
    return client

def subscribe(client: mqtt_client):  #订阅主题
    def on_message(client, userdata, msg): #接收消息
        sql_0.main(msg.topic, msg.payload.decode('gbk')) #调用sql_0.py中的main函数
        print(msg.topic,":", msg.payload.decode('gbk'))
    client.subscribe(topic) #订阅主题
    client.on_message = on_message # 启动 MQTT 客户端

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()