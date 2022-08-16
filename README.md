# Cogs402longformer

This is the repository for COGS402 S2022 project. While you can clone this on to your own machine, there is a high GPU memory cost because of the requirements for the Longformer. The work for this project is primarily done on google colab, and the repository can also be found here for you to "clone": https://drive.google.com/drive/folders/1T0bmf2eqGK63pjqNtV25vIPsN9OcPZiS?usp=sharing. 

## Data Processing

The research papers dataset in its raw form can be found in the data folder of the repository. It is formatted as both its respective .RAR files as well as folders containing the extracted data. The file `src/datasetcreate` converts both folders into a csv file. The csv file can be found [here](https://huggingface.co/datasets/danielhou13/cogs402dataset) and is already split into a training set and a testing set with a 0.8/0.2 ratio respectively.

The news dataset can be found [here](https://huggingface.co/datasets/hyperpartisan_news_detection) and can be directed imported using the huggingface datasets function `load_dataset`.

## Model Training

The code used to the train the models can be found wihtin the `src/training_notebooks` folder in the`longformer_news` and `longformer_research_papers` notebooks, indicating what task each model was finetuned for. Both models, once trained, were published to the huggingface website and can be found [here](https://huggingface.co/danielhou13).

## Model Visualizations and Interpretations

At the top of each notebook will be more information about the visualizations used.

### Attributions
The attribution visualizations for the model can be found in the `src/Attributions...` files. We visualize the attributions in two ways. The first is to use an overlay for the attributions scores by mapping the attribution score into a colour that increases in saturation the larger the score. The second method is to create a few dataframes which sort the attribution scores from largest to smallest.

### Attentions
The attention visualization notebooks for the model can be found in the folder `src/`, highlighted by the term "attention" or "attn" on the notebook names. We create 2d heatmaps for all layers and heads of an example example, or we can use T3-vis to get the aggregate attentions over all examples in the dataset. We visualize the 2d heatmap in `src/example_attn_plot.ipynb` and the aggregate in `src/T3-vis/visualize_aggregate_attn.ipynb`

We examine each token's most attended and attending tokens and the most attended tokens in the example for different attention layers and heads in the notebook `src/token_attention_with_head_importance.ipynb`. The notebook `src/token_attention_with_head_importance_pdf.ipynb` serves only to quickly create the attention overlay using the summed attention for each token. Similar to the attribution overlay, we convert each attention weight into a colour where the larger the attention weight, the stronger the saturation.

### Comparing Attention and Attributions

`Attention_attribution_similarities.ipynb` and `Attn_attr_sim_means.ipynb` compares summed attention weights with attribution scores. `Attn_attr_sim_means.ipynb` looks at the mean over a dataset while `Attention_attribution_similarities.ipynb` takes an in-depth look at one example.

## Adjustments for T3-vis

A portion of this project involves an adjustment and usage of some functions found in the [T3-vis](https://github.com/raymondzmc/T3-Vis) implementation. 

Modifications to T3-vis for longformer use can be found in the folder `src/T3-vis/`. This mainly includes the code to find the aggregate attention of the model across a specific testing set. 

To learn more about T3-vis, I recommend reading their [paper](https://arxiv.org/abs/2108.13587)

## Fake Clinical Notes

Our notebooks for the clinical notes dataset is in the folder `fakeclinicalnotes`. All notebooks for visualizations are in the folder `src/cogs402projecttestnotes` and the files to be used with T3-vis is in `t3-visapplication`.
