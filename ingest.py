from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Load PDF
loader = PyPDFLoader("./Data/Resume.pdf")
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in vector database
vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# Save vector database locally
vectorstore.save_local("faiss_index")

print("FAISS index created successfully!")