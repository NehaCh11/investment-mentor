import os
import asyncio
from dotenv import load_dotenv
from agents import Runner
from inv_agents.coordinator import investment_mentor

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    print("❌ Missing OPENAI_API_KEY in .env.")
    exit(1)

async def main():
    runner = Runner()
    print("💬 Welcome! Type 'quit' or 'exit' to end.\n")

    history = None  # No history at the start

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["quit", "exit"]:
            print("👋 Mentor: Thank you for chatting! Wishing you a successful investment journey.")
            break

        if history is None:
            # First turn: pass a simple string
            result = await runner.run(investment_mentor, user_input)
        else:
            # Add user message as an input item (dict)
            input_list = history.to_input_list()
            input_list.append({"role": "user", "content": user_input})
            result = await runner.run(investment_mentor, input_list)

        print("\nMentor:", result.final_output)

        # Save full chat history for the next turn
        history = result

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❗ An error occurred: {e}")
        exit(1)