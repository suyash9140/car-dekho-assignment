import ollama
from pydantic_ai import Agent

from csv_handler import get_dataframe

class CSVQueryModel(Agent):
    def __init__(self, question, csv_data, **kwargs):
        super().__init__(**kwargs)
        self.question = question
        self.csv_data = csv_data

    def execute(self) -> str:
        prompt = f"""
        You are an AI that answers questions based on CSV data.
        CSV Data:
        {self.csv_data[:1000]}  

        Question:
        {self.question}
        """
        try:
            response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
            return response['message']['content']
        except Exception as e:
            return f"Error processing query: {e}"

def answer_question(question):
    df = get_dataframe()
    if df is None:
        return "Please upload a CSV file."
    if not question:
        return "Please enter a question."

    try:
        csv_data = df.to_csv(index=False)[:5000]  
        model = CSVQueryModel(question=question, csv_data=csv_data)
        return model.execute()
    except Exception as e:
        return f"Error processing query: {e}"
