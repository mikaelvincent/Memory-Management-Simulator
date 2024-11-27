# Memory Management Simulator

## Overview

This application simulates various page replacement algorithms, including First In First Out (FIFO), Least Recently Used (LRU), Least Frequently Used (LFU), and Optimal. It calculates and displays key metrics such as page hits, page faults, and their respective percentages, and visualizes the memory state after each page replacement.

## Installation

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare the Input File

Create a text file containing the page reference sequence. The file should have space-separated integers representing page numbers. For example:

```
7 0 1 2 0 3 0 4 2 3 0 3 2
```

### 2. Run the Application

Execute the main application script:

```bash
python main.py
```

### 3. Provide Input When Prompted

- **Enter the path to the page reference file:** Specify the path to your page reference sequence file.

- **Enter the number of frames:** Input the number of frames in physical memory.

- **Select Page Replacement Algorithms:** Choose the desired page replacement algorithms by entering the corresponding numbers separated by commas. For example:
  - `1`: FIFO (First In First Out)
  - `2`: LRU (Least Recently Used)
  - `3`: LFU (Least Frequently Used)
  - `4`: Optimal

### 4. View Results

- The application will display the memory state after each page reference is processed.
- A detailed log of page swaps, specifying which pages were replaced and which were loaded into memory, will be displayed.
- A summary of performance metrics, including the number of page hits, page faults, and their percentages for each selected algorithm, will be shown.
