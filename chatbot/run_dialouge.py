# %%
# from os import times
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig
from rasa.core import run
from rasa.core.utils import read_endpoints_from_path
from rasa.core.agent import Agent
import asyncio
import sys
# %%
def run_dialouge(endpoint_cfg: str, model: str):
    endpoint_config = read_endpoints_from_path('./endpoints_custom.yml')

    run.serve_application("./models/dialogue/rasa-model-05-05.tar.gz", endpoints=endpoint_config,channel='rest', port=4096, log_file='last.log' )
# %%
if __name__ == '__main__':
    endpoint_cfg, model = sys.argv[1], sys.argv[2]
    try:
        if endpoint_cfg and model:
            run_dialouge(endpoint_cfg, model)
        else:
            run_dialouge('./endpoints_custom.yml', "./models/dialogue/rasa-model-05-05.tar.gz" )
    except Exception as e:
        print(f"Run dialouge failed!, {e}")
        exit()


import os
os.path.join('./data',' '  )
