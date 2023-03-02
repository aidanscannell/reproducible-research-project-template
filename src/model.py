#!/usr/bin/env python3


class AwesomeModel:
    def __init__(self, message: str, parameter: float, random_seed: int):
        self.message = message
        self.parameter = parameter
        self.random_seed = random_seed

    def __call__(self):
        print(self.message)
        print("parameter={}".format(self.parameter))
        print("random_seed={}".format(self.random_seed))
