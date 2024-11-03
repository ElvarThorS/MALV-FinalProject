# MALV-FinalProject
This is the description for the Final Project for the course T-725-MALV in Reykjavík University<br>
<br>
**Project Members:**
- Elvar Þór Sævarsson (elvars20@ru.is)
- Sirus Palsson (sirus24@ru.is)

## Goals
Data-driven methods to study history are limited due to the lack of validated quantitative time series data that "define" history. The data of history is almost entirely comprised of text-based, qualitative data. Therefore, we aim to develop a neural network-based methodology to study the sequence of events in history, in an attempt to quantify events and create an easily interpretable "line graph of history".

Many challenges need to be addressed to develop this methodology. To name a few:
1. A Named-Entity Recognition (NER) task to identify what is an event and what is not. 
2. The "quantification" of events in order to determine the importance or relevance of events over time.
3. An event type detection to ensure that events that are being linked together share a common topical relevance.

## Approach/Methodology:
Use a pre-trained bidirectional model (BERT) and fine-tune on historical articles from the Wikipedia corpus. Given that Wikipedia is availabe in multiple languages, the approach will be to create a methodology that works with Modern English, and a transfer learning exercise to other languages would be feasible task in the future. The highly-structured nature of the Wikipedia corpus will allow us to implement several NLP tasks with minimal data processing, including:
- Entity-linking
- Span Labelling
- Named Entity Recognition
- Information Retrieval
- Classification with feature extraction and self-supervised learning

## Benefits
- A general increase in historical knowlegdge for society
- Knowledge gained benefits entities engaged in long-term planning based on the anticiaption of historical events "repeating"


## Status
November 3, 2024: 
- Go with structured Wikipedia, contains more features from which we can feature extraction
- Created some (bad) code that extracts some features from the dataset (incomplete, needs to loop overall sections of 'sections' and needs to be modularized with functions)


## Related Material
**Hugging Face Libraries** <br>
Datasets (PyPi):https://pypi.org/project/datasets/ <br>
Datasets (Hugging Face): https://huggingface.co/docs/datasets/en/index <br>
Transformers (PyPi): https://pypi.org/project/transformers/ <br>
Transformers (Hugging Face): https://huggingface.co/docs/transformers/en/index <br>
**BERT Transformer** <br>
BERT pre-trained model on Huggingface: https://huggingface.co/google-bert/bert-base-cased <br>
Other pre-trained models on Huggingface: https://huggingface.co/transformers/v3.3.1/pretrained_models.html <br>
Huggingface documentation on using BERT models: https://huggingface.co/docs/transformers/model_doc/bert <br>
Original BERT paper: https://arxiv.org/abs/1810.04805 <br>
BERT Github: https://github.com/google-research/bert <br>
**Wikipedia Corpus**<br>
Structured Wikipedia Corpus: https://huggingface.co/datasets/wikimedia/structured-wikipedia <br>
Unstructured Wikipedia Corpus: https://huggingface.co/datasets/wikimedia/wikipedia <br>
History Category Outline: https://en.wikipedia.org/wiki/Category:History <br>
Outline of War: https://en.wikipedia.org/wiki/Outline_of_war <br>
**Entity Linking**<br> 
**Span Labeling** <br>

## ChatGPT Prompts
Can you write Python code for me that fine-tunes bert-base-cased using the transformers library on the wikimedia/structured-wikipedia using the datasets library? <br>
Can you change the above code for multi-class classification and include early stopping?

How to Stream datasets from Hugging face (from https://huggingface.co/datasets/not-lain/wikipedia-small-3000-embedded): <br>

```python
from datasets import load_dataset, Dataset
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

# load dataset in streaming mode (no download and it's fast)
dataset = load_dataset(
    "wikimedia/wikipedia", "20231101.en", split="train", streaming=True
)

# select 3000 samples
from tqdm import tqdm
data = Dataset.from_dict({})
for i, entry in enumerate(dataset):
    # each entry has the following columns
    # ['id', 'url', 'title', 'text']
    data = data.add_item(entry)
    if i == 3000:
        break
# free memory
del dataset

# embed the dataset
def embed(row):
  return {"embedding" : model.encode(row["text"])}
data = data.map(embed)

# push to hub
data.push_to_hub("not-lain/wikipedia-small-3000-embedded")
```

