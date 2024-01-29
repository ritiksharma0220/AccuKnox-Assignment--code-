import shutil
import os
import datetime

# backup source and destination
SOURCE_DIR = "/path_to/source"
DESTINATION_DIR = "/path_to/destination"

# backup filename
backup_file = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"

try:
    # create backup
    shutil.make_archive(os.path.join(DESTINATION_DIR, backup_file), 'gztar', SOURCE_DIR)
    print(f"Backup successful: {backup_file}")
except Exception as e:
    print("Backup failed:", str(e))
