import os
import random

import numpy as np

from tqdm import tqdm

import persia

from persia.prelude import PyPersiaBatchData
from persia.logger import get_logger
from persia.ctx import BaseCtx
from persia.utils import setup_seed
from data_generator import make_dataloader

logger = get_logger("data_compose")

setup_seed(3)

train_filepath = os.path.join("/data/", "train.npz")

logger.info("init py client done...")
if __name__ == "__main__":
    with BaseCtx() as ctx:
        _, loader = make_dataloader(train_filepath)
        for (dense, batch_sparse_ids, target) in tqdm(loader, desc="gen batch data..."):
            batch_data = PyPersiaBatchData()
            batch_data.add_dense([dense])
            batch_data.add_sparse(batch_sparse_ids)
            batch_data.add_target(target)
            ctx.backend.send_data(batch_data)