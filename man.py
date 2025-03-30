import google.generativeai as genai
import os
from dotenv import load_dotenv

# LOAD DOTENV
load_dotenv()

# LAOD API KEY
Api_Key = os.getenv("API_KEY")

# CONFIGURE THE GEN AI USING API
genai.configure(api_key=Api_Key)


model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Can nt tell me anyother jokes")

print(response.text)

             