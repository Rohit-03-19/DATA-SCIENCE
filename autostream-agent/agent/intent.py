def detect_intent(message):
    msg = message.lower()

    # 1️⃣ High intent first (most important)
    if any(x in msg for x in ["buy", "sign up", "try", "get started", "i want", "pro plan"]):
        return "high_intent"

    # 2️⃣ Product queries second
    if any(x in msg for x in ["price", "pricing", "plan", "cost", "features"]):
        return "product_query"

    # 3️⃣ Greeting last
    if any(x in msg for x in ["hi", "hello", "hey"]):
        return "greeting"

    return "general"
