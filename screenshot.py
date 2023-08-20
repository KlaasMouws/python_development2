from datetime import datetime
from PIL import ImageGrab
from github import Github
import schedule
import time
import os


class Screenshot:
    def __init__(self):
        self.teller = 0
        self.dir = "screenshots"
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('pythonDevelopment2')
        
    def take_screen(self):
        # Take screen and name it
        timestamp = str(datetime.now()).replace(":", "_")
        image_name = f"screenshot-{timestamp}"
        image = ImageGrab.grab()
        self.teller = self.teller + 1

        # Save the screenshot in the correct directory
        image_path = os.path.join(self.dir, f"{image_name}.png")
        image.save(image_path)
        with open(image_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{image_name}.png", f"Added screenshot {image_name}", file.read())
        
        print(f"Screenshot genomen: {image_name}")

        if self.teller >= 5:
            print("Aantal screenshots bereikt. De applicatie wordt afgesloten.")
            exit()

    def auto_screen(self, interval=5):
        schedule.every(interval).seconds.do(self.take_screen)            

        while True:
            schedule.run_pending()
            time.sleep(1)
