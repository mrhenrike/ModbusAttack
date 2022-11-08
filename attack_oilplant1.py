#!/usr/bin/env python3
""" 
1 PLC_FEED_PUMP: open/close the feed pump
2 PLC_TANK_LEVEL: tank level sensor
3 PLC_OUTLET_VALVE: open/close the outlet valve
4 PLC_SEP_VALVE: open/close the separator vessel valve
5 -
6 PLC_OIL_SPILL: wasted oil counter
7 PLC_OIL_PROCESSED: processed oil counter
8 PLC_WASTE_WATER_VALVE: open/close waste water valve
"""

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(1, 1)  # PLC_FEED_PUMP
  client.write_register(3, 0)  # PLC_OUTLET_VALVE
