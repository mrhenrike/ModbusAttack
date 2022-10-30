#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(1, 0)  # Bottle is not filled (Desligar sensor do limite de envase)
  client.write_register(2, 0)  # Bottle is under the nozzle (Desligar o sensor de presença da garrafa)
  client.write_register(3, 0)  # Stop the motor (Desligar o motor da esteira)
  client.write_register(4, 0)  # Close the nozzle (Fechar o bico de envasamento)
  client.write_register(16, 0) # Shutdown the plant (Desligar a planta)