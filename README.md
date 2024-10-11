# Streamlit CSV Analysis App

Welcome to the **Streamlit CSV Analysis App**! This application allows users to upload CSV files and ask questions about their data, utilizing a language model to generate insightful responses.

## Features

- Upload a CSV file and interact with the data.
- Ask questions about the uploaded CSV, such as total rows and columns, specific data queries, etc.
- Receive default responses for common questions like "Hi" and "Who are you".
- Chat interface for seamless interaction with the assistant.

# Output:
![image](https://github.com/user-attachments/assets/b9fabd94-5455-440f-9177-ff588a7102f8)


## Requirements

- Python 3.8 or higher
- Streamlit
- LangChain
- dotenv
- langchain_google_genai

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repository-name
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the root directory:
   ```plaintext
   # Example .env file content
   API_KEY=your_api_key_here
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and go to `http://localhost:8501`.
3. Upload your CSV file.
4. Interact with the assistant by typing your questions into the chat interface.

## Example Questions

- "Hi"
- "Who are you?"
- "How many total rows and columns are there?"

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Streamlit and LangChain communities for their amazing tools and resources.
```

### Customizing the README

- **Project Name**: Update the title if your project has a different name.
- **GitHub Link**: Replace `https://github.com/yourusername/repository-name.git` with your actual repository link.
- **Requirements**: Add any additional libraries or dependencies your project might need.
- **Example Questions**: Feel free to modify the list of example questions based on your application's functionality.

This README provides a clear overview of your project and its usage, making it easier for others (or yourself in the future) to understand and utilize the application. Let me know if you need any further customization or details!
