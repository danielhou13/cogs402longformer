# cogs402longformer





## Data Processing

Theresearch papers dataset in its raw form can be found in the data folder of the repository. It is formatted as both its respective .RAR files as well as folders containing the extracted data. The file `src/datasetcreate` converts both folders into a csv file. The csv file can be found [here](https://huggingface.co/datasets/danielhou13/cogs402dataset) and is already split into a training set and a testing set with a 0.8/0.2 ratio respectively.

The news dataset can be found [here](https://huggingface.co/datasets/hyperpartisan_news_detection) and can be directed imported using the huggingface datasets function `load_dataset`.

## Model Training

The code used the train the models can be found in the src folder under `longformer_news` and `longformer_research_papers`, indicating what task each model was finetuned for. Both models, once trained, were published to the huggingface website and can be found [here](https://huggingface.co/danielhou13).


## Model Visualizations

The visualizations for the model can be found in the `src/Captum...` files.  
