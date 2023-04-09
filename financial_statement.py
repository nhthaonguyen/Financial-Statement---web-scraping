import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

#Beautiful Soup browser agent set up for laptop/pc
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

ticker = "AAPL"

urls = {}
urls['income statement annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
urls['balance sheet annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/"
urls['cash flow annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/"

xlwriter = pd.ExcelWriter(f'financial statement ({ticker}).xlsx', engine = 'xlsxwriter')

for key in urls.keys():
    response = requests.get(urls[key], headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    df= pd.read_html(str(soup), attrs={'data-test': 'financials'})[0]
    df.to_excel(xlwriter, sheet_name = key, index = False)

xlwriter.save()