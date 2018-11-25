from parser import input_parser
from runner import Runner
import argparse


parser = argparse.ArgumentParser(
    description="Python module to run experiments using METCO")
parser.add_argument("file", help="Input file in JSON format with the experiment configuration")
args = parser.parse_args()
exps = input_parser(args.file)
runner = Runner(exps)
runner.run_all()
