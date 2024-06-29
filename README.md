# Synchronize_two_folders
Implementing a program that synchronizes two folders: source and replica. The  program will maintain a full, identical copy of source folder at replica folder.
To run the program it must be followed the structure:

Python folders_sync.py c:/your/source_file/location 30 c:/your/replica_file/location c:/your/log_file/location

This means that the arguments are 
1-the location of the source.
2-the time in seconds to run the infinite loop updating the replica_folder.
3-The replica_folder location.
4-The log file location.


Code Description for folders_sync.py:
This Python script contains a function synchronize_folders designed to synchronize the contents of two folders: a source folder and a replica folder. The synchronization process involves three main steps:

Copying Unique Items from Source to Replica: The function first identifies items (either files or directories) that are present in the source folder but not in the replica folder. These items are then copied over to the replica folder, maintaining the original structure. Each successful copy operation (whether it's a file or a directory) is logged, indicating the source and destination paths.

Removing Items Only in the Replica: Next, the function identifies items that are present in the replica folder but not in the source folder. These items are considered extraneous to the synchronization process and are removed from the replica folder. The removal of each item, whether it's a file or a directory, is logged with its path.

Updating Differing Files: The script outlines a process for updating files that exist in both folders but differ in content. However, the specific implementation details of this step are not provided in the excerpt.

The synchronization process is detailed, ensuring that the replica folder mirrors the contents of the source folder accurately, with logging for each significant action to aid in tracking the synchronization process.


Log File Structure Description
The log file associated with folders_sync.py appears to follow a structured format for logging events, based on the provided code excerpt. Each log entry likely contains the following information:

Timestamp: The date and time when the event occurred, providing a chronological context for the synchronization actions.
Event Type: This indicates whether the event was a file or directory copy, or a file or directory removal.
Source Path: For copy operations, the source path specifies the original location of the file or directory that was copied to the replica folder.
Destination Path: For copy operations, this indicates the path in the replica folder where the file or directory was copied to.
Removed Path: For removal operations, this specifies the path of the file or directory that was removed from the replica folder.
Each log entry is designed to provide a clear and concise record of the synchronization actions, making it easier to audit the process and troubleshoot any issues that may arise.
