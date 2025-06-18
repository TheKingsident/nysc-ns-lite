# NYSC Registration Checker (Lite)

A simple Python script to check if NYSC registration is open by scraping the official NYSC portal.

---

## 🚀 Features

- Checks the NYSC portal for the registration status.
- Simple command-line output: tells you if registration is open or closed.
- Easy to configure with your own keyword (no code changes needed).

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TheKingsident/nysc-ns-lite.git
cd nysc-ns-lite
```

### 2. Install Dependencies

Make sure you have Python 3 installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Configure the Keyword

Create a `.env` file in the project directory (if it doesn't exist) and add the line below.  
**The value should match the text shown on the NYSC portal when registration is closed.**

```
KEYWORD=No Active Registration
```

*Do not use quotes. Copy the text exactly as it appears on the website.*

### 4. Run the Script

```bash
python checker.py
```

You will see output indicating whether NYSC registration is open or closed.

---

## ⚠️ Disclaimer

This script is for personal use and educational purposes only.  
It does not send notifications or store any personal data.

---

## 📬 Want Automatic Alerts?

If you'd like to receive automatic notifications (email or WhatsApp) when registration opens,  
contact me on [hello@kingsleyusa.dev](mailto:hello@kingsleyusa.dev) for access to the full version.
