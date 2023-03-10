from pyautogui import *
import pyautogui
import time
import keyboard
import random

Random = ['a','w','s','d','4','q','1','2','3','4']

while True:
    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
        pyautogui.click(230, 950)
        time.sleep(0.5)
        pyautogui.click(230, 950)     
        time.sleep(0.5)
        pyautogui.click(230, 950)  
        
    if pyautogui.locateOnScreen('Team.png', region=(3,520,445,304), grayscale=True, confidence=0.9) != None:
        pyautogui.click(171, 675)
        time.sleep(0.5)
        pyautogui.click(171, 675)
                
    if pyautogui.locateOnScreen('InGame.png', region=(87,755,379,304), grayscale=True, confidence=0.5) != None:
         print("In game waiting")
         keyboard.press_and_release(Random)
         time.sleep(0.5)
    
    if pyautogui.locateOnScreen('dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
         print("dead")
         pyautogui.press('space')
                
                
             
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
                pyautogui.click(963, 623)
                time.sleep(0.5)
                pyautogui.press('esc')
     
    if pyautogui.locateOnScreen('space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
     keyboard.press_and_release('space')
     
    if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(850, 713)
         time.sleep(0.5)
         pyautogui.click(850, 713)
         

    if pyautogui.locateOnScreen('Contunue.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)
         
    if pyautogui.locateOnScreen('startmanu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)
    if pyautogui.locateOnScreen('startmanu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)
