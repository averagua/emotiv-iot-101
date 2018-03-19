#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018, Alejandro Veragua-Albornoz. All rights reserved.

"""
Emotiv client for publish events to Watson IoT Plafform
Documentation of ibmiotf in
https://console.bluemix.net/docs/services/IoT/index.html

"""
import sys
from dotenv import load_dotenv
import os
from os.path import join, dirname
import ibmiotf.device

load_dotenv(join(dirname(__file__), '.env'))


def create_client(options):
    try:
        print("Creating IBM iot device client in org %s for type device %s with id %s" %(options["org"], options["type"], options["id"]))
        device_client = ibmiotf.device.Client(options)
        device_client.connect()
        return device_client

    except ibmiotf.ConnectionException as e:
        return e


def eeg_data(params=None):
    """
    Function that create a eeg data and publish it
    :param params: Optional {dict} - with some params
    """
    print("Exectuging eeg data event ")
    print(params)
    data_event = {
        "event_name":  "hello World",
        "data": "hello world"
    }
    client.publishEvent("status", "json", data_event)


options = {
            "org": os.getenv('org'),
            "type": os.getenv('type'),
            "id": os.getenv('id'),
            "auth-method": "token",
            "auth-token": os.getenv('auth-token'),
            "clean-session": True
        }
client = create_client(options)


# Export the module that executes an action for send a event to ibmiotf
Events = {
    "eegData": eeg_data
}


"""
Usage:

python EmotivClient.py <eventName>

For example, 
python EmotivClient.py eegData 
Send a event with the emotiv data
"""
if __name__ == "__main__":
    name = sys.argv[1]
    params = {"param1": None}
    Events[name](params)