import pyautogui
import schedule
import time
import os
from datetime import datetime

def take_screen():
    #Take screen and name it
    image_name = f"screenshot-{str(datetime.now())}"
    image = pyautogui.screenshot()

    #Save the screenshot in the correct map
    dir = "screenshots"
    image_path = os.path.join(dir,f"{image_name}.png")
    image.save(image_path)

    return image_path

#def main():
    schedule.every(10).seconds.do(take_screen())

    while True:
        schedule.run_pending()
        time.sleep(1)
#image.save("img")



take_screen()