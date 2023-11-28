import streamlit as st
import googletrans
from langchain.llms import CTransformers

translator = googletrans.Translator()

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K (2).bin",
    model_type="llama"
)

st.title('AI tutor')

content = st.text_input("답변을 요청하세요!")

if st.button('요청하기'):
    with st.spinner('잠시만 기다려주세요...'):
        content_en = translator.translate(content, dest="en", src='auto').text
        result = llm.predict("Explain about" + content_en + " to elementary school students:")
        translation = translator.translate(result, src='en', dest='ko').text  # 영어에서 한국어로 번역
        st.write(translation)  # 번역된 결과 출력
