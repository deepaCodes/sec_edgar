from sec_edgar.edgar_search import EDGARSearch


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
