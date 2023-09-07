from rembg import remove
from PIL import Image
import sys

def removebg(inputPath, outputPath):
    originalImage = Image.open(inputPath)
    imageWithoutBg = remove(originalImage)
    imageWithoutBg.save(outputPath)

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Usage: python removebg.py <input_path> <output_path")
        sys.exit(1)

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    removebg(inputPath, outputPath)