from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import cohere
from langchain.llms import Cohere

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medicalchatbot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

llm = Cohere(temperature=0.4, max_tokens=500)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Initialize conversation history
conversation_history = []  # List to store the conversation history

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    global conversation_history  # Declare to use the global variable
    msg = request.form["msg"]
    input_message = msg
    print("Input Message:", input_message)  # Log the input message

    # Append the user's message to the conversation history
    conversation_history.append(f"User: {input_message}")

    # Combine the conversation history into the input for the model
    combined_input = "\n".join(conversation_history) + "\nAssistant:"

    try:
        response = rag_chain.invoke({"input": combined_input})
        answer = response.get("answer", "No answer provided.")
        print("Response:", answer)  # Log the response

        # Append the assistant's answer to the conversation history
        conversation_history.append(f"Assistant: {answer}")

        return str(answer)
    except Exception as e:
        print("Error during API call:", str(e))  # Log the error
        return "An error occurred while processing your request.", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
