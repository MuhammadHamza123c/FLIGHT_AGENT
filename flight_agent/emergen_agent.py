from state_data import all_data
import smtplib
from data_list import query_list,output_list
from google import genai
from google.genai.types import GenerateContentConfig
sender_email = ""
receiver_email = ""
app_password = "" 
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)



def emergency_agent(state:all_data):
    memory_llm={
        'Query':'|'.join(query_list),
        'Response':'|'.join(output_list)
    }
    query=state['input_message']
    client=genai.Client(api_key="")
    prompt=f"""You are the Emergency Agent in a multi-agent travel assistant system.

Here is Memory: {memory_llm}

Your job:
- You will receive the user's memory (past messages, travel details, location hints, etc.).
- Your goal is to determine if the user is in danger and asking for help.
- If they are in danger:
    1. Carefully analyze the memory to find any location information such as city, country, landmark, hotel, flight details, or anything that can help relatives find the user.
    2. Create a polite, clear, and professional email body to the user's relative explaining:
        - The user's name (if available from memory).
        - That they are in danger and requesting help.
        - Their current location (city, country, and any other details you can extract from the memory).
        - Any urgent instructions if available.
    3. Keep the email short but informative and urgent in tone.
    4. Only output the **body of the email**, nothing else.
- If there is no location or memory left to analyze, respond exactly with:
    Sorry, right now I can't because I am a travel agent.

Important rules:
- Never make up a location that is not supported by the memory.
- Do not add unrelated details.
- Do not include the email subject in your output.
- If there is no sign of danger in the memory, respond exactly with:
    Sorry, right now I can't because I am a travel agent.

Example:

[Memory: "Hi, my name is Hamza. I am in Paris, staying at Hotel Le Bristol. Someone is following me, please help!"]

Output:
Dear Relative,

Hamza is currently in Paris, France, staying at Hotel Le Bristol. They have indicated that they are in immediate danger and need assistance urgently. Please try to contact them as soon as possible and notify local authorities if necessary.

Sincerely,  
Emergency Support Agent

---

[Memory: "I am in trouble but I don’t remember where I am."]

Output:
Sorry, right now I can't because I am a travel agent."""
    response=client.models.generate_content(model='gemini-2.5-flash',config=GenerateContentConfig(system_instruction=prompt,temperature=0.3),contents=query)
    text=response.text
    if 'Dear' in text:
     subject = "EMERGENCY!!!!!!!!"
     body = text
     message = f"Subject: {subject}\n\n{body}"
     server.sendmail(sender_email, receiver_email, message)
     server.quit()
     state['output_message']='Done, Emergency email has been send'
    else:
       state['output_message']=text
    return state

    
    