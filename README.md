# Read Preprocessing Pipeline

This pipeline is designed to process Next-Generation Sequencing (NGS) reads by combining Fastp, FastQC, and MultiQC into a Python script. The goal is to streamline quality control, trimming, and filtering, and to generate comprehensive reports.

## How to Run the Pipeline

### Prerequisites

Make sure you have Conda installed and configured on your system.
- Conda installed ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda)

### Step 1: Create and activate the conda environment
```bash
conda create -n preprocess -c bioconda fastp fastqc multiqc
conda activate preprocess
```
### Step 2: Step 2: Prepare Your Files

Place your raw read files (e.g., reads1.fastq and reads2.fastq) in the same directory as the pre-process.py script.

### Step 3: Step 3: Execute the Pipeline

Run the Python script from your terminal, providing the paths to your input files and an output directory.

    python3 pre-process.py -r1 reads1.fastq -r2 reads2.fastq -o output_dir


Command-Line Parameters:

    -r1, --read1: Path to the forward reads file (R1).

    -r2, --read2: Path to the reverse reads file (R2).

    -o, --output: The directory where all output files and reports will be saved.

    -t, --threads (optional): The number of threads to use (default: 16).
    
### Generated Output

The pipeline will create an output directory containing the following files:

Trimmed and Filtered Reads:

        prefix_trimmed_R1.fq.gz

        prefix_trimmed_R2.fq.gz

Quality Reports (fastp and FastQC):

        prefix_fastp_trim_report.html (Detailed fastp report)

        prefix_R1_fastqc.html (FastQC report for trimmed R1 reads)

        prefix_R2_fastqc.html (FastQC report for trimmed R2 reads)

Consolidated Report (MultiQC):

        multiqc_report.html (A single HTML report that summarizes the results from both fastp and FastQC)

You can open the multiqc_report.html file in your web browser for a comprehensive and visual analysis of your data's quality.
