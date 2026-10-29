import os, sys
from .config import build_parser
from .tree import generate_tree

APP_NAME = "tree-gen"

# def build_parser() -> argparse.Namespace:
#     parser = argparse.ArgumentParser(
#         prog=APP_NAME,
#         description="Generate a visual directory tree with depth control",
#         epilog="Thanks for using %(prog)s! :)",
#     )
#     group = parser.add_argument_group('Configurations', 'Tree generation settings')
    
#     group.add_argument(
#         'root_path',
#         type=str,
#         nargs='?',
#         default=".",
#         help="Root directory path (default: current directory)"
#     )
#     group.add_argument('-d', '--max_depth',
#         type=int, default=None,
#         help="Maximum depth of the directory tree to display"
#     )
#     group.add_argument( '-o', '--output_file',
#         type=str,
#         help="Output to a specific file instead of console"
#     )
#     group.add_argument('-i', '--ignore_list',
#         nargs='*', default=[],
#         help="List of names (files or folders) to ignore"
#     )
#     group.add_argument('-l', '--follow_symlinks',
#         action='store_true',  help="Follow symbolic links"
#     )
#     return parser.parse_args()

# def generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file):
#     # items = [i for i in os.listdir(root_path) if i not in ignore_list]
#     prefix = ""
#     try:
#        items = [i for i in os.listdir(root_path) if i not in ignore_list]
#     except PermissionError:
#         output_file.write(f"{follow_symlinks}└── [Permission Denied]")
#         return
#     items.sort()
#     count = len(items)

#     print(items, count)
    
#     for index, item in enumerate(items):
#         path = os.path.join(root_path, item)
#         is_last = (index == count - 1)
#         is_dir = os.path.isdir(path)
#         connector = "└── " if is_last else "├── "
#         # output_file.write(f"{prefix}{connector}{item}{'/' if is_dir else ''}\n")
#         print(f"{prefix}{connector}{item}{'/' if is_dir else ''}\n")
        
#     with os.scandir(root_path) as entries:
#         for entry in entries:
#             print(entry.name)


#     # pass


# def generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file=None):
#     if output_file:
#         out = open(output_file, 'w', encoding='utf-8')
#     else:
#         if sys.stdout.encoding.lower() != 'utf-8':
#             sys.stdout.reconfigure(encoding='utf-8')
#         out = sys.stdout

#     try:
#         out.write(f"{os.path.abspath(root_path)}/\n")
#         _walk_recursive(root_path, "", follow_symlinks, set(ignore_list), max_depth, out, current_depth=0)
#     finally:
#         if output_file:
#             out.close()

# def _walk_recursive(current_path, prefix, follow, ignore, max_depth, out, current_depth):
#     # Stop if we've reached the user-defined limit
#     if max_depth is not None and current_depth >= max_depth:
#         return
#     # Get the contents of the current working directory, handling permission errors gracefully
#     try:
#         items = [i for i in os.listdir(current_path) if i not in ignore]
#     except PermissionError:
#         out.write(f"{prefix}└── [Permission Denied]\n")
#         return
#     items.sort()
#     count = len(items)
    
#     for index, item in enumerate(items):
#         path = os.path.join(current_path, item)
#         is_last = (index == count - 1)
#         is_dir = os.path.isdir(path)
        
#         connector = "└── " if is_last else "├── "
#         out.write(f"{prefix}{connector}{item}{'/' if is_dir else ''}\n")

#         if is_dir:
#             # Check for symlink loop protection
#             if not follow and os.path.islink(path):
#                 continue
            
#             new_prefix = prefix + ("    " if is_last else "│   ")
#             _walk_recursive(path, new_prefix, follow, ignore, max_depth, out, current_depth + 1)



# def main() -> None:
#     # If arguments are passed, use the parser
#     # parser = build_parser()
#     # args = parser.parse_args()
     
#     # if args.init:
#     #     return init_database(args.init)
     
#     #      if args.path:
#     #          return use_database_file(args.path)
     
#     #      parser.print_help()
#     #      return 1
   
#     if len(sys.argv) > 1:
#        args = build_parser()
#     #    root_path = os.path.abspath(args.root_path)
#        root_path = os.getcwd()
#        output_file = args.output_file
#        #    ignore_list = args.ignore_list
#        ignore_list = {'.git', '__pycache__', '.venv', '.DS_Store'}
    
#     #    follow_symlinks = args.follow_symlinks
#     #    max_depth = args.max_depth
    
#        max_depth = 3
#        follow_symlinks = False
#     else:
#        # Default behavior for quick local runs
#        root_path = os.getcwd()
#        output_file = None
#        ignore_list = {'.git', '__pycache__', '.venv', '.DS_Store'}
#        follow_symlinks = False
#        max_depth = 2  # Shallow default for safety
#        print(f"--- Running in default mode (Depth: {max_depth}) ---\n")

#     if not os.path.exists(root_path):
#         print(f"Error: Path '{root_path}' does not exist.")
#         return
#     generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file)

def main1():
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
        ignore_list = {'.git', '__pycache__', '.venv', '.DS_Store'}
        follow_symlinks = False
        max_depth = 2  # Shallow default for safety
        print(f"--- Running in default mode (Depth: {max_depth}) ---\n")

    if not os.path.exists(root_path):
        print(f"Error: Path '{root_path}' does not exist.")
        return

    generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file)


def main():
    my_list = [-1, 2, -3, 5, -4, 6]
    output = [item for item in my_list if item < 0]  # [-4]
    print(output)
    
    # еквівалент циклу може виглядати так:
    output = []
    for item in my_list:
        if item < 0:
            output.append(item)
    print(output)


# List all files in a directory using scandir()
with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
            
# Виклик entry.is_file() для кожного елемента повертає True, якщо об’єкт є файлом. 

# Код можна зробити більш лаконічним, якщо об’єднати цикл for і оператор if в list comprehension:
for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
    print(file) # step 1
# Використання os.scandir(): 
for file in [item for item in os.scandir('.') if os.path.isfile(item)]:
    print(file.name)
