# Env file = .(dot.env)
# Store credentials in this file
# pip install python-dotenv

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()
    url = os.getenv("URL")
    print(url)