# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import mwparserfromhell



def make_usable():
    """
    tr - s
    '[[:punct:][:space:]]' '\n' < dewiki - 20190620 - pages - articles - multistream.xml > dewiki_clean.txt
    split - b
    1000
    m
    dewiki_clean.txt
    small - chunk
    for X in small - chunk *; do sort < $X > sorted-$X; done

    for X in sorted - small - chunk *; do uniq -c < $X | sort -nr > count-$X; done
    """
    pass

def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    data_processed_dir= project_dir.joinpath("data", "processed")
    data_raw_dir = project_dir.joinpath("data", "raw")
    raw_file = data_raw_dir.joinpath("dewiki-20190620-pages-articles-multistream.xml")
    processed_file = data_processed_dir.joinpath("dewiki-lines.csv")
    processed_file = open(processed_file, "w")
    print(data_raw_dir)
    from xml.etree import ElementTree as et
    f = open(raw_file)
    for event, element in et.iterparse(f):
        if element.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
            element_text = mwparserfromhell.parse(element.text).filter_text()
            element_text = "".join([t.value for t in element_text])
            processed_file.write(element_text + "\n")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
