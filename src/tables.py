#!/usr/bin/env python3
import argparse
import os

import numpy as np
from tabulate import tabulate

def make_tables(save_dir: str="../tables", random_seed: int=42):
    # Fix random seed for reproducibility
    np.random.seed(random_seed)

    table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
            ["Moon",1737,73.5],["Mars",3390,641.85]]
    headers = ["Planet","R (km)", "mass (x 10^29 kg)"]


    table = tabulate(table, headers=headers, tablefmt="latex")

    save_file = os.path.join(save_dir, "example_table.tex")
    with open(save_file, 'w') as file:
        file.write(table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save_dir",
        help="directory to save tables",
        default="../tables",
    )
    parser.add_argument(
        "--random_seed",
        type=int,
        help="fix random seed for reproducibility",
        default=42,
    )
    args = parser.parse_args()

    make_tables(save_dir=args.save_dir, random_seed=args.random_seed)
