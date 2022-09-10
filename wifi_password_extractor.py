import subprocess
#import sys
import sys
import os.path




data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    #file = open('saved_passwords.txt','w')
    #file.write(str(results))
    #file.close
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    #file = open('saved_passwords.txt', 'w')
    #file.write(str(results))
    #file.close
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))

#file.write(str(data))
#file.write(str(profiles))
#file.write(str(results))
#file.write(str(results))
#file.close()


#passwords = input("geef hier de naam van het wifi wachtwoord + wifi naam bv wifinaam = password om het te saven in een bestand")
#file = open("saved_passwords.txt","w")
#file.write(passwords)
#file.close
#orig = sys.stdout
#with open("passwords.txt", "wb") as f:
#    sys.stdout = f
#    try:
#        exec("codeattack_wifi_password_extractor.py", {})
#    finally:
#        sys.stdout = orig
output = ("{:<30}|  {:<}".format(i, results[0]))
file = open("passwords.txt")

file.close
file.write(output)
input("")
