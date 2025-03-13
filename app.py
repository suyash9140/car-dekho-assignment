import gradio as gr
from csv_handler import upload_csv
from llm_agent import answer_question
from graph_plotter import plot_graph

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# 📊 CSV Question Answering and Visualization App")

    with gr.Row():
        csv_input = gr.File(label="📂 Upload CSV File", type="filepath")
        csv_output = gr.Dataframe()
        x_column = gr.Dropdown(label="X-Axis Column", allow_custom_value=True)
        y_column = gr.Dropdown(label="Y-Axis Column", allow_custom_value=True)


    csv_input.change(upload_csv, inputs=csv_input, outputs=[csv_output, x_column, y_column])

    with gr.Row():
        question_input = gr.Textbox(label="💬 Ask a question")
        answer_output = gr.Textbox(label="✅ Answer")

    question_input.submit(answer_question, inputs=[question_input], outputs=[answer_output])

    with gr.Row():
        graph_type = gr.Dropdown(label="Graph Type", choices=["Line", "Bar", "Scatter"])
        plot_output = gr.Image(type="pil")

    plot_button = gr.Button("📈 Plot Graph")
    
    plot_button.click(plot_graph, inputs=[x_column, y_column, graph_type], outputs=[answer_output, plot_output])


if __name__ == "__main__":
    app.launch()
