#!/usr/bin/env python3
import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from argon2.low_level import hash_secret_raw, Type
import secrets
import base64
import argparse
import getpass

MAGIC_HEADER = b'ChaEnc1\n'  # 8 bytes
SALT_SIZE = 16
NONCE_SIZE = 12
VENV_DIR = os.path.join(os.path.dirname(__file__), ".venv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python3") if os.name != "nt" else os.path.join(VENV_DIR, "Scripts", "python.exe")

# --- Auto-venv setup ---
def ensure_venv():
    if sys.prefix == sys.base_prefix and not os.path.exists(VENV_DIR):
        print("[+] Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
    
    if sys.prefix == sys.base_prefix:
        print("[+] Re-running inside virtual environment...")
        os.execv(VENV_PYTHON, [VENV_PYTHON] + sys.argv)

ensure_venv()

# --- Ensure dependencies are installed inside venv ---
REQUIRED_PACKAGES = ["cryptography", "argon2-cffi"]
try:
    import cryptography
    import argon2
except ImportError:
    print("[+] Installing required packages in venv...")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + REQUIRED_PACKAGES)

# --- Now safe to import ---
def secure_delete(filepath):
    try:
        with open(filepath, "ba+", buffering=0) as f:
            length = f.tell()
            f.seek(0)
            f.write(secrets.token_bytes(length))
        os.remove(filepath)
    except Exception as e:
        print(f"Error securely deleting {filepath}: {e}")

def derive_key(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=1,
        hash_len=32,
        type=Type.ID
    )

def encrypt_file(filepath, password):
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)
    key = derive_key(password, salt)

    with open(filepath, "rb") as f:
        data = f.read()

    filename = os.path.basename(filepath).encode()
    filename_len = len(filename).to_bytes(2, 'big')

    aead = ChaCha20Poly1305(key)
    ciphertext = aead.encrypt(nonce, filename_len + filename + data, None)

    out_path = filepath + ".enc"
    with open(out_path, "wb") as f:
        f.write(MAGIC_HEADER + salt + nonce + ciphertext)

    secure_delete(filepath)
    return out_path

def decrypt_file(filepath, password):
    with open(filepath, "rb") as f:
        content = f.read()

    if not content.startswith(MAGIC_HEADER):
        print("❌ Not a valid ChaCrypt encrypted file.")
        sys.exit(1)

    salt = content[8:8+SALT_SIZE]
    nonce = content[8+SALT_SIZE:8+SALT_SIZE+NONCE_SIZE]
    ciphertext = content[8+SALT_SIZE+NONCE_SIZE:]

    key = derive_key(password, salt)
    aead = ChaCha20Poly1305(key)

    try:
        plaintext = aead.decrypt(nonce, ciphertext, None)
        name_len = int.from_bytes(plaintext[:2], 'big')
        filename = plaintext[2:2+name_len].decode()
        data = plaintext[2+name_len:]
    except Exception as e:
        print("❌ Decryption failed: wrong password or corrupted file.")
        sys.exit(1)

    out_path = os.path.join(os.path.dirname(filepath), filename)
    with open(out_path, "wb") as f:
        f.write(data)

    secure_delete(filepath)
    return out_path

def gui_mode():
    root = tk.Tk()
    root.title("ChaCrypt - Encrypt/Decrypt Files")
    
    # Window properties for a professional look
    root.geometry("400x300")  # Fixed size
    root.config(bg="#f4f4f4")
    
    # Display the selected file path
    file_path_label = tk.Label(root, text="File Path: Not Selected", bg="#f4f4f4")
    file_path_label.pack(pady=10, padx=10, anchor="w")

    def select_file():
        filepath = filedialog.askopenfilename(title="Select file to encrypt/decrypt")
        if filepath:
            file_path_label.config(text=f"File Path: {filepath}")
            select_button.config(state=tk.DISABLED)
            # Store the filepath for later use
            return filepath
        return None

    select_button = tk.Button(root, text="Select File", command=select_file, relief="raised", width=20)
    select_button.pack(pady=10)

    # Password input fields with validation
    password_frame = tk.Frame(root, bg="#f4f4f4")
    password_frame.pack(pady=10)

    password_label = tk.Label(password_frame, text="Enter password:", bg="#f4f4f4")
    password_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    password_entry = tk.Entry(password_frame, show="*", width=30)
    password_entry.grid(row=0, column=1, padx=10, pady=5)

    confirm_label = tk.Label(password_frame, text="Confirm password:", bg="#f4f4f4")
    confirm_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    confirm_entry = tk.Entry(password_frame, show="*", width=30)
    confirm_entry.grid(row=1, column=1, padx=10, pady=5)

    def encrypt_decrypt():
        filepath = file_path_label.cget("text").replace("File Path: ", "")
        if not filepath:
            messagebox.showerror("Error", "Please select a file to encrypt/decrypt.")
            return
        
        password = password_entry.get()
        confirm_password = confirm_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        if filepath.endswith(".enc"):
            result = decrypt_file(filepath, password)
            messagebox.showinfo("Decryption Complete", f"Decrypted: {result}")
        else:
            result = encrypt_file(filepath, password)
            messagebox.showinfo("Encryption Complete", f"Encrypted: {result}")

    action_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt, relief="raised", width=20)
    action_button.pack(pady=20)

    root.mainloop()

def cli_mode():
    parser = argparse.ArgumentParser(description="ChaCha20 File Encryptor/Decryptor")
    parser.add_argument("filepath", help="Path to file to encrypt/decrypt")
    args = parser.parse_args()

    password = getpass.getpass("Enter password: ")  # Hide password input in CLI
    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("❌ Passwords do not match!")
        return

    if args.filepath.endswith(".enc"):
        result = decrypt_file(args.filepath, password)
        print(f"✅ Decrypted: {result}")
    else:
        result = encrypt_file(args.filepath, password)
        print(f"✅ Encrypted: {result}")

if __name__ == "__main__":
    # Check if running from a terminal or a GUI environment
    if sys.stdout.isatty():  # CLI mode
        cli_mode()
    else:  # GUI mode
        gui_mode()
