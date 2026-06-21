import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(


api_key=os.getenv(
    "GOOGLE_API_KEY"
)


)

model = genai.GenerativeModel(
"gemini-2.5-flash"
)

def generate_plan(subjects):


    if not subjects:
        return "No subjects added."

    prompt = f"""
    ```

    Create a study timetable.

    Subjects:
    {subjects}

    Return:

    Morning:
    Afternoon:
    Night:

    Give one study tip.

    """

    
    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except:

        return (
            "Could not generate timetable."
        )

