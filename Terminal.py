
#Installing if not:
import subprocess

# Check if Colorama is installed
try:
    import colorama
except ImportError:
    # If not installed, install it
    subprocess.check_call(["pip", "install", "colorama"])

import time,os,sys
from colorama import init, Fore, Back, Style
import psutil
import subprocess
import sys

import os
# clear the console output

# Get the path to the User's Documents directory
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')

# Create the Testing folder if it doesn't already exist
Configs_folder_path = os.path.join(documents_path, 'Terminal')
if not os.path.exists(Configs_folder_path):
    os.mkdir(Configs_folder_path)

# Create a text file named "idk" inside the Testing folder
text_file_path = os.path.join(Configs_folder_path, 'Logs.txt')
with open(text_file_path, 'w') as f:
    f.write('Logs\n')
    f.write('#configs in Config.cfg\n')
    f.write('##Runned Terminal\n')

text_file_path = os.path.join(Configs_folder_path, 'Config.cfg')
with open(text_file_path, 'w') as t:
    t.write('#Config\n')
    t.write('Dir location = [Current User Documents Location]\n')
    t.write('CFG Location save = [Current User Documents Location] / ConfigFolder\n')
    t.write('Max file size = 100MB\n')
    t.write('Enable logging = true\n')
    t.write('Custom directory = C:\Windows\n')
    t.write('RootUser = Irox\n')
    t.write('\n')
    t.write('Enable Optionals? = true\n')
    t.write('#Optionals Configs, By defult the Optionals are set to true\n')
    t.write('Add Luascripting? = false\n')

configFolder_folder_path = os.path.join(Configs_folder_path, 'ConfigFolder')
if not os.path.exists(configFolder_folder_path):
    os.mkdir(configFolder_folder_path)

init()
import os
os.system('cls' if os.name == 'nt' else 'clear')


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")
print(Back.BLACK + Fore.CYAN + "  ______ _______ __   _   ______               ")
print(" |  ____ |______ | \  |   |     \ |      |     ")
print(" |_____| |______ |  \_| . |_____/ |_____ |_____")

while True:
    print("Choose an option:")
    print("1. CMD ")

    choice = input("> ")
    
    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Type 'Cmds' for help")
        import win32api
        import win32con

    win32api.SetConsoleTitle("Terminal")


    while True:
      if choice == "1":
        terminalsend = input(Style.RESET_ALL + Back.BLACK + Fore.LIGHTYELLOW_EX + "\n#$> Terminal\\Users\\RootUser >> " + Style.RESET_ALL)

      if terminalsend == "Cmds":
         typingPrint("Those are available commands.\n")
         print("Key - Validate Key")
         print("Logs - Logs")
         print(" Version - What version are you using\n")
         print("Close - Close the terminal")
         print("Cls - Clears the terminal")
         print("Update - Checks for Updates")
         print("Dir - Dir location")
         print("sans.sound - Play song: 'sans.'")

      elif terminalsend == "Logs":
        typingPrint("\n1.00v - Beta testing\n")
        typingPrint("1.01v - Fix bugs, changed name of the Title bar\n")
        typingPrint("1.02v - Added ")
        typingPrint(Back.BLACK + Fore.CYAN + "Update " + Style.RESET_ALL)
        typingPrint("option, restarts Terminal.\n")
        typingPrint(Back.BLACK + Fore.RED + "1.03 - Config's and Log's in User documents.\n")
        typingPrint("1.04v - Changed Configs, main direction: 'The user documents direction.'\n" + Style.RESET_ALL)
        typingPrint("1.05v - Added ")
        typingPrint(Back.BLACK + Fore.GREEN + "Key " + Style.RESET_ALL)
        typingPrint("Validation\n")
        typingPrint(Back.BLACK + Fore.GREEN + "1.06v - Bored? Use new command: 'sans.sound'!\n" + Style.RESET_ALL)
        typingPrint("1.10v - First release.")

      elif terminalsend == "Version":
        typingPrint("Version running: ")
        typingPrint(Back.WHITE + Fore.RED + "1.10v\n" + Style.RESET_ALL)
        typingPrint("If version updates, type 'Logs'\n")

      elif terminalsend == "Cls":
        typingPrint("Alr cleaning terminal")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

      elif terminalsend == "Key":
        typingPrint("[")
        typingPrint(Back.BLACK + Fore.GREEN + "VALIDATION" + Style.RESET_ALL)
        typingPrint("] Key is Validate\n") 
        typingPrint("\n[")
        typingPrint(Back.BLACK + Fore.RED + "TERMINALROOT" + Style.RESET_ALL)
        typingPrint("] no reason to change it so why\n") 

      elif terminalsend == "Update":
        print("Updating...")
        time.sleep(1)
        subprocess.Popen([sys.executable, __file__])
        sys.exit(0)

        

      elif terminalsend == "Close":
        typingPrint("Terminal.end")
        time.sleep(1)
        sys.exit()



      elif terminalsend == "Dir":
        typingPrint("Current dir is user documents location\n")



      elif terminalsend == "sans.sound":
          print(Back.WHITE + Fore.BLACK + "ok, dont ask questions about pygame, its used to play the audio.") 
          print("Tho if it ended please play it again, i can't do loop becuse it will crash the python script.")
          print("Unless it wont work + Place the audio named: 'sans.mp3' in ya Desktop and replace 'ghost' to your user (on python script ofc)\n" + Style.RESET_ALL)
          print("Song will start in 5 seconds")


          time.sleep(5)



          import threading
          import time
          import pygame
          os.system('cls' if os.name == 'nt' else 'clear')

          pygame.display.init()
          os.system('cls' if os.name == 'nt' else 'clear')


# load audio file
          pygame.mixer.init()
          pygame.mixer.music.load("C:\\Users\\ghost\\Desktop\\sans.mp3")

# set volume to 50% (0.5)
          pygame.mixer.music.set_volume(0.3)

# start playback in a separate thread
          def play_audio():
            pygame.mixer.music.play()
          while pygame.mixer.music.get_busy():
            time.sleep(1)

          audio_thread = threading.Thread(target=play_audio)
          audio_thread.start()

          os.system('cls' if os.name == 'nt' else 'clear')
