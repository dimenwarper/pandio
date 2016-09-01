import pandas as pd
import numpy as np
import argparse
import sys

def print_help():
    print 'pandio COMMAND [FILE]'
    print 'Example:'
    print 'cut -f 1-10 data_frame.txt | pandio "log(df)"'

def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', default='df')
    parser.add_argument('--file', type=argparse.FileType('r'), default=None)
    parser.add_argument('--delimiter', type=str, default='\t')

    args = parser.parse_args()

    if args.file is None:
        args.file = sys.stdin
    return args

def execute():
    args = get_cli_arguments()
    df = pd.read_csv(args.file, sep=args.delimiter, index_col=0)
    res_df = pd.DataFrame()
    exec('res_df = ' + args.command)
    sys.stdout.write(res_df.to_csv(sep=args.delimiter))
