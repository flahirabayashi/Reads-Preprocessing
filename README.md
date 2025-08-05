# Read Trimming and Filtering with fastp

A fast, efficient, and user-friendly tool for NGS read preprocessing, combining QC, trimming, and filtering in few steps.

## How to Run fastp in a Conda Environment

This guide explains how to run fastp using a shell script (`run_fastp.sh`).

### Prerequisites
- Conda installed ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda)
- fastp installed in a Conda environment

### Step 1: Create and activate the conda environment
```bash
conda create -n fastp -c bioconda fastp
conda activate fastp
```
### Step 2: Prepare the (`run_fastp.sh`) script and adapt it
### Step 3: Make the script executable and run it

    chmod +x run_fastp.sh
    ./run_fastp.sh
    
### Expected output: merged and umerged files, report.json and report.html
