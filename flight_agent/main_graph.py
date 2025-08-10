from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from state_data import all_data
from analyze_agent import LLM_AGENT
from decide_agent import decide_agent
from language_teacher import language_teacher
from Planning_agent import Planning_agent
from document_agent import document_agent
from images_agent import images_agent
from flight_agent import book_flight
from emergen_agent import emergency_agent
from hotel_agent import book_hotel
memory1=MemorySaver()
builder=StateGraph(all_data)
builder.add_node("ANALYZE_LLM",decide_agent)

builder.add_node("LLM",LLM_AGENT)

builder.add_node('Language',language_teacher)

builder.add_node("Planning",Planning_agent)

builder.add_node('Documents',document_agent)

builder.add_node("Book",book_flight)

builder.add_node("IMAGE_AGENT",images_agent)

builder.add_node("EMERGENCY_AGENT",emergency_agent)

builder.add_node("HOTEL_AGENT",book_hotel)

builder.add_node("FLIGHT_AGENT",book_flight)

builder.set_entry_point("ANALYZE_LLM")

builder.add_conditional_edges("ANALYZE_LLM",lambda s:s['route'],{
    'Language Teacher':"Language",
    'Info_Agent':"LLM",
    'Itinerary Planner Agent':"Planning",
    'Visa & Travel Document Agent':'Documents',
    'Image Show of tourist places':"IMAGE_AGENT",
    'Emergency':'EMERGENCY_AGENT',
    'Hotel':"HOTEL_AGENT",
    'Flight':"FLIGHT_AGENT"
})


builder.set_finish_point("LLM")

builder.set_finish_point("Language")

builder.set_finish_point("Planning")

builder.set_finish_point("Documents")

builder.set_finish_point("IMAGE_AGENT")

builder.set_finish_point("EMERGENCY_AGENT")

builder.set_finish_point("HOTEL_AGENT")

builder.set_finish_point("FLIGHT_AGENT")

covo=builder.compile(checkpointer=memory1)







