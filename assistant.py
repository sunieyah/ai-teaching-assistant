import subprocess
from prompts import explanation_prompt, mcq_prompt, short_questions_prompt

def get_ai_response(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

def main():
    print("AI-Powered Teaching Assistant (Generative AI)")
    print("-------------------------------------------")
    print("1. Explain a topic")
    print("2. Generate MCQs")
    print("3. Generate Short Questions")

    choice = input("Enter choice (1/2/3): ").strip()
    topic = input("Enter CS topic: ").strip()

    if choice == "1":
        prompt = explanation_prompt(topic)
    elif choice == "2":
        prompt = mcq_prompt(topic)
    elif choice == "3":
        prompt = short_questions_prompt(topic)
    else:
        print("Invalid choice")
        return

    print("\nGenerating response...\n")
    print(get_ai_response(prompt))

if __name__ == "__main__":
    main()
