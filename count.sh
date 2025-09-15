#!/bin/bash
dirs=("000-050" "051-100" "101-150" "151-200")
count=0
for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        num_files=$(find "$dir" -type f | wc -l)
        count=$((count + num_files))
        echo "Directory $dir has $num_files files."
    else
        echo "Directory $dir does not exist."
    fi
done

echo "$count"