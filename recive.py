from paho.mqtt import client as mqtt_client
import random

broker = '180.76.231.63' #云服务器公网IP,与发送端一致
port = 1883   #MQTT 协议端口
topic = "Topics fangbinbin Pub"  #与发送端一致

# 调用 Python random.randint 函数随机生成 MQTT 客户端 id
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()