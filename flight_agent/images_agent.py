from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig
import requests


def images_agent(state:all_data):
    query=state['input_message']
    client=genai.Client(api_key="")
    prompt=f"""You are an Image Search Place Extractor.
Your task: From the user's message, extract only the place name that refers to a city, country, landmark, tourist attraction, or geographic location anywhere in the world.

Rules:
1. Ignore extra words like "show me", "images of", "pictures of", "please", etc.
2. Do not include any other text, punctuation, or explanation.
3. Return only the place name exactly as it should be searched (e.g., "Ankara", "Eiffel Tower", "Machu Picchu").
4. If there is no valid place in the query, return an empty string.

Example inputs and outputs:
- Input: "Show me some images of Ankara" → Output: Ankara
- Input: "Can you find pictures of the Eiffel Tower?" → Output: Eiffel Tower
- Input: "Give me photos from New York City" → Output: New York City
- Input: "Show me some cats" → Output: (empty string)
"""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    place_name=response.text
    url=f"https://pixabay.com/api/?key=51639631-e376af61aab645634b3d0feb9&q={place_name}&image_type=photo&pretty=true"
    response=requests.get(url)
    data=response.json()
    result=f'Here is Image of {place_name}: '
    for i in range(0,2):
     url_web=data['hits'][i]['webformatURL']
     result+=f'{url_web}\n\n'
    state['output_message']=result
    return state
    