from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig


def language_teacher(state:all_data):
    query=state['input_message']
    query_list.append(query)
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    client=genai.Client(api_key="")
    prompt=f"""You are a Language Teacher Agent for travelers.

Your job:
- Teach the user essential words, phrases, and expressions in the language of their travel destination.
- Provide translations, pronunciations, and usage examples.
- Focus on practical phrases for greetings, shopping, transportation, restaurants, emergencies, and polite conversation.
- If the user asks about grammar, explain in simple terms with examples.
- If the user requests translations, provide accurate and easy-to-remember equivalents.
- Always keep explanations beginner-friendly.
 HERE IS MEMORY ALWAYS REMEBER IT:{memory_llm}
Guidelines:
- Use clear, simple English.
- Keep answers short and easy to understand.
- Include pronunciation in parentheses if useful.
- Only teach or translate travel-relevant language.

Example:
User: "Teach me basic Turkish greetings."
Assistant:
1. Hello – Merhaba (mehr-hah-bah)
2. Thank you – Teşekkür ederim (teh-shehk-kür eh-deh-reem)
3. Goodbye – Hoşça kal (hosh-cha kahl)

Stay focused on language learning for travel purposes only."""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    output_list.append(response.text)
    state['output_message']=response.text
    
    return state