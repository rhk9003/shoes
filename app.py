import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# --- 1. 頁面設定與 CSS ---
st.set_page_config(
    page_title="DK小白鞋行銷戰役覆盤",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定義 CSS：維持簡報卡片風格
st.markdown("""
<style>
    /* 核心背景色 */
    .stApp { background-color: #f1f5f9; }
    
    /* 簡報卡片容器 - 模擬投影片 */
    .slide-card {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 40px;
        border: 1px solid #e2e8f0;
    }
    
    /* 統一標題樣式（章節標題） */
    .slide-card h2 {
        color: #1e3a8a;
        font-weight: 700;
        border-left: 6px solid #3b82f6;
        padding-left: 15px;
        margin-top: 0;
        margin-bottom: 20px;
    }
    h3 { color: #334155; margin-top: 5px; }
    
    /* 圖片說明 */
    .caption { 
        text-align: center; 
        color: #64748b; 
        font-size: 14px; 
        margin-top: 10px;
        font-style: italic;
    }
    
    /* 關鍵指標樣式 */
    div[data-testid="metric-container"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        transition: transform 0.2s;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        font-size: 2.5rem;
        color: #2563eb;
        font-weight: 800;
    }
    
    /* 列表間距 */
    ul { margin-bottom: 15px; }
    li { margin-bottom: 5px; }
    
    /* 若有 tabs 元件則隱藏（本頁不用 tabs） */
    .stTabs { display: none; } 
</style>
""", unsafe_allow_html=True)

# --- 2. 圖片載入系統 ---

IMAGE_MAP = {
    # 產品圖
    "product_hero": "截圖 2025-12-05 晚上11.40.59.png",
    # 口碑/社群
    "fb_ugc": "截圖 2025-12-05 晚上11.41.05.png",
    "dcard": "截圖 2025-12-05 晚上11.42.03.png",
    # 權威背書
    "marie_claire": "截圖 2025-12-05 晚上11.41.34.png",
    "kol_abby": "截圖 2025-12-05 晚上11.41.56.png",
    "kol_achi": "截圖 2025-12-05 晚上11.41.49.png",
    # 廣告與收割
    "meta_ads": "截圖 2025-12-05 晚上11.41.20.png",
    "google_ads": "截圖 2025-12-05 晚上11.41.27.png",
    "group_buy": "截圖 2025-12-05 晚上11.42.09.png"
}

def render_image(key, caption=None, width=None):
    """
    智能圖片載入器：從目前工作目錄尋找圖片
    """
    filename = IMAGE_MAP.get(key, key)
    final_path = filename
        
    if os.path.exists(final_path):
        st.image(final_path, caption=caption, use_column_width=(width is None), width=width)
    else:
        st.error("🖼️ 圖片載入失敗！")
        st.caption(f"系統找不到檔案：`{filename}`。請確認該檔案存在於專案根目錄下。")

# --- 3. 側邊欄導航 ---
with st.sidebar:
    st.header("DK DR.KAO")
    st.info("💡 報告為單頁垂直簡報模式，請直接捲動閱讀。")
    st.markdown("---")
    st.markdown("**報告結構（點擊跳轉）：**")
    st.markdown("- [戰績總覽](#1-戰績總覽)")
    st.markdown("- [聲量趨勢](#2-聲量趨勢)")
    st.markdown("- [策略飛輪](#3-策略飛輪)")
    st.markdown("- [口碑與信任](#4-口碑與信任)")
    st.markdown("- [權威背書](#5-權威背書)")
    st.markdown("- [廣告與收割](#6-廣告與收割)")
    st.markdown("- [結論](#7-結論)")

# --- 4. 頁首主標 ---
st.title("DK小白鞋：從新品到市場冠軍的勝利方程式")
st.markdown("#### 🏆 6個月內逆勢突圍的整合行銷戰役覆盤")

# === Slide 1: 戰績總覽 ===
st.markdown('<div id="1-戰績總覽" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 1. 戰績總覽")

col1, col2 = st.columns([1, 1.2])
with col1:
    render_image("product_hero", "DK 呼吸空氣小白鞋 - 簡約美學與機能的結合")
with col2:
    st.subheader("📊 四個關鍵勝利指標")
    st.write("在此次行銷戰役中，我們在多項重要指標上取得了顯著突破：")
    
    m1, m2 = st.columns(2)
    with m1:
        st.metric("市場聲量", "NO.1", "超越競品")
        st.caption("品牌產品字搜尋量制霸")
        st.write("")
        st.metric("團購銷量", "400+", "雙 / 月")
        st.caption("七月單月爆發")
    with m2:
        st.metric("銷售排名", "TOP 3", "常態熱銷")
        st.caption("全公司原價鞋款")
        st.write("")
        st.metric("網路聲量", "2X", "整體成長")
        st.caption("帶動品牌整體聲量翻倍")

st.markdown('</div>', unsafe_allow_html=True)

# === Slide 2: 聲量趨勢 ===
st.markdown('<div id="2-聲量趨勢" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 2. 聲量趨勢")

st.subheader("📈 在對手退步時一飛沖天")
st.markdown("推出僅兩個月，Google 搜尋量即追平對手，半年內實現反超並拉開差距。")

data = {
    'Month': ['2022-08', '2022-10', '2022-12', '2023-02', '2023-04', '2023-05', '2023-06', '2023-07'],
    'DK': [10, 12, 15, 30, 80, 450, 300, 750],
    'Vanger': [50, 55, 60, 55, 50, 45, 40, 35],
    '林果': [80, 75, 70, 65, 60, 65, 60, 55]
}
df = pd.DataFrame(data)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Month'], y=df['Vanger'], mode='lines',
                         name='Vanger (-34%)',
                         line=dict(color='#94a3b8', width=2, dash='dot')))
fig.add_trace(go.Scatter(x=df['Month'], y=df['林果'], mode='lines',
                         name='林果 (-29%)',
                         line=dict(color='#cbd5e1', width=2, dash='dot')))
fig.add_trace(go.Scatter(x=df['Month'], y=df['DK'], mode='lines+markers',
                         name='DK (+177%)',
                         line=dict(color='#2563eb', width=5)))

fig.update_layout(
    title="品牌搜尋量趨勢比較 (Google Trends)",
    xaxis_title="時間",
    yaxis_title="搜尋熱度",
    hovermode="x unified",
    height=450,
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
fig.add_annotation(x='2023-05', y=450, text="策略啟動點",
                   showarrow=True, arrowhead=1, ax=-40, ay=-40)

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# === Slide 3: 策略飛輪 ===
st.markdown('<div id="3-策略飛輪" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 3. 策略飛輪")

st.subheader("🔄 成功來自環環相扣的策略設計")
s_col1, s_col2, s_col3 = st.columns(3)
with s_col1:
    st.info("**🛡️ 建立信任 (Build Trust)**")
    st.markdown("""
    * 雜誌廣編
    * KOL 合作
    * 會員試穿心得
    """)
with s_col2:
    st.warning("**🔥 創造需求 (Create Demand)**")
    st.markdown("""
    * Meta 廣告
    * Dcard 議題
    * 穿搭內容
    """)
with s_col3:
    st.success("**💰 驅動轉換 (Drive Conversion)**")
    st.markdown("""
    * Google Ads
    * 團購合作
    * 促銷活動
    """)

st.markdown('</div>', unsafe_allow_html=True)

# === Slide 4: 口碑與信任 ===
st.markdown('<div id="4-口碑與信任" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 4. 執行：口碑與信任")

col_ugc1, col_ugc2 = st.columns([1.2, 1])

with col_ugc1:
    st.markdown("#### 👥 會員試穿活動 (UGC)")
    st.markdown("**策略目標：** 正式開跑前先累積第一手好評，作為後續行銷素材基底。")
    render_image("fb_ugc", "FB 粉絲專頁：試穿募集貼文（377 個讚、33 則留言）")

with col_ugc2:
    st.markdown("#### 🗣️ 社群議題操作 (Dcard)")
    st.markdown("**策略目標：** 在年輕族群中「種下問題」，引發自然討論並兼顧 SEO 佈局。")
    render_image("dcard", "Dcard 穿搭板：真實討論串")

st.markdown('</div>', unsafe_allow_html=True)

# === Slide 5: 權威背書 ===
st.markdown('<div id="5-權威背書" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 5. 執行：權威背書")

st.subheader("Step 2 & 3：結合時尚權威與部落客見證")

col_auth1, col_auth2 = st.columns(2)
with col_auth1:
    st.markdown("#### 👠 Marie Claire 美麗佳人廣編")
    render_image("marie_claire", "將「機能鞋」拉升至「時尚單品」層次的關鍵廣編")

with col_auth2:
    st.markdown("#### ✈️ KOL 白白 Abby（前空姐）")
    render_image("kol_abby", "抓住長榮換鞋潮，強調久站舒適與職場穿搭")

st.divider()
st.markdown("#### 👟 阿淇博士部落客推薦（高影響力穿搭部落客）")
render_image("kol_achi", "阿淇博士穿搭部落客推薦貼文，強調「好穿到像走在雲上」")

st.markdown('</div>', unsafe_allow_html=True)

# === Slide 6: 廣告與收割 ===
st.markdown('<div id="6-廣告與收割" class="slide-card">', unsafe_allow_html=True)
st.markdown("## 6. 廣告與收割")

st.subheader("Step 4 & 5：精準投放與轉換收割")

st.markdown("#### 🎯 Meta 廣告分層策略")
st.markdown("針對不同階段消費者，投遞「節慶折扣」、「庫存告急」、「新客優惠」等不同訊息。")
render_image("meta_ads", "多樣化素材測試：情境、利益點與行動呼籲交叉實驗")

st.divider()

c_col1, c_col2 = st.columns(2)
with c_col1:
    st.markdown("#### 🔍 Google 關鍵字攔截")
    st.markdown("鎖定「小白鞋」、「好穿小白鞋」等高意圖關鍵字，精準攔截搜尋流量。")
    render_image("google_ads", "Google Search Ads 截圖")

with c_col2:
    st.markdown("#### 📦 KOL 團購收割")
    st.markdown("在聲量與信任累積後，啟動團購合作，單次合作創造 **232 雙以上** 的銷量。")
    render_image("group_buy", "KOL 團購貼文與成效")

st.markdown('</div>', unsafe_allow_html=True)

# === Slide 7: 結論 ===
st.markdown('<div id="7-結論" class="slide-card" style="background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%); border-left: 10px solid #1e3a8a;">', unsafe_allow_html=True)
st.markdown("## 7. 結論")

st.subheader("🎯 DK 小白鞋勝利方程式")
st.markdown("這不僅是一款產品的勝利，更是市場溝通策略的升級，關鍵在於：")
st.markdown("""
* **📢 聲量先行：** 在投入大量轉換廣告前，先集中資源透過 UGC 與 Dcard 創造口碑。
* **🔥 情境觸發：** 敏銳抓住時事（長榮空姐換鞋潮），把專業需求轉嫁到大眾日常情境。
* **🤝 信任疊加：** 結合「媒體」、「KOL」、「素人」三方背書，降低首次購買阻力。
* **🔄 全通路整合：** 線上廣告與線下門市緊密配合，形成 O2O 導流與回購循環。
""")

st.markdown('</div>', unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.caption("© 2025 DK White Sneaker Strategy Review | Created with Streamlit")
