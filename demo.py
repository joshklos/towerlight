from towerlight import TowerLight
import time

recording_light = TowerLight('/dev/tty.usbserial-1130')
recording_light.red('ON')
time.sleep(10)
recording_light.clear_all()