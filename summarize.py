import subprocess


def summarize_data():

    print("Generating summaries...\n")

    subprocess.run("""
    qiime feature-table summarize \
    --i-table results/table.qza \
    --o-visualization results/table.qzv
    """, shell=True)

    subprocess.run("""
    qiime feature-table tabulate-seqs \
    --i-data results/rep-seqs.qza \
    --o-visualization results/rep-seqs.qzv
    """, shell=True)
