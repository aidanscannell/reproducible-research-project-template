# Academic Project Template

## TODOs
- [] Add a link to longer example
- [] Add a short example
- [] Add paper citation

### Example
See INSERT LINK for how to use our method in detail.

A short example:
```python
import torch
import src.train

```

### Reproducing experiments
All [experiments/](./configs/experiment) use the base hydra config in [experiments/configs/main.yaml](experiments/configs/main.yaml).
Each experiment then overrides specific parts of the config which are detailed in their experiment override configs in [experiments/](experiments/configs/experiment).

You can display the base config using:
``` shell
python train.py --cfg=job
```
An experiment's config can be viewed with:
``` shell
python train.py +experiment=INSERT_EXPERIMENT_NAME --cfg=job
```


To reproduce the experiments of the paper can be found in the [`experiments` folder](./experiments). Check the folder for details.
```sh
python train.py 
```

### Build PDF
The paper can be built using our `Makefile`:
```sh
make paper
```
This should automatically build the figures if they do not exist. 
Alternately, make the figures with:
```sh
make figures
```

### Citation
```bibtex
@article{XXX,
    title={{F}ast {U}pdates for {M}odel-based {R}einforcement {Learning}
    author={Scannell, Aidan},
    journal={Advances in Neural Information Processing Systems},
    year={2023}
}
```
