from models.page import Page
from collections import defaultdict

class LFUReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = [None] * self.num_frames
        self.frequency = defaultdict(int)
        self.page_map = {}
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []

    def access_page(self, page_number):
        if page_number in self.page_map:
            self.page_hits += 1
            self.frequency[page_number] += 1
        else:
            self.page_faults += 1
            new_page = Page(page_number=page_number)
            if None in self.frames:
                frame_index = self.frames.index(None)
                self.frames[frame_index] = new_page
                self.page_map[page_number] = new_page
                self.frequency[page_number] = 1
                self.replacement_log.append(f"Loaded page {page_number} into Frame {frame_index + 1}.")
            else:
                # Find the page with the lowest frequency
                min_freq = min(self.frequency.values())
                candidates = [p for p in self.page_map if self.frequency[p] == min_freq]
                # Replace the oldest page among candidates
                for frame_index, page in enumerate(self.frames):
                    if page.page_number in candidates:
                        page_to_replace = page.page_number
                        break
                del self.page_map[page_to_replace]
                del self.frequency[page_to_replace]
                self.replacement_log.append(f"Replaced page {page_to_replace} with page {page_number} in Frame {frame_index + 1}.")
                self.frames[frame_index] = new_page
                self.page_map[page_number] = new_page
                self.frequency[page_number] = 1

    def get_statistics(self):
        total_accesses = self.page_hits + self.page_faults
        hit_percentage = (self.page_hits / total_accesses) * 100 if total_accesses else 0
        fault_percentage = (self.page_faults / total_accesses) * 100 if total_accesses else 0
        return {
            'page_hits': self.page_hits,
            'page_faults': self.page_faults,
            'hit_percentage': hit_percentage,
            'fault_percentage': fault_percentage
        }

    def get_replacement_log(self):
        return self.replacement_log
