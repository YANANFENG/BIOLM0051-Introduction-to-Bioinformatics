Introduction to Bioinformatics Assignment# BIOLM0051-Introduction-to-Bioinformatics

This repository contains scripts and data used for analyzing DNA sequence data, specifically for the task of identifying species in a set of seized meat samples. The analysis includes processing raw FASTQ data, converting it to FASTA, translating sequences to amino acids, and conducting species identification using BLAST and phylogenetic tree construction using EBI tools.

file structure：
Sample_data/
   fasta_output/: Contains the output files after processing the raw sequences through the shell script.
   ref_seq/: Contains the reference species sequences obtained from BLAST results.
   samples/: Contains the raw sample data (original FASTQ files) used for the analysis.
   final_sequence.fasta: The final FASTA file used for generating the phylogenetic tree on the EBI network server.

process_sequences.sh: Shell script used to convert raw FASTQ files into FASTA format for further analysis.

translate_seq.py: Python script (using BioPython) for translating the DNA sequences into protein sequences to help in alignment.

README.md: This file, providing an overview of the project and usage instructions.

How to Use:
1. Clone the Repository
First, clone the repository from GitHub:

            git clone https://github.com/YANANFENG/BIOLM0051-Introduction-to-Bioinformatics.git

2. Data Preprocessing
The process_sequences.sh script will convert the raw FASTQ files into FASTA format. Run the script in the command line:

             bash process_sequences.sh
This script will convert the FASTQ files in the samples/ folder into FASTA files in the fasta_output/ folder.

3. BLAST Alignment
Align the translated FASTA files against the reference database to identify potential species. The reference species data can be found in the ref_seq/ folder.

4. Translating DNA Sequences
Use the translate_seq.py script to translate the DNA sequences into amino acid sequences for alignment. Run the Python script:

             python translate_sequence.py.ipynb
This script will read the data from fasta_output/ and red_seq/, generate the translated protein sequences.

5. Phylogenetic Tree Construction
Use EBI tools to perform multiple sequence alignment and generate the phylogenetic tree. The final FASTA file (final_sequence.fasta) will be located in the samples/ folder and used for constructing the tree on the EBI network server.

Results:
The fasta_output/ folder contains the converted FASTA files.
The ref_seq/ folder contains reference species data for comparison.
The final_sequence.fasta file is the input used for constructing the phylogenetic tree.
The tree will be generated on the EBI server and show the evolutionary relationships between the different samples.

Contribution:
This project was created and completed by Yanan Feng. If you have any questions or suggestions for improvements, feel free to contact me.
