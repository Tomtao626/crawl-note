import uiautomator2 as ui2
import os
import pandas as pd
import time
import unittest
import json
import re
import csv

serial = '1333e1d50606'
d = ui2.connect_usb(serial)

# 确认面板
if d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/PowerOn1").exists:
    print(1, True)
    d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/PowerOn1").click()

elif d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/power").exists:
    print(2, True)
    d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/power").click()

else:
    print(False)
d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/working").click()


