#!/usr/bin/env python3
import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib

def plot_figures(save_dir: str="../figures", random_seed: int=42):
    # Fix random seed for reproducibility
    np.random.seed(random_seed)

    x = np.linspace(0,1,10)
    y = np.sin(x)

    plt.plot(x, y)

    tikzplotlib.save(os.path.join(save_dir,"example_fig.tex"),
                     axis_width='\\figurewidth',
                     axis_height='\\figureheight')
    plt.savefig(os.path.join(save_dir, "example_fig.pdf"), transparent=True)

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save_dir",
        help="directory to save figures",
        default="../figures",
    )
    parser.add_argument(
        "--random_seed",
        type=int,
        help="fix random seed for reproducibility",
        default=42,
    )
    args = parser.parse_args()

    plot_figures(save_dir=args.save_dir, random_seed=args.random_seed)
