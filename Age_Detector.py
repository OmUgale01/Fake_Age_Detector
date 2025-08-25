import time
import sys
import random

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_loading(task, dots=3, wait=0.3):
    slow_print(f"[+] {task}", 0.03)
    for i in range(dots):
        sys.stdout.write("   Searching" + "." * (i + 1) + "   \r")
        sys.stdout.flush()
        time.sleep(wait)
    print()

def main():
    slow_print("=== Advanced Research Age Detector ===", 0.03)
    age = input("Enter your age: ")

    slow_print("\nInitializing ultra-secure connections...\n", 0.03)
    fake_loading("Connecting to NASA supercomputers...")
    fake_loading("Accessing Government Citizen Records Database...")
    fake_loading("Cross-checking with Secret Intelligence Files...")
    fake_loading("Running Deep AI Analysis...")
    fake_loading("Decrypting hidden files...")
    
    time.sleep(1)
    slow_print("\n[✓] Research Completed!", 0.04)
    time.sleep(1)

    slow_print(f"\n>>> After heavy research, your age is: {age} 🎉", 0.06)
    slow_print("\nThank you for using Age Research Tool!", 0.03)

if __name__ == "__main__":
    main()
