from collections import OrderedDict
from models.page import Page

class LRUReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = [None] * self.num_frames
        self.page_map = {}
        self.access_order = OrderedDict()
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []

    def access_page(self, page_number):
        if page_number in self.page_map:
            self.page_hits += 1
            self.access_order.move_to_end(page_number)
        else:
            self.page_faults += 1
            new_page = Page(page_number=page_number)
            if None in self.frames:
                frame_index = self.frames.index(None)
                self.frames[frame_index] = new_page
                self.page_map[page_number] = new_page
                self.access_order[page_number] = None
                self.replacement_log.append(f"Loaded page {page_number} into Frame {frame_index + 1}.")
            else:
                # Replace the least recently used page
                lru_page = next(iter(self.access_order))
                frame_index = self.frames.index(self.page_map[lru_page])
                del self.page_map[lru_page]
                del self.access_order[lru_page]
                self.replacement_log.append(f"Replaced page {lru_page} with page {page_number} in Frame {frame_index + 1}.")
                self.frames[frame_index] = new_page
                self.page_map[page_number] = new_page
                self.access_order[page_number] = None

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
