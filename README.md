# MALV-FinalProject
This is the description for the Final Project for the course T-725-MALV in Reykjavík University
Project Members:
- Elvar Þór Sævarsson
- Sirus Palsson

## Goals
Data-driven methods to study history are limited due to the lack of validated quantitative time series data. The data on history almost is entirely comprised of text-based, qualitative data. Therefore, we aim to develop a neural network-based methodology to study the sequuence of events in history, in an attempt to create easily an interpretable "line graph of history".

A few challenges need to be addressed. To name a few:
1. A Named-entity Recognition task to identify what is an event and what is not. 
2. The "quantification" of events in order to determine the importance or relevance of events over time.
3. An event type detection to ensure that events that are being linked together chare a common topical relevance.

## Approach/Methodology:
Use a pre-trained bidirectional model (BERT) and fine-tuned on historical articles from the Wikipedia corpus. Given that wikipedia is availabe in multiple languages, the approach will be to create a methodology that works with Modern English, and a transfer learning exercise to other languages is feasible task in the future. The highly-structured nature of the Wikipedia corpus will allow us to implement several NLP tasks without much data processing, including:
- Entity-linking
- Span Labelling
- Named Entity Recognition
- Information Retrieval
- Classification with feature extraction and self-supervised learning

## Benefits
- A general increase in historical knowlegdge for society
- Knowledge gained benefits entities engaged in long-term planning based on the anticiaption of historical events "repeating"





## Related Material
**Entity Linking**<br>
**Wikipedia corpus**<br>
**Span Labeling** <br>
