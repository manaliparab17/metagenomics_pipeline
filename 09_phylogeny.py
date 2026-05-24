import subprocess


def generate_tree():

    print("Generating phylogenetic tree...\n")

    subprocess.run("""
    qiime phylogeny align-to-tree-mafft-fasttree \
    --i-sequences results/rep-seqs.qza \
    --o-alignment results/aligned-rep-seqs.qza \
    --o-masked-alignment results/masked-aligned-rep-seqs.qza \
    --o-tree results/unrooted-tree.qza \
    --o-rooted-tree results/rooted-tree.qza
    """, shell=True)
