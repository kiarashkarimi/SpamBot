# Spam Bot With Python

import pyautogui, time

def spam():
    inputDir = input("Enter the Directory Path: ")
    time.sleep(5)
    spamFile = open(inputDir, 'r')
    for word in spamFile:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def makeNewFile():
    newFileName = input("Enter the file Name: ")
    file = open(f"txt-files/{newFileName}", 'x')

    newFileText = input("Ok, Enter the text below: \n")
    file.write(newFileText)

    print("Wait a Sec ...")
    time.sleep(3)
    print("OK!, please Restart the bot")

helpMsg = "\nhelp, ?    -> Shows this help massage\nspam       -> Runs spam bot\nmknew      -> makes new spam list\nquit, bye  -> quit this bot"

userInput = input("What do you want to do ?: ").lower()
if userInput == 'help' or userInput == '?':
    print(helpMsg)
elif userInput == 'spam':
    spam()
elif userInput == 'mknew':
    makeNewFile()
elif userInput == 'quit' or userInput == 'bye':
    time.sleep(1)
    print("Shutting Down ...")
    time.sleep(2)
else:
    raise ValueError("Please Enter a Valid value ... ( use ? for help )")