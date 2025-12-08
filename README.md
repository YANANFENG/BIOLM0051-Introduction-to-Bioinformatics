Introduction to Bioinformatics Assignment# BIOLM0051-Introduction-to-Bioinformatics

This repository contains scripts and data used for analyzing DNA sequence data, specifically for the task of identifying species in a set of seized meat samples. The analysis includes processing raw FASTQ data, converting it to FASTA, translating sequences to amino acids, and conducting species identification using BLAST and phylogenetic tree construction using EBI tools.

Directory Structure
The project is organized as follows:

.
├── process_sequences.sh      # Shell script for data preprocessing (FASTQ -> FASTA)
├── translate_seq.py          # Python script using BioPython for translation & filtering
├── README.md                 # Project documentation
└── sample_data/
    ├── samples/              # Raw Input: Original segmented FASTQ files (Samples A-D)
    ├── fasta_output/         # Intermediate: Cleaned and merged FASTA sequences
    ├── ref_seq/              # References: Reference sequences identified via BLAST
    └── final_sequence/       # Final Output: Protein dataset used for Phylogenetic Tree construction


    
How to Use:
1. Clone the Repository
   First, clone the repository from GitHub:

            git clone https://github.com/YANANFENG/BIOLM0051-Introduction-to-Bioinformatics.git
            cd BIOLM0051-Introduction-to-Bioinformatics
   
3. Data Preprocessing
   Convert raw FASTQ files to FASTA format using the provided shell script.

   Note: Ensure your raw data(samples/) is in the raw_data/ directory (or update the path in the script).

             chmod +x process_sequences.sh
             ./process_sequences.sh
   
This script will convert the FASTQ files in the samples/ folder into FASTA files in the fasta_output/ folder.

3. BLAST Alignment
   Perform BLASTn search (manually via NCBI website or CLI) using the files in fasta_output/ to identify species and download reference sequences into ref_seq/.

4. Translating DNA Sequences
   Use the translate_seq.py script to translate the DNA sequences into amino acid sequences for alignment. Run the Python script:

             python translate_seq.py
Note: This script requires Biopython installed. It reads from fasta_output/ and ref_seq/ and outputs protein sequences.

5. Phylogenetic Tree Construction
   The file final_sequence.fasta contains the combined protein sequences. Upload this file to EBI Clustal Omega or MAFFT to generate the Multiple Sequence Alignment (MSA) and Phylogenetic Tree.

Results:

The fasta_output/ folder contains the converted FASTA files.

The ref_seq/ folder contains reference species data for comparison.

The final_sequence.fasta file is the input used for constructing the phylogenetic tree.

The tree will be generated on the EBI server and show the evolutionary relationships between the different samples.

Species Identified: Eubalaena japonica，Delphinapterus leucas，Thunnus thynnus，Dermochelys coriacea.

Conclusion: The shipment contains illegal wildlife products protected under CITES.

Dependencies:

Shell/Bash (for data cleaning)

Python 3.x

BioPython (for sequence translation) 

Clustal Omega (Web server or command line tool)


Author:

Yanan Feng
If you have any questions, feel free to contact me.
