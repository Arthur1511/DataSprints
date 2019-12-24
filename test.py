import pandas as pd
import plotly.offline as ply
import numpy as np


data = pd.read_json("data-sample_data-nyctaxi-trips-2009-json_corrigido.json", lines=True)
data.
    max_of_two = data[data.passenger_count <3]

