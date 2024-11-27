from typing import List, Tuple
from utils.memory_visualization import display_memory_state
from utils.statistics import StatisticsAggregator

def run_algorithms(selected_algorithms: List[Tuple[str, object]], num_frames: int, page_references: List[int], stats_aggregator: StatisticsAggregator):
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
        
        print("\n--- Replacement Log ---")
        for log_entry in replacement.get_replacement_log():
            print(log_entry)
