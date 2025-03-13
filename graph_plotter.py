import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from PIL import Image
from csv_handler import get_dataframe

def plot_graph(x_column, y_column, graph_type):
    df = get_dataframe()
    if df is None:
        return "Please upload a CSV file.", None

    if x_column not in df.columns or y_column not in df.columns:
        return "Invalid column names.", None

    try:
        plt.figure(figsize=(8, 5))
        sns.set_style("whitegrid")

        if graph_type == 'Line':
            sns.lineplot(x=x_column, y=y_column, data=df)
        elif graph_type == 'Bar':
            sns.barplot(x=x_column, y=y_column, data=df)
        elif graph_type == 'Scatter':
            sns.scatterplot(x=x_column, y=y_column, data=df)
        else:
            return "Unsupported graph type.", None

        plt.title(f"{graph_type} Plot of {x_column} vs {y_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)

        # Save plot to a bytes buffer
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # Convert to a mutable PIL Image
        img = Image.open(buf).copy()

        plt.close()

        return None, img  # Return mutable PIL image

    except Exception as e:
        return f"Error generating graph: {e}", None
