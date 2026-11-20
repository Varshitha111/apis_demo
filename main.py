import os
from dotenv import load_dotenv
load_dotenv()
data=os.getenv("api_key")
print(data)