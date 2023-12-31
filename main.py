

import streamlit as st
from googletrans import Translator
from langchain.llms import CTransformers



translator = Translator()


llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('AI tutor')

content = st.text_input("답변을 요청하세요!")

if st.button('요청하기'):
    with st.spinner('잠시만 기다려주세요...'):
        content_en = translator.translate(content, dest="en", src='auto').text
        result = llm.predict("Please tell the teacher how to teach elementary school students to understand 10 kinds of:"+ content_en)
        translation = translator.translate(result, src='en', dest='ko').text  # 영어에서 한국어로 번역
        st.write(translation)  # 번역된 결과 출력
