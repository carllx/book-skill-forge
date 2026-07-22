import os
import argparse
import sys

def rename_books(task_folder):
    """
    A helper script to outline the required book renaming process.
    Note: Real automatic renaming might require an LLM API to extract Author/Year from the PDF.
    This script provides the structural framework for the Agent.
    """
    input_dir = os.path.join(r"E:\MinerU\Tasks", task_folder)
    if not os.path.exists(input_dir):
        print(f"Error: Input directory {input_dir} not found.")
        sys.exit(1)

    print(f"Scanning directory: {input_dir}")
    print("WARNING: Files must be named according to the academic standard: 'Author - Year - Title.pdf'")
    
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    
    needs_rename = []
    for f in files:
        # A simple heuristic to check if it matches "Author - Year - Title.pdf"
        # We expect at least two " - " separators.
        parts = f.split(" - ")
        if len(parts) >= 3:
            print(f"[OK] {f}")
        else:
            print(f"[NEEDS RENAME] {f}")
            needs_rename.append(f)
            
    if needs_rename:
        print("\nACTION REQUIRED BY AGENT:")
        print("The following files do not meet the naming standard (Author - Year - Title.pdf):")
        for f in needs_rename:
            print(f" - {f}")
        print("\nAgent Instruction: Please use your tools (like web search or LLM analysis) to infer the correct Author, Year, and Title for these files, and rename them BEFORE proceeding with the MinerU workflow.")
        sys.exit(1)
    else:
        print("\nAll files meet the naming standard. Ready for OCR processing.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check book naming conventions in a Task folder.")
    parser.add_argument("--task", required=True, help="Name of the task folder.")
    args = parser.parse_args()
    rename_books(args.task)
