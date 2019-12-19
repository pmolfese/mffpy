"""
This script is used to export the contents of segmented MFF files into a JSON format using mffpy.
It will convert either a single MFF file, or a directory of MFF files.

@author: Damian Persico - persicodamian@gmail.com
@author: Wayne Manselle - wayne.manselle@belco.tech

Copyright 2019 Brain Electrophysiology Laboratory Company LLC

Licensed under the ApacheLicense, Version 2.0(the "License");
you may not use this module except in compliance with the License.
You may obtain a copy of the License at:

http: // www.apache.org / licenses / LICENSE - 2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
ANY KIND, either express or implied.
"""
from os.path import splitext, sep
from mffpy import Reader, Writer
from argparse import ArgumentParser

import glob


def mff2json(input_path):
    """
    This function undertakes the work of effectuating the conversions of a passed MFF file, or set of MFF files into
    a JSON format.

    These JSON formatted conversions will be saved in the same directory as the MFF(s) converted.
    :param input_path: A string describing a path to a specific MFF, or a collection of them.
    :return:
    """

    file_list = []

    if '.mff' in input_path:
        file_list = [input_path]
    else:
        file_list = glob.glob(''.join([input_path, '*.mff']))

    print(file_list)

    for file in file_list:
        # Check .mff input
        dir_and_base, ext = splitext(file.rstrip(sep))
        # assert ext.lower() == '.mff', f"{input_path} is not a valid .mff directory"
        output_filename = dir_and_base + '.json'

        # Read data from an MFF file
        reader = Reader(file)
        print("Reading data from " + str(file))
        data = reader.get_mff_content()

        # Write data into a JSON file
        writer = Writer(output_filename)
        print("Writing data out to " + str(output_filename))
        writer.export_to_json(data)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--mff_file", type=str, help="Path to an MFF File, or Collection of MFF Files")
    mff2json(parser.parse_args().mff_file)
