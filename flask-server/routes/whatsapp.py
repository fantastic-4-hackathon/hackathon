import pywhatkit

try:
    # Schedule a WhatsApp message
    pywhatkit.sendwhatmsg("+27836681148", "Geeks For Geeks!", 18, 30)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
