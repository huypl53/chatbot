import logging
from rasa.core.agent import Agent
from rasa.core.policies.ted_policy import TEDPolicy
from rasa.core.policies.fallback import FallbackPolicy
from rasa.core.policies.memoization import MemoizationPolicy
import asyncio
import sys

def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models/dialogue'):
    logging.basicConfig(level='INFO')
    fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)

    agent = Agent(domain_file,
              policies=[MemoizationPolicy(max_history=1),TEDPolicy(), fallback])
    loop = asyncio.get_event_loop()

    training_data = loop.run_until_complete(agent.load_data(dialog_training_data_file))
    agent.train(
        training_data,
        augmentation_factor=50,
        validation_split=0.2)
    agent.persist(path_to_model)

# Train
#--------
if __name__ == "__main__":
    stories = str(sys.argv[1])
    domain = str(sys.argv[2])
    try:
        if stories and domain:
            train_dialog(stories, domain)
        else:
            train_dialog('./data/stories.md', './data/domain.yml')
    except Exception as e:
        print(f"Training failed! {e} ")
        exit()
