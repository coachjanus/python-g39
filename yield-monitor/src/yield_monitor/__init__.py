import sys
from .monitor import watch_directory

def main():
    path_to_watch = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"yield-project directory monitor")
    print(f"Monitoring: {path_to_watch}")
    print("Press Ctrl+C to stop.")
    
    try:
        for event in watch_directory(path_to_watch):
            print(f"[{event['event'].upper()}] {event['path']}")
    except KeyboardInterrupt:
        print("\nMonitor stopped.")

if __name__ == "__main__":
    main()