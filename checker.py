#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
KEYWORD = os.getenv("KEYWORD")

def check_registration():
    url = "https://portal.nysc.org.ng/nysc1/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        if KEYWORD not in soup.text:
            print("🟢 NYSC registration is open!")
        else:
            print("🔴 Registration is still closed.")
    except Exception as e:
        print(f"Error checking site: {e}")

def main():
    check_registration()

if __name__ == "__main__":
    main()
