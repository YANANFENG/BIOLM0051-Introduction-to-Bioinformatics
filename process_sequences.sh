#!/bin/bash

INPUT_DIR="$HOME/Assessment_Project/raw_data"
OUTPUT_DIR="$HOME/Assessment_Project/fasta_output"

echo "Starting processing pipeline..."
echo "Reading data from: $INPUT_DIR"

if [ -f "${INPUT_DIR}/sampleB_part2.fastq" ]; then
    echo "Detected sampleB_part2.fastq, applying fix (removing first line)..."
    sed '1d' "${INPUT_DIR}/sampleB_part2.fastq" > "${INPUT_DIR}/sampleB_part2_fixed.fastq"
    mv "${INPUT_DIR}/sampleB_part2.fastq" "${INPUT_DIR}/sampleB_part2.fastq.bak"
    mv "${INPUT_DIR}/sampleB_part2_fixed.fastq" "${INPUT_DIR}/sampleB_part2.fastq"
    echo "Fix applied: sampleB_part2.fastq has been sanitized."
fi

for file in ${INPUT_DIR}/*_part1.FASTQ
do
    filename=$(basename "$file")
    sample_id=${filename%_part1.FASTQ}
 
    echo "Processing sample: $sample_id"

    cat "${INPUT_DIR}/${sample_id}_part"*.FASTQ | \
    sed -n '1~4s/^@/>/p;2~4p' > "${OUTPUT_DIR}/${sample_id}.fasta"

    echo "Finished $sample_id -> Saved to ${OUTPUT_DIR}/${sample_id}.fasta"

done

echo "All tasks completed successfully!"
