ChaCrypt - Secure File Encryption and Decryption using ChaCha20
ChaCrypt is a lightweight and secure encryption/decryption tool designed to encrypt and decrypt files using the ChaCha20 algorithm. The application supports both CLI (Command Line Interface) and GUI (Graphical User Interface) for easy use across various platforms including Linux, Windows, and macOS.

Features
File Encryption and Decryption using the ChaCha20 algorithm.

Cross-platform support for Linux, Windows, and macOS.

Secure Password-based Authentication.

Command-Line Interface (CLI) for advanced users.

Graphical User Interface (GUI) for a user-friendly experience.

File Deletion after encryption to maintain security (optional).

Password Confirmation to ensure the entered password is correct.

Table of Contents
Installation

Usage

Command-Line Interface (CLI)

Windows GUI

Linux GUI

Contributing

License

Installation
Prerequisites
Ensure that you have the following installed:

Python 3.x

pip (Python's package installer)

Tkinter (for GUI support)

For Linux/MacOS
You can install Python and Tkinter using the following commands:

bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip python3-tk
For Windows
Python 3 should come with Tkinter bundled, so simply ensure Python 3.x is installed.

Step 1: Clone the Repository
To get started, clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/ajmatson/ChaCrypt.git
cd ChaCrypt
Step 2: Create a Virtual Environment (Optional but Recommended)
Create and activate a Python virtual environment to manage dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate.bat  # Windows
Step 3: Install Required Dependencies
Install the required Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Command-Line Interface (CLI)
Navigate to the Project Folder where the script is located.

Run the Script with the following command:

bash
Copy
Edit
python3 ChaCrypt.py <file_path>
Replace <file_path> with the path to the file you want to encrypt or decrypt.

Password Prompt: You will be prompted to enter a password for encryption or decryption. For security, the password will be obfuscated (shown as *******).

Confirm the Password: After entering the password, you will be prompted to confirm it to avoid any typos.

Windows GUI
Navigate to the Project Folder where the script is located.

Double-Click the Script or create a shortcut to launch the application.

File Selection: A file explorer window will open where you can select the file to encrypt or decrypt.

Password Prompt: You will be prompted to enter a password for encryption or decryption. Passwords must be entered twice for confirmation.

Encryption/Decryption: The encrypted file will be saved with a .enc extension, and the original file will be securely deleted (optional).

Linux GUI
Navigate to the Project Folder where the script is located.

Run the Script with the following command:

bash
Copy
Edit
python3 ChaCrypt.py
File Selection: A file explorer window will open, allowing you to choose the file to encrypt or decrypt.

Password Prompt: Enter your password twice to confirm.

Encryption/Decryption: The encrypted file will be saved with a .enc extension, and the original file will be securely deleted (optional).

Contributing
We welcome contributions to ChaCrypt! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to your fork (git push origin feature-branch).

Open a pull request to the main branch.

License
This project is licensed under the MIT License - see the LICENSE file for details.
