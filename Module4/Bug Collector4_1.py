# Bug Collector4_1

def main():
    # Initialize the accumulator.
    total=0

    # Get the bugs collected for each day.
    for day in range(1,8):
        # Prompt the user to enter number of bugs
        print('Enter the number of bugs collected on day',day)
        bugs=int(input())
        # Add bugs to total
        total+=bugs

    # Display the total bugs
    print('You collected a total of',total,'bugs')
main()
