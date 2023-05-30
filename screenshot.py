import pyautogui
import schedule
import time
from PIL import Image, ImageGrab
import os
from datetime import datetime

class Screenshot:
    def __init__(self):
        self.dir = "screenshots"

    def take_screen(self):
        # Take screen and name it
        timestamp = str(datetime.now()).replace(":", "_")
        image_name = f"screenshot-{timestamp}"
        image = ImageGrab.grab()

        # Save the screenshot in the correct directory
        image_path = os.path.join(self.dir, f"{image_name}.png")
        image.save(image_path)
        return image_path

    def auto_screen(self, interval=5):
        schedule.every(interval).seconds.do(self.take_screen)

        while True:
            schedule.run_pending()
            time.sleep(1)