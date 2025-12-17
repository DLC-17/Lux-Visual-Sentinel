# Lux-Visual-Sentinel
An autonomous cybersecurity agent powered by the Lux Foundation Model. It visually audits your screen to detect phishing, social engineering, and UI-based malware triggers that code scanners miss. 🛡️👁️

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

## 🚀 How It Works
The agent operates on a continuous **Vision-Reasoning-Action Loop**:

1.  **OBSERVE:** The agent takes a screenshot of the current active window.
2.  **REASON:** The Lux model analyzes the pixels to answer: *"Does this page look trustworthy? Are there deceptive UI elements?"*
3.  **ACT:** If a threat is detected or a summary is requested, the agent physically moves the mouse to open a text editor (Notepad/TextEdit) and types out its findings.

## 📦 Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/lux-visual-sentinel.git](https://github.com/yourusername/lux-visual-sentinel.git)
    ```

2.  **Install Dependencies**
    ```bash
    pip install oagi asyncio
    ```

3.  **Run the Sentinel**
    ```bash
    python security_agent.py
    ```

4.  **Demo Instructions**
    * Open a "safe" phishing test site (e.g., a screenshot of a known scam or a training site).
    * Run the script.
    * Watch as the agent analyzes the screen and opens your text editor to write the **Security Audit Report**.

## 📄 License
MIT License
