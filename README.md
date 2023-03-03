# Template for Reproducible ML Research Paper
This repository contains a basic template for making a reproducible research paper.
Running `make all` in the top level directory should:
1. make a python virtual environment and install dependencies in `requirements.txt`
2. (optional) run all experiments
3. make figures for paper (as `.tex` files straight from python)
4. make tables for paper (as `.tex` files straight from python)
4. build `main.pdf`

As running the experiments (step 2) can take a long time, it is often better to setup the experiments to run separately with:
```sh
make run
```
And perhaps this should be run on a cluster...
The figures/tables/paper (without running experiments) can then be made with:
```sh
make paper
```
All figures and tables can be reproduced with:
```sh
make media
```
This runs [./src/figures.py](./src/figures.py) and [./src/tables.py](./src/tables.py) which generates the figures and tables and puts them inside 
[./paper/figs](./paper/fig) and [./paper/tables](./paper/tables).

## Powerful tools in this template
These are some of my favourite tools. See the links for more information on how to use them.
1. Experiment configuration with [hydra](https://hydra.cc/),
    - Use it to [instantiate objects](https://hydra.cc/docs/advanced/instantiate_objects/overview/) from `yaml` configs.
    - Use it to easily sweep over parameters and random seeds.
    - Use it to deploy experiments in parallel on a cluster using [submitit](https://hydra.cc/docs/plugins/submitit_launcher/) and [multirun](https://hydra.cc/docs/intro/#multirun).
2. Experiment tracking with Weights & Biases,
    - Weights & Biases can log experiments running on a cluster so you can easily see them in your browser (with minimal set up).
3. Use [tikzplotlib](https://github.com/nschloe/tikzplotlib) to directly save figures in python as `.tex` files (instead of `pdf`/`png`) so that axis labels, titles and so on, are formatted using your LaTeX style,
    - You also get the added benefit that you can easily edit the `.tex` file if you want to make changes to your plot (e.g. axis lables).
    That is, you don't need to re run your python code.
    - Thanks to Arno Solin for showing me this!
4. Create LaTeX tables directly in python using [tabulate](https://github.com/astanin/python-tabulate) and save them as `.tex` files.
    - Now when you need to re run experiments you don't need to manually update tables in your main `LaTeX` file.
    - Agian, thanks to Arno Solin for showing me this!
5. GitHub action builds `main.pdf` from [`main.tex`](./paper/main.tex),
    - This doesn't run the code or make the figures, it just builds the pdf.

## Development
If you want to make changes to the code in [src/](.src/) you should install `pre-commit` with:
```sh
pre-commit install
```
pre-commit allows us to auto format all python/yaml files using `black` and `isort` when you commit files.
This avoids the issue of having file changes due to each collaborator having different formatting  settings.


## TODO before finishing project
- [ ] Update the short example
- [ ] Add a longer example (perhaps a jupyter notebook)
- [ ] Update paper citation
- [ ] Add details for running all experiments
- [ ] At end of project run `pip freeze > requirements.txt` to pin the projects dependencies

## Example
See INSERT LINK for how to use our method in detail.

A short example:
```python
# TODO update this
import torch

print("Hello world")
```

## Reproducing experiments
Note that [src/train.py](src/train.py) uses [Weights and Biases](https://wandb.ai/site) for tracking experiments.
All experiments use the base hydra config in [configs/main.yaml](configs/main.yaml).
Each experiment then overrides specific parts of the config which are detailed in their experiment override configs in [experiments/](configs/experiment/).

You can display the base config using:
``` shell
python train.py --cfg=job
```
Run an experiment with:
``` shell
python train.py +experiment=experiment_1
```
Ideally, all experiments can be run in paralell (on a cluster) with:
``` shell
python train.py  --multirun +experiment=glob(*)
```
Note that we can sweep over config value using hydra, for example, we can sweep over a set of random seeds with:
``` shell
python train.py --multirun ++random_seed=42,1,5,100
```
However, the best thing to do is to specify the sweeps directly in an experiment's config.
For example, we can we sweep over `models.AwesomeModel`'s `parameter` argument and it's `random_seed` with the [following config](./configs/experiment/sweep_over_models_parameter_and_seed.yaml):
``` yaml
# @package _global_
hydra:
  sweeper:
    params:
      mode.parameter: 1,2,3,4,5
      random_seed: 1,42,69,50,100
```


## Citation
```bibtex
@article{XXX,
    title={Insert awesome title,
    author={Scannell, Aidan},
    journal={Awesome venue},
    year={2023}
}
```
