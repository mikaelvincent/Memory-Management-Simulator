from algorithms.fifo import FIFOReplacement
from algorithms.lfu import LFUReplacement
from algorithms.lru import LRUReplacement
from algorithms.optimal import OptimalReplacement
from utils.memory_visualization import display_memory_state
from utils.statistics import StatisticsAggregator
from models.page import Page
import sys

def get_page_references():
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

def get_num_frames():
    while True:
        try:
            num_frames = int(input("Enter the number of frames: "))
            if num_frames <= 0:
                print("Number of frames must be a positive integer.")
                continue
            return num_frames
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def select_algorithms():
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

def display_statistics(stats_aggregator: StatisticsAggregator):
    stats_aggregator.display_summary()

def main():
    print("=== Memory Management Simulator ===")
    
    page_references = get_page_references()
    num_frames = get_num_frames()
    
    selected_algorithms = select_algorithms()
    stats_aggregator = StatisticsAggregator()
    
    for algorithm_name, AlgorithmClass in selected_algorithms:
        print(f"\n--- Running {algorithm_name} Algorithm ---")
        if algorithm_name == 'Optimal':
            replacement = AlgorithmClass(num_frames, page_references)
        else:
            replacement = AlgorithmClass(num_frames)
        
        for page_number in page_references:
            replacement.access_page(page_number)
            display_memory_state(replacement.frames)
        
        stats = replacement.get_statistics()
        stats_aggregator.add_statistics(algorithm_name, stats)
        display_statistics(stats_aggregator)
        
        print("\n--- Replacement Log ---")
        for log_entry in replacement.get_replacement_log():
            print(log_entry)
    
    display_statistics(stats_aggregator)

if __name__ == "__main__":
    main()
