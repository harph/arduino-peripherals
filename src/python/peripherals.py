import sys
import os
import glob
import appscript
from serial import Serial


def _get_arduino_port():
    serial_port = None
    cu_ports = glob.glob('/dev/cu.usbmodem*')
    port = None
    if cu_ports:
        port = cu_ports[0]
    else:
        tty_ports = glob.glob('/dev/tty.usbmodem*')
        if tty_ports:
            port = tty_ports[0]
    if not port:
        raise Exception('Arduino port not found')
    return Serial(port, 9600)


SERIAL_PORT = _get_arduino_port()


def OS_say(msg):
    os.system('say %s' % msg)


def launch_chrome():
    app = appscript.app('Google Chrome')
    if not app.isrunning():
        app.launch()
    else:
        OS_say('Chrome is already open')

def execute():
    while True:
        serial_input = SERIAL_PORT.readline().replace('\r\n', '').split(':')
        print serial_input
        if not serial_input:
            continue
        event_type = serial_input[0]
        if event_type == 'HELLO':
            OS_say('hello tinkers!')
        elif event_type == 'APP':
            launch_chrome()


if __name__ == '__main__':
  execute() 
