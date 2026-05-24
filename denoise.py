import subprocess


def run_dada2():

    print("Running DADA2...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime dada2 denoise-paired \
    --i-demultiplexed-seqs results/demux.qza \
    --p-trunc-len-f 240 \
    --p-trunc-len-r 220 \
    --o-table results/table.qza \
    --o-representative-sequences results/rep-seqs.qza \
    --o-denoising-stats results/stats.qza
    """, shell=True)
