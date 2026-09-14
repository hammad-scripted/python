from dotenv import load_dotenv
from google import genai
load_dotenv()


client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="hi there i am hammad"
)


print(interaction.output_text)