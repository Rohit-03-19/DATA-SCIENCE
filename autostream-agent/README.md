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

````bash
python -m venv venv

venv\Scripts\activate# AutoStream – Social-to-Lead Agentic Workflow

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

yaml
Copy code

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Create virtual environment
```bash
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the agent
bash
Copy code
python app.py
You should see:

nginx
Copy code
AutoStream AI Agent Started
🧪 Example Test Flow
Type the following in order:

css
Copy code
Hi, tell me about your pricing
I want to try the Pro plan for my YouTube channel
Rohit
rohit@gmail.com
YouTube
You will see:

nginx
Copy code
Lead captured successfully: Rohit, rohit@gmail.com, YouTube
````
