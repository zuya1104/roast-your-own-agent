import os

LINE = "My agent entered 40 bounties, banked $10 once, and now introduces itself as a professional prize-winner without cracking a smile."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
