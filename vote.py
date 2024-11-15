import heapq

# Hash Map to store votes
votes = {}

# Max Heap to maintain top candidates
max_heap = []

# Function to cast a vote
def cast_vote(candidate):
    if not candidate:
        print("Candidate name is required!")
        return

    # Update votes in the hash map
    votes[candidate] = votes.get(candidate, 0) + 1

    # Rebuild the heap
    rebuild_heap()
    print(f"Vote cast for {candidate}!")

# Function to rebuild the heap
def rebuild_heap():
    global max_heap
    max_heap = [(-vote_count, candidate) for candidate, vote_count in votes.items()]
    heapq.heapify(max_heap)

# Function to display the top candidates
def display_results():
    print("\nTop Candidates:")
    for votes, candidate in sorted(max_heap, reverse=True):
        print(f"Candidate: {candidate}, Votes: {-votes}")

# Menu-driven program
def main():
    while True:
        print("\nOnline Voting System")
        print("1. Cast Vote")
        print("2. View Results")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            candidate = input("Enter candidate name: ").strip()
            cast_vote(candidate)
        elif choice == "2":
            display_results()
        elif choice == "3":
            print("Exiting the voting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
