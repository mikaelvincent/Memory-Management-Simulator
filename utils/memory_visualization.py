from typing import List
from models.page import Page
from tabulate import tabulate

def display_memory_state(frames: List[Page]):
    """
    Visualizes the current state of physical memory.
    
    Args:
        frames (List[Page]): A list of Page objects currently in physical memory.
    """
    table = [["Frame", "Page Number"]]
    for idx, page in enumerate(frames, start=1):
        page_number = page.page_number if page else " "
        table.append([f"Frame {idx}", page_number])
    
    print("\nCurrent Physical Memory State:")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
