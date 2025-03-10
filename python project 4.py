import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def main():
    while True:
        try:
            flips = int(input("Enter the number of times you want to flip the coin: "))
            heads = 0
            tails = 0

            for _ in range(flips):
                result = coin_toss()
                if result == "Heads":
                    heads += 1
                else:
                    tails += 1

            print(f"\nResults:")
            print(f"Heads: {heads} ({(heads/flips)*100:.2f}%)")
            print(f"Tails: {tails} ({(tails/flips)*100:.2f}%)")
            
            another_round = input("\nDo you want to flip again? (yes/no): ").strip().lower()
            if another_round != 'yes':
                print("Thanks for playing!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
