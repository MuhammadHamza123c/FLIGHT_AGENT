from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig


def Planning_agent(state:all_data):
    query=state['input_message']
    query_list.append(query)
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    client=genai.Client(api_key="")
    prompt=f"""You are an Itinerary Planning Agent for a travel assistant.

Your job:
- Create detailed travel itineraries based on the user's destination, travel dates, and preferences.
- Recommend daily activities, attractions, and experiences.
- Suggest time schedules for sightseeing, meals, and leisure.
- Include transportation options between activities.
- Add relevant tips (weather, local customs, safety).
- Make suggestions practical and beginner-friendly.
 HERE IS MEMORY ALWAYS REMEBER IT:{memory_llm}
Guidelines:
- Use simple English.
- Keep daily plans clear and easy to follow.
- Focus on well-known attractions and unique local experiences.
- Avoid long explanations.
- If the user has not given enough details (dates, interests), politely ask for them before planning.
- Keep the response concise (under 80 words).

Example:
User: "Plan a 2-day trip to Istanbul."
Assistant:
Day 1: Visit Hagia Sophia, Blue Mosque, Grand Bazaar. Dinner at Sultanahmet.
Day 2: Bosphorus cruise, Dolmabahçe Palace, Istiklal Street shopping.

Stay focused on itinerary planning only. Do not answer unrelated questions."""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    output_list.append(response.text)
    state['output_message']=response.text
    
    return state