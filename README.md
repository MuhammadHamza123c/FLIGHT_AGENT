AI-Powered Flight Agent
An all-in-one AI travel assistant that plans trips, books flights & hotels, teaches local languages, shows destination images, and ensures your safety all powered by multi-agent AI systems.

How This Idea Came

While planning a trip, I realized how fragmented the process is:

Flight booking on one website.

Hotel booking on another.

Language learning on a separate app.

Emergency contacts stored elsewhere.

I thought: What if one AI agent could do all of this seamlessly in one place?
That question became the Flight Agent

Why We Need This
Travel is not only about moving from point A to point B — it’s about making the journey stress-free.
Currently:

Tools are disconnected.

There’s no emergency integration in trip planners.

Learning local phrases requires a separate app.

Flight Agent solves all of these by providing:
✔️ One AI interface for all tasks.

 About the Project
Flight Agent is an AI-powered multi-agent system that can:

Plan your trip — suggest destinations & itineraries.

Provide detailed location info — history, attractions, tips.

Teach local languages — essential travel phrases.

Show destination images — via Pixabay API.

Book flights — using integrated APIs.

Book hotels — find & reserve accommodations.

Inform relatives in case of emergency — auto-email alerts via SMTP.


Tech Stack
Category	Tools / Libraries
AI & Agents	Google Gemini, LangChain, LangGraph
Automation	Python Scripting, APIs
Communication	SMTP (Email Sending)
Image Search	Pixabay API
Data Processing	JSON, REST APIs
Environment	Python 3.x, Virtualenv

 How It Works
User Input → Destination, travel dates, preferences.

Trip Planner Agent → Generates itinerary with Gemini & LangChain.

Location Info Agent → Fetches details about the destination.

Language Agent → Teaches essential local phrases.

Image Agent → Fetches destination images using Pixabay API.

Flight Booking Agent → Searches & reserves flights.

Hotel Booking Agent → Finds and books accommodations.

Emergency Contact Agent → Sends safety alerts to relatives.

 Installation & Setup

# Clone the repository
git clone https://github.com/MuhammadHamza123c/FLIGHT_AGENT.git
cd FLIGHT_AGENT

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add API keys in .env file
GEMINI_API_KEY=your_gemini_key
PIXABAY_API_KEY=your_pixabay_key
SMTP_EMAIL=your_email
SMTP_PASSWORD=your_password


## 📸 Screenshots / Demo

**Flight Booking**  
![Flight Booking](flight.png)  

**Hotel Booking**  
![Hotel Booking](book_hotel.png)  

**Destination Images**  
![Destination Images](images.png)  

**Language Learning Module**  
![Language Learning](language.png)  

**Generated Travel Document**  
![Generated Document](document.png)  

**Emergency Alert System**  
![Emergency Alert](emergency.png)  

**Email Response Confirmation**  
![Email Response](email_response.png)  


 

✔️ Automation for booking & planning.
✔️ Built-in safety measures for emergencies.
