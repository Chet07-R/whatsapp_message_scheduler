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
