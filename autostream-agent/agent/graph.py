from agent.intent import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture

def process_message(state, user_input):

    state.intent = detect_intent(user_input)

    if state.intent == "greeting":
        return "Hi 👋 I’m AutoStream AI. Ask me about pricing or features."

    if state.intent == "product_query":
        return str(get_answer(user_input))

    if state.intent == "high_intent":
        if not state.name:
            return "Great! What’s your name?"
        if not state.email:
            return "Thanks. What’s your email?"
        if not state.platform:
            return "Which platform do you create on? (YouTube, Instagram, etc)"

    if state.name and state.email and state.platform:
        mock_lead_capture(state.name, state.email, state.platform)
        return "You’re all set 🚀 Our team will contact you soon."

    return "Can you clarify?"
