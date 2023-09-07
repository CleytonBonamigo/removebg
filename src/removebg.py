from rembg import remove
from PIL import Image
import sys
import os

def removebg(inputPath, outputPath):
    # Get the file extension
    file_extension = os.path.splitext(inputPath)[1][1:].lower()

    # Check if the file extension is in the list of accepted file types
    if file_extension not in ['jpg', 'jpeg', 'png']:
        print(f"Warning: Unsupported file type '{file_extension}'. Supported file types are: jpg, jpeg, png.")
        sys.exit(1)

    originalImage = Image.open(inputPath)
    imageWithoutBg = remove(originalImage)
    imageWithoutBg.save(outputPath)

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Usage: python removebg.py <input_path> <output_path>")
        sys.exit(1)

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    removebg(inputPath, outputPath)