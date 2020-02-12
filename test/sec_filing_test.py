from sec_edgar.filing import SecFiling, SecFilingType

DIR_PATH = 'E:/python/data/sec_filing/'
import logging

logging.basicConfig(level=logging.INFO)


def _fetch_apple_filing():
    """
    10-Q filings for Apple
    :return:
    """
    apple_filing = SecFiling(cik='0000320193', filing_type=SecFilingType.FILING_10Q)
    apple_filing.save(DIR_PATH)


if __name__ == '__main__':
    _fetch_apple_filing()
