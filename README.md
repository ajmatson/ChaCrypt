![Logo](https://github.com/ajmatson/ChaCrypt/blob/master/images/logo2.png)

# ChaCrypt - Secure File Encryption and Decryption using ChaCha20

ChaCrypt is a lightweight and secure encryption/decryption tool designed to encrypt and decrypt files using the ChaCha20 algorithm. The application supports both CLI (Command Line Interface) and GUI (Graphical User Interface) for easy use across various platforms including Linux, Windows, and macOS.

## Features

- File Encryption and Decryption using the ChaCha20 algorithm.
- Cross-platform support for Linux, Windows, and macOS.
- Secure Password-based Authentication.
- Command-Line Interface (CLI) for advanced users.
- Graphical User Interface (GUI) for a user-friendly experience.
- File Deletion after encryption to maintain security (optional).
- Password Confirmation to ensure the entered password is correct.

## Table of Contents

- Installation
- Usage
- Command-Line Interface (CLI)
- Windows GUI
- Linux GUI
- Contributing
- License

## Installation

### Prerequisites

All pre-reqisits are written in the script to pull/install.



## Usage

### Command-Line Interface (CLI)

```bash
python3 ChaCrypt.py <file_path>
```

- Replace `<file_path>` with the path to the file you want to encrypt or decrypt.
- You will be prompted to enter and confirm a password.
- The encrypted file will be saved as `<originalname>.<ext>.enc`, and the original file will be deleted.

### Windows GUI

- Double-click `ChaCrypt.bat` or create a shortcut to run it.
- Select the file using the file dialog.
- Enter and confirm your password.
- Encrypted or decrypted file will be saved accordingly.

### Linux GUI

- Double-click ChaCrypt.desktop
- A GUI window will open to select a file.
- Enter and confirm the password.
- Process will complete with file saved as either encrypted or decrypted.

## Contributing

1. Fork the repository

2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit changes:

   ```bash
   git commit -am 'Add new feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Thanks for using ChaCrypt! If you like the project, give it a ⭐ on GitHub!
