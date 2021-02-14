import functools
import math
import torch
import torch.nn as nn
import pytorch_quantum as tq
import numpy as np

from string import ascii_lowercase

C_DTYPE = torch.complex64
F_DTYPE = torch.float32

ABC = ascii_lowercase
ABC_ARRAY = np.array(list(ABC))

INV_SQRT2 = 1 / math.sqrt(2)

