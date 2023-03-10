import streamlit as st

st.title("streamlit Demo App")
st.write("---")
hensu1 = st.text_input("名字を入力してください")
hensu2 = st.text_input("名前を入力してください")

#名字と名前結合する関数
def out_fullname(hensu1,hensu2):
    return  hensu1 + ' ' + hensu2

if st.button("デバッグ体験",type='primary',use_container_width=True):
    fullname = out_fullname(hensu1,hensu2)
    if len(fullname) > 1:
        st.info(fullname)
    elif len(fullname) > 10:
        st.error('10文字以内にしてください')
    elif len(fullname) == 1:
        st.error('何か入力してください')






