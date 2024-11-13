import streamlit as st
import streamlit.components.v1 as components

def run():
    # HTML code with Botpress scripts
    st.title('Botpress Example')
    botpress_code = """
    
        <script src="https://cdn.botpress.cloud/webchat/v2.2/inject.js"></script>
        <script src="https://files.bpcontent.cloud/2024/11/13/06/20241113061509-EA4PHMES.js"></script>
    """
    # Use components.html to render the JavaScript in Streamlit
    #components.html(botpress_code, height=1024, width=1024)  # Adjust the height and width as needed
    st.markdown(botpress_code, unsafe_allow_html=True)
if __name__ == "__main__":
    run()
