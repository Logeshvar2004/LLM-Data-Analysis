import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Custom CSS to fix the input box at the bottom, style it, and align the title at the top
st.markdown("""
    <style>
    .stTextInput {
        position: fixed;
        bottom: 20px; /* Add some space from the bottom */
        left: 50%; /* Center the input */
        transform: translateX(-50%); /* Adjust for centering */
        width: 70%; /* Set a width for the input box */
        max-width: 600px; /* Max width for larger screens */
    }
    .chat-history {
        max-height: 70vh; /* Limit height of the chat history */
        overflow-y: auto; /* Enable scrolling for long chats */
        padding-bottom: 80px; /* Give space for the input box */
    }
    h1 {
        text-align: center; /* Center the title */
        margin-top: 1px; /* Add some space above the title */
        margin-bottom : 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title aligned to the top
st.title("Data analysis Made easier...!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'query' not in st.session_state:
    st.session_state['query'] = ""  # Initialize query

# CSV file uploader without label
uploaded_file = st.file_uploader("", type=["csv"])

if uploaded_file is not None:
    try:
        # Use Langchain's create_csv_agent to load and process the CSV
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, max_tokens=None, timeout=None)

        # Create the CSV agent and allow dangerous code execution (opt-in)
        agent = create_csv_agent(llm, uploaded_file, verbose=True, allow_dangerous_code=True)

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask a question about the CSV file:"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Process the user query with the CSV agent
            response = agent.run(prompt)

            # Display the assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)  # Display the entire response at once
                time.sleep(0.05)  # Simulate a slight delay for better UX

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Display the chat history without header
        with st.container():
            st.markdown('<div class="chat-history">', unsafe_allow_html=True)
            if st.session_state['history']:
                for idx, (q, a) in enumerate(st.session_state['history']):
                    st.markdown(f"**Q{idx+1}:** {q}")
                    st.markdown(f"**A{idx+1}:** {a}")
            st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error processing the uploaded CSV file: {e}")
