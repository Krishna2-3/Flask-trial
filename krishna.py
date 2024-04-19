import requests
import time

# Replace 'YOUR_REPLIT_APP_URL' with your Replit app's URL
REPLIT_URL = 'https://45c44f95-28c3-4946-8171-6037a62c2e8e-00-26l9spix6h05w.sisko.replit.dev/'

def self_ping():
    try:
        response = requests.get(REPLIT_URL)
        if response.status_code == 200:
            print("Self-ping successful!")
        else:
            print(f"Self-ping failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Self-ping failed with error: {str(e)}")

if __name__ == "__main__":
    # Ping the app every 5 minutes (300 seconds)
    while True:
        self_ping()
        time.sleep(60)
