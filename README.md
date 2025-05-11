# Train Service Delay Notifier 🚉

This Python script monitors Transperth train services and sends you real-time alerts when a delay is detected for your selected line and station. You’ll get both a desktop notification and an SMS alert when your train might be disrupted — giving you time to plan an alternative route.

The script runs every 5 minutes until the service is confirmed to be on time again.

This idea was inspired by a similar course registration project from datababedev, whose approach to scraping and alerting helped shape the initial structure of this tool.

---

## 🚀 Features

- Monitors Transperth live train times for a specific line and station
- Automatically checks status every 5 minutes
- Uses Selenium to handle dynamic JavaScript-loaded content
- Sends SMS alerts via Twilio when a delay is detected
- Shows desktop notifications for both delays and normal status
- Stores credentials securely using a .env file

---

## Requirements

- Python 3.7+
- Google Chrome + ChromeDriver
- [Twilio account](https://www.twilio.com/)
- Transperth live train times URL (constructed automatically)

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/datababedev/CourseNotificationScript.git

2. **Install required packages**
   ```bash
   pip install -r requirements.txt

3. **Create a `.env` file**
   In the project root, create a file named `.env` and paste the following:

   ```env
   COURSE_URL=https://your-college-course-page.com
   COURSE_CODE=COMMST3029
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   MESSAGING_SERVICE_SID=your_messaging_service_sid
   MY_NUMBER=+12045551234
   ```

  ***Don’t share this file! It contains your private API keys and phone number.***

---

## How To Use
Run the script with:

```bash
python course_checker.py
```

You’ll see output like:

```bash
Still full... checking again soon.
Still full... checking again soon.
COMMST3029 might be available! Sending notification...
Twilio text sent! SID: SMxxxxxxxxxxxx
```
---

## How It Works

- The script sends a request to the course registration page using requests
- It uses BeautifulSoup to parse the HTML and search for your course code
- If the course code is found and doesn't say "Full" nearby:
  - It sends a desktop notification using plyer
  - It sends an SMS alert using Twilio
- The script runs every 10 minutes in a loop until the course becomes available

---

## How you can customize it
- Update your Course Code
- Change what the notifications say
- Add a testing feature to test if it works
- Change text notifications to emails or completely change it from SMS to discord or other notification servers
- Remove or update the desktop notifications
- Change the amount of time it takes to refresh the check

---

## FAQ

**Q: Can I use this for a different course?**  
A: Yes! Just change `COURSE_CODE` and `COURSE_URL` in your `.env` file.

**Q: Will this work if the course page is behind a login?**  
A: No, unfortunately the script can only access publicly available pages.

**Q: Can I get email alerts instead of SMS?**  
A: This version uses Twilio for SMS. You can modify it to use `smtplib` for email.

**Q: Can I run this script on a schedule in the background?**  
A: Yes! You can use Task Scheduler (Windows) or cron (Mac/Linux) to run it at intervals.

**Q: Can I use this without having my laptop running?**  
A: Not by default. This script runs *locally* on your computer, so it only works while your laptop is on and the script is running.

If you want it to run 24/7 without keeping your laptop open, you have a few options:
- Host it on a cloud server
- Use a Raspberry Pi or another device that stays on
- Deploy it on AWS Lambda or another serverless platform
**Let me know what you do!**

## Community
Join the Discussions to ask questions or suggest features!
