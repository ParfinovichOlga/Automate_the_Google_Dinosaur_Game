import pyautogui as pg
import time

URL = "https://elgoog.im/dinosaur-game"

pg.hotkey('winleft')
time.sleep(2)

pg.typewrite(URL+'\n', 0.5)
time.sleep(2)

pg.hotkey('winleft', 'up')
translate = pg.locateCenterOnScreen('translate.PNG', confidence=0.8)
time.sleep(4)
pg.moveTo(translate)
time.sleep(2)
pg.click()
time.sleep(2)

pg.press('space')
time.sleep(4)
dinosaur = pg.locateOnScreen('dinosaur.PNG', confidence=0.8)
dinosaur_centre_point = pg.center(dinosaur)

# USE FOR DETERMINING DINOSAUR'S COLOR
x_center = int(dinosaur_centre_point[0])
y_center = int(dinosaur_centre_point[1])

# USE FOR DETERMINING REGION OF SCREENSHOT
x = x_center + int(dinosaur[2]/2)
y = y_center - int(dinosaur[3]/2) + 20

continue_game = True


# CHECK DINOSAUR'S COLORS IS IN  SCREENSHOT
def jump(barrier_bellow, color):
    if color in barrier_bellow:
        return pg.press('space')


while continue_game:
    jump(pg.screenshot(region=(x, y, 299, 35)).getdata(), pg.pixel(x_center, y_center))


