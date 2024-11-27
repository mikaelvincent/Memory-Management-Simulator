from typing import List
from models.page import Page

def display_memory_state(frames: List[Page]):
    """
    Visualizes the current state of physical memory.
    
    Args:
        frames (List[Page]): A list of Page objects currently in physical memory.
    """
    if not frames:
        print("Physical Memory is empty.")
        return
    
    memory_representation = " | ".join(f"Page {page.page_number}" for page in frames)
    print(f"Physical Memory State: [{memory_representation}]")
    print("-" * (len(memory_representation) + 25))
