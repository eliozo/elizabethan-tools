# -*- coding: utf-8 -*-
import sys

def salabot(filename):
    try:
        with open(filename, "rb") as f:

            mybytearray = bytearray()
            byte = f.read(1)
            # Do stuff with byte.
            while byte:
                mybytearray += f.read(1)
                byte = f.read(1)
            print(mybytearray)
            print(len(mybytearray))

    except IOError:
        print('Error While Opening the file!')

def main():
    if len(sys.argv) < 2:
        print ("Kļūda! Vajag norādīt faila vārdu!")
        exit(1)
    fin = open(sys.argv[1], "rt", encoding='utf-8')
    # output file to write the result to
    # fout = open("out.txt", "wt", encoding='utf-8')
    # for each line in the input file
    visas_rindas = []
    for line in fin:
        # read replace the string and write to output file
        # fout.write(line.replace('   ', '  \n'))
        visas_rindas.append(line.replace('   ', '  \n'))
    # close input and output files
    fin.close()
    fout = open(sys.argv[1], "wt", encoding='utf-8')
    for line in visas_rindas:
        fout.write(line)
    fout.close()
    #else:
        #filename = sys.argv[1]
        #salabot(filename)

if __name__ == '__main__':
    main()