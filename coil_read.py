#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient
import random
import time
import sys

SERVER_IP = sys.argv[1] # aka modbus slave
SERVER_PORT = 502
ADDRESS_START  = 35
ADDRESS_LENGTH = 10
DEVICE_ID = 1


client = ModbusTcpClient(host=SERVER_IP, port=SERVER_PORT)
if not client.connect() :  # .connect() returns True if connection established
  print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
  exit()

# client.read_coils(address, count, unit)
t1 = time.time()
coil_response = client.read_coils(address=ADDRESS_START, count=ADDRESS_LENGTH, unit=DEVICE_ID) # the unit is the device ID
t2 = time.time()

print("[INFO] Read time cost {:7f} second.".format(t2-t1))
if coil_response.isError():  # .isError() returns True if the modbus slave returns exception
  print("[Error] The modbus slave connected but exception code returned: %d." % coil_response.exception_code)
else:
  i = 0
  x = ADDRESS_START
  while i < ADDRESS_LENGTH:
    # coil_response has attribute .bits if no error return from the modbus slave
    print("[INFO] Addr ", x+i, ":", coil_response.bits[i])
    i += 1

client.close()
