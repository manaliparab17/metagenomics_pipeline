import subprocess


def taxonomy_analysis():

    print("Running taxonomy classification...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime feature-classifier classify-sklearn \
    --i-classifier silva-138.qza \
    --i-reads results/rep-seqs.qza \
    --o-classification results/taxonomy.qza
    """, shell=True)

    subprocess.run("""
    qiime metadata tabulate \
    --m-input-file results/taxonomy.qza \
    --o-visualization results/taxonomy.qzv
    """, shell=True)

    subprocess.run("""
    qiime taxa barplot \
    --i-table results/table.qza \
    --i-taxonomy results/taxonomy.qza \
    --m-metadata-file metadata.tsv \
    --o-visualization results/taxa-barplot.qzv
    """, shell=True)
