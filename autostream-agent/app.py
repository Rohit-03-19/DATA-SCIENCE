from agent.state import AgentState
from agent.graph import process_message

state = AgentState()

print("AutoStream AI Agent Started\n")

while True:
    user = input("You: ")

    if state.intent == "high_intent" and not state.name:
        state.name = user
    elif state.intent == "high_intent" and not state.email:
        state.email = user
    elif state.intent == "high_intent" and not state.platform:
        state.platform = user

    reply = process_message(state, user)
    print("Agent:", reply)
