from state_data import all_data
from  data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig


def decide_agent(state:all_data):
    query=state['input_message']
    query_list.append(query)
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    client=genai.Client(api_key="")
    prompt=f"""
You are a Query Analysis Agent for a travel assistant.

Your job:
- Read the user's latest query.
- Decide which specialized agent should handle it.
- Return ONLY one of these exact labels (no explanation):
    - Flight
    - Hotel
    - Itinerary Planner Agent
    - Visa & Travel Document Agent
    - Language Teacher
    - Info_Agent
    - Image Show of tourist places
    -Emergency
    -hotel detail
    -flight

Guidelines:
- If the user asks about booking or finding flights → choose "Flight".
- If the user asks about booking or finding hotels, hostels, or stays → choose "Hotel".
- If the user wants a day-by-day plan, things to do, or trip schedule → choose "Itinerary Planner Agent".
- If the user asks about visas, passports, or travel documents → choose "Visa & Travel Document Agent".
- If the user wants help learning or translating a language for their trip → choose "Language Teacher".
- If the user wants to watch/show/see images of some places in the world → choose "Image Show of tourist places"
-If the user is in danger  → choose  "Emergency"
-if the user wants to know/check if there is hotel free in spcific place then → choose "hotel detail"
-if user wants to know about flight → choose 'flight
- If the query is about general information about a country, city, culture, safety, weather, attractions, currency, or history (not booking, not language learning) → choose "Info_Agent".

Return ONLY the category name. No extra words, no punctuation.
"""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    output_list.append(response.text)
    state['route']=response.text
    return state