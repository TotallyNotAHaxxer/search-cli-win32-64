import os
import sys 
import time 
import webbrowser


def scan():
    os.system(' python3 scan.py ')

def CS(X):
    time.sleep(X)
    os.system(' clear ')

os.system(' clear ')
print(" [+] Amazon ")
time.sleep(0.1)
print(" [+] Google ")
time.sleep(0.1)
print(" [+] Youtube ")
time.sleep(1)
A = str(input(" what website would you like to search? => "))

os.system(' clear ')


if 'amazon' in A:
            CS(1)
            print(" [!] ok, now what is the content you would like to search  ")
            B = str(input(" => "))
            url = (f" https://www.amazon.com/s?k={B} ")
            webbrowser.open(url)

elif 'Youtube' in A:
               CS(1)
               print(" [+] alright then, what is the content you would like to search? ")
               B = str(input(" =>  "))
               url = (f"https://www.youtube.com/results?search_query={B}")
               webbrowser.open(url)

elif 'youtube' in A:
               CS(1)
               print(" [+] alright then, what is the content you would like to search? ")
               print(" EX | kalle hallden ")
               B = str(input(" =>  "))
               url = (f"https://www.youtube.com/results?search_query={B}")
               webbrowser.open(url)


elif 'google' in A:
              CS(1)
              print(" [+] alright then, what is the content you would like to search? ")
              B = str(input(" =>  "))
              url = (f" https://www.google.com/search?q={B}")
              webbrowser.open(url)

elif 'Google' in A:
              CS(1)
              print(" [+] alright then, what is the content you would like to search? ")
              B = str(input(" =>  "))
              url = (f"https://www.google.com/search?q={B}")
              webbrowser.open(url)

elif 'Amazon' in A:
              time.sleep(1)
              os.system(' clear ')
              print(" [!] ok, now what is the content you would like to search  ")
              B = str(input(" => "))
              url = (f" https://www.amazon.com/s?k={B} ")
              webbrowser.open(url)
