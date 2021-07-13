"""
Created on July 14, 2019

@author: Joselle Abagat Barnett
"""
from src import ingest
from pypif import pif


def main():
    """
    test file to output a pif system into a json file
    :return: empty
    """
    ls_pif = ingest.ingest()
    file = "test_output.json"
    pif_json = pif.dumps(ls_pif, indent=4)

    with open(file, 'w') as outfile:
        pif.dump(pif_json, outfile)

    exit()


if __name__ == '__main__':
    main()
