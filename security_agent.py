import asyncio

# Captures the screenshot from your local computer
from oagi import AsyncScreenshotMaker 

# Controls your local keyboard and mouse based on the model predicted actions
from oagi import AsyncPyautoguiActionHandler 
from oagi import TaskerAgent

async def main():
    agent = TaskerAgent(model="lux-actor-1")

    # We define a task that focuses on observation and reporting.
    # Since the agent "acts," we instruct it to output its findings 
    # by opening a text editor and typing the report for the user to read.
    agent.set_task(
        task="Conduct a visual security audit of the current webpage for malicious indicators.",
        todos=[
            # Step 1: Context Gathering
            "Analyze the entire screen, specifically looking at the browser URL bar and the main content area.",
            
            # Step 2: Identification (Internal reasoning step for the model)
            "Identify potential threats: Check for 'Typosquatting' (misspelled domains), fake 'System Update' popups, aggressive countdown timers, or mismatched UI fonts that indicate a phishing attempt.",
            
            # Step 3: Reporting - Open the tool to communicate
            "Open your computer's text editor (e.g., Notepad on Windows, TextEdit on Mac, or a new Google Doc tab).",
            
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