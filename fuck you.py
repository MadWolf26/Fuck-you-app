import os
from time import sleep

os = input("""Choose your OS
           1.Linux 2.MacOS 3.Windows""")

def clean():
    if os == "1":
        os.system('clear')
        
    if os == "2":
        os.system('clear')
    
    if os == "3":
        os.system('cls')
    
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
