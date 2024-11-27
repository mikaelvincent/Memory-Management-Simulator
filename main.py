from models.page import Page
import sys

def parse_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("Input file must contain at least two lines: page references and number of frames.")
            
            page_references = list(map(int, lines[0].strip().split()))
            num_frames = int(lines[1].strip())
            
            if num_frames <= 0:
                raise ValueError("Number of frames must be a positive integer.")
            
            return page_references, num_frames
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    page_references, num_frames = parse_input(input_file)
    
    # Proceed with simulation using page_references and num_frames

if __name__ == "__main__":
    main()
