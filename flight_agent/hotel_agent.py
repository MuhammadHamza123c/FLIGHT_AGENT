from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig
from apify_client import ApifyClient
APIFY_TOKEN = ""
client_app = ApifyClient(APIFY_TOKEN)




def book_hotel(state:all_data):
    query=state['input_message']
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    query=state['input_message']
    client=genai.Client(api_key="")
    prompt=f"""You are the Hotel Booking Place Extractor.
    Here is Memory remember: {memory_llm}
Your task: From the user's message, extract only the city or place name where they want hotel information.

Rules:
1. Ignore extra words like "tell me details about", "hotels in", "show hotels in", "please", etc.
2. Do not include any other text, punctuation, or explanation.
3. Return only the place name exactly as it should be searched (e.g., "Ankara", "Istanbul", "New York City").
4. If no valid city or place name is found, return an empty string.

Examples:
- Input: "Tell details about hotel in Ankara" → Output: Ankara
- Input: "Show me hotels in Istanbul" → Output: Istanbul
- Input: "Can you find hotels in Paris?" → Output: Paris
- Input: "Find hotel rooms in New York City" → Output: New York City
- Input: "Show me hotels" → Output: (empty string)
"""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    text=response.text
    run = client_app.actor("jupri/booking-hotels").call(
        run_input={
    "dev_dataset_clear": False,
    "dev_no_strip": False,
    "entire_place": False,
    "health_safety": False,
    "includes.description": False,
    "includes.facilities": False,
    "includes.fineprints": False,
    "includes.gallery": False,
    "includes.host": False,
    "includes.policies": False,
    "includes.rooms": False,
    "includes.surroundings": False,
    "limit": 3,
    "location": text,
    "sustainable": False
}
    )
    dataset = client_app.dataset(run["defaultDatasetId"])
    result=f"Here is Hotel details for {text} "
    for item in dataset.iterate_items():
        name = item['name']
        description=item['description']
        url=item['url']
        city=item['address']['city']
        result+=f'Name: {name}\nDescription: {description}\nUrl: {url}\nCity: {city}\n\n'
    state['output_message']=result
    return state

    
