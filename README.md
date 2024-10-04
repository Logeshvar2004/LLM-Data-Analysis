# LLM-Data-Analysis
A LLM Specifically developed for data analysis using RAG.

This project demonstrates a language model-based question-answering system that utilizes the **Gemini API** to process CSV data, retrieve relevant information, and answer queries. The system is built using the **LangChain** framework, enabling seamless document loading, embedding generation, and retrieval-based question answering.

## Features

- **CSV Data Processing**: Load and process CSV files, making the data available for querying.
- **Gemini API Integration**: Leverage the Gemini API for both language model generation and embedding queries.
- **Vector Store for Efficient Retrieval**: Uses **FAISS** for indexing document embeddings and retrieving relevant context efficiently.
- **Flexible Querying**: Provides answers to natural language questions based on the provided CSV data.

## Project Structure

- `main.py`: The core script to run the question-answering system.
- `.env`: Environment variables file for securely storing API keys.
- `data/`: Directory for CSV files that are loaded and processed by the system.
- `requirements.txt`: Lists the required Python libraries for the project.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/gemini-qa-system.git
   cd gemini-qa-system
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: .\env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file in the root directory with your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Place your CSV file in the `data/` directory.

## Usage

1. Run the `main.py` script:

   ```bash
   streamlit run main.py
   ```

2. The system will load the CSV data and initialize the Gemini API-based question-answering pipeline. You can input natural language questions, and the system will respond with concise answers based on the data.

## Example

Given a CSV file `customers-100.csv`, you can ask:

```text
Which company does Sheryl Baxter work for?
```

The system will retrieve relevant context from the CSV and provide an answer like:

```text
Sheryl Baxter works for ABC Corporation.
```

## Dependencies

- Python 3.x
- LangChain
- FAISS
- pandas
- dotenv
- requests
