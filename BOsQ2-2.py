def simulate_paging(memory_size, page_size, page_requests, algorithm):
    num_frames = memory_size // page_size
    memory = []
    page_table = {}
    page_faults = 0

    print(f"\nMemory Size: {memory_size}, Page Size: {page_size}, Frames: {num_frames}")
    print(f"Page Requests: {page_requests}")
    print(f"Algorithm: {algorithm}\n")
    print("Simulation Start:\n")

    for i, page in enumerate(page_requests):
        if page not in memory:  # Page fault occurs
            page_faults += 1
            if len(memory) < num_frames:
                memory.append(page)
            else:
                if algorithm == "FIFO":
                    memory.pop(0)  # Remove the oldest page
                elif algorithm == "LRU":
                    lru_page = sorted(page_table, key=lambda k: page_table[k])[0]
                    memory.remove(lru_page)
                elif algorithm == "Optimal":
                    future_uses = [
                        (page, page_requests[i + 1 :].index(page) if page in page_requests[i + 1 :] else float("inf"))
                        for page in memory
                    ]
                    future_uses.sort(key=lambda x: x[1], reverse=True)
                    memory.remove(future_uses[0][0])

                memory.append(page)
        page_table[page] = i  # Update the last use of the page

        print(f"Step {i + 1}: Requesting Page {page}")
        print(f"Memory State: {memory}")
        print(f"Page Table: {page_table}")
        print(f"Page Faults so far: {page_faults}\n")

    print("Simulation End\n")
    print(f"Total Page Faults: {page_faults}")


# Input from the user
try:
    memory_size = int(input("Enter the size of physical memory (in KB): "))
    page_size = int(input("Enter the size of a page (in KB): "))
    
    print("Enter the sequence of page requests (comma-separated):")
    page_requests = list(map(int, input().strip().split(',')))
    
    print("Choose the page replacement algorithm (FIFO, LRU, Optimal):")
    algorithm = input().strip().upper()

    if algorithm not in ["FIFO", "LRU", "OPTIMAL"]:
        raise ValueError("Invalid algorithm selected. Please choose FIFO, LRU, or Optimal.")

    simulate_paging(memory_size, page_size, page_requests, algorithm)
except ValueError as e:
    print(f"Error: {e}")