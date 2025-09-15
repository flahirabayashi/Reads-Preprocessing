import os
import subprocess
import argparse

def run_fastp(r1, r2, out_dir, threads=16):
    print(f"Running FastP for {r1} e {r2}...")

    prefix = os.path.basename(r1).replace("_R1_001.fastq", "").replace("_R1.fq.gz", "").replace("_R1.fastq", "")
    
    r1_out = os.path.join(out_dir, f"{prefix}_trimmed_R1.fq.gz")
    r2_out = os.path.join(out_dir, f"{prefix}_trimmed_R2.fq.gz")
    html_out = os.path.join(out_dir, f"{prefix}_fastp_trim_report.html")
    json_out = os.path.join(out_dir, f"{prefix}_fastp_trim_report.json")

    cmd = [
        "fastp",
        "-i", r1,
        "-I", r2,
        "-o", r1_out,
        "-O", r2_out,
        "--detect_adapter_for_pe",
        "--correction",
        "--qualified_quality_phred", "20",
        "--low_complexity_filter",
        "-h", html_out,
        "-j", json_out,
        "-w", str(threads)
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    print(f"Done Trimming! Outs: {r1_out} e {r2_out}")
    return r1_out, r2_out


def run_fastqc(r1_trimmed, r2_trimmed, out_dir, threads=4):
    print("Running FastQC...")
    cmd = [
        "fastqc",
        r1_trimmed,
        r2_trimmed,
        "-o", out_dir,
        "-t", str(threads)
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    print("FastQC Analysis Done!")


def run_multiqc(out_dir):
    print("Running MultiQC...")
    cmd = [
        "multiqc",
        out_dir,
        "-o", out_dir
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    print(f"MultiQC Report on: {os.path.join(out_dir, 'multiqc_report.html')}")


def main():
    parser = argparse.ArgumentParser(description="Read PreProcessing Pipeline")
    parser.add_argument("-r1", "--read1", required=True, help="Forward Reads (R1)")
    parser.add_argument("-r2", "--read2", required=True, help="Reverse Reads (R2)")
    parser.add_argument("-o", "--output", required=True, help="Output Directory")
    parser.add_argument("-t", "--threads", default=16, type=int, help="Thread Number (default: 16)")
    
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    r1_trimmed, r2_trimmed = run_fastp(args.read1, args.read2, args.output, args.threads)
    run_fastqc(r1_trimmed, r2_trimmed, args.output, args.threads)
    run_multiqc(args.output)

    print("Pipeline Finished!")
    print(f"Output on: {args.output}")


if __name__ == "__main__":
    main()
