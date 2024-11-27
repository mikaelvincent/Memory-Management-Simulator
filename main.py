from utils.cli import get_page_references, get_num_frames, select_algorithms
from utils.runner import run_algorithms
from utils.statistics import StatisticsAggregator

def main():
    print("=== Memory Management Simulator ===\n")
    
    page_references = get_page_references()
    num_frames = get_num_frames()
    
    selected_algorithms = select_algorithms()
    stats_aggregator = StatisticsAggregator()
    
    run_algorithms(selected_algorithms, num_frames, page_references, stats_aggregator)
    
    stats_aggregator.display_summary()

if __name__ == "__main__":
    main()
