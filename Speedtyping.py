import time
import random

def main():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "In the middle of difficulty lies opportunity.",
        "Life is really simple, but we insist on making it complicated."
    ]

    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    sentence = random.choice(sentences)
    print("\nType the following sentence as quickly as you can:")
    print(sentence)

    input("\nPress Enter when you're ready to start typing...")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(sentence.split())
    typing_speed = words / (time_taken / 60)

    print("\nTime taken:", round(time_taken, 2), "seconds")
    print("Typing speed:", round(typing_speed, 2), "words per minute")

if __name__ == "__main__":
    main()
