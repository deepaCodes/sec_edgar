import datetime
import multiprocessing
import os
import requests

from sec_edgar.network.edgar_network_client import NetworkClient
from sec_edgar.utils import sanitize_date, make_path

from sec_edgar.cik import CIK
from sec_edgar.filing.filing_types import SecFilingType
from sec_edgar.exception.edgar_exceptions import FilingTypeError
import logging


class SecFiling:
    """
    downloading EDGAR filings.
    multiprocessing : parallel downloading for faster processing

    Attributes:
        cik (str): Central Index Key (CIK) for company of interest.
        filing_type (SECEdgar.filings.filing_types.FilingType): Valid filing type enum.
        dateb (Union[str, datetime.datetime], optional): Date after which not to fetch reports.
            Stands for "date before." Defaults to today.

    """

    def __init__(self, cik, filing_type, dateb=datetime.datetime.today(), client=None, **kwargs):
        self.dateb = dateb
        self.filing_type = filing_type
        if not isinstance(cik, CIK):  # make CIK for users if not given
            cik = CIK(cik)
        self._ciks = cik.ciks
        self._params = {
            'action': 'getcompany',
            'count': kwargs.get('count', 10),
            'dateb': self.dateb,
            'output': 'xml',
            'owner': 'exclude',
            'start': 0,
            'type': self.filing_type.value
        }
        # Make default client NetworkClient and pass in kwargs
        if client is None:
            # create NetworkClient with kwargs
            self._client = NetworkClient(**kwargs)

    @property
    def path(self):
        return "cgi-bin/browse-edgar"

    @property
    def params(self):
        return self._params

    @property
    def client(self):
        return self._client

    @property
    def dateb(self):
        return self._dateb

    @dateb.setter
    def dateb(self, val):
        self._dateb = sanitize_date(val)

    @property
    def filing_type(self):
        return self._filing_type

    @filing_type.setter
    def filing_type(self, filing_type):
        if not isinstance(filing_type, SecFilingType):
            raise FilingTypeError(SecFilingType)
        self._filing_type = filing_type

    @property
    def ciks(self):
        return self._ciks

    def get_urls(self, **kwargs):
        """Get urls for all CIKs given to Filing object.

        Args:
            kwargs: Anything to be passed to requests when making get request.

        Returns:
            urls (list): List of urls for txt files to download.
        """
        urls = []
        for cik in self.ciks:
            urls.extend(self._get_urls_for_cik(cik, **kwargs))
        logging.info('filing url: %s', urls)
        return urls

    def _get_urls_for_cik(self, cik, **kwargs):
        """
        Get all urls for specific company according to CIK that match
        dateb, filing_type, and count parameters.

        Args:
            cik (str): CIK for company.
            kwargs: Anything to be passed to requests when making get request.

        Returns:
            txt_urls (list of str): Up to the desired number of URLs for that specific company
            if available.
        """
        self.params['CIK'] = cik
        data = self._client.get_soup(self.path, self.params, **kwargs)
        links = []

        # TODO: Make paginate utility outside of this class
        while len(links) < self._client.count:
            links.extend([link.string for link in data.find_all("filinghref")])
            self.params["start"] += 100
            if len(data.find_all("filinghref")) == 0:
                break
        self.params["start"] = 0  # set start back to 0 after paginating
        txt_urls = [link[:link.rfind("-")] + ".txt" for link in links]
        logging.info('cik url: %s', txt_urls)
        return txt_urls[:self.client.count]

    def save(self, directory):
        """Save files in specified directory.
        Each txt url looks something like:
        https://www.sec.gov/Archives/edgar/data/1018724/000101872419000043/0001018724-19-000043.txt

        Args:
            directory (str): Path to directory where files should be saved.

        Returns:
            None

        Raises:
            ValueError: If no text urls are available for given filing object.
        """
        urls = self.get_urls()
        if len(urls) == 0:
            raise ValueError("No filings available.")
        doc_names = [url.split("/")[-1] for url in urls]
        logging.info('Document Names: %s', doc_names)

        # parallel downloading of files
        cpu_count = multiprocessing.cpu_count()
        logging.info("cpu count: %d", cpu_count)
        logging.info("Parallel downloading starts using multiprocessing")

        pool_args = []
        for (url, doc_name) in list(zip(urls, doc_names)):
            pool_args.append((url, doc_name, directory, self.filing_type))

        with multiprocessing.Pool(processes=cpu_count) as pool:
            pool.map(_download_filing, pool_args)

        logging.info("downloading complete")


def _download_filing(params):
    """
    download each doc name to given target directory
    :param params:
    :return:
    """

    url, doc_name, directory, filing_type = params
    logging.info('Downloading from: %s', url)
    cik = doc_name.split('-')[0]
    data = requests.get(url).text
    path = os.path.join(directory, cik, filing_type.value)
    make_path(path)
    path = os.path.join(path, doc_name)
    logging.info('saving to path: %s', path)
    with open(path, "w") as f:
        f.write(data)
