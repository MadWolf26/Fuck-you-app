import os
from time import sleep

os = input("Your operating system")

def clean():
    if os == "Windows" or "windows":
        os.system('cls')
        
    if os == "MacOs" or "macos" or "mac":
        os.system('clean')
    
    if os == "Linux" or "linux":
        os.system('clean')
    
    else:
        print(os + "is not recognized")

speed = float(input("Enter the speed"))
clean()

while True:
    print("""




         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |  """)
    sleep(speed)
    clean()
    
    print("""



          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |  """)
    sleep(speed)
    clean()

    print("""    


          | |                     | |               
          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |  """)
    sleep(speed)
    clean()

    print("""  

          |U|                     | |               
          | |                     | |               
          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |  """)
    sleep(speed)
    clean()
    
    print("""
          .-.                     .-.               
          |U|                     | |               
          | |                     | |               
          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |            
       |       |               |       |  """)
    sleep(speed)
    clean()
