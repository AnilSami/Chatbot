from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Page title
st.set_page_config(page_title="RAG Chatbot")

st.title("AI Resume Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
query = st.chat_input("Ask a question about the resume")

if query:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    # Load embeddings
    embeddings = OpenAIEmbeddings()

    # Load vector database
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retriever
    retriever = vectorstore.as_retriever()

    # Search relevant docs
    docs = retriever.invoke(query)

    # Combine context
    context = "\n\n".join([
        doc.page_content for doc in docs
    ])

    # Prompt
    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY from the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    # LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    # Generate response
    response = llm.invoke(prompt)

    answer = response.content

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)