import subprocess
import os


def run_ancombc():

    print("Preparing files for ANCOM-BC...\n")

    os.makedirs("results/ancombc", exist_ok=True)

    subprocess.run("""
    qiime tools export \
    --input-path results/table.qza \
    --output-path results/ancombc
    """, shell=True)

    print("Run ANCOM-BC separately in R.\n")
