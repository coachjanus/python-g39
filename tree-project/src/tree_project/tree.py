"""
generate visual directory tree starting from specified root path.
Supports output to file or stdout, with options for ignoring certain files/directories
and following symbolic links. Designed for cross-platform compatibility.
"""
    
import os
import sys

# def generate_tree(root_path, follow_symlinks, ignore_list, output_file=None):
#     """
#     Generate directory tree and output it to specified file or stdout.
#     Handles symbolic links and ignores specified files/directories.
#     """
    
#     output = open_output_file(output_file)

#     try:
#         walk_directory(root_path, follow_symlinks, ignore_list, output)
#     finally:
#         if output_file:
#             output.close()

def generate_tree(root_path, follow_symlinks, ignore_list, max_depth, output_file=None):
    if output_file:
        out = open(output_file, 'w', encoding='utf-8')
    else:
        if sys.stdout.encoding.lower() != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')
        out = sys.stdout

    try:
        out.write(f"{os.path.abspath(root_path)}/\n")
        _walk_recursive(root_path, "", follow_symlinks, set(ignore_list), max_depth, out, current_depth=0)
    finally:
        if output_file:
            out.close()

def _walk_recursive(current_path, prefix, follow, ignore, max_depth, out, current_depth):
    # Stop if we've reached the user-defined limit
    if max_depth is not None and current_depth >= max_depth:
        return
    # Get the contents of the current working directory, handling permission errors gracefully
    try:
        items = [i for i in os.listdir(current_path) if i not in ignore]
    except PermissionError:
        out.write(f"{prefix}└── [Permission Denied]\n")
        return

    items.sort()
    count = len(items)

    for index, item in enumerate(items):
        path = os.path.join(current_path, item)
        is_last = (index == count - 1)
        is_dir = os.path.isdir(path)
        
        connector = "└── " if is_last else "├── "
        out.write(f"{prefix}{connector}{item}{'/' if is_dir else ''}\n")

        if is_dir:
            # Check for symlink loop protection
            if not follow and os.path.islink(path):
                continue
            
            new_prefix = prefix + ("    " if is_last else "│   ")
            _walk_recursive(path, new_prefix, follow, ignore, max_depth, out, current_depth + 1)


def open_output_file(output_file=None):
    """
    Open output file in write mode or configure stdout for writing.

    Returns:
        file object: File object or sys.stdout configured for writing.
    """
    if output_file:
        return open(output_file, 'w', encoding='utf-8')
    else:
        sys.stdout.reconfigure(encoding='utf-8')
        return sys.stdout

def walk_directory(root_path, follow_symlinks, ignore_list, output):
    """
    Walk through directory tree and process each directory and file.

    Args:
        root_path (str): Root directory path.
        follow_symlinks (bool): Whether to follow symbolic links.
        ignore_list (list): List of file/directory names to ignore.
        output (file object): Output file or stdout to write tree to.
    """
    for root, dirs, files in os.walk(root_path, topdown=True, followlinks=follow_symlinks):
        dirs.sort()  # Ensure consistent order
        process_directory(root_path, ignore_list, root, dirs, files, output)

def process_directory(root_path, ignore_list, root, dirs, files, output):
    """
    Process each directory, writing its structure to output.

    Args:
        root_path (str): Root directory path.
        ignore_list (list): List of file/directory names to ignore.
        root (str): Current directory path.
        dirs (list): List of subdirectories in current directory.
        files (list): List of files in current directory.
        output (file object): Output file or stdout to write to.
    """
    # Calculate depth level of current directory relative to root
    level = root.replace(root_path, '').count(os.sep)
    # Create indentation based on directory level
    indent = '|   ' * (level - 1) if level > 0 else ''
    if level > 0:
        parent_path, _ = os.path.split(root)
        parent_dirs = next(os.walk(parent_path))[1]
        # Choose appropriate branch symbol based on position in parent
        if root == os.path.join(parent_path, parent_dirs[-1]):
            indent += '└── '
        else:
            indent += '├── '
    output.write(f"{indent}{os.path.basename(root)}/\n")
    if os.path.basename(root) in ignore_list:
        output.write(f"{indent}|   ...\n")
        dirs[:] = []  # Clear dirs list to prevent walking into them
        return  # Skip processing children
    process_files(ignore_list, files, level, output)
    # Only add vertical bar if there are subdirectories or files
    if dirs:
        subindent = '|   ' * level + '|'
        output.write(f"{subindent}\n")

def process_files(ignore_list, files, level, output):
    """
    Process each file in current directory, writing to output.

    Args:
        ignore_list (list): List of file/directory names to ignore.
        files (list): List of files in current directory.
        level (int): Depth level of current directory.
        output (file object): Output file or stdout to write to.
    """
    subindent = '|   ' * level
    for f in files:
        if f not in ignore_list:
            output.write(f"{subindent}|   {f}\n")
    # Do not add extra vertical bar after last file
    if not files and not dir:
        subindent = '|   ' * level
        output.write(f"{subindent}\n")