import sys

"""
Call checkAndFixBed, check the integrity of bed file. If the strand is not "+" or "-" truncate that line and report to users
create a column and move the score column to that column.
"""
def checkAndFixBed(bedfile, revised_file):
# Store the lines that have been removed
    removedLines = []
    scoreLines = []
# Remove the lines with invalid strand, create a score column to store the original scores and change scores in the original score column all to 1000
    with open(revised_file, 'w') as tmp:
        with open(bedfile, 'r') as f:
            lines = f.readlines()
            i = 1
            for line in lines:  
                fields = line.split()
                strand = fields[5]
                score = fields[4]
                if (int(fields[4]) > 1000):
                    scoreLines.append("line" + str(i) + ":" + line) 
                    fields[4] = '1000' 
                if (strand == '+' or strand == '-'):
                    tmp.write('\t'.join(map(str, fields)))
                    tmp.write("\n")
                else:
                    removedLines.append("line" + str(i) + ": " + line)
                i = i+1

    return removedLines, scoreLines 

def main():
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
    removed, changed = checkAndFixBed(inputfile, outputfile)
    if (removed != []):
        print "\nRemoved invalid lines: \n"
        print "\n".join(removed)
    if (changed != []):
        print "\nThe following lines have scores > 1000, so they are changed to 1000:\n"
        print "\n".join(changed)

if __name__ == "__main__":
    main()
