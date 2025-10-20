# WhatsApp Bulk Message Automation with Selenium

## Overview
This project automates sending personalized WhatsApp messages to multiple contacts or groups using Python and Selenium.  
It reads contact names and messages from an Excel file and uses your logged-in WhatsApp Web session to send bulk messages reliably.

---

## Features
- Bulk sends WhatsApp messages (text only) from your contact sheet.
- Uses Excel file for easy management of contacts and messages.
- Searches for contacts directly, bypassing WhatsApp Web's lazy loading issue.
- Maintains logged-in WhatsApp session with Chrome user profile for convenience.
- Includes delays and error handling comments for troubleshooting.

---

## Setup Instructions

### Prerequisites
- Python 3.x installed.
- Google Chrome installed.
- ChromeDriver matching your Chrome version installed and in your PATH.
- Install Python packages:


### WhatsApp Profile Setup
- Log into WhatsApp Web manually once using any Chrome profile directory, then set that path in your script's Chrome options to keep your session between runs.
- Use the profile directory in the script (see code).

---

## Excel File Format (`contacts.xlsx`)
| Name          | Message                    |
|---------------|---------------------------|
| Di            | Happy Diwali! 🪔✨         |
| John          | Hello John, how are you?  |
| Family Group  | Have a great day, family! |

- **Name:** Exact WhatsApp contact or group name as shown in WhatsApp.
- **Message:** Text message you wish to send.

---

## How to Use

1. Populate `contacts.xlsx` with target contacts and messages.
2. Run the Python automation script:

3. WhatsApp Web will open; the script will search for each contact, type the message, and send.
4. Monitor the console for progress and instructions.

---

## Code Structure

The script will:
- Open WhatsApp Web and wait for you to authenticate (first time).
- Read the contacts and messages from your Excel file.
- For each contact:
- Search via WhatsApp Web's search bar.
- Open the chat and send the specified message.
- Print progress for each message sent.

Comments are included to help you tweak waits, debug lazy loading, and adapt for future enhancements.

---

## Notes
- No images or files are sent; this version is **text-only** by design.
- Protect sensitive data: add `contacts.xlsx` and Chrome profile folders to your `.gitignore`.
- Adjust delays (`time.sleep()`) for your internet speed if needed.
- For troubleshooting, consult inline comments and console output.

---

## References
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

---

This project is ideal for automating simple WhatsApp outreach, alerts, and event-based reminders for groups or individuals. Extend as needed!
