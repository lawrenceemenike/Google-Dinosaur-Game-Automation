import pyautogui
import time
from PIL import ImageGrab
import numpy as np

# Game coordinates (you may need to adjust these based on your screen resolution)
DINOSAUR = (480, 400)  # Dinosaur's position
SCAN_AREA = (520, 400, 600, 430)  # Area to scan for obstacles

def start_game():
    pyautogui.click(DINOSAUR[0], DINOSAUR[1])
    pyautogui.press('space')
    time.sleep(1)

def detect_obstacle():
    image = ImageGrab.grab(SCAN_AREA)
    gray_image = np.array(image.convert('L'))
    return np.any(gray_image < 100)  # Detect dark pixels (obstacles)

def play_game():
    start_game()
    while True:
        if detect_obstacle():
            pyautogui.press('space')
        time.sleep(0.01)  # Small delay to prevent excessive CPU usage

if __name__ == "__main__":
    print("Starting the game in 3 seconds. Switch to the game window!")
    print("Make sure the game is visible on your screen.")
    time.sleep(3)
    play_game()