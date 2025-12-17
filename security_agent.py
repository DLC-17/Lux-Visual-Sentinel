import asyncio
import os
import sys

# Captures the screenshot from your local computer
from oagi import AsyncScreenshotMaker 

# Controls your local keyboard and mouse based on the model predicted actions
from oagi import AsyncPyautoguiActionHandler 
from oagi import TaskerAgent

async def main():
    # --- SECURITY CONFIGURATION ---
    # Retrieve the API key from environment variables for safety.
    # This prevents accidental leaking of keys in GitHub commits.
    api_key = os.getenv("LUX_API_KEY")

    if not api_key:
        print("❌ ERROR: API Key not found!")
        print("Please set your environment variable: export LUX_API_KEY='your_key_here'")
        sys.exit(1)

    # Initialize the agent with the Lux model and the secure key
    # (Assuming TaskerAgent accepts api_key as a parameter, or relies on the env var)
    agent = TaskerAgent(model="lux-actor-1", api_key=api_key)

    # --- TASK DEFINITION ---
    agent.set_task(
        task="Conduct a visual security audit of the current webpage for malicious indicators.",
        todos=[
            # Step 1: Context Gathering
            "Analyze the entire screen, specifically looking at the browser URL bar and the main content area.",
            
            # Step 2: Identification (Internal reasoning step for the model)
            "Identify potential threats: Check for 'Typosquatting' (misspelled domains), fake 'System Update' popups, aggressive countdown timers, or mismatched UI fonts that indicate a phishing attempt.",
            
            # Step 3: Reporting - Open the tool to communicate
            "Open your computer's text editor (e.g., Notepad on Windows, TextEdit on Mac).",
            
            # Step 4: Write the Report
            "Type a header: 'SECURITY AUDIT REPORT'.",
            "Type a summary of the screen state. State clearly if the site looks Safe, Suspicious, or Dangerous.",
            "List any detected threats found on the previous screen (e.g., 'Warning: The download button looks like a fake ad', 'URL domain does not match the logo').",
            
            # Step 5: Finalize
            "Save the file as 'Security_Scan_Results.txt' or simply leave it open for the user to read."
        ]
    )

    print("🛡️ Starting Visual Security Scan...")
    print("Please keep the suspicious webpage visible on your screen.")

    await agent.execute(
        instruction="Analyze the screen for malware/phishing and write a report",
        action_handler=AsyncPyautoguiActionHandler(),
        image_provider=AsyncScreenshotMaker(),
    )

if __name__ == "__main__":
    asyncio.run(main())