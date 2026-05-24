import subprocess
import os


def import_data():

    os.makedirs("results", exist_ok=True)

    print("Importing sequences...\n")

    # Import paired-end FASTQ files

    subprocess.run("""
    qiime tools import \
    --type 'SampleData[PairedEndSequencesWithQuality]' \
    --input-path bc_manifest.tsv \
    --output-path results/demux.qza \
    --input-format PairedEndFastqManifestPhred33V2
    """, shell=True, check=True)

    # Generate demultiplexed sequence summary

    subprocess.run("""
    qiime demux summarize \
    --i-data results/demux.qza \
    --o-visualization results/demux.qzv
    """, shell=True, check=True)

    print("Import completed.\n")
