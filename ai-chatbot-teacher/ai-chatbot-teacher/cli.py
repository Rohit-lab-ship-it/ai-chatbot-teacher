
import argparse
from teacher_bot import generate_answer

def main():
    parser = argparse.ArgumentParser(description="AI Chatbot Teacher - CLI")
    parser.add_argument("-q", "--question", type=str, help="Your question (any supported language).")
    args = parser.parse_args()

    if not args.question:
        print("Enter your question (press Ctrl+C to exit):")
        try:
            while True:
                q = input("> ").strip()
                if not q:
                    continue
                print("\n--- Answer ---")
                print(generate_answer(q))
                print("\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
    else:
        print(generate_answer(args.question))

if __name__ == "__main__":
    main()
