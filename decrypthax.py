import webbrowser
import time
import sys
import os

os.system('cls')

def load_txt(fname):
    f = open(fname,"r")
    if f.mode == 'r':
        contents =f.read()

    return contents

def start_loading_screen(toolbar_width):
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar

CRED = '\033[91m'
CEND = '\033[0m'


print('Loading program')
start_loading_screen(50)
os.system('cls')
print(CRED + "__________________________________________" + CEND)
print(CRED + "WELCOME TO SECRET CODE DECRYPTING SERVICE!" + CEND)
print(CRED + "TRUST ME, I'M ENGINEER" + CEND)
print(CRED + "__________________________________________" + CEND)

time.sleep(3)
print(CRED + "Loading secret code" + CEND)

contents=load_txt("secretcode.txt")
start_loading_screen(25)
os.system('cls')
print(CRED + "Content ready for decryption" + CEND)
print(CRED + "CODE:" + CEND)
print(contents.replace('"',''))

time.sleep(3)
os.system('cls')
print(CRED + "Starting decryption phase... please wait." + CEND)
time.sleep(2)
print(CRED + "Ready for DECRYPTING" + CEND)
print(CRED + "This may take a while, please take a comfort position..." + CEND)
time.sleep(3)
print(CRED + "DECRYPTING" + CEND)
start_loading_screen(100)

binary_values = contents.replace('"','').split()

ascii_string = ""
for binary_value in binary_values:
    an_integer = int(binary_value, 2)

    ascii_character = chr(an_integer)

    ascii_string += ascii_character

print(CRED + "DECRYPTED MESSAGE:" + CEND)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(ascii_string)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

time.sleep(3)
start_loading_screen(10)
#lolo best part here: 
print("Plus....")
time.sleep(3)
print("...I Godsmack'd your PC :D")
time.sleep(3)
new=2
url='https://youtu.be/UC-0DBDkXOw'
webbrowser.open(url, new=new)