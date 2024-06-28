import argparse
import logging
import os
import shutil
import time
from filecmp import dircmp

# Setup logging configuration
def configure_logging(log_destination):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_destination),
                            logging.StreamHandler()
                        ])

# Synchronize directories
def synchronize_folders(source_folder, replica_folder):
    def sync_process(folder_comparison):
        # Copy unique items from source to replica
        for item in folder_comparison.left_only:
            source_path = os.path.join(folder_comparison.left, item)
            replica_path = os.path.join(folder_comparison.right, item)
            if os.path.isdir(source_path):
                shutil.copytree(source_path, replica_path)
                logging.info(f"Directory copied: {source_path} to {replica_path}")
            else:
                shutil.copy2(source_path, replica_path)
                logging.info(f"File copied: {source_path} to {replica_path}")
        # Remove items that are only in the replica
        for item in folder_comparison.right_only:
            replica_path = os.path.join(folder_comparison.right, item)
            if os.path.isdir(replica_path):
                shutil.rmtree(replica_path)
                logging.info(f"Directory removed: {replica_path}")
            else:
                os.remove(replica_path)
                logging.info(f"File removed: {replica_path}")
        # Update differing files
        for item in folder_comparison.diff_files:
            source_path = os.path.join(folder_comparison.left, item)
            replica_path = os.path.join(folder_comparison.right, item)
            shutil.copy2(source_path, replica_path)
            logging.info(f"File updated: {source_path} to {replica_path}")
        # Recursively handle subdirectories
        for sub_comparison in folder_comparison.subdirs.values():
            sync_process(sub_comparison)

    comparison = dircmp(source_folder, replica_folder)
    sync_process(comparison)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("sync_interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()

    configure_logging(args.log_file)

    # Periodic synchronization loop
    while True:
        logging.info("Starting synchronization")
        synchronize_folders(args.source_folder, args.replica_folder)
        logging.info("Synchronization completed")
        time.sleep(args.sync_interval)

if __name__ == "__main__":
    main()