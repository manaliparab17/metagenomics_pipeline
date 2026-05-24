import subprocess


def diversity_analysis():

    print("Running diversity analysis...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime diversity core-metrics-phylogenetic \
    --i-phylogeny results/rooted-tree.qza \
    --i-table results/table.qza \
    --p-sampling-depth 10000 \
    --m-metadata-file metadata.tsv \
    --output-dir results/diversity
    """, shell=True)

    subprocess.run("""
    qiime diversity alpha-rarefaction \
    --i-table results/table.qza \
    --i-phylogeny results/rooted-tree.qza \
    --p-max-depth 10000 \
    --m-metadata-file metadata.tsv \
    --o-visualization results/alpha-rarefaction.qzv
    """, shell=True)
