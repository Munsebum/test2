from dotenv import load_dotenv
load_dotenv()

# from langchain_openai import ChatOpenAI
# llm=ChatOpenAI()
# result=llm.invoke("ISO19650 에 대해 설명해줘")
# print(result)

# 2)
# from langchain_openai import ChatOpenAI
# chat_model = ChatOpenAI()

# content = "부자가 되는 방법"

# result = chat_model.predict(content + '에 대해 알려줘')
# # predict 는 예전 버전의 함수 invoke가 최신 함수

# print(result)

# 3)
# from langchain_openai import ChatOpenAI
# import streamlit as st
# chat_model = ChatOpenAI()

# st.title('BIM 관련 기술')

# content = st.text_input('BIM 관련 기술 제시해주세요')


# if st.button('BIM 기술에 대한 설명 요청하기'):
#     with st.spinner('BIM 기술 생성중!!!!!!!!!!!!!!!!!!!!!!'):
#         result = chat_model.predict(content + '에 대한 기술 설명해줘')
#         st.write(result)

# 4)
# import streamlit as st
# from langchain.llms import ctransformers

# llm=ctransformers(
#     model ="",
#     model_type = 'llama'
# )

# st.title('BIM 관련 기술')

# content = st.text_input('BIM 관련 기술 제시해주세요')

# if st.button('BIM 기술에 대한 설명 요청하기'):
#     with st.spinner('BIM 기술 생성중!!!!!!!!!!!!!!!!!!!!!!'):
#         result = llm.invoke(content + '에 대한 기술 설명해줘')
#         st.write(result)

# 5)