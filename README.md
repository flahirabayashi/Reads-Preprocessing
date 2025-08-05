# Read-Trimming-and-Filtering
A fast, efficient, and user-friendly tool for NGS read preprocessing, combining QC, trimming, and filtering in few steps.

How to Run fastp in a Conda Environment using a shell script (run_fastp.sh)

Prerequisites
    Conda installed (Miniconda or Anaconda).
    fastp installed in a Conda environment.

Step 1: Create and Activate the Conda Environment (if needed).

    conda create -n fastp -c bioconda fastp
    
Step 2: Prepare the run_fastp.sh Script
Step 3: Make the Script Executable and Run It

    chmod +x run_fastp.sh
    ./run_fastp.sh
    
Expected Output: merged and umerged files, report.json and report.html  
