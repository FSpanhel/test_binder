import os
import sys

from numpy.random import default_rng

assert len(sys.argv) == 2, "one argument required"
branch = sys.argv[1]
random_int = default_rng().integers(int(1e6))

branch_name = f"{branch}_{random_int}"

os.system(f"git branch {branch_name} && git checkout {branch_name}")
