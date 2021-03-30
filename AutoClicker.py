import pyautogui as pg
import cv2
import numpy as np
from PIL import ImageGrab

sleepspeed = 0.115
last_time = pg.time.time()

while True:

    # create img
    img = ImageGrab.grab()

    # img = cv2.cvtColor(imgunprep, cv2.COLOR_BGR2RGB)
    frame = np.array(img)
    screen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out.write(frame)
    cv2.imshow("", frame)

    for y in range(500, 400, -1):
        for x in range(1160,1150, -1):
            c = screen[y][x] == 0
            d = screen[y][x - 120] == 0
            e = screen[y][x - 240] == 0
            f = screen[y][x - 360] == 0
            if c.any():
                newX = x
                newY = y
                pg.mouseDown(x=newX, y=newY)

                pg.sleep(0.06)
                pg.mouseUp(x=newX, y=newY)
                break
            elif d.any():
                newX = x - 120
                newY = y
                pg.mouseDown(x=newX, y=newY)

                pg.sleep(0.06)
                pg.mouseUp(x=newX, y=newY)
                break
            elif e.any():
                newX = x - 240
                newY = y
                pg.mouseDown(x=newX, y=newY)

                pg.sleep(0.06)
                pg.mouseUp(x=newX, y=newY)
                break

            elif f.any():
                newX = x - 360
                newY = y
                pg.mouseDown(x=newX, y=newY)

                pg.sleep(0.06)
                pg.mouseUp(x=newX, y=newY)
                break

        break

    print("Loop took {} seconds", format(pg.time.time() - last_time))
    last_time = pg.time.time()
    pg.PAUSE = 0.001

    # frame = np.array()

    # pg.sleep(0.1)
    # pg.click(x=36, y=559)
    if (cv2.waitKey(1)) == ord("q"):
        break
print(frame[750][750])

cv2.destroyAllWindows()

# out.release()
