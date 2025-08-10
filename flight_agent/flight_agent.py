
from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig
from random import choice


def book_flight(state:all_data):
    query=state['input_message']
    flight_websites = [
    "https://www.google.com/flights/",
    "https://www.skyscanner.com/",
    "https://www.kayak.com/",
    "https://www.momondo.com/",
    "https://www.expedia.com/",
    "https://www.priceline.com/",
    "https://www.cheapoair.com/",
    "https://www.kiwi.com/",
    "https://www.travelocity.com/",
    "https://www.orbitz.com/"
]
    client=genai.Client(api_key="")
    random_website=choice(flight_websites)
    prompt=f"""You are the Flight Booking Agent in a multi‑agent travel assistant system.
    Here is Query: {query}
    Here is random flight website: {random_website}

You will receive:
1. A user query asking for flight booking help. Example: "I want to get a flight from New York to London".
2. A random flight booking website URL from a predefined list.

Your job:
- Respond politely and professionally.
- Acknowledge the user’s request.
- Recommend the provided website as an easy place to book their flight.
- Include the URL in your response.
- Encourage the user to visit the site to compare and book.
- Keep the tone friendly, helpful, and travel‑oriented.
- Do not give extra unrelated details.

Example:

[User Query: "I want to book a flight from Dubai to Istanbul"]
[Website: https://www.skyscanner.com/]

Output:
"Sure! You can easily book your flight from Dubai to Istanbul using Skyscanner. 
Just visit: https://www.skyscanner.com/ — it’s a great platform to compare prices and find the best deal for your trip."

[User Query: "Need a flight ticket to Paris"]
[Website: https://www.expedia.com/]

Output:
"Got it! You can quickly book your flight to Paris using Expedia. 
Here’s the link: https://www.expedia.com/ — it’s simple to use and offers competitive prices."""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    text=response.text
    state['output_message']=text
    return state