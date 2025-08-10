from main_graph import covo
from langgraph.constants import CONF
from fastapi import FastAPI 
app=FastAPI()
@app.get('/FLIGHT_AGENT')
def flight_agent(query:str):
 config = {
    CONF: {
        "thread_id": "user_trip_session_1"
    }

}



 given_input={
    'input_message':query,
    'output_message':''
}
 result=covo.invoke(given_input,config)
 print(result)
    
 return{
 'Agent':f'{result['output_message']}'
 }
