import json

with open("data/knowledge_base.json") as f:
    KB = json.load(f)

def get_answer(query):
    query = query.lower()

    if "basic" in query:
        plan = KB["pricing"]["basic"]
        return (
            "Here is our Basic Plan 👇\n"
            f"• Price: {plan['price']}\n"
            f"• Video limit: {plan['videos']}\n"
            f"• Resolution: {plan['resolution']}\n\n"
            "This plan is great for beginners who are just getting started with content creation."
        )

    if "pro" in query or "pricing" in query or "plans" in query:
        basic = KB["pricing"]["basic"]
        pro = KB["pricing"]["pro"]

        return (
            "Here are AutoStream’s pricing plans 👇\n\n"
            "🔹 Basic Plan\n"
            f"• Price: {basic['price']}\n"
            f"• Videos: {basic['videos']}\n"
            f"• Resolution: {basic['resolution']}\n\n"
            "🔹 Pro Plan\n"
            f"• Price: {pro['price']}\n"
            f"• Videos: {pro['videos']}\n"
            f"• Resolution: {pro['resolution']}\n"
            f"• Extra features: {', '.join(pro['features'])}\n\n"
            "Most professional creators choose the Pro plan for high-quality 4K videos and AI captions."
        )

    if "refund" in query:
        return "Our policy is simple: No refunds are available after 7 days of purchase."

    if "support" in query:
        return "We provide 24/7 customer support, but it is available only on the Pro plan."

    return "I couldn’t find that in AutoStream’s knowledge base. Try asking about pricing, plans, or support."
