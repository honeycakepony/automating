# created 14-01-2024
# author: honeycakepony
""" IDEA: automatically compare digests, append digest to .txt-file"""

import subprocess
import os
from pathlib import Path

DOWNLOADS = os.path.join(Path.home(), 'Downloads')
DESKTOP = os.path.join(Path.home(), 'Desktop')
DEFAULTS = ['.DS_Store', '.localized']

if __name__ == '__main__':
    for file in os.listdir(DOWNLOADS):
        if file in DEFAULTS:
            continue

        if file in os.listdir(DESKTOP):
            hashing_command = f'shasum -a 256 {file}'
            os.chdir(DESKTOP)
            hash_desktop = subprocess.run(hashing_command, shell=True, capture_output=True, text=True)

            os.chdir(DOWNLOADS)
            hash_downloads = subprocess.run(hashing_command, shell=True, capture_output=True, text=True)

            if hash_desktop.stdout == hash_downloads.stdout:
                digest = hash_desktop.stdout.split()[0]
                print(f'File {file} was successfully uploaded.')
                with open(os.path.join(DESKTOP, 'hash-sums.txt'), 'a') as f:
                    f.write(f'file \"{file}\"\n'
                            f'digest: {digest}\n\n')
            else:
                print(f'Error: File {file} was corrupted.')
