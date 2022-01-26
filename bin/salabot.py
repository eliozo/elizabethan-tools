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
    else:
        filename = sys.argv[1]
        salabot(filename)


if __name__ == '__main__':
        main()