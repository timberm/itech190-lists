#lists & loops & functions

def while_loop(lyst):
    index = 0
    while index < len(lyst):
        print(lyst[index])
        index += 1

def for_loop(lyst):
    for i in range(len(lyst)):
        print(lyst[i])

def main():
    animals = [
        "beaver", "eagle", "basketball", "frog", "woodpecker", "bear"
    ]

    while_loop(animals)
    for_loop(animals)
    for_loop(animals[2:5])

if __name__ == "__main__":
    main()


