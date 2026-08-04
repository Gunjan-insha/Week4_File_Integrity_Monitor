import os
import hashlib


# SHA-256 hash generate karne ke liye
def get_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Folder scan karne ke liye
def scan_folder(folder_path):
    hashes = {}

    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        if os.path.isfile(full_path):
            hashes[file_name] = get_hash(full_path)

    return hashes


# User se folder path lena
folder = input("Enter Folder Path: ")

print("\nScanning folder...")
old_hashes = scan_folder(folder)

input("\nFolder scanned successfully.\n"
      "Make any changes (add, delete or modify files) and then press ENTER.")

print("\nScanning again...")
new_hashes = scan_folder(folder)


# Compare results
print("\n----- RESULTS -----")

# Added files
for file in new_hashes:
    if file not in old_hashes:
        print(f"New File Added : {file}")

# Modified files
for file in new_hashes:
    if file in old_hashes:
        if new_hashes[file] != old_hashes[file]:
            print(f"File Modified : {file}")

# Deleted files
for file in old_hashes:
    if file not in new_hashes:
        print(f"File Deleted : {file}")

print("\nMonitoring Completed.")