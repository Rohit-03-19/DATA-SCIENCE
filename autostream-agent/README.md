# AutoStream – Social-to-Lead Agentic Workflow

This project implements an **agentic conversational AI** for a fictional SaaS company called **AutoStream**, which provides automated video editing tools for content creators.  
The agent is designed to convert social media conversations into **qualified sales leads**, similar to how ServiceHive’s **Inflx** platform works.

The system goes beyond a chatbot by combining:

- Intent detection
- RAG-based knowledge retrieval
- Stateful multi-turn conversations
- Tool-based lead capture

---

## 🧠 What the Agent Can Do

The AutoStream agent is capable of:

1. **Understanding user intent**

   - Casual greeting
   - Product or pricing inquiry
   - High-intent lead (ready to sign up)

2. **Answering product questions using RAG**

   - Pricing plans
   - Features
   - Company policies

3. **Qualifying leads**

   - Detects when a user is ready to buy
   - Collects name, email, and creator platform

4. **Triggering backend actions**
   - Calls a mock API only after all lead details are collected

---

## 📁 Project Structure

autostream-agent/
│
├── app.py
├── agent/
│ ├── state.py
│ ├── intent.py
│ ├── rag.py
│ ├── tools.py
│ └── graph.py
│
├── data/
│ └── knowledge_base.json
│
├── requirements.txt
└── README.md

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Create virtual environment

```bash
python -m venv venv

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

```

2️⃣ Install dependencies

```bash
pip install -r requirements.txt

```

3️⃣ Run the agent

```bash
python app.py


You should see:

AutoStream AI Agent Started

```

🧪 Example Test Flow

Type the following in order:

Hi, tell me about your pricing
I want to try the Pro plan for my YouTube channel
Rohit
rohit@gmail.com
YouTube

You will see:

Lead captured successfully: Rohit, rohit@gmail.com, YouTube

## 🏗️ Architecture Explanation

LangGraph was chosen for this project because it is specifically designed for building stateful, multistep AI agents. Unlike basic chatbots, this agent must remember information across multiple turns, detect intent shifts, and trigger actions only when conditions are satisfied. LangGraph allows us to model the agent as a workflow with clear control over state and transitions.

The system maintains an AgentState object that stores the user’s intent, name, email, and creator platform. This state persists across multiple conversation turns, enabling the agent to behave like a real sales assistant instead of a stateless chatbot.

A Retrieval Augmented Generation (RAG) pipeline is implemented using a local JSON knowledge base that contains AutoStream’s pricing, features, and policies. Whenever a user asks about pricing or features, the agent retrieves the relevant information from this knowledge base and formats it into natural language responses.

Tool execution is strictly controlled. The mock lead capture function is only triggered after all three required values (name, email, platform) are present in the state. This ensures realistic, production-style behavior similar to real SaaS lead automation systems.

## 📲 How This Would Be Deployed on WhatsApp

To deploy this agent on WhatsApp, a webhook-based integration can be used through Meta WhatsApp Cloud API or Twilio WhatsApp API.

Each incoming WhatsApp message would be sent to a backend webhook. This webhook would:

Extract the user’s phone number (used as a session ID)

Load or create an AgentState for that user

Pass the message to the agent

Send the agent’s response back to WhatsApp

The agent state can be stored in Redis or a database so that conversations remain consistent even if the server restarts. This allows thousands of WhatsApp users to interact with the AutoStream agent simultaneously while maintaining individual conversation memory.
