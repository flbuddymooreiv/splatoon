#!/usr/bin/env python3

# Copyright 2020 Buddy Moore <buddy.moore@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
# USE OR OTHER DEALINGS IN THE SOFTWARE.

from pynput import mouse
import time
import pyautogui


vectorx = None
vectory = None
flankx = None
flanky = None


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    print("{0} at {1}".format("Pressed" if pressed else "Released", (x, y)))
    if pressed:
        global vectorx, vectory, flankx, flanky
        if not vectorx and not vectory:
            vectorx = x
            vectory = y
            return True
        if not flankx and not flanky:
            flankx = x
            flanky = y
        if vectorx and vectory and flankx and flanky:
            return False


def on_scroll(x, y, dx, dy):
    pass




def execute(spiders, pause):

    if spiders <=0 or spiders >10:
        print('Error: Spiders must currently be between 0 and 10')
    else:

        # Collect events until released
        with mouse.Listener(
            on_move=on_move, on_click=on_click, on_scroll=on_scroll
        ) as listener:
            listener.join()

        print(vectorx, vectory, flankx, flanky)

        deltax = (flankx - vectorx)
        deltay = (flanky - vectory)

        pyautogui.PAUSE = pause

        for s in range(0, spiders):
            dx = (deltax / spiders) * s
            dy = (deltay / spiders) * s
            px = vectorx + dx
            py = vectory + dy

            pyautogui.press(str(s + 1) if s + 1 < 10 else "0")
            pyautogui.moveTo(px, py)
            pyautogui.mouseDown()
            pyautogui.mouseUp()

        pyautogui.press("q")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--spiders", default=10, help="Number of spidertrons (1-10)")
    parser.add_argument("-p", "--pause", default=0.06, help="Pause after each PyAutoGUI call")
    args = parser.parse_args()

    execute(args.spiders, args.pause)
