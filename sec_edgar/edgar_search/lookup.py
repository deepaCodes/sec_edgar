import requests

_CIK_LOOKUP_URL = 'https://www.sec.gov/Archives/edgar/cik-lookup-data.txt'


class EDGARSearch:
    """
    edgar search by company name, cik etc.
    https://www.sec.gov/edgar/search-and-access

    https://www.sec.gov/Archives/edgar/cik-lookup-data.txt

    """

    def __init__(self):
        all_companies_page = requests.get(_CIK_LOOKUP_URL)
        all_companies_content = all_companies_page.content.decode("latin1")
        all_companies_array = all_companies_content.split("\n")
        del all_companies_array[-1]
        all_companies_array_rev = []
        for i, item in enumerate(all_companies_array):
            if item == "":
                continue
            _name, _cik = EDGARSearch.split_raw_string_to_cik_name(item)
            all_companies_array[i] = (_name, _cik)
            all_companies_array_rev.append((_cik, _name))
        self.all_companies_dict = dict(all_companies_array)
        self.all_companies_dict_rev = dict(all_companies_array_rev)

    def get_cik_by_company_name(self, name):
        return self.all_companies_dict[name]

    def get_company_name_by_cik(self, cik):
        return self.all_companies_dict_rev[cik]

    def find_company_name(self, words):
        possible_companies = []
        words = words.lower()
        for company in self.all_companies_dict:
            if all(word in company.lower() for word in words.split(" ")):
                possible_companies.append(company)
        return possible_companies

    @classmethod
    def split_raw_string_to_cik_name(cls, item):
        item_arr = item.split(":")[:-1]
        return ":".join(item_arr[:-1]), item_arr[-1]
