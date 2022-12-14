import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4430/4430494.png", width=100)
st.sidebar.markdown("##### The app uses CLIP Interrogator to generate a text prompt which is then processed through Mubert text-to-music to generate melody from the input image")
st.sidebar.subheader("About CLIP Interrogator Model")
st.sidebar.markdown("##### The CLIP Interrogator is a prompt engineering tool that combines OpenAI's CLIP and Salesforce's BLIP to optimize text prompts to match a given image")
st.sidebar.subheader("About Mubert Text-to-Music Model")
st.sidebar.markdown("##### Mubert is a startup that uses AI to generate music. The company has developed a text-to-music technology that can turn any text into a melody. Mubert is a leading provider of AI-powered sound design and composition tools")


st.sidebar.header("Powered By")
st.sidebar.image("icons.png", width=200)

st.sidebar.caption("</Shahnab>")

st.subheader("Image to Music AI Generator")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-imagetomusic.hf.space", width=1500, height=650, scrolling=True)
