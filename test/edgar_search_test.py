from sec_edgar.edgar_search import EDGARSearch


def _lookup_cik():
    """
    apple: 0000320193
    :return:
    """
    cik = '0000320193'
    search = EDGARSearch()

    _search_for = cik
    company_result = search.get_company_name_by_cik(cik)
    print('Search result by cik - {} is : {}'.format(_search_for, company_result))

    _search_for = 'google'
    company_result = search.find_company_name(words=_search_for)
    print('Search result by partial company name- {} is : {}'.format(_search_for, company_result))

    _search_for = 'APPLE COMPUTER INC'
    company_result = search.get_cik_by_company_name(_search_for)
    print('Search result by full company name - {} is : {}'.format(_search_for, company_result))


if __name__ == '__main__':
    _lookup_cik()
