import streamlit as st
from PIL import Image

def data():
    st.title('相關文獻數據彙整')
    expander1 = st.expander('台灣鹽的來源')
    expander1.image(Image.open('images/p.png'), caption='台灣鹽的來源')
    expander1.button('Download', key=1)
    
    expander2 = st.expander('一般用鹽數量表')
    expander2.image(Image.open('images/q.png'), caption='一般用鹽數量表')
    expander2.button('Download', key=2)

    expander3 = st.expander('犯則事件比例圖')
    expander3.image(Image.open('images/r.png'), caption='犯則事件比例圖')
    expander3.button('Download', key=3)

    expander4 = st.expander('犯則事件數量圖')
    expander4.image(Image.open('images/s.png'), caption='犯則事件數量圖')
    expander4.button('Download', key=4)

    expander5 = st.expander('遭查獲私鹽數量表')
    expander5.image(Image.open('images/t.png'), caption='遭查獲私鹽數量表')
    expander5.button('Download', key=5)
    return 

if __name__=='__main__':
    data()