import os
import openai

from dotenv import load_dotenv
from BookGenerator import BookGenerator

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", None)

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    BookGenerator(topic, confirm = True, use_existing_outline = False, dry_run = False).generate()