from cryptography.fernet import Fernet
import os, sys

def decrypt_file(encrypted_file, key_file):
    A = encrypted_file
    C = Fernet(key_file)
    D, E = os.path.splitext(os.path.basename(A))
    F = os.path.dirname(A)
    B = os.path.join(F, f"{D}{E}")
    
    # Remove the ".zoro" extension
    if E == ".zoro":
        B = os.path.join(F, D)
    
    with open(A, 'rb') as G:
        H = G.read()
    
    I = C.decrypt(H)
    
    with open(B, 'wb') as J:
        J.write(I)
    
    return B

if len(sys.argv) < 2:
    print("Usage: decrypt.exe <file_path> <provided_key>")
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
         decrypt_file(arg1, arg2)
    except Exception as e:
         print("[Error] Could not decrypt file!")
         print(str(e))