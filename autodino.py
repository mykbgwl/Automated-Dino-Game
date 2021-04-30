import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(215, 500):
        for j in range(410, 574):
            if data[i, j] < 100:
                hit("down")
                return

    # Draw the rectangle for cactus
    for i in range(215, 500):
        for j in range(574, 700):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Dino game about to start in 2 seconds")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


''' For Calculating the strip
        # Draw the rectangle for cactus
        for i in range(215, 500):
            for j in range(574, 700):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(215, 500):
            for j in range(410, 574):
                data[i, j] = 80

        image.show()
        break
'''
