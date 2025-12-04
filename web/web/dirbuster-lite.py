import requests

url = input("Enter URL (e.g. http://site.com/): ")
wordlist = ["admin", "login", "uploads", "images", "config", "test"]

print("\nStarting directory scan...\n")

for word in wordlist:
    full = url + word
    r = requests.get(full)
    if r.status_code == 200:
        print(f"[+] Found: {full}")
