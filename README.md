# Accessing SEC EDGAR Data (Electronic Data Gathering, Analysis, and Retrieval system) using Python

https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm

This project contains the following features 
 1. Search EDGAR for Company or fund name, ticker symbol, Central Index Key (CIK). https://www.sec.gov/edgar/search-and-access
 2. Scrapping EDGAR filling forms and downloading (parallel downloading for faster)
 

## Useful SEC links

https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm

https://www.sec.gov/oiea/Article/edgarguide.html

https://www.sec.gov/edgar/search-and-access

https://www.sec.gov/files/company_tickers.json

https://www.sec.gov/Archives/edgar/cik-lookup-data.txt

https://www.sec.gov/include/ticker.txt

 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.7.0 or higher, I have not tested in previous version of python
Dependency lib's are added into requirement.txt, run dependency.txt to install required python packages.



### Installing and running

A step by step series of examples that tell you how to get a development env running

Install dependency packages 

```
cd ./sec_edgar
pip install -r requirements.txt

```
### Running - Test code

```
1. Search for the company or cik
    
    def _lookup_cik():
        """
        apple: 0000320193
        :return:
        """
        cik = '0000320193'
        search = EDGARSearch()
    
        company_result = search.get_company_name_by_cik(cik)
        print('Search result by cik : {}'.format(company_result))
    
        company_result = search.find_company_name(words='apple')
        print('Search result by partial company name : {}'.format(company_result))
    
        company_result = search.get_cik_by_company_name(company_result[0])
        print('Search result by full company name : {}'.format(company_result))

    
    if __name__ == '__main__':
        _lookup_cik()

Program output:
    
    C:\ProgramData\Anaconda3\python.exe E:/python/sec_edgar/test/edgar_search_test.py
    Search result by cik - 0000320193 is : APPLE INC
    Search result by partial company name- google is : ['GOOGLE CAPITAL 2016 GP, L.L.C.', 'GOOGLE CAPITAL 2016, L.P.', 'GOOGLE INC.', 'GOOGLE INC', 'GOOGLE TECHNOLOGY INC', 'GOOGLE VENTURES 2011 GP, L.L.C.', 'GOOGLE VENTURES 2011, L.P.', 'GOOGLE VENTURES 2013, L.P.']
    Search result by full company name - APPLE COMPUTER INC is : 0000320193

2. Scrape and download sec filing forms for the given company or cik
    
    DIR_PATH = 'E:/python/data/sec_filing/'

    def _fetch_apple_filing():
        """
        download 10-Q filings for Apple
        :return:
        """
        apple_filing = SecFiling(cik='0000320193', filing_type=SecFilingType.FILING_10Q)
        apple_filing.save(DIR_PATH)


    if __name__ == '__main__':
        _fetch_apple_filing()

    
Program output:

    C:\ProgramData\Anaconda3\python.exe E:/python/sec_edgar/test/sec_filing_test.py
    INFO:root:Fetching soup from: cgi-bin/browse-edgar with params: {'action': 'getcompany', 'CIK': '0000320193'}
    INFO:root:Fetching soup from: cgi-bin/browse-edgar with params: {'action': 'getcompany', 'count': 10, 'dateb': '20200212', 'output': 'xml', 'owner': 'exclude', 'start': 0, 'type': '10-q', 'CIK': '0000320193'}
    INFO:root:cik url: ['https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt']
    INFO:root:filing url: ['https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt']
    INFO:root:Document Names: ['0000320193-20-000010.txt', '0000320193-19-000076.txt', '0000320193-19-000066.txt', '0000320193-19-000010.txt', '0000320193-18-000100.txt', '0000320193-18-000070.txt', '0000320193-18-000007.txt', '0000320193-17-000009.txt', '0001628280-17-004790.txt', '0001628280-17-000717.txt']
    INFO:root:cpu count: 4
    INFO:root:Parallel downloading starts using multiprocessing
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000076.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-20-000010.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000066.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000010.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000100.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000070.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000007.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-17-000009.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0001628280\10-q\0001628280-17-004790.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0001628280\10-q\0001628280-17-000717.txt
    INFO:root:downloading complete
    
    Process finished with exit code 0

```

## Author

* **Deepa Aswathaiah**



## Program out

```

    C:\ProgramData\Anaconda3\python.exe E:/python/sec_edgar/test/sec_filing_test.py
    INFO:root:Fetching soup from: cgi-bin/browse-edgar with params: {'action': 'getcompany', 'CIK': '0000320193'}
    INFO:root:Fetching soup from: cgi-bin/browse-edgar with params: {'action': 'getcompany', 'count': 10, 'dateb': '20200212', 'output': 'xml', 'owner': 'exclude', 'start': 0, 'type': '10-q', 'CIK': '0000320193'}
    INFO:root:cik url: ['https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt']
    INFO:root:filing url: ['https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt', 'https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt']
    INFO:root:Document Names: ['0000320193-20-000010.txt', '0000320193-19-000076.txt', '0000320193-19-000066.txt', '0000320193-19-000010.txt', '0000320193-18-000100.txt', '0000320193-18-000070.txt', '0000320193-18-000007.txt', '0000320193-17-000009.txt', '0001628280-17-004790.txt', '0001628280-17-000717.txt']
    INFO:root:cpu count: 4
    INFO:root:Parallel downloading starts using multiprocessing
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019320000010/0000320193-20-000010.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/0000320193-19-000066.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019319000010/0000320193-19-000010.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000076.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-20-000010.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000066.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-19-000010.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/0000320193-18-000100.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/0000320193-18-000007.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000032019317000009/0000320193-17-000009.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000100.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000070.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-18-000007.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0000320193\10-q\0000320193-17-000009.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000162828017004790/0001628280-17-004790.txt
    INFO:root:Downloading from: https://www.sec.gov/Archives/edgar/data/320193/000162828017000717/0001628280-17-000717.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0001628280\10-q\0001628280-17-004790.txt
    INFO:root:saving to path: E:/python/data/sec_filing/0001628280\10-q\0001628280-17-000717.txt
    INFO:root:downloading complete
 
```