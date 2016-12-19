# regtools
A Galaxy Wrapper for regtools

This is a modified Galaxy wrapper for regtools which is based on the previous wrapper written by Remi Marenco (https://github.com/remimarenco/regtools). "regtools is a set of tools that integrate DNA-seq and RNA-seq data to help interpret mutations in a regulatory and splicing context" (https://regtools.readthedocs.io/en/latest/).

This wrapper add an validation step to check if the output files are valid BED format. The lines with invalid strand (neighter "+" or "-") will be removed. The scores higher than 1000 will be changed to 1000. All modified lines will be reported to the standard output.
