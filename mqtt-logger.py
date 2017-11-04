import time
import datetime
import csv
import paho.mqtt.client as paho
import re
broker="broker.hivemq.com"
#broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):


    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

    aika = datetime.datetime.now().isoformat()

    m = re.match(".*\D(?P<no>\d+)\W+(?P<value>\d+).*", str(message.payload.decode("utf-8")))
    if m:
        with open("lampologi.csv", 'a') as csvfile:
            #    fieldnames = ['datetime', 'temp','hum']
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            print('Measurement nro {0}, Value: {1}, Kello {2}'.format(m.group('no'),int(m.group('value'))/100,aika))
            spamwriter.writerow([aika,m.group('no'),int(m.group('value'))/100])



client= paho.Client("client-001")
#create client object client1.on_publish = on_publish
# #assign function to callback client1.connect(broker,port)
# #establish connection client1.publish("house/bulb1","on")
######Bind function to callback

client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("out799a586")#subscribe
#client.subscribe("outTopic")#subscribe
#time.sleep(20)




while 1:
    pass
#print("publishing ")
#client.publish("house/bulb1","on")#publish
#time.sleep(4)
#client.disconnect() #disconnect
#client.loop_stop() #stop loop