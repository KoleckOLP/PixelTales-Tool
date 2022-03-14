import sys, os
import glob


def FixDDSHeadder(pathToPMT: str, outputPath=""):
    hexString = ""

    with open(pathToPMT, "rb") as f:
        while (byte := f.read(1)):
            hexString = hexString + byte.hex()

    offset = hexString.find("444453")
    if offset != -1:
        hexStringFixed = hexString[offset:]

        hexArray = [hexStringFixed[i:i+2] for i in range(0, len(hexStringFixed), 2)]

        newFileName = os.path.basename(path)[:-3] + "dds"

        with open(outputPath+newFileName, "wb") as w:
            for i in hexArray:
                w.write(bytes.fromhex(i))
        print(f"{offset} {pathToPMT} - {outputPath+newFileName}")
    else:
        print(f"{pathToPMT} - does not seem to be a valid DDS texture")


paths = ""
outputPath = ""

try:
    if "-i" in sys.argv[1]:
        path = sys.argv[2]
        try:
            if sys.argv[3] == "-o":
                outputPath = sys.argv[4]
        except IndexError:
            pass
        if "r" in sys.argv[1]:
            paths = glob.glob(path+"\\*.pmt")
        if paths != "":
            for path in paths:
                FixDDSHeadder(path, outputPath)
        else:
            FixDDSHeadder(path, outputPath)
except IndexError:
    print("PixelTales Texture Header Fixer\n" +
          "made by Koleq (C) 2022\n\n" +
          "-i pathToFile.pmt = fixes a single file\n" +
          "-ir pathToFolder = fixes all the .pmt files in the folder\n" +
          "-o path = sets path where to put Fixed dds files (must be after -i/-ir)\n\n" +
          "example: ptthf.py -i pmtfiles\\reference.pmt -o ddsfiles\\reference.dds\n")
