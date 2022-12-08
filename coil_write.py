#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient
import time
import sys

SERVER_IP = sys.argv[1] # aka modbus slave
SERVER_PORT = 502

client = ModbusTcpClient(host=SERVER_IP, port=SERVER_PORT)
if not client.connect() :  # .connect() returns True if connection established
  print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
  exit()

while True:
  coil_response = client.write_coil(address=35, value=True, unit=1)
  coil_response = client.write_coil(address=36, value=True, unit=1)
  coil_response = client.write_coil(address=37, value=True, unit=1)
  coil_response = client.write_coil(address=38, value=True, unit=1)
  coil_response = client.write_coil(address=39, value=True, unit=1)
  coil_response = client.write_coil(address=40, value=False, unit=1)
  coil_response = client.write_coil(address=41, value=True, unit=1)
  coil_response = client.write_coil(address=42, value=True, unit=1)
  coil_response = client.write_coil(address=43, value=True, unit=1)
  coil_response = client.write_coil(address=44, value=True, unit=1)
  coil_response = client.write_coil(address=45, value=True, unit=1)

client.close()