import streamlit as st

def history():
    st.title('日治時期台灣鹽業年表')
    st.subheader('1895 年 (明治 28 年)')
    st.text('日本政府設置鹽政取調委員調查臺灣鹽業舊制')
    expander1 = st.expander('基於以下內容並建議廢除官鹽')
    expander1.text('1. 清官透過轉手價差可得數倍獲利，招致官員腐敗')
    expander1.text('2. 官府利用專賣權廉買貴賣，其獲利由消費者負擔，形同苛稅')
    expander1.text('3. 鹽是維持生存之基本必需品，應當廉價供應')
    expander1.text('4. ')
    st.text('於同年 7 月 31 號發布命令')
    expander2 = st.expander('總督府命令如下')
    expander2.text('臺灣總督海軍大將子爵樺山，為剴切出示曉諭事')
    expander2.text('照得塩乃百味之祖，人間不可一日缺乏，向來臺地塩務統歸官辦，壟斷其利，而民困已甚矣')
    expander2.text('我大皇帝體念民艱，痛恨宿弊，特命本總督一切弊竇盡行革廢。塩乃日食之需，豈有官辦私販之理')
    expander2.text('自示之後，無論塩販食戶，概行自買自賣，以便民生。爾諸色人等，')
    expander2.text('當知聖皇體卹愛民之至意，其各凜遵，切切特示。明治二十八年七月三十一日。')
    st.text('總督府雖於當年廢除專賣制度，但又於 1898 年 (明治 32 年) 重新施行專賣制度')
    return

if __name__=='__main__':
    history()