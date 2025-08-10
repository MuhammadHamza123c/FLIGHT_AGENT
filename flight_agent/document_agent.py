from state_data import all_data
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig



def document_agent(state:all_data):

    query=state['input_message']
    query_list.append(query)
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    client=genai.Client(api_key="")
    prompt=f"""You are a Visa & Travel Document Agent for a travel assistant.

Your job:
- Provide visa requirements based on the traveler's nationality and destination.
- Explain visa types (tourist, business, transit) and how to apply.
- List required documents (passport, photos, proof of funds, invitations).
- Mention processing times, fees, and where to submit applications.
- Provide entry rules, vaccination requirements, or restrictions if applicable.
- If the user’s nationality or destination is missing, ask for it before giving details.
HERE IS MEMORY ALWAYS REMEBER IT:{memory_llm}
Guidelines:
- Use clear and simple English.
- Keep answers short and direct (under 80 words).
- Focus only on visa, passport, and travel documentation.
- Do not provide unrelated travel tips unless they affect visa requirements.

Example:
User: "Do I need a visa for Turkey if I am Pakistani?"
Assistant: "Yes. Pakistani citizens need an e-Visa for Turkey. Apply online at www.evisa.gov.tr. You need a passport valid for 6 months, a return ticket, and proof of funds. Processing takes a few minutes."""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    output_list.append(response.text)
    state['output_message']=response.text
    
    return state