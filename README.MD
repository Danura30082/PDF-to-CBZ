# PDF to CBZ Converter

This project contains a Python script that converts PDF files to CBZ (Comic Book Archive) format.

## Dependencies

The script uses the following Python libraries:

- `fitz`: Part of the PyMuPDF package, used for PDF processing.
- `os`: Provides functions for interacting with the operating system.
- `shutil`: Offers a number of high-level operations on files and collections of files.
- `glob`: Finds all the pathnames matching a specified pattern.

## Usage

1. Ensure you have the necessary Python libraries installed. You can install them using pip.
2. Run the script with the path to the PDF file you want to convert. The script will convert the PDF to a series of images and then package them into a CBZ file.

## Project Structure

- `PDF to CBZ.py`: The main script that converts PDF files to CBZ format.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.MD`: This file, which provides an overview of the project.

Please note that this README assumes that you have Python and pip installed on your system. If not, you will need to install them first.