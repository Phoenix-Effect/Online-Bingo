# Online Bingo

Simple bingo website that lets you host your very own bingo party with a computer. The code has two components

## Cards
* `num_gener.py` Lets us generate a csv with 24 random numbers between 1-75 per row. 
* `bingocards.csv` Output produced by our python number generator.
* `Bingo page.indd` This is a template for indesign that contain variables. Using data merge with our csv file we can produce our bingo cards.
* `Bingo page.pdf` Output produced by InDesign data merge.

## Generator
Generator is the web component the code. It is a simple website that generates numbers between 1-75 for our bingo. It has a small animation and keeps track of previously generated numbers. To run the generator simply download the code and run `index.html` in generator folder.