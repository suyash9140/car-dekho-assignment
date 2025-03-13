import pandas as pd
import gradio as gr

df = None  # Global dataframe to hold CSV data

def upload_csv(file):
    global df
    if file is None:
        return "Please upload a CSV file.", gr.update(choices=[]), gr.update(choices=[])

    try:
        df = pd.read_csv(file.name)
        columns = list(df.columns)
        return df.head(), gr.update(choices=columns), gr.update(choices=columns)
    except Exception as e:
        return f"Error reading file: {e}", gr.update(choices=[]), gr.update(choices=[])

def get_dataframe():
    return df

