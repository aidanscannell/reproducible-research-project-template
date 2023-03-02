#!/usr/bin/env python3
import logging


logging.basicConfig(level=logging.INFO)

import hydra
import matplotlib.pyplot as plt
import numpy as np
import omegaconf
import wandb


logger = logging.getLogger(__name__)


@hydra.main(config_path="../configs", config_name="main")
def train(cfg: omegaconf.DictConfig):
    # Make experiment reproducible
    # set_random_seed(cfg.random_seed) # TODO implement function to set random seed

    if cfg.wandb.use_wandb:
        # Initialise WandB
        run = wandb.init(
            project="INSET-PROJECT-NAME",  # TODO insert project name
            group=cfg.wandb.group,
            tags=cfg.wandb.tags,
            name=cfg.wandb.run_name,
            config=omegaconf.OmegaConf.to_container(
                cfg, resolve=True, throw_on_missing=True
            ),
        )

    logger.info("Instantiating model")
    model = hydra.utils.instantiate(cfg.model)
    model()
    logger.info("Successfully instantiated model")

    # We can log metrics to WandB
    for iteration in range(0, 2):
        loss = iteration * 2
        wandb.log(
            {
                "Iteration": iteration,
                "Training loss": loss,
            }
        )

    # We can log images to WandB
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(np.array([0, 1, 2]), np.array([0, 1, 2]))
    wandb.log({"An image": wandb.Image(fig)})


if __name__ == "__main__":
    train()  # pyright: ignore
