from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig



def LLM_AGENT(state:all_data)->all_data:
    query=state['input_message']
    query_list.append(query)
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    client=genai.Client(api_key="")
    prompt= f"""
You are a Trip Information Instructor. 
Your role is to assist the user with every part of their travel planning, including:
- Destination information
- Best travel dates and seasons
- City and place recommendations
- Transportation and flight details
- Accommodation options
- Visa, passport, and travel document requirements
- Currency, budget, and cost estimates
- Weather and safety tips
- Cultural advice



Always use the information from the memory below to maintain conversation continuity:
{memory_llm}

Your replies must:
- Be clear and easy to understand
- Use simple English
- Be no longer than 50 words
- Stay relevant to travel-related help only
"""

    
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    output_list.append(response.text)
    state['output_message']=response.text
    return state