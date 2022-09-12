import streamlit as st
from PIL import Image
import numpy as np

def main():
    st.title('ピンボケ除去(うそ)')
    st.write('〇画像アップロード')
    uploaded_file = st.file_uploader("画像をアップロードしてください。")
    image=Image.open(uploaded_file)
    img_array = np.array(image)
    st.write('〇元画像↓')
    st.image(img_array,caption = 'もと',use_column_width = True)
    st.write('〇変換後画像↓')
    trans_img_array = trans(img_array)
    st.image(trans_img_array,caption = 'へんかん',use_column_width = True)

def trans(img):
    return img-50

if __name__=="__main__":
    main()