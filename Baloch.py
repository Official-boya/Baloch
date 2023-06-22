import os,platform

os.system('git pull')

Baloch=platform.architecture()[0]

if Baloch=="32bit":

    os.system("clear")

    print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 

    print('\033[1;31m Sorry  Your Phone is 32bit and This Toll is sported on 64bit please change your Device... ')

    print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0;97m") 

elif Baloch=="64bit":

    __import__("Baloch")
