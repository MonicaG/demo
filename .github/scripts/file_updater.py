import logging
import sys
import os
import yaml

def update_file(file_path):
   with open(file_path, 'a') as file:
      file.write("Appended content\n")

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  if len(sys.argv) < 1:
    logging.error("Usage: python file_updater.py file_path")
    sys.exit(1)
  target_file= sys.argv[1]
  if not os.path.isfile(target_file):
    logging.error(f"{target_file} is not a valid file")
  else:
    logging.info(f"Updating {target_file}")
    update_file(target_file)
    logging.info("Done")
