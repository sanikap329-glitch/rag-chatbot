from graph import build

def main():
    app = build()

    print("🤖 Bot ready. Type 'exit' to quit.\n")

    while True:
        q = input("You: ")

        if q.lower() == "exit":
            print("👋 Goodbye!")
            break

        result = app.invoke({"query": q})

        if result and "answer" in result:
            print("Bot:", result["answer"])
        else:
            print("Bot: No response generated.")

if __name__ == "__main__":
    main()