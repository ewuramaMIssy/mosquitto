import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("gc/yourtopic")


def on_message(client, userdata, msg):
    print('\033[92m' + msg.topic + ":\033[40m \n" + str(msg.payload) + "n")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.5", 1883,60)
client.loop_forever()





client.loop_forever()
