from paho.mqtt import client as mqtt_client
import random
import time
import sql_0
broker = '180.76.231.63'  #云服务器公网IP
port = 1883  #MQTT协议端口
topic = "Topics fangbinbin Pub"  #发送与接收端topic需保持一致

#调用 Python random.randint 函数随机生成 MQTT 客户端 id
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        # msg = f"messages: {msg_count}"
        topics = input("请输入主题：")
        msg = input("请输入消息：")
        result = client.publish(topics, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            # sql_0.main(topics, msg)
            print(f"Send `{msg}` to topic `{topics}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()