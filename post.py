import time
import requests
import pyfiglet

# Configuration
text_to_be_posted = """
:evergreen_tree: Pine Tree (Asia Server) - 
# NO RESET, STRICTLY 5 PEOPLE ONLY. WILL BAN CLOSEST TO BEESMAS TREE
Level: 16+
Puffs and Mondo: **MUST ON**
At least 1 Gifted (Buoyant, Tadpole, Fuzzy) **WILL KICK IF NOT MET**
**PLEASE REPOST WHEN JOINING!**
https://www.roblox.com/share?code=bf50853031ee914e9b7c13218ab58d3c&type=Server
"""

# Channels to be posted
channels_and_slow_modes = {
    'https://discord.com/api/v9/channels/1282753706252828672/messages': {'server_name': 'General1'},
}

# API Key and Webhook URL
api_key = "MTA4OTM3NjkzNzQ1OTMzNTIzOA.GKjlIn.X4O018BUhoXxzHrABzppAzNWYZVRjekvCK1J0Y"
webhook_url = "https://discord.com/api/webhooks/1345022687902175302/AIm1bKHVkLTesUVtM75QGLeFViQ_wE2lqL2tXQX1qXIWjHSnPWzV3trPbvG18xAYUoZw"

# Print process started banner
f = pyfiglet.figlet_format("Process Started", font="slant")
print(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'authorization': f"{api_key}"
}

def post_to_webhook(webhook_url, content, server_name):
    payload = {
        'content': content,
        'embeds': [
            {
                'title': f"Message Is Posted to {server_name}", 
                'description': content,
                'color': 0x00ff00,
            }
        ]
    }
    requests.post(webhook_url, json=payload)

# Get the current UNIX timestamp
current_timestamp = int(time.time())

# Format the timestamp for Discord
discord_timestamp = f"<t:{current_timestamp}:R>"
# Notify the webhook that the process has started
post_to_webhook(webhook_url, "Sent: " + discord_timestamp, "System")

# Send message once to each channel
for channel, data in channels_and_slow_modes.items():
    server_name = data['server_name']

    payload = {
        'content': text_to_be_posted
    }
    r = requests.post(channel, data=payload, headers=headers)

    # Check if the message was successfully posted
    if r.status_code == 200:
        print(f"Message posted to {channel}")
        post_to_webhook(webhook_url, f"Message Is Posted to {server_name}", server_name)
    else:
        print(f"Failed to post message to {channel}. Status Code: {r.status_code}")
post_to_webhook(webhook_url, "Session END!", "System")
exit()
