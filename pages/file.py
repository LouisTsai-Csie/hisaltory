import streamlit as st
from PIL import Image


def files():
    st.header('相關文獻史料彙整')
    st.text('可於該區域查找日治時期相關文獻之內容與簡介')

    expander1 = st.expander('一般用鹽數量及價格')
    expander1.image(Image.open('images/a.png'), caption="一般用鹽數量及價格")

    expander2 = st.expander('中國輸入的鹽數量及價格')
    expander2.image(Image.open('images/b.png'), caption="中國輸入的鹽數量及價格")

    expander3 = st.expander('日治時期希望廢除官鹽的九點理由')
    expander3.image(Image.open('images/c.png'), caption='日治時期希望廢除官鹽的九點理由')

    expander4 = st.expander('台灣生產的鹽數量及價格')
    expander4.image(Image.open('images/d.png'), caption='台灣生產的鹽數量及價格')
    expander4.image(Image.open('images/e.png'), caption='台灣生產的鹽數量及價格')

    expander5 = st.expander('自作小作鹽田富樹面積及治鹽者戶數')
    expander5.image(Image.open('images/f.png'), caption='自作小作鹽田富樹面積及治鹽者戶數')

    expander6 = st.expander('在私鹽製造盛行的地方設置請願巡查與巡查捕')
    expander6.image(Image.open('images/g.png'), caption='在私鹽製造盛行的地方設置請願巡查與巡查捕')

    expander7 = st.expander('明治 38 年末時臺灣島內第一期鹽田擴張結果')
    expander7.image(Image.open('images/h.png'), caption='明治 38 年末時臺灣島內第一期鹽田擴張結果')

    expander8 = st.expander('明治 32 年 5 月開始實施食鹽專賣制度')
    expander8.image(Image.open('images/i.png'), caption='明治 32 年 5 月開始實施食鹽專賣制度')

    expander9 = st.expander('官方覺得私鹽盛行的原因')
    expander9.image(Image.open('images/j.png'), caption='官方覺得私鹽盛行的原因')

    expander10 = st.expander('官方對於私鹽的默許')
    expander10.image(Image.open('images/k.png'), caption='官方對於私鹽的默許')

    expander11 = st.expander('鹽民的收入')
    expander11.image(Image.open('images/l.png'), caption='鹽民的收入')

    expander12 = st.expander('第二期鹽田擴張結果')
    expander12.image(Image.open('images/m.png'), caption='第二期鹽田擴張結果')

    expander13 = st.expander('食鹽犯則鹽事件紀錄')
    expander13.image(Image.open('images/n.png'), caption='食鹽犯則鹽事件紀錄')

    expander14 = st.expander('鹽田修復與擴張之原因')
    expander14.image(Image.open('images/o.png'), caption='鹽田修復與擴張之原因')
    return

if __name__=='__main__':
    files()