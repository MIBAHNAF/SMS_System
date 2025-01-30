import sys
import requests

# Your API secret from (Tools -> API Keys) page
api_secret = "a35130ec7b17917f90a4b1de648ff337455fbb34"

def send_sms(phone_number, name):
    # Create the default message
    personalized_message = f"Student {name} was absent!"

    # Prepare the payload
    payload = {
        "secret": api_secret,
        "mode": "devices",
        "campaign": "bulk test",
        "numbers": phone_number,  # Single phone number
        "device": "00000000-0000-0000-aae8-51abe9d16857",  # Replace with your device ID
        "sim": 2,  # Replace with your SIM slot number
        "priority": 1,
        "message": personalized_message,  # Default message
    }

    # Send the SMS
    response = requests.post(url="https://www.cloud.smschef.com/api/send/sms.bulk", params=payload)

    # Log the response
    if response.status_code == 200:
        print(f"SMS sent to {phone_number}: {response.json()}")
    else:
        print(f"Error sending SMS to {phone_number}: {response.status_code} - {response.text}")

# Main script logic
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python send_sms.py <phone_number> <name>")
    else:
        phone_number = sys.argv[1]
        name = sys.argv[2]
        send_sms(phone_number, name)

