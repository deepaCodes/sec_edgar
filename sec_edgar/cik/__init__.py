from sec_edgar.cik.cik_validator import CIKValidator


class CIK(object):
    """
    Validates CIKs (Central Index Keys) by ticker.

    Attributes:
        lookup (Union[str, list]): Ticker, company name, or list of tickers and/or company names.

    """

    def __init__(self, lookups, **kwargs):
        super(CIK, self).__init__(**kwargs)
        self._validator = CIKValidator(lookups)
        self._lookup_dict = self._validator.get_ciks()
        self._ciks = self._lookup_dict.values()

    @property
    def ciks(self):
        return self._ciks

    @property
    def lookup_dict(self):
        return self._lookup_dict
