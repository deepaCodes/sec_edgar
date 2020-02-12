# Accessing EDGAR Data (Electronic Data Gathering, Analysis, and Retrieval system) using Python

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
    Search result by cik : APPLE INC
    Search result by partial company name : ['ADS APPLE VALLEY INC', 'ADS APPLE VALLEY LTD PARTNERSHIP', 'APM APPLETON CURRENCY FUND L P', 'APPLE ALLAN VICTOR', 'APPLE BEACH COUNTY LTD LIABILITY CO', 'APPLE BLOSSOM REIT, LLC', 'APPLE BLOSSOM ROYALTIES LLC', 'APPLE BOX PRODUCTIONS SUB INC', 'APPLE BOYS MUSICAL NYC, LLC', 'APPLE BROOKE INCOME FUND, LLC', 'APPLE C CHRIS', 'APPLE CAPITAL GROUP, INC.', 'APPLE COMPUTER INC/ FA', 'APPLE COMPUTER INC', 'APPLE CREEK ACQUISITION CORP', 'APPLE FUNDING, LLC', 'APPLE GREEN HOLDING, INC.', 'APPLE GREG', 'APPLE HOMES CORP INC', 'APPLE HOSPITALITY FIVE INC', 'APPLE HOSPITALITY REIT, INC.', 'APPLE HOSPITALITY TWO INC', 'APPLE INC.', 'APPLE INC', 'APPLE INVESTORS LLC', 'APPLE JAMES G', 'APPLE JIM B', 'APPLE KENNETH W', 'APPLE LANE GROUP LLC', 'APPLE LESLIE M', 'APPLE MELISSA', 'APPLE ORANGE LLC', 'APPLE ORTHODONTIX INC', 'APPLE REIT EIGHT, INC.', 'APPLE REIT NINE, INC.', 'APPLE REIT SEVEN, INC.', 'APPLE REIT SIX INC', 'APPLE REIT TEN, INC.', 'APPLE RESIDENTIAL INCOME TRUST INC', 'APPLE RIDGE ASSISTED LIVING LLC', 'APPLE ROBERT E', 'APPLE ROBERT F', 'APPLE RUN ACQUISITION CORP', 'APPLE RUSH CO., INC', 'APPLE SEEDS, LLC', 'APPLE SOLAR CO', 'APPLE SOUTH FINANCING I', 'APPLE SOUTH INC', 'APPLE SUITES INC', 'APPLE SUN LLC', 'APPLE TOWERS INVESTORS LLC', 'APPLE TREE CONSOLIDATED BVBA SPRL', 'APPLE TREE INVESTMENTS S.A.R.L', 'APPLE TREE INVESTMENTS, INC.', 'APPLE TREE PARTNERS I LP', 'APPLE TREE PARTNERS II - ANNEX, L.P.', 'APPLE TREE PARTNERS II LP', 'APPLE TREE PARTNERS IV, L.P.', 'APPLE TREE RESOURCES INC', 'APPLE VALLEY / HESPERIA HOME DEVELOPMENT LLC', 'APPLE VALLEY INVESTORS, LLC', 'APPLE VALLEY LIMITED PARTNERSHIP', 'APPLE VALLEY OPERATING CORP.', 'APPLE VALLEY PARTNERSHIP HOLDING CO INC', 'APPLE VALLEY PORK, LLP', 'APPLEBACH RICHARD JR', 'APPLEBAUM EUGENE', 'APPLEBAUM HOWARD M', 'APPLEBAUM JAY I', 'APPLEBAUM MARC', 'APPLEBAUM MICHELLE GALANTER', 'APPLEBAUM SCOTT', 'APPLEBAUM STANLEY A', 'APPLEBEE ANDREW F', "APPLEBEE'S ENTERPRISES LLC", "APPLEBEE'S FRANCHISING LLC", "APPLEBEE'S HOLDINGS II CORP.", "APPLEBEE'S HOLDINGS LLC", "APPLEBEE'S IP LLC", "APPLEBEE'S RESTAURANTS KANSAS LLC", "APPLEBEE'S RESTAURANTS MID-ATLANTIC LLC", "APPLEBEE'S RESTAURANTS NORTH LLC", "APPLEBEE'S RESTAURANTS TEXAS LLC", "APPLEBEE'S RESTAURANTS VERMONT, INC.", "APPLEBEE'S RESTAURANTS WEST LLC", "APPLEBEE'S RESTAURANTS, INC.", "APPLEBEE'S SERVICES, INC.", "APPLEBEE'S UK, LLC", 'APPLEBEES INTERNATIONAL INC', 'APPLEBERRY LEE BERT', 'APPLEBROOK ASSOCIATES LLC', 'APPLEBROOK ASSOCIATES LP', 'APPLEBY ADAM D', 'APPLEBY CG', 'APPLEBY JARRETT', 'APPLEBY LANDING LLC', 'APPLEBY MICHAEL JOSEPH', 'APPLEBY PARTNERS & COMPANY, LLC', 'APPLEBY PARTNERS LTD', 'APPLEBY PAUL', 'APPLEBY RICHARD E', 'APPLEBY ROBERT P', 'APPLEBY SCOTT W.', 'APPLEBY TELECOMMUNICATIONS LLC', 'APPLECARE, LLC', 'APPLEGATE BRION B', 'APPLEGATE COMMODITIES HOLDING LLC', 'APPLEGATE DAVID B', 'APPLEGATE DAVID M', 'APPLEGATE DIANE L', 'APPLEGATE FRED C', 'APPLEGATE MICHAEL T', 'APPLEGATE THOMAS J', 'APPLEGATH JOHN KIEL', 'APPLEMAN JAMES R.', 'APPLEPALM PARTNERS LTD', 'APPLEPALM WEST, LP', 'APPLEPIE CAPITAL, INC.', 'APPLEPIE FINANCE, LLC', 'APPLEPIE TRUST', 'APPLEQUIST DALE M', 'APPLERA CORP', 'APPLES TO GO INC', 'APPLESEED DISCOVERY FUND, LP', 'APPLESEED LLC', 'APPLESEED PIONEER FUND, LP', 'APPLESEED PORTAL LLC', 'APPLESEED VENTURES GROWTH OPPORTUNITY FUND LLC', 'APPLESEEDS TOPCO INC', 'APPLETICS INC', 'APPLETON ADVISORS LLC', 'APPLETON ALBERT F', 'APPLETON CAPITAL LLC', 'APPLETON CURRENCY FUND L P', 'APPLETON DOUGLAS S', 'APPLETON FUNDS', 'APPLETON GROUP WEALTH MANAGEMENT LLC', 'APPLETON GROUP, LLC', 'APPLETON INVESTORS LLC', 'APPLETON JAMES R', 'APPLETON LEARNING CORP', 'APPLETON MICHAEL D.', 'APPLETON NAVIGATION S.A.', 'APPLETON PAPERS INC/WI', 'APPLETON PARTERS INC/MA', 'APPLETON PARTNERS INC/MA', 'APPLETON PARTNERS L P', 'APPLETON RETIREMENT, LLC', 'APPLETON ROADHOUSE INC', 'APPLETON STEAM INC.', 'APPLETON STEVEN R', 'APPLETON SUPPLY COMPANY, INC.', 'APPLETON WILLIAM', 'APPLETREE COMPANIES INC', 'APPLETREE.COM, INC', 'APPLEWAY CHEVROLET INC', 'APPLEWICK STEVEN L', 'APPLEWOOD ASSOCIATES L P', 'APPLEWOOD HEALTH RESOURCES INC', 'APPLEWOODS INC', 'APPLEWOODS RESTAURANTS INC', 'APPLEYARD IAN', 'ATLANTIC MULTI FAMILY 7 - APPLE, LLC', 'AXIOM-APPLETREE, LLC', 'BIG APPLE BASEBALL LLC', 'BIG APPLE CONSULTING USA INC', 'BIG APPLE ENTERTAINMENT PARTNERS LLC', 'BIG APPLE HOLDINGS FLORIDA I LLC', 'BIG APPLE HOLDINGS INC', 'BIG APPLE WALLCOVERING INC', 'BLUEAPPLE, INC.', 'BRIDGE APPLETON INVESTORS LLC', 'C J APPLEGATE & SONS INC', 'CATERPILLAR SHOW BIG APPLE LIMITED PARTNERSHIP', 'CHAPPLE JOHN F IIII', 'CHAPPLE JOHN', 'CHAPPLE THOMAS L', 'CLEVELAND APPLE INVESTOR L.P.', 'CRAPPLE GEORGE E', 'DR PEPPER SNAPPLE GROUP, INC.', 'EQUITY APPLE, INC.', 'FUND I, A SERIES OF PINEAPPLE CAPITAL, LP', 'GOLDEN APPLE INCOME INC', 'GOLDEN APPLE TRADING, L.P.', 'GREEN APPLE VENTURES LLC', 'HARRINGTON TRUST LIMITED AS TRUSTEE OF THE APPLEBY TR', 'HFS CRABAPPLE CROSSROADS, LP', 'HOLESAPPLE PROSPECT I LTD', 'HOLESAPPLE PROSPECT II LTD.', 'JOHNNY APPLESTIX LLC', 'KAPPLER ANN M', 'KAPPLER JEFFREY', 'KAPPLES JOHN W.', 'LCP APPLE CHARLOTTE, LLC', 'LCP APPLE CONCORD, LLC', 'LCP APPLE FAYETTEVILLE, LLC', 'LG APPLE ABERDEEN, LLC', 'LG APPLE GARNER, LLC', 'LG OWASSO APPLE FARMS, LLC', 'LINEAPPLE INC', 'MAUI LAND & PINEAPPLE CO INC EMPLOYEE STOCK OWNERSIP PLAN', 'MAUI LAND & PINEAPPLE CO INC', 'MITCHELL SAMUEL APPLETON', 'ML APPLETON FUTURESACCESS LLC', 'NBM RAPPLER, L.P.', 'NICHOLAS APPLEGATE CAPITAL MANAGEMENT A CA LP          /ADV', 'NICHOLAS APPLEGATE CAPITAL MANAGEMENT LLC', 'NICHOLAS APPLEGATE CAPITAL MANAGEMENT', 'NICHOLAS APPLEGATE CONVERTIBLE & INCOME FUND II', 'NICHOLAS APPLEGATE CONVERTIBLE & INCOME FUND', 'NICHOLAS APPLEGATE EMERGING COUNTRIES SERIES', 'NICHOLAS APPLEGATE FUND INC', 'NICHOLAS APPLEGATE GLOBAL EQUITY & CONVERTIBLE INCOME FUND', 'NICHOLAS APPLEGATE INSTITUTIONAL FUNDS', 'NICHOLAS APPLEGATE INVESTMENT TRUST', 'NICHOLAS APPLEGATE MUTUAL FUNDS', 'NICHOLAS APPLEGATE SECURITIES LLC', 'NICHOLAS APPLEGATE SERIES TRUST', 'NICHOLAS APPLEGATE U S CONVERTIBLE ARBITRAGE FUND LLC', 'NICHOLAS-APPLEGATE EQUITY & CONVERTIBLE INCOME FUND', 'NICHOLAS-APPLEGATE EQUITY & INCOME CAPTURE FUND', 'NICHOLAS-APPLEGATE INTERNATIONAL & PREMIUM STRATEGY FUND', 'NICHOLAS-APPLEGATE INTERNATIONAL SYSTEMATIC FUND LLC', 'NICHOLAS-APPLEGATE SECURITIES (A CALIFORNIA LIMITED PARTNERS', 'NICHOLAS-APPLEGATE SECURITIES LLC', 'ORGANIC PINEAPPLE HOLDINGS, LLC', 'PACIFIC SNAPPLE DISTRIBUTORS INC', 'PAFM NICHOLAS APPLEGATE NFJ CONVERTIBLE & INCOME FUND', 'PANAMA GOLDEN PINEAPPLE LP', 'PINEAPPLE DC LLC', 'PINEAPPLE EXPRESS, INC.', 'PINEAPPLE PICTURES LLC', 'PINEAPPLE VENTURES, INC.', 'PINK PINEAPPLE LLC', 'PR APPLETON WEST, INC.', 'PROJECT APPLECART LLC', 'R APPLE PIE CO', 'ROAD APPLES INC', 'SCA-APPLECARE PARTNERS, LLC', 'SCAPPLE INC', 'SNAPPLE BEVERAGE CORP', 'SNAPPLE BEVERAGE GROUP INC', 'SNAPPLE CARRIBEAN CORP', 'SNAPPLE DISTRIBUTORS, INC.', 'SNAPPLE FINANCE CORP', 'SNAPPLE INTERNATIONAL CORP', 'SNAPPLE WORLDWIDE CORP', 'SPROVY 7 APPLEGATE TX 1, LLC', 'SSIF - APPLE VALLEY, LLC', 'SWANSEA APPLEGATE INVESTORS, LLC', 'THG APPLE HOTEL VENTURES, LLC', 'THORN APPLE VALLEY INC', 'THORNAPPLE RIVER CAPITAL - FINANCIAL SERVICES INDUSTRY FUND LLC', 'THORNAPPLE RIVER CAPITAL - VENTURE FUND LLC', 'WAPPLER J MICHAEL', 'WP APPLE 2008 LLC', 'WP APPLE LLC']
    Search result by full company name : 0001281227

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