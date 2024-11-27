from typing import Dict, List
from tabulate import tabulate

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
            print("No statistics available to display.\n")
            return

        table = [["Algorithm", "Hits", "Faults", "Hit Percentage (%)", "Fault Percentage (%)"]]
        for algo, stats in self.algorithm_stats.items():
            table.append([
                algo,
                stats['page_hits'],
                stats['page_faults'],
                f"{stats['hit_percentage']:.2f}",
                f"{stats['fault_percentage']:.2f}"
            ])
        
        print("\n=== Performance Metrics Summary ===")
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
        print()
