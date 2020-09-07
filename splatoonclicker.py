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

from pynput import mouse,keyboard
import random
import pyautogui


finished = False

def execute(spiders, pause):

    global finished

    def on_press(key): 
        global finished
        if key == keyboard.KeyCode.from_char('q'):
            print('exiting')
            finished = True
            return False

    with keyboard.Listener(on_press = on_press) as listener: 
        pyautogui.PAUSE = pause
        while not finished:
            pyautogui.keyDown('shift')
            pyautogui.keyDown('1')
            pyautogui.keyUp('1')
            pyautogui.keyUp('shift')

            remotes = list(range(0,10))
            random.shuffle(remotes)
            for x in remotes:
                pyautogui.press(str(x))
                pyautogui.mouseDown()
                pyautogui.mouseUp()

            pyautogui.keyDown('shift')
            pyautogui.keyDown('1')
            pyautogui.keyUp('1')
            pyautogui.keyUp('shift')
        listener.join() 


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--spiders", default=10, help="Number of spidertrons (1-10)")
    parser.add_argument("-p", "--pause", default=0.04, help="Pause after each PyAutoGUI call")
    args = parser.parse_args()

    if args.spiders <=0 or args.spiders >10:
        print('Error: Spiders must currently be between 0 and 10')
        exit(-1)

    execute(args.spiders, args.pause)
