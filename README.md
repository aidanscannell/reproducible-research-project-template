# Reproducible Academic Research Project Template


## Using this template
### Reproducing figures
All figures and tables can be reproduced by running:
```sh
make
```
This creates a python virtual environment and installs the dependencies in `requirements.txt`.
It then runs [./src/figures.py](./src/figures.py) and [./src/tables.py](./src/tables.py) which generates the figures and tables and puts them inside 
[./paper/fig](./paper/fig) and [./paper/tables](./paper/tables).

### Development
To develop the project pre-commit must be installed with:
```sh
pre-commit install
```
pre-commit will now auto format all python/yaml files using `black` and `isort` when you commit files.

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

### Build PDF
The paper can be built using the `Makefile` in the [paper/](./paper/) directory.
```sh
make paper
```
This should automatically build the figures if they do not exist. 
Alternately, make the figures with:
```sh
make figures
```

## Things to put in final README
### Project TODOs
- [] Add a link to longer example
- [] Update a short example
- [] Update paper citation

### Example
See INSERT LINK for how to use our method in detail.

A short example:
```python
# TODO update this
import torch

print("Hello world")
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
