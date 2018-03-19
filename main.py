import ibmiotf.device
import numpy as np
import time
try:
    options = {
        "org": "r0brbj",
        "type": "Emotiv",
        "id": "00001",
        "auth-method": "token",
        "auth-token": "Qm9CUCkWP3x-()ElQg",
        "clean-session": False

    }
    client = ibmiotf.device.Client(options)
except ibmiotf.ConnectionException as e:
    print(e)

client.connect()

#print(random_cpu)
#print(type(random_cpu))
for i in range(100):
	random_cpu = np.random.randint(0, 100)
	myData = {
	    "name": "foo",
	    "cpu": random_cpu,
	    "men": 50
	}

	client.publishEvent("status", "json", myData)
	time.sleep(0.5)