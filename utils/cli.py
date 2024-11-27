from typing import List, Tuple
from algorithms.fifo import FIFOReplacement
from algorithms.lfu import LFUReplacement
from algorithms.lru import LRUReplacement
from algorithms.optimal import OptimalReplacement

def get_page_references() -> List[int]:
    while True:
        try:
            input_str = input("Enter page reference sequence (space-separated integers): ")
            page_references = list(map(int, input_str.strip().split()))
            if not page_references:
                print("Page reference sequence cannot be empty.")
                continue
            return page_references
        except ValueError:
            print("Invalid input. Please enter space-separated integers.")

def get_num_frames() -> int:
    while True:
        try:
            num_frames = int(input("Enter the number of frames: "))
            if num_frames <= 0:
                print("Number of frames must be a positive integer.")
                continue
            return num_frames
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def select_algorithms() -> List[Tuple[str, object]]:
    algorithms = {
        '1': ('FIFO', FIFOReplacement),
        '2': ('LRU', LRUReplacement),
        '3': ('LFU', LFUReplacement),
        '4': ('Optimal', OptimalReplacement)
    }
    
    print("\nSelect Page Replacement Algorithms (separated by commas, e.g., 1,3):")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")
    
    selected = set()
    while True:
        choices = input("Enter your choices: ").split(',')
        valid = True
        for choice in choices:
            choice = choice.strip()
            if choice not in algorithms:
                print(f"Invalid choice: {choice}. Please select valid options.")
                valid = False
                break
            selected.add(algorithms[choice][0])
        if valid and selected:
            break
        else:
            selected.clear()
    return [(name, cls) for key, (name, cls) in algorithms.items() if name in selected]
