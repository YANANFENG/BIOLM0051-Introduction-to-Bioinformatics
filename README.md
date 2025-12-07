Introduction to Bioinformatics Assignment# BIOLM0051-Introduction-to-Bioinformatics

This repository contains scripts and data used for analyzing DNA sequence data, specifically for the task of identifying species in a set of seized meat samples. The analysis includes processing raw FASTQ data, converting it to FASTA, translating sequences to amino acids, and conducting species identification using BLAST and phylogenetic tree construction using EBI tools.

file structure：
Sample_data/
   fasta_output/: Contains the output files after processing the raw sequences through the shell script.
   ref_seq/: Contains the reference species sequences obtained from BLAST results.
   samples/: Contains the raw sample data (original FASTQ files) used for the analysis.
   final_sequence.fasta: The final FASTA file used for generating the phylogenetic tree on the EBI network server.

process_sequences.sh: Shell script used to convert raw FASTQ files into FASTA format for further analysis.

translate_sequence.py.ipynb: Python script (using BioPython) for translating the DNA sequences into protein sequences to help in alignment.

README.md: This file, providing an overview of the project and usage instructions.

How to Use

1. Clone the Repository
First, clone the repository from GitHub:

            git clone https://github.com/YANANFENG/BIOLM0051-Introduction-to-Bioinformatics.git

3. Data Preprocessing

The process_sequences.sh script will convert the raw FASTQ files into FASTA format. Run the script in the command line:
            bash process_sequences.sh
