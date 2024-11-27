from models.page import Page

class OptimalReplacement:
    def __init__(self, num_frames, page_references):
        self.num_frames = num_frames
        self.page_references = page_references
        self.frames = []
        self.page_hits = 0
        self.page_faults = 0
        self.replacement_log = []
        self.current_index = 0

    def access_page(self, page_number):
        if page_number in [page.page_number for page in self.frames]:
            self.page_hits += 1
        else:
            self.page_faults += 1
            if len(self.frames) < self.num_frames:
                new_page = Page(page_number=page_number)
                self.frames.append(new_page)
                self.replacement_log.append(f"Loaded page {page_number} into physical memory.")
            else:
                # Determine the page to replace
                future_indices = {}
                for page in self.frames:
                    try:
                        future_index = self.page_references[self.current_index + 1:].index(page.page_number)
                        future_indices[page.page_number] = self.current_index + 1 + future_index
                    except ValueError:
                        future_indices[page.page_number] = float('inf')
                # Select the page with the farthest next use
                page_to_replace = max(future_indices, key=future_indices.get)
                self.frames = [page for page in self.frames if page.page_number != page_to_replace]
                self.replacement_log.append(f"Replaced page {page_to_replace} with page {page_number}.")
                new_page = Page(page_number=page_number)
                self.frames.append(new_page)
        self.current_index += 1

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
