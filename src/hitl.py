def human_fallback(state):
    print("\n⚠️ Escalating to human...")

    user_input = input("Human agent response: ")

    return {"answer": user_input}