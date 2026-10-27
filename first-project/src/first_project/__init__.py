import argparse
import sys
from pathlib import Path
# def main() -> None:
#     print("The value of __name__ is:", repr(__name__))
#     print("This is module __init__ insude package first-project. Hello from first-project!")
APP_NAME = "contact-manager"

def init_database(db_dir: Path) -> int:
    """Initialize database directory."""
    try:
        db_dir = db_dir.expanduser().resolve()
        db_dir.mkdir(parents=True, exist_ok=True)

        print(f"✅ Database initialized at: {db_dir}")
        return db_dir

    except Exception as e:
        print(f"❌ Failed to initialize database: {e}", file=sys.stderr)
        return 


def use_database_file(target: Path) -> int|Path:
    """Validate or create database file."""

    try:
        target = target.expanduser().resolve()
        target_dir = target.parent

        print(f"Target file: {target}")
        print(f"Target directory: {target_dir}")

        if not target_dir.exists():
            print(f"❌ Directory does not exist: {target_dir}", file=sys.stderr)
            return 1

        if not target_dir.is_dir():
            print(f"❌ Not a directory: {target_dir}", file=sys.stderr)
            return 1

        if not target.exists():
            print(f"❌ File does not exist, creating: {target}")
            target.touch()

        print(f"✅ Using database file: {target}")
        return target

    except Exception as e:
        print(f"❌ Error handling database file: {e}", file=sys.stderr)
        return 1
# ---------- CLI ----------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description="Contact Manager CLI tool",
        epilog="Thanks for using %(prog)s! :)",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-i", 
        "--init",
        type=Path,
        metavar="DIR",
        help="Initialize database directory",
    )

    group.add_argument(
        "-p",
        "--path",
        type=Path,
        metavar="FILE",
        help="Use database file",
    )

    return parser


def main() -> int|Path:
    parser = build_parser()
    args = parser.parse_args()

    if args.init:
        return init_database(args.init)

    if args.path:
        return use_database_file(args.path)

    parser.print_help()
    return 1
