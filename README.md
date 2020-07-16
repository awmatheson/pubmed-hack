# pubmed-hack
get pubmed id for nct id entries from the search

## Getting Started

To use this you first need to have python installed on your machine and to know how to use terminal.

Macs come with python, but it is usually python 2.7 which is old and won't work.

Press Command + Space Bar and search for "terminal"

Open the terminal, now you will be in your home directory.

Now download homebrew to help you install python, run this in your terminal

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

Now install python by typing in your terminal

`brew install python`

Now you have python installed you can start using the script.

The script relies on what is called a library, you will need to install the libraries with pip.

in your terminal again:

`pip install -r requirements.txt`

Once that is complete we can run the script.

## How the script works

The script takes the nct numbers from `ncts.txt` and it will put them into a data structure called a list, which is just like a normal list :)

The numbers in the list are then searched with a url hack and the returned html is parsed and the pubmed ids are output. 

To run the script:

`python scrape.py`

It will output the nct followed by the pubmed ids. 

We can change that later once you get it working.