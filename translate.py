
# TODO:
#   Have the pi gpio pins turn on and off an LED according to the morse code

import RPi.GPIO as GPIO
import time

led = 11
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)

def end():
    GPIO.cleanup()

def output(char):
    if char == "*":
        print("*")
        GPIO.output(led,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.5)
    if char == "-":
        print("-")
        GPIO.output(led,GPIO.HIGH)
        time.sleep(2.5)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.5)


text = input("Please enter some text. You can only use letters or numbers. \n")

lText = text.lower()

morse = lText
# Big block of code that'll translate the text. I might refine this at some point.
morse = morse.replace(" "," ,")
morse = morse.replace("a","*-,")
morse = morse.replace("b","-***,")
morse = morse.replace("c","-*-*,")
morse = morse.replace("d","-**,")
morse = morse.replace("e","*,")
morse = morse.replace("f","**-*,")
morse = morse.replace("g","--*,")
morse = morse.replace("h","****,")
morse = morse.replace("i","**,")
morse = morse.replace("j","*---,")
morse = morse.replace("k","-*-,")
morse = morse.replace("l","*-**,")
morse = morse.replace("m","--,")
morse = morse.replace("n","-*,")
morse = morse.replace("o","---")
morse = morse.replace("p","*--*,")
morse = morse.replace("q","--*-,")
morse = morse.replace("r","*-*,")
morse = morse.replace("s","***,")
morse = morse.replace("t","-,")
morse = morse.replace("u","**-,")
morse = morse.replace("v","***-,")
morse = morse.replace("w","*--,")
morse = morse.replace("x","-**-,")
morse = morse.replace("y","-*--,")
morse = morse.replace("z","--**,")
#numbers
morse = morse.replace("1","*----,")
morse = morse.replace("2","**---,")
morse = morse.replace("3","***--,")
morse = morse.replace("4","****-,")
morse = morse.replace("5","*****,")
morse = morse.replace("6","-****,")
morse = morse.replace("7","--***,")
morse = morse.replace("8","---**,")
morse = morse.replace("9","----*,")
morse = morse.replace("0","-----,")

# Convert the single string to a list to make some stuff much easier later
morseL = morse.split(',')

print("Your morse code:" + '   '.join(morseL))

# LED
try:
    if lText.isalnum() == True:
        print("All available characters")
        setup()
        chars = list(morse)
        mapL = list(map(output,chars))

        print("Done.")
        end()
except KeyboardInterrupt:
    end()