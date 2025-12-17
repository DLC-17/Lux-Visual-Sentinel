# 🛡️ Lux Visual Sentinel: Autonomous Security Auditor

## 🚨 The Problem
Traditional antivirus software scans **code** and **files**. However, modern threats often rely on **Visual Deception** and **Social Engineering**—tactics that look innocent in code but are dangerous to the user.
* *Typosquatting* (e.g., `paypa1.com` looks like `paypal.com`)
* *Tech Support Scams* (Full-screen HTML popups claiming infection)
* *Dark Patterns* (Fake "Download" buttons or urgency timers)

## 💡 The Solution
**Lux Visual Sentinel** is a "Large Action Model" (LAM) agent built on the **Lux Foundation Model** and **OAGI**. Instead of parsing HTML, it **looks** at your screen like a human security analyst would.

It continuously observes the browser, identifies visual irregularities, and autonomously generates a plain-text report for the user, acting as a second pair of eyes against cyber threats.

## ⚡ Key Features
* **Visual Phishing Detection:** Identifies mismatched fonts, low-resolution logos, and URL typos that indicate a spoofed site.
* **Behavioral Analysis:** Recognizes "urgency tactics" (countdown timers) often used in scams.
* **Autonomous Reporting:** The agent controls the mouse and keyboard to open a text editor and type a real-time audit report, requiring zero API integration with the browser itself.

## 🛠️ Tech Stack
* **Model:** Lux Foundation Model (`lux-actor-1`)
* **Framework:** [OAGI](https://github.com/oagi) (Open AGent Interface)
* **Capabilities:**
    * `AsyncScreenshotMaker` (Vision)
    * `AsyncPyautoguiActionHandler` (Action)
* **Language:** Python 3.10+

## 🔑 Configuration
To use this agent, you must provide your Lux API Key. For security, we use environment variables.

**Mac / Linux:**
```bash
export LUX_API_KEY="your_actual_key_here"