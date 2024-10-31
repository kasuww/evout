import requests

def send_webhook_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

if __name__ == '__main__':
    # Replace with your actual Discord webhook URL
    webhook_url = 'https://discord.com/api/webhooks/1301314115343487017/FIXTgagljJftkw-hap4YdauN146l4qbuJaQptYX6FEK8HTSJOaRDUTmjeRS5tOTuvv7C'
    message = 'gangshit!'  # Customize your message here

    send_webhook_message(webhook_url, message)
