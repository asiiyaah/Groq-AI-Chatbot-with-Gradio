# 🤖 Groq AI Chatbot with Gradio

An interactive, streaming chat application built using Python, **Gradio**, and the **Groq API**. This chatbot features real-time text generation (token streaming) and dynamic parameter configurations.

## 📊 Application Interface

### 1️⃣ Default Setup (Chatbot View)
_Our base interface layout ready for interactions._
![Groq Chatbot View 1](screenshot1.png)

### 2️⃣ Persona Configuration (Custom System Prompt)
_Demonstrating the dynamic shift in behavior by tweaking the system rules profile panel._
![Groq Chatbot View 2](screenshot2.png)

### 3️⃣ High Temperature Mode (Creative Output)
_Testing creativity fluctuations by altering the randomness slider scale parameters._
![Groq Chatbot View 3](screenshot3.png)


## 🚀 Features
* **Real-Time Streaming**: Responses appear word-by-word just like ChatGPT.
* **Customizable System Prompt**: Adjust the AI's persona, role, and tone on the fly.
* **Adjustable Temperature Slider**: Dynamically tune creativity vs. deterministic output.
* **Persistent Conversation Memory**: Maintains complete historical chat tracking across turns.
* **Blazing Fast Inference**: Powered by the Groq LLaMA architecture.

## 🛠️ Project Structure
* `app.py` - Main application interface and execution logic.
* `requirements.txt` - Python package dependencies.
* `README.md` - Project documentation.


## 💻 Local Setup Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment API Key**:
   * Set your Groq API Key as an environment variable:
   ```bash
   export GROQ_API="your_actual_groq_api_key_here"
   ```

4. **Launch the Application**:
   ```bash
   python app.py
   ```

