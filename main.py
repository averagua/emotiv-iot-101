import ibmiotf.device

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
myData = {
    "name": "foo",
    "cpu": 60,
    "men": 50
}

client.publishEvent("status", "json", myData)