from collections import OrderedDict
from models.page import Page

class LRUReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = OrderedDict()
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []

    def access_page(self, page_number):
        if page_number in self.frames:
            self.page_hits += 1
            self.frames.move_to_end(page_number)
        else:
            self.page_faults += 1
            new_page = Page(page_number=page_number)
            if len(self.frames) < self.num_frames:
                self.frames[page_number] = new_page
                self.replacement_log.append(f"Loaded page {page_number} into physical memory.")
            else:
                oldest_page_number, _ = self.frames.popitem(last=False)
                self.replacement_log.append(f"Replaced page {oldest_page_number} with page {page_number}.")
                self.frames[page_number] = new_page

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
