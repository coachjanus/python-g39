
import sys
import os
from config import build_parser
from tree import generate_tree

# def main():
#     if len(sys.argv) > 1: # checks if user added args
#         args = build_parser()
        
#         root_path = os.path.abspath(args.root_path)
        
#         output_file = args.output_file
#         follow_symlinks = args.follow_symlinks # aka shortcuts
        
#         ignore_list = args.ignore_list or []
        

        
#     else: # hardcode in file directions
#         root_path = os.path.dirname(__file__)
#         output_file = os.path.join(root_path, 'directory_tree_output.txt')
#         ignore_list = ['venv','.git', '.gitignore','.DS_Store','.vscode'] # example
#         follow_symlinks=False
        

        
#     generate_tree(root_path, follow_symlinks, ignore_list, output_file)

def main():
    # If arguments are passed, use the parser
    if len(sys.argv) > 1:
        args = build_parser()
        root_path = os.path.abspath(args.root_path)
        output_file = args.output_file
        ignore_list = args.ignore_list
        follow_symlinks = args.follow_symlinks
        max_depth = args.max_depth
    else:
        # Default behavior for quick local runs
        root_path = os.getcwd()
        output_file = None
        ignore_list = {'.git', '__pycache__', 'venv', '.DS_Store'}
        follow_symlinks = False
        max_depth = 2  # Shallow default for safety
        print(f"--- Running in default mode (Depth: {max_depth}) ---\n")

    if not os.path.exists(root_path):
        print(f"Error: Path '{root_path}' does not exist.")
        return

    generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file)

if __name__ == "__main__":
    main()
