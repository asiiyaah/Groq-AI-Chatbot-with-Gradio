import os
import gradio as gr
from groq import Groq

# Pulling the key from environment variables
client = Groq(api_key=os.environ.get("GROQ_API"))

def respond(message, history, system_prompt, temperature):
    messages = [{"role": "system", "content": system_prompt}]

    # Rebuild conversation history loop
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=float(temperature),
        stream=True
    )

    response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            response += content
            yield response

demo = gr.ChatInterface(
    fn=respond,
    additional_inputs=[
        gr.Textbox(label="System Prompt", value="You are a helpful AI assistant.", lines=3),
        gr.Slider(minimum=0.0, maximum=2.0, value=0.7, step=0.1, label="Temperature")
    ],
    title="Groq AI Chatbot",
    description="Customize personality using System Prompt and control creativity using Temperature."
)

if __name__ == "__main__":
    demo.launch(debug=True, share=True)
