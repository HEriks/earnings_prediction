from typing import Optional
from borsdata_sdk import BorsdataAPI
import csv


def find_insid_by_ticker(borsdata, ticker) -> Optional[int]:
    instruments = borsdata.get_instruments()
    for instrument in instruments:
        if instrument.ticker == ticker:
            return instrument.insId
    return None


def find_insid_by_name(borsdata, name) -> Optional[int]:
    instruments = borsdata.get_instruments()
    for instrument in instruments:
        if instrument.name == name:
            return instrument.insId
    return None


def report_to_csv_eps(borsdata, ticker, type='year', out="data/data.csv"):
    reports = borsdata.get_instrument_reports(ticker, type)
    
    header = [type, 'EPS']
    rows = []
    if type == 'year':
        for report in reports:
            rows.append([report.year, report.earnings_per_share])
    elif type == 'quarter':
        for report in reports:
            rows.append([f"{report.year}Q{report.period}", report.earnings_per_share])
    else:
        Exception("Type of data not found (should be 'year', 'quarter', or 'r12')")

    # open the file in the write mode
    with open(out, 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)

        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def main():
    f = open("apikey.txt", "r")
    apikey = f.readline()

    borsdata = BorsdataAPI('7007525b91fd4980aaa034c2f3740ff2')

    ticker = find_insid_by_ticker(borsdata, "EVO")
    ticker1 = find_insid_by_name(borsdata, "Volvo B")

    report_to_csv_eps(borsdata, ticker, 'year')


if __name__ == "__main__":
    main()