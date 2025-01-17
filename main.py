from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time
import threading


stop_flag = threading.Event()
def listen_for_stop():
    while not stop_flag.is_set():
        if keyboard.is_pressed("esc"):
            stop_flag.set()
        time.sleep(0.1)

stop_listener = threading.Thread(target=listen_for_stop)
stop_listener.start()

space_pressed = threading.Event()
def listen_for_space():
    while not stop_flag.is_set():
        if keyboard.is_pressed("space"):
            space_pressed.set()
        time.sleep(0.1)

space_listener = threading.Thread(target=listen_for_space)
space_listener.start()


def type_words():
    while not stop_flag.is_set():
        try:
            words = driver.find_elements(By.CSS_SELECTOR, "div.word:not(.typed)")
            
            if not words:
                break
            
            type_letters = ""
            
            for word in words:
                letters = word.find_elements(By.CSS_SELECTOR, "letter")

                for letter in letters:
                    type_letters += letter.text  
                    
                type_letters += " "

            keyboard.write(type_letters)

        except Exception:
            break


url = "https://monkeytype.com/"
driver = webdriver.Chrome()
driver.get(url)

while not stop_flag.is_set():
    if space_pressed.is_set():
        type_words()
        space_pressed.clear()
    time.sleep(0.1)
