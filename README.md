# WhatsApp Bulk Messaging Automation with Selenium

## Overview
This project automates sending personalized WhatsApp messages with images to multiple contacts or groups using Python and Selenium.  
It reads contact details, messages, and image paths from an Excel file and uses a persistent WhatsApp Web login session to send bulk customized greetings efficiently.

## Features
- Bulk send WhatsApp messages with custom text and images.
- Uses an Excel file for contact management.
- Handles WhatsApp Web's lazy loading by searching contacts.
- Maintains session with Chrome user profile to avoid repeated QR scans.
- Includes delays and waits for reliable operation.

## Setup Instructions

### Prerequisites
- Python 3.x installed.
- Google Chrome installed.
- ChromeDriver matching your Chrome installed and in PATH.
- Install dependencies:  


### WhatsApp Profile Setup
Log into WhatsApp Web manually once using any Chrome profile directory, then set that path in the script's Chrome options to persist the session.

### Excel File Format (`contacts.xlsx`)
| Name          | Message                         | ImagePath                          |
|---------------|---------------------------------|-----------------------------------|
| Di            | Happy Diwali! 🪔✨              | C:/Users/LENOVO/Desktop/images/di1.jpg |
| John          | Hello John, wishing you success!| C:/Users/LENOVO/Desktop/images/john1.jpg |
| Family Group  | Happy Diwali to my family 🎆    | C:/Users/LENOVO/Desktop/images/family.jpg |

- **Name:** Exact WhatsApp contact/group name.
- **Message:** Text message to send.
- **ImagePath:** Absolute local path to the image file.

## Usage

1. Populate your `contacts.xlsx` file with names, messages, and image paths.
2. Run the Python automation script:

3. The script will open WhatsApp Web, search each contact, attach images, type messages, and send them.
4. Follow console prompts if any, e.g., to close when done.

## Notes
- Image files must be local; URLs are not supported.
- Use delays to prevent WhatsApp rate limiting.
- Protect your Excel and image files by adding them to `.gitignore`.
- Errors are logged; you can extend by adding try-except blocks for robustness.

## References
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

---

This project serves as a solid foundation for custom WhatsApp automation with scalable personalization options. Extend or modify as needed for your use case!
