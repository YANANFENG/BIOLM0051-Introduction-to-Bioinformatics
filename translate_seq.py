import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Configuration
TARGET_FOLDER = "Sample_data"
OUTPUT_FILE = "final_sequence.fasta"
TRANSLATION_TABLE = 2 

def main():
    final_records = []
    
    # Set up directory paths
    base_dir = os.getcwd()
    work_dir = os.path.join(base_dir, TARGET_FOLDER)
    
    print(f"Scanning directory: {work_dir}")
    
    if not os.path.exists(work_dir):
        print(f"Error: Directory {TARGET_FOLDER} not found.")
        return

    # Get all FASTA and TXT files
    all_files = [f for f in os.listdir(work_dir) if f.endswith(('.fasta', '.fa', '.txt'))]
    print(f"Found {len(all_files)} files.")

    sample_count = 0
    ref_count = 0

    for filename in all_files:
        # Skip output files and temporary files
        if filename == OUTPUT_FILE or "alignment" in filename or "_prot" in filename: 
            continue
        if "best" in filename or "clean" in filename: 
            continue 

        file_path = os.path.join(work_dir, filename)
        
        try:
            records = list(SeqIO.parse(file_path, "fasta"))
            if not records: 
                continue

            # Check if file is a sample or reference
            is_sample = filename.lower().startswith("sample")
            
            if is_sample:
                # Process Unknown Samples: Select the longest sequence
                best_record = None
                max_len = 0
                
                for record in records:
                    try:
                        aa_seq = record.seq.translate(table=TRANSLATION_TABLE)
                        if len(aa_seq) > max_len:
                            max_len = len(aa_seq)
                            best_record = record
                            best_aa = aa_seq
                    except: 
                        pass
                
                if best_record and max_len > 50:
                    final_id = f"{filename.split('.')[0]}_Unknown"
                    new_record = SeqRecord(
                        best_aa,
                        id=final_id,
                        description=f"[Sample] {best_record.description}"
                    )
                    final_records.append(new_record)
                    sample_count += 1
                    print(f"Processed sample: {filename} (Length: {max_len})")
            
            else:
                
                for record in records:
                    try:
                        aa_seq = record.seq.translate(table=TRANSLATION_TABLE)
                        if len(aa_seq) > 50:
                            
                            clean_id = record.id.split()[0][:15]
                            final_id = f"{clean_id}_Ref"
                            
                            new_record = SeqRecord(
                                aa_seq,
                                id=final_id,
                                description=f"[Ref] {record.description}"
                            )
                            final_records.append(new_record)
                            ref_count += 1
                    except: 
                        pass
                print(f"Added reference file: {filename}")

        except Exception as e:
            print(f"Error reading {filename}: {e}")

    # Write output to file
    if final_records:
        output_path = os.path.join(work_dir, OUTPUT_FILE)
        SeqIO.write(final_records, output_path, "fasta")
        print("-" * 30)
        print(f"Success! Output saved to: {output_path}")
        print(f"Stats:")
        print(f"  Samples: {sample_count}")
        print(f"  References: {ref_count}")
        print(f"  Total Sequences: {len(final_records)}")
    else:
        print("Error: No valid sequences generated.")

if __name__ == "__main__":
    main()
