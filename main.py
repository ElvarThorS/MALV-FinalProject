from datasets import load_dataset, Dataset, load_dataset_builder, get_dataset_split_names
import pandas as pd

# Load the dataset
dataset = load_dataset(
    "wikimedia/structured-wikipedia", "20240916.en", split="train", streaming=True)

# Define rules to fiter out event articles
def keyword_based_rules(article):
    events = []
    keywords = ["Battle of", "War of", "Assassination of", "established", "founded", "discovered"]
    for keyword in keywords:
        if keyword in article['title'] or keyword in article['text']:
            # Extract surrounding text or related entity
            if keyword in ["Battle of", "War of", "Assassination of"]:
                event_text = article['text'].split(keyword)[1].split('.')[0]
                events.append({'Event': event_text, 'Type': 'Conflict'})
            elif keyword in ["established", "founded", "discovered"]:
                entity = article['text'].split(keyword)[1].split('.')[0]
                events.append({'Event': entity, 'Type': 'Founding'})
    return events

# Filter the dataset to create a subset of articles
subset = dataset.filter(
    keyword_based_rules()
)
