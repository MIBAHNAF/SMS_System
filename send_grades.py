import sys
import requests

# Your API secret from (Tools -> API Keys) page
api_secret = "7d4aba2e905b30ef29dc586944703f0ce4d70ca2"

def send_grades(phone_number, name, grades, custom_msg ):
    # Create the default message
    personalized_message = f" Student {name} {grades} {custom_msg}"

    # Prepare the payload
    payload = {
        "secret": api_secret,
        "mode": "devices",
        "campaign": "bulk test",
        "numbers": phone_number,  # Single phone number
        "device": "00000000-0000-0000-bc54-df34ca89e493",  # Replace with your device ID
        "sim": 1,  # Replace with your SIM slot number
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
    if len(sys.argv) != 5:
        print("Usage: python send_grades.py <phone_number> <name> <grades> <custom_msg> ")
    else:
        phone_number = sys.argv[1]
        name = sys.argv[2]
        grades = sys.argv[3]
        custom_msg = sys.argv[4]
        send_grades(phone_number, name, grades, custom_msg )

