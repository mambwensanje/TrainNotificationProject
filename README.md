# Train Service Delay Notifier 🚉

This Python script monitors Transperth train services and sends you real-time alerts when a delay is detected for your selected line and station. You’ll get both a desktop notification and an SMS alert when your train might be disrupted, giving you time to plan an alternative route.

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

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/mambwensanje/TrainNotificationProject.git
   cd TrainNotificationProject

2. **Install required packages**
   ```bash
   pip install -r requirements.txt

3. **Create a `.env` file**
   In the project root, create a file named `.env` and paste the following:

   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   MESSAGING_SERVICE_SID=your_messaging_service_sid
   MY_NUMBER=+61XXXXXXXXX
   ```

  ***Never share this file! It contains your private API keys and phone number.***

---

## 🧠 How It Works

- You input your desired train line and station (e.g. “Joondalup” and “Perth”)
- The script builds the corresponding Transperth live status URL
- Using Selenium, it loads the site and waits for the dynamic train data table
- BeautifulSoup parses the rendered HTML to check each train’s status
- If any train shows a delay, you’ll receive:
   - A desktop alert
   - A Twilio SMS to your phone
- The script waits 5 minutes, then checks again — repeating until services are confirmed to be on time

## ▶️ How To Run
From the notificationScript/ folder, run the script:

```bash
python trainNotificationScript.py
```

You’ll be prompted to enter:

- Train line (e.g., Yanchep)
- Station name (e.g., Perth)

If delays are detected, you'll receive:

- A desktop alert
- An SMS with the disruption details

---

## 🔄 Customization Ideas
- Change notification interval (default is 5 mins)
- Replace Twilio SMS with email or Discord webhooks
- Make it GUI-based with Tkinter or web-based with Flask
- Extend to buses or ferry routes
- Auto-detect your nearest station using location APIs
- Automate to run everyday at your regular travel times

---

## ❓ FAQ

**Q: Will this work with any train line?**  
A: Yes, as long as the line and station exist on the Transperth live times website.

**Q: Can I use this on a schedule?**  
A: Yes, run it in the background or set it up with cron (Linux/Mac) or Task Scheduler (Windows).

**Q: Can I get email alerts instead of SMS?**  
A: This version uses Twilio for SMS. You can modify it to use `smtplib` for email.

**Q: Can I use this without having my laptop running?**  
A: Not by default. This script runs *locally* on your computer, so it only works while your laptop is on and the script is running.

If you want it to run 24/7 without keeping your laptop open, you have a few options:
- Host it on a cloud server
- Use a Raspberry Pi or another device that stays on
- Deploy it on AWS Lambda or another serverless platform
**Let me know what you do!**

## 🤝 Credits
Inspired by [datababedev](https://www.instagram.com/datababe.dev/)’s [CourseNotificationScript](https://github.com/datababedev/CourseNotificationScript/blob/main/README.md).
Created and adapted for Perth’s public transport system.
