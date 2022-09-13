import streamlit as st
from PIL import Image
import numpy as np

# def main():
#     st.title('ピンボケ除去(うそ)aaaaa')
#     st.write('〇画像アップロード')
#     uploaded_file = st.file_uploader("画像をアップロードしてください。")
#     image=Image.open(uploaded_file)
#     img_array = np.array(image)
#     st.write('〇元画像↓')
#     st.image(img_array,caption = 'もと',use_column_width = True)
#     st.write('〇変換後画像↓')
#     trans_img_array = trans(img_array)
#     st.image(trans_img_array,caption = 'へんかん',use_column_width = True)

# def trans(img):
#     return img-50

# if __name__=="__main__":
#     main()

st.title('ピンボケ除去(うそ)')  # タイトルの表示
st.write('〇画像アップロード')  # 説明文表示
uploaded_file = st.file_uploader("画像をアップロードしてください。")  # 画像のUP、一時格納
image=Image.open(uploaded_file)  # 画像データに変換
img_array = np.array(image)  # 画像データを配列データに変換
st.write('〇元画像↓')  # 説明文表示
st.image(img_array,caption = 'もと',use_column_width = True)  # 元画像表示
st.write('〇変換後画像↓')  # 説明文表示
trans_img_array = img_array-50  # 元画像を適当に変換
st.image(trans_img_array,caption = 'へんかん',use_column_width = True)  # 返還後画像を表示

