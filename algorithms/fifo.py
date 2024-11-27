from collections import deque
from models.page import Page

class FIFOReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = [None] * self.num_frames  # Fixed frame list
        self.queue = deque()
        self.page_map = {}
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []

    def access_page(self, page_number):
        if page_number in self.page_map:
            self.page_hits += 1
            # No need to update the queue for FIFO
        else:
            self.page_faults += 1
            new_page = Page(page_number=page_number)
            if None in self.frames:
                frame_index = self.frames.index(None)
                self.frames[frame_index] = new_page
                self.page_map[page_number] = new_page
                self.queue.append(frame_index)
                self.replacement_log.append(f"Loaded page {page_number} into Frame {frame_index + 1}.")
            else:
                oldest_frame_index = self.queue.popleft()
                oldest_page = self.frames[oldest_frame_index]
                del self.page_map[oldest_page.page_number]
                self.replacement_log.append(f"Replaced page {oldest_page.page_number} with page {page_number} in Frame {oldest_frame_index + 1}.")
                self.frames[oldest_frame_index] = new_page
                self.page_map[page_number] = new_page
                self.queue.append(oldest_frame_index)

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
