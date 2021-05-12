# %%
from rasa.shared.nlu.training_data.loading import load_data
from rasa.nlu.model import Trainer
from rasa.nlu import config
import sys

# %%
def train(data: str, config_file: str, model_dir: str):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory= trainer.persist(model_dir, fixed_model_name=model_dir)
    return model_directory

if __name__ == '__main__':
    data, config_file, model_dir = sys.argv[1:4]
    try:
        train(data, config_file, model_dir)
    except Exception as e:
        print("Train error: {}".format(e))
        pass
