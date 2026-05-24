from import_data import import_data
from denoise import run_dada2
from summarize import summarize_data
from phylogeny import generate_tree
from diversity import diversity_analysis
from taxonomy import taxonomy_analysis
from ancombc import run_ancombc


def main():

    print("\nStarting Microbiome Pipeline...\n")

    # Step 1: Import FASTQ files
    import_data()

    # Step 2: DADA2 denoising
    run_dada2()

    # Step 3: Generate summaries
    summarize_data()

    # Step 4: Generate phylogenetic tree
    generate_tree()

    # Step 5: Diversity analysis
    diversity_analysis()

    # Step 6: Taxonomy classification
    taxonomy_analysis()

    # Step 7: Export files for ANCOM-BC
    run_ancombc()

    print("\nPipeline Finished Successfully.\n")


if __name__ == "__main__":
    main()
