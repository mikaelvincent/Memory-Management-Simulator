from typing import Dict, List

class StatisticsAggregator:
    """
    Aggregates and summarizes performance metrics from multiple page replacement algorithms.
    """
    def __init__(self):
        self.algorithm_stats: Dict[str, Dict[str, float]] = {}

    def add_statistics(self, algorithm_name: str, stats: Dict[str, float]):
        """
        Adds statistics for a specific algorithm.

        Args:
            algorithm_name (str): The name of the algorithm.
            stats (Dict[str, float]): The performance metrics.
        """
        self.algorithm_stats[algorithm_name] = stats

    def display_summary(self):
        """
        Displays a summary of performance metrics for all algorithms.
        """
        if not self.algorithm_stats:
            print("No statistics to display.")
            return

        print("\n=== Summary of Performance Metrics ===")
        print(f"{'Algorithm':<10} | {'Hits':<5} | {'Faults':<7} | {'Hit%':<6} | {'Fault%':<7}")
        print("-" * 45)
        for algo, stats in self.algorithm_stats.items():
            print(f"{algo:<10} | {stats['page_hits']:<5} | {stats['page_faults']:<7} | "
                  f"{stats['hit_percentage']:<6.2f} | {stats['fault_percentage']:<7.2f}")
