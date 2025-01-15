#469 574
#145 588
import time

from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
class Dino:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino
        self.counter = 0
        self.width = 55
        self.grow = 1.0024

    def restartgame(self):
        pyautogui.click(self.replaybtn)
        self.width = 55

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def grabImage(self):
        box = (self.dino[0]+self.width,self.dino[1],
               self.dino[0]+40+self.width,self.dino[1]+30)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        return a.sum()

    def start(self):
        self.width *= self.grow
        print(self.width)
        if self.grabImage() != 1447:
            self.jump()

def main():
    bot = Dino((469, 582), (145, 588))
    bot.restartgame()
    time.sleep(1)
    bot.jump()
    while True:
        bot.start()
        print(str(bot.grabImage()))


if __name__ == "__main__":
    main()