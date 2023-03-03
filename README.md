# Reproducible Academic Research Project Template
This repository contains a basic template for making a reproducible research paper.
Running `make all` in the top level directory should:
1. make a python virtual environment and install dependencies in `requirements.txt`
2. (optional) run all experiments
3. make figures for paper (as `.tex` files straight from python)
4. make tables for paper (as `.tex` files straight from python)
4. build the `paper.pdf`

As running the experiments (step 2) can take a long time, it is often better to setup the experiments to run separately with `make run`.
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


### Development
If you want to make changes to the code in [src/](.src/) you should install `pre-commit` with:
```sh
pre-commit install
```
pre-commit allows us to auto format all python/yaml files using `black` and `isort` when you commit files.
This avoids the issue of having file changes due to each collaborator having different formatting  settings.


### TODO before finishing project
- [] Update the short example
- [] Add a longer example
- [] Update paper citation
- [] Add details for running all experiments
- [] At end of project run `pip freeze > requirements.txt` to pin the projects dependencies

### Example
See INSERT LINK for how to use our method in detail.

A short example:
```python
# TODO update this
import torch

print("Hello world")
```

### Reproducing experiments
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
Sweep over a set of random seeds with:
``` shell
python train.py --multirun ++random_seed=42,1,5,100
```



### Citation
```bibtex
@article{XXX,
    title={Insert awesome title,
    author={Scannell, Aidan},
    journal={Advances in Neural Information Processing Systems},
    year={2023}
}
```
