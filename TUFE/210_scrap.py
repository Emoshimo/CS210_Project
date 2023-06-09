import os, sys, glob, re
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import uuid

from config import LINK_LIST_PATH

# Encoding for writing the URLs to the .txt file
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"

if __name__ == "__main__":
    #download_links_from_index()

    url = "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri/Tuketici+Fiyatlari"
    response = requests.get(url)

    file_ = 'example.txt'  # Specify the path and name of the file
    file = open(file_, 'w')

    # Create a BeautifulSoup object with the webpage HTML content
    soup = bs(response.content, 'html.parser')

    # Find all table rows (tr tags) in the HTML
    table_rows = soup.find_all('tr')

    # Iterate over the table rows and print the HTML content
    indexx = 1
    for row in table_rows:
        data = row.find_all('td')
        if(indexx != 1):
            value1 = str(data[0].text)
            value2 = str(data[1].text)
            value3 = str(data[2].text)
            roww = value1 + "\t" + value2 + "\t" + value3 + "\n"
            file.write(roww)
            #print(data)

        indexx = 2

    file.close()




