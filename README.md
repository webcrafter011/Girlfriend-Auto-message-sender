# WhatsApp Auto Messenger (Selenium + Brave)

This script automates sending messages to a WhatsApp contact using Selenium and the Brave browser. It will send random messages from a predefined list to a specified contact until a reply is detected in the chat.

## Features
- Uses Brave browser for WhatsApp Web automation
- Sends random messages from a customizable list
- Stops automatically if a reply is detected
- Infinite message sending (until reply)

## Requirements
- Python 3.x
- Selenium (`pip install selenium`)
- Brave browser installed
- ChromeDriver compatible with your Brave/Chrome version

## Setup
1. **Install Brave Browser**
   - Download and install from [Brave official site](https://brave.com/download/)
2. **Install Selenium**
   ```bash
   pip install selenium
   ```
3. **Download ChromeDriver**
   - Get the version matching your Brave/Chrome from [ChromeDriver downloads](https://chromedriver.chromium.org/downloads)
   - Place `chromedriver.exe` in your PATH or the script directory
4. **Edit Script**
   - Set `BRAVE_PATH` to your Brave browser executable location
   - Set `contact_name` to the exact name of your WhatsApp contact
   - Optionally, customize the `messages` list

## Usage
1. Run the script:
   ```bash
   python index.py
   ```
2. Scan the QR code in the Brave window to log in to WhatsApp Web
3. The script will start sending messages to the specified contact
4. Automation stops if a reply is detected

## Notes
- Use responsibly. Spamming contacts may violate WhatsApp's terms and annoy recipients.
- The script creates a new Brave profile for automation (`BraveSeleniumNewProfile`).
- You can adjust the random delay between messages in the script.

## Disclaimer
This project is for educational purposes only. Use at your own risk.
