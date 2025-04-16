conversations = {
    "conv1": [
        {
            "role": "user", 
            "content": "Hey, It seems that I am unable to connect to the VPN for some reason"
        },
        {
            "role": "assistant", 
            "content": """Hey! I see, before troubleshooting, could you please answer a few questions:
            1. What is your operating system? 
            2. Which country are you connecting from?"""
        },
        {
            "role": "user", 
            "content": "Windows and I am from Lithuania"
        },
        {
            "role": "assistant", 
            "content": """Thank you! Here are a few troubleshooting steps you can try to resolve the VPN connectivity issue on your Windows device: 
            1. Check NordVPN Application Version: Ensure that you are using the latest version of the NordVPN application. The latest version as per the document is 7.27.5. You can check this by opening the NordVPN app, clicking on Settings (the gear icon at the bottom), and the version should be displayed at the top right below the Settings headline.
            2. Switch Protocols: Try switching between TCP and UDP protocols within the NordVPN app settings. This can sometimes resolve connection issues.
            3. Connect to a Different Server: Attempt to connect to another VPN server. If you're still experiencing issues, you can reset the application through the diagnostics section in the settings""",
            "article": "https://support.nordvpn.com/hc/en-us/articles/19748510235921-Troubleshooting-NordVPN-connectivity-on-Windows"
        }
    ],
    "conv2": [
        {"role": "user", "content": "How do i setup proxy on Deluge"},
        {
            "role": "assistant", 
            "content": """To set up a NordVPN proxy on Deluge, you can follow these steps:

            1. Open Deluge: Depending on your operating system, access the Preferences in Deluge.
                - On Windows and Linux: Click Edit > Preferences.
                - On macOS: In the menu bar, click Deluge > Preferences.
            2. Select the Proxy Section: In the Preferences window, navigate to the Proxy section. From the Proxy dropdown menu, select Socks5 Auth.
            3. Fill in Proxy Details: Input the following information into the relevant fields:
                - Username: Your NordVPN service username.
                - Password: Your NordVPN service password.
                - Hostname: Address of a selected proxy server (you can choose from the list provided in the document, such as amsterdam.nl.socks.nordhold.net or atlanta.us.socks.nordhold.net).
                - Port: 1080.
            You can find your NordVPN service credentials in the Nord Account dashboard by clicking Set up NordVPN manually. You will need to verify your email to access these details.

            After completing these steps, click Apply and OK to save the changes. To verify if your proxy setup is working, you can visit the ipleak.net website and check the Torrent Address detection section.""",
            "article": "https://support.nordvpn.com/hc/en-us/articles/20341624031505-NordVPN-proxy-setup-on-Deluge"
        },
    ]
}
