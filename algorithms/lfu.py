from models.page import Page
from collections import defaultdict

class LFUReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = {}
        self.frequency = defaultdict(int)
        self.min_frequency = 0
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []

    def access_page(self, page_number):
        if page_number in self.frames:
            self.page_hits += 1
            self.frequency[page_number] += 1
        else:
            self.page_faults += 1
            if len(self.frames) < self.num_frames:
                new_page = Page(page_number=page_number)
                self.frames[page_number] = new_page
                self.frequency[page_number] = 1
                self.replacement_log.append(f"Loaded page {page_number} into physical memory.")
                self.min_frequency = 1
            else:
                # Find the page with the lowest frequency
                min_freq = min(self.frequency.values())
                candidates = [p for p in self.frames if self.frequency[p] == min_freq]
                # Replace the oldest page among candidates
                page_to_replace = candidates[0]
                del self.frames[page_to_replace]
                del self.frequency[page_to_replace]
                self.replacement_log.append(f"Replaced page {page_to_replace} with page {page_number}.")
                new_page = Page(page_number=page_number)
                self.frames[page_number] = new_page
                self.frequency[page_number] = 1
                self.min_frequency = 1

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
