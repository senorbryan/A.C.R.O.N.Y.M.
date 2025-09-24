import time     #For implementing delays in code execution to run smoothly with sound effects
import sys      #For the smoothness to simulate a transmission character by character
import os       #For clearing the terminal
import pygame   #For playing sound effects during transmission

#Acronym method records the user's acronym and its meaning
def acronymize():
    acronym = ""
    words = []

    print()
    print("Please state your A.C.R.O.N.Y.M.:")
    str = input()
    acronym = str.upper()

    print()
    print("State the meaning for each letter in the A.C.R.O.N.Y.M.")

    for char in acronym:
        print()
        print(f"What does {char} stand for?")
        char = input()
        words.append(char.upper())

    return acronym, words

#Transmits the acronym
def transmit_acronym(text):
    delay = typing_speed
    title.play(-1)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    title.stop()
    sys.stdout.write("\n")
    line.play()
    sys.stdout.flush()

#Transmits the expansion of the acronym
def transmit_expansion(text):
    delay = typing_speed
    expansion.play(-1)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    expansion.stop()
    sys.stdout.write("\n")
    line.play()
    sys.stdout.flush()

#Transmits the final line of the acronym
def transmission_final_line(text):
    delay = typing_speed
    expansion.play(-1)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    expansion.stop()
    sys.stdout.flush()

#Blinks the cursor
def blink(duration: float, blink_speed):
    """
    Blink a temporary cursor at the current print position.
    Draws '_' and removes it with backspace so nothing remains.
    """
    end = time.time() + duration
    visible = False
    blinking.play()

    #Alternates between a blinking cursor and an "_" underscore
    while time.time() < end:
        if visible:
            # erase the underscore and restore position
            sys.stdout.write("\b \b")
            sys.stdout.flush()
        else:
            sys.stdout.write("_")
            sys.stdout.flush()

        visible = not visible
        time.sleep(blink_speed)

    #Clears cursor
    blinking.stop()
    if visible:
        sys.stdout.write("\b \b")
        sys.stdout.flush()

pygame.mixer.init()

#Audio file declarations and speed variables
typing_speed = 0.07
blinking_speed = 0.5
blinking = pygame.mixer.Sound("Transmission Sounds/blinking.wav")
line = pygame.mixer.Sound("Transmission Sounds/line.wav")
title = pygame.mixer.Sound("Transmission Sounds/typing acronym.wav")
vertical = pygame.mixer.Sound("Transmission Sounds/vertical.wav")
expansion = pygame.mixer.Sound("Transmission Sounds/typing expansion.wav")
acronym, words = acronymize()

#Clears the terminal of all text
time.sleep(0.1)
if os.name == "nt":
    os.system("cls")

#Types the acronym
title.play(-1)
for char in acronym:
    sys.stdout.write(char)
    title.play()
    sys.stdout.flush()
    time.sleep(typing_speed)
title.stop()
blink(2.5, blink_speed = 0.5)

#Clears the terminal of all text
time.sleep(0.1)

if os.name == "nt":
    os.system("cls")

vertical.play()
time.sleep(0.5)
line.play()

#Types the letters of the acronym
for i, word in enumerate(words):
    if i < len(words) - 1:
        transmit_expansion(words)
    
    else:
        transmission_final_line(word)
        blink(2.5, blink_speed=0.5)
        sys.stdout.flush()

#Clears the terminal of all text
time.sleep(0.1)

if os.name == "nt":
    os.system("cls")