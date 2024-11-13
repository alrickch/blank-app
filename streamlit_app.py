import streamlit as st
import streamlit.components.v1 as components

def run():
    # Assuming you have a direct URL to embed the Botpress chat
    iframe_url = "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2024/11/13/06/20241113061509-EYEAY5FQ.json"  # Replace with your bot's URL

    # Embed the iFrame with the Botpress chatbot
    components.iframe(iframe_url, height=1024, width=1024)  # Adjust as needed

if __name__ == "__main__":
    run()
