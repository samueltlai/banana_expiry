"""
Scans a folder of banana photos named like:
    banana1_day0.jpg
    banana1_day1.jpg
    banana2_day0.jpg

...and generates a skeleton labels.csv with columns:
    filename, banana_id, day_index, expiry_day, days_until_expiry

expiry_day and days_until_expiry are left BLANK for you to fill in
once you know when each banana actually hit your expiry rule.

Usage:
    python3 generate_labels_csv.py
(edit PHOTO_DIR and OUTPUT_CSV below if needed)
"""

import os
import re
import csv

PHOTO_DIR = "banana_images"          # folder containing your images
OUTPUT_CSV = "labels.csv"     # where the skeleton CSV will be written

# Matches filenames like: banana1_day0.jpg, banana12_day7.JPG, etc.
PATTERN = re.compile(r"banana(\d+)_day(\d+)", re.IGNORECASE)

def main():
    if not os.path.isdir(PHOTO_DIR):
        print(f"Folder '{PHOTO_DIR}' not found. Edit PHOTO_DIR at the top of this script.")
        return

    rows = []
    skipped = []

    for fname in sorted(os.listdir(PHOTO_DIR)):
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        match = PATTERN.search(fname)
        if not match:
            skipped.append(fname)
            continue

        banana_id = int(match.group(1))
        day_index = int(match.group(2))

        rows.append({
            "filename": fname,
            "banana_id": banana_id,
            "day_index": day_index,
            "expiry_day": "",              # fill in once banana finishes its cycle
            "days_until_expiry": "",       # = expiry_day - day_index, fill in later
        })

    # Sort rows nicely: by banana_id, then day_index
    rows.sort(key=lambda r: (r["banana_id"], r["day_index"]))

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "banana_id", "day_index", "expiry_day", "days_until_expiry"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")

    if skipped:
        print(f"\nSkipped {len(skipped)} file(s) that didn't match the naming pattern 'bananaN_dayM':")
        for s in skipped:
            print(f"  - {s}")
        print("\nRename these to match e.g. banana3_day2.jpg, or edit the CSV manually to add them.")

if __name__ == "__main__":
    main()