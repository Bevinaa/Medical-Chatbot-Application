# **End-to-End Medical Chatbot Application**

## **Overview**

This repository contains an **End-to-End Medical Chatbot** powered by **Generative AI**, designed to provide accurate and contextually relevant responses to medical queries. Built using **Flask**, **Cohere’s Language Model**, and **Pinecone** for vector storage, this chatbot can answer a wide range of health-related questions and offer context-aware follow-ups. The chatbot remembers previous queries to offer more personalized responses.

---

## **Key Features**

- **Generative AI-Powered Responses**: Uses **Cohere’s Language Model** to generate medical answers.
- **Context-Aware Conversations**: The chatbot can maintain the context of the conversation, enabling more accurate follow-up answers.
- **Efficient Document Retrieval**: Integrated with **Pinecone**, a vector database, for fast and scalable document search.
- **Flask Web Application**: A user-friendly web interface powered by Flask for seamless interaction.
- **Easy Setup**: Simple installation steps and easy API key configuration for deployment.

---

## **Technologies Used**

- **Flask**: Web framework for building the backend.
- **Cohere**: Language model for generating answers.
- **Pinecone**: Vector database for document retrieval and storage.
- **HTML/CSS/Bootstrap**: Frontend for the chat interface.
- **Python**: Programming language for implementing AI logic and web server.

---

## **Pre-requisites**

To get started with the project, you’ll need the following:

- **Python 3.7+** (preferably in a virtual environment)
- **Cohere API Key**: For generating AI responses.
- **Pinecone API Key**: For vector search and document retrieval.
- **Flask**: To run the web application.

---

## **Setting Up the Project**

Follow the steps below to set up and run the chatbot on your local machine:

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone (https://github.com/Bevinaa/Medical-Chatbot-Application)
cd End-to-end-Medical-Chatbot-Generative-AI
```

### 2. Set Up a Virtual Environment (Recommended)

You can set up a virtual environment to isolate dependencies for this project:
"venv" is used here as environment name

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Create API Keys

You will need two API keys: **Cohere API Key** for the language model and **Pinecone API Key** for vector storage. Here's how to get them:

#### Cohere API Key:
1. Go to [Cohere API](https://cohere.ai/) and create an account if you haven’t already.
2. Once logged in, navigate to the **API Keys** section and generate a new API key.
3. Copy the API key for use in the project.

#### Pinecone API Key:
1. Visit [Pinecone](https://www.pinecone.io/) and create an account.
2. After logging in, navigate to **API Keys** from your dashboard.
3. Generate an API key and copy it.

### 5. Configure API Keys

Create a `.env` file in the root directory of the project and add the following lines, replacing the placeholders with your actual API keys:

```env
COHERE_API_KEY=your_cohere_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 6. Running the Flask Application

Once you've set up the environment and configured the API keys, you can run the Flask app with the following command:

```bash
python app.py
```

The chatbot should now be running at `http://127.0.0.1:5000/`. Open this URL in your browser to interact with the chatbot.

---

## **How to Use the Chatbot**

1. Visit the main page (`/`).
2. You’ll see a user interface where you can type your health-related question.
3. After submitting your question, the chatbot will generate a response based on the medical documents it retrieves from Pinecone.

You can ask follow-up questions, and the chatbot will maintain the context of your conversation to provide more relevant answers.

---

## **Project Structure**

- **app.py**: Main Python script that runs the Flask application.
- **chat.html**: HTML template for the chatbot user interface.
- **requirements.txt**: List of Python dependencies for the project.
- **src/**: Contains helper functions and code for document embedding and retrieval.
- **.env**: Configuration file to store sensitive API keys.
  
---

## **Contributing**

If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. 

Make sure to follow the standard guidelines for Python projects and ensure that all dependencies are correctly listed in the `requirements.txt` file.

---

## **Contact**

For any questions, issues, or support, feel free to reach out:

**Bevina**  
Email: [bevina2110@gmail.com](mailto:bevina2110@gmail.com)

---
