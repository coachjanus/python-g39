import argparse

APP_NAME = "tree-gen"

def build_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description="Generate a visual directory tree with depth control",
        epilog="Thanks for using %(prog)s! :)",
    )

    group = parser.add_argument_group('Configurations', 'Tree generation settings')

    group.add_argument(
        'root_path', 
        type=str,
        nargs='?',
        default=".",
        help="Root directory path (default: current directory)"
    )
    group.add_argument(
        '-d', '--max_depth',
        type=int,
        default=None,
        help="Maximum depth of the directory tree to display"
    )
    group.add_argument(
        '-o', '--output_file', 
        type=str, 
        help="Output to a specific file instead of console"
    )
    group.add_argument(
        '-i', '--ignore_list', 
        nargs='*', 
        default=[],
        help="List of names (files or folders) to ignore"
    )
    group.add_argument(
        '-l', '--follow_symlinks', 
        action='store_true',
        help="Follow symbolic links"
    )

    return parser.parse_args()