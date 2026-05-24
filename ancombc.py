import subprocess
import os


def run_ancombc():

    print("Running ANCOM-BC...\n")

    os.makedirs("results/ancombc", exist_ok=True)

    # Filter samples if needed

    subprocess.run("""
    qiime feature-table filter-samples \
    --i-table results/table.qza \
    --m-metadata-file metadata.tsv \
    --p-where "[group]='Diseased' OR [group]='Healthy'" \
    --o-filtered-table results/ancombc/filtered-table.qza
    """, shell=True, check=True)

    # Run ANCOM-BC

    subprocess.run("""
    qiime composition ancombc \
    --i-table results/ancombc/filtered-table.qza \
    --m-metadata-file metadata.tsv \
    --p-formula group \
    --o-differentials results/ancombc/ancombc.qza
    """, shell=True, check=True)

    # Generate ANCOM-BC barplot visualization

    subprocess.run("""
    qiime composition da-barplot \
    --i-data results/ancombc/ancombc.qza \
    --p-significance-threshold 0.001 \
    --o-visualization results/ancombc/ancombc-barplot.qzv
    """, shell=True, check=True)

    print("ANCOM-BC analysis completed.\n")
    print("Differential abundance analysis finished.\n")
