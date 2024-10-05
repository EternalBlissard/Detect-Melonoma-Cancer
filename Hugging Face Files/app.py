### Imports for Modules ### 
import gradio as gr
import os
import torch
from typing import Tuple, Dict
from timeit import default_timer as timer

### Functional Imports
from predictor import predictionMakerViT as predictionMaker

exampleList = [["examples/" + example] for example in os.listdir("examples")]

title = "Detect Melanoma Cancer"
description = "Trained a Vision Transformer to classify images of Based on [🔬Melanoma Cancer Image Dataset](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset)."


# Create the Gradio demo
demo = gr.Interface(fn=predictionMaker, 
                    inputs=[gr.Image(type="pil")], 
                    outputs=[gr.Label(num_top_classes=3, label="Predictions"),
                             gr.Number(label="Prediction time (s)")],
                    examples=exampleList, 
                    title=title,
                    description=description,)

# Launch the demo!
demo.launch()
# If you want to share then comment the above and uncomment the below one
# demo.launch(share=True) 




