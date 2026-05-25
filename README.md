This project is a simple automated microbiome analysis pipeline developed using Python and QIIME2. The pipeline performs major 16S rRNA analysis steps including sequence import, DADA2 denoising, feature table generation, phylogenetic tree construction, diversity analysis, taxonomy classification, taxa visualization, and ANCOM-BC.

The workflow is divided into separate Python scripts for better organization. The main script, run_pipeline.py, executes the complete pipeline automatically. Other scripts handle specific tasks such as data import, denoising, summarization, phylogeny generation, diversity analysis, taxonomy assignment, and ANCOM-BC export preparation.

Paired-end FASTQ files should be stored in a folder such as data/. A manifest.tsv file is required for importing sequencing data into QIIME2. This file contains sample IDs along with absolute paths to forward and reverse FASTQ files. A metadata.tsv file is also required for diversity and taxa analysis and should contain sample information such as disease and healthy groups.

The pipeline uses a pre-trained SILVA classifier file (silva-138.qza) for which download SILVA reference sequence and taxonomy files from the official QIIME2 resources page:
Download:
SILVA reference sequences
SILVA reference taxonomy 
Then train the classifier using the command mentioned below:

qiime feature-classifier fit-classifier-naive-bayes \
--i-reference-reads reference-sequences.qza \
--i-reference-taxonomy reference-taxonomy.qza \
--o-classifier silva-138-classifier.qza

The generated classifier file is used in the taxonomy analysis step of the pipeline. This classifier should be placed in the main project directory before running the workflow.

The pipeline is designed for Linux, Ubuntu, or WSL environments with Python 3 and QIIME2 already installed.
The complete workflow can be executed using:

python run_pipeline.py

All generated outputs are stored inside the results/ folder, including feature tables, taxonomy assignments, phylogenetic trees, and visualization files (.qzv).
