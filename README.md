# Information Extraction Program
The goal of this exercise is to write a program that can extract common information from a variety of documents.

## Expected Behavior
* Each document within `documents/` is a .txt file, each of which is scanned from some real life document
* Some documents are receipts, while others are bank statements
* Write a program that does the following:
    * Takes as input a list of paths to files with text (i.e. `['/documents/1.txt', '/documents/1.txt', ...]`)
    * Returns text in CSV format with the following information:
        * PATH - Path to document
        * TYPE - Detected type of document (either `RECEIPT` or `BANK`)
        * AMOUNT - The total bank balance if a bank statement, or the total amount for the receipt
        * OTHER - Extra information for this document based on the type:
            * If a receipt, the change due (if not available, use `0`)
            * If a bank statement, at least one phone number for that bank
* Please provide code or a script that also runs the set of given documents through your method and prints the result (i.e some sort of `main` method)

*Feel free to extract other fields if you would like, but this not necessary!*


## Details
* Feel free to use Google to look up any resources you need.
* You can use any libraries or frameworks you want.
* You can use any programming language you want, as long as we are also able to run that code (i.e. a common language such as Python, Java, JavaScript, etc...). Please send an email letting us know what language you would like to use when receiving this challenge.


## Guidelines
* The focus will be on correctness, efficiency, and extensibility
* Aim to spend 4 hours or less on this question, though there is no lower or upper bound.

## How to Submit
* Preferably, submit your code in a Github repo, with a link to a working version we can play with.
* You can also submit you code as a zip file, with instructions on how we can set it up and run it locally.
