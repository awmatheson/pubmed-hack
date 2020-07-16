import requests
from bs4 import BeautifulSoup

# this code will read in the ncts numbers into a list => ['nct134134124', 'nct13434234', ...]
with open('ncts.txt', 'r') as f:
    ncts = f.readlines()

# now we will loop through the ncts and get all the pubmed ids and print those out
for nct in ncts:

    # print the nct
    print(nct)

    ## this code will make an http request to the search page on pubmed.com
    resp = requests.get("https://pubmed.ncbi.nlm.nih.gov/?term={}".format(nct))

    # then we will take the html portion and pull out the pubmed ids
    soup = BeautifulSoup (resp.text, "html.parser")
    pubmed_ids = soup.findAll("span", {"class": "docsum-pmid"})

    # and print them
    for pmid in pubmed_ids:
        print(pmid.text)