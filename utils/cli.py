from typing import List, Tuple
from algorithms.fifo import FIFOReplacement
from algorithms.lfu import LFUReplacement
from algorithms.lru import LRUReplacement
from algorithms.optimal import OptimalReplacement
from tabulate import tabulate

def get_page_references() -> List[int]:
    """
    Prompts the user to provide a file containing the page reference sequence.
    Parses the file to extract a list of page references.

    Returns:
        List[int]: A list of page reference integers.
    """
    while True:
        file_path = input("Please enter the path to the page reference file: ").strip()
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                page_references = list(map(int, content.strip().split()))
                if not page_references:
                    print("Error: The page reference file is empty.")
                    continue
                return page_references
        except FileNotFoundError:
            print(f"Error: File not found at '{file_path}'. Please provide a valid file path.")
        except ValueError:
            print("Error: Invalid file format. Ensure the file contains space-separated integers.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")

def get_num_frames() -> int:
    while True:
        try:
            num_frames = int(input("Please enter the number of frames: "))
            if num_frames <= 0:
                print("Error: Number of frames must be a positive integer.")
                continue
            return num_frames
        except ValueError:
            print("Error: Invalid input. Please enter a positive integer.")

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
                print(f"Error: Invalid choice '{choice}'. Please select valid options.")
                valid = False
                break
            selected.add(algorithms[choice][0])
        if valid and selected:
            break
        else:
            selected.clear()
    return [(name, cls) for key, (name, cls) in algorithms.items() if name in selected]
