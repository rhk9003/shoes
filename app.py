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
    
    /* 調整 Tab 標籤大小和樣式 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px; 
        border-bottom: 2px solid #3b82f6; /* 強調分頁線 */
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: nowrap;
        background-color: #f8fafc;
        border-radius: 8px 8px 0 0;
        margin-right: 2px;
        padding: 0 15px;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: white;
        font-weight: bold;
        color: #1e3a8a;
        border-top: 3px solid #2563eb;
        border-left: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
    }
    
    /* 統一標題樣式 */
    h2 { color: #1e3a8a; font-weight: 700; border-left: 6px solid #3b82f6; padding-left: 15px; margin-top: 10px; margin-bottom: 20px; }
    h3 { color: #334155; margin-top: 5px; }
    
    /* 圖片說明 */
    .caption { 
        text-align: center; 
        color: #64748b; 
        font-size: 14px; 
        margin-top: 10px;
        font-style: italic;
    }
    
    /* 簡報卡片容器 */
    .slide-card {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 40px;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. 圖片載入系統 (最終修復版本) ---

# 這裡定義 "程式碼中的名稱" 對應到 "您真實的中文檔名"
# 確保檔名、空格、大小寫和副檔名完全匹配
IMAGE_MAP = {
    "product_hero": "截圖 2025-12-05 晚上11.40.59.png", 
    "fb_ugc": "截圖 2025-12-05 晚上11.41.05.jpg", 
    "dcard": "截圖 2025-12-05 晚上11.42.03.jpg", 
    "marie_claire": "截圖 2025-12-05 晚上11.41.41.jpg", 
    "kol_abby": "截圖 2025-12-05 晚上11.41.56.jpg", 
    "kol_achi": "截圖 2025-12-05 晚上11.41.49.jpg", 
    "meta_ads": "截圖 2025-12-05 晚上11.41.20.jpg", 
    "google_ads": "截圖 2025-12-05 晚上11.41.27.jpg", 
    "group_buy": "截圖 2025-12-05 晚上11.42.09.jpg" 
}

def render_image(key, caption=None, width=None):
    """
    智能圖片載入器：強制從根目錄尋找圖片
    """
    filename = IMAGE_MAP.get(key, key)
    # 僅檢查根目錄（當前程式碼所在目錄）
    final_path = filename
        
    if os.path.exists(final_path):
        st.image(final_path, caption=caption, use_column_width=(width is None), width=width)
    else:
        # 如果找不到，顯示一個漂亮的錯誤框，而不是報錯
        st.error(f"🖼️ 圖片載入失敗！")
        # os.getcwd() 獲取當前工作目錄
        st.caption(f"系統找不到檔案：`{filename}`。請確認該檔案是否存在於專案根目錄下。")

# --- 3. 側邊欄導航 ---
with st.sidebar:
    st.header("DK DR.KAO")
    st.info("💡 報告已轉換為**分頁模式**，請點擊上方標籤切換簡報頁面。")
    st.markdown("---")
    st.markdown("**報告結構：**")
    st.markdown("- 戰績與趨勢")
    st.markdown("- 策略飛輪總覽")
    st.markdown("- 口碑與權威")
    st.markdown("- 轉換與收割")
    st.markdown("- 結論")

# --- 4. 主要內容 (Tab 分頁式佈局) ---

# 設定主標題
st.title("DK小白鞋：從新品到市場冠軍的勝利方程式")
st.markdown("#### 🏆 6個月內逆勢突圍的整合行銷戰役覆盤")

# 定義 Tabs
tab_wins, tab_trends, tab_strategy, tab_trust, tab_authority, tab_conversion, tab_conclusion = st.tabs([
    "1. 戰績總覽", 
    "2. 聲量趨勢", 
    "3. 策略飛輪", 
    "4. 口碑與信任", 
    "5. 權威背書", 
    "6. 廣告與收割",
    "7. 結論"
])

# === Tab 1: Title & Key Wins ===
with tab_wins:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 戰績總覽")

    col1, col2 = st.columns([1, 1.2])
    with col1:
        render_image("product_hero", "DK 呼吸空氣小白鞋 - 簡約美學與機能的結合")
    with col2:
        st.subheader("📊 我們達成了四個關鍵勝利")
        st.write("在此次行銷戰役中，我們在多項重要指標上取得了顯著的突破：")
        
        m1, m2 = st.columns(2)
        with m1:
            st.metric("市場聲量", "NO.1", "超越競品")
            st.caption("品牌產品字搜尋量制霸")
            st.write("")
            st.metric("團購銷量", "400+", "雙/月")
            st.caption("七月單月爆發")
        with m2:
            st.metric("銷售排名", "TOP 3", "常態熱銷")
            st.caption("全公司原價鞋款")
            st.write("")
            st.metric("網路聲量", "2X", "100%")
            st.caption("帶動品牌整體成長")
    st.markdown('</div>', unsafe_allow_html=True)


# === Tab 2: Trend Analysis ===
with tab_trends:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("2. 聲量趨勢")
    st.subheader("📈 在對手退步時一飛沖天")
    st.markdown("推出僅兩個月，Google 搜尋量即追平對手，半年內實現反超並拉開差距。")

    # 模擬數據 (根據 PDF 趨勢重建)
    data = {
        'Month': ['2022-08', '2022-10', '2022-12', '2023-02', '2023-04', '2023-05', '2023-06', '2023-07'],
        'DK': [10, 12, 15, 30, 80, 450, 300, 750],
        'Vanger': [50, 55, 60, 55, 50, 45, 40, 35],
        '林果': [80, 75, 70, 65, 60, 65, 60, 55]
    }
    df = pd.DataFrame(data)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Vanger'], mode='lines', name='Vanger (-34%)', line=dict(color='#94a3b8', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['林果'], mode='lines', name='林果 (-29%)', line=dict(color='#cbd5e1', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['DK'], mode='lines+markers', name='DK (+177%)', line=dict(color='#2563eb', width=5)))

    fig.update_layout(
        title="品牌搜尋量趨勢比較 (Google Trends)",
        xaxis_title="時間",
        yaxis_title="搜尋熱度",
        hovermode="x unified",
        height=450,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.add_annotation(x='2023-05', y=450, text="策略啟動點", showarrow=True, arrowhead=1, ax=-40, ay=-40)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# === Tab 3: Strategy Flywheel ===
with tab_strategy:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("3. 策略飛輪")
    st.subheader("🔄 成功來自環環相扣的策略飛輪總覽")
    
    s_col1, s_col2, s_col3 = st.columns(3)
    with s_col1:
        st.info("**🛡️ 建立信任 (Build Trust)**")
        st.markdown("""
        * **雜誌廣編**
        * **KOL 合作**
        * **會員試穿心得**
        """)
    with s_col2:
        st.warning("**🔥 創造需求 (Create Demand)**")
        st.markdown("""
        * **Meta 廣告**
        * **Dcard 議題**
        * **穿搭內容**
        """)
    with s_col3:
        st.success("**💰 驅動轉換 (Drive Conversion)**")
        st.markdown("""
        * **Google Ads**
        * **團購合作**
        * **促銷活動**
        """)
    st.markdown('</div>', unsafe_allow_html=True)


# === Tab 4: Execution - Trust ===
with tab_trust:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("4. 執行：口碑與信任")
    st.subheader("Step 1: 真實口碑建立信任護城河")

    col_ugc1, col_ugc2 = st.columns([1.2, 1])

    with col_ugc1:
        st.markdown("#### 👥 會員試穿活動 (UGC)")
        st.markdown("**策略目標：** 在正式開跑前，先累積第一手好評，作為後續行銷素材。")
        render_image("fb_ugc", "FB 粉絲專頁：試穿募集貼文（創造 377 個讚、33 則留言）")

    with col_ugc2:
        st.markdown("#### 🗣️ 社群議題操作 (Dcard)")
        st.markdown("**策略目標：** 在年輕族群中「種下問題」，引發自然討論與 SEO 佈局。")
        render_image("dcard", "Dcard 穿搭板：真實討論串")
    st.markdown('</div>', unsafe_allow_html=True)


# === Tab 5: Execution - Authority ===
with tab_authority:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("5. 執行：權威背書")
    st.subheader("Step 2 & 3: 結合時尚權威與 KOL 見證")

    col_auth1, col_auth2 = st.columns(2)
    with col_auth1:
        st.markdown("#### 👠 Marie Claire 美麗佳人廣編")
        render_image("marie_claire", "將「機能鞋」提升至「時尚單品」層次")

    with col_auth2:
        st.markdown("#### ✈️ KOL 白白 Abby (前空姐)")
        render_image("kol_abby", "策略：抓住長榮換鞋潮，強調久站舒適與職場穿搭")
    
    st.divider()
    st.markdown("#### 👟 阿淇博士團購推薦（另一位高影響力 KOL）")
    render_image("kol_achi", "阿淇博士推薦貼文，強調舒適度像走在雲上")
    st.markdown('</div>', unsafe_allow_html=True)


# === Tab 6: Execution - Conversion ===
with tab_conversion:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("6. 執行：社群與廣告")
    st.subheader("Step 4 & 5: 精準投放與收割")

    st.markdown("#### 🎯 Meta 廣告分層策略")
    st.markdown("針對不同階段消費者，投遞「節慶折扣」、「庫存告急」、「新客優惠」等不同訊息。")
    render_image("meta_ads", "多樣化的廣告素材測試")

    st.divider()

    c_col1, c_col2 = st.columns(2)
    with c_col1:
        st.markdown("#### 🔍 Google 關鍵字攔截")
        st.markdown("鎖定「小白鞋」、「好穿小白鞋」等高意圖關鍵字，精準攔截流量。")
        render_image("google_ads", "Google Search Ads 截圖")
    with c_col2:
        st.markdown("#### 📦 KOL 團購收割")
        st.markdown("在累積了足夠聲量後，進行團購轉化，單次合作創造 **232雙+** 的銷量。")
        render_image("group_buy", "KOL 團購貼文與成效")

    st.markdown('</div>', unsafe_allow_html=True)

# === Tab 7: Conclusion ===
with tab_conclusion:
    st.markdown('<div class="slide-card" style="background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%); border-left: 10px solid #1e3a8a;">', unsafe_allow_html=True)
    st.header("7. 結論")
    st.subheader("🎯 DK 小白鞋勝利方程式")
    st.markdown("這不僅是一款產品的勝利，更是市場溝通策略的升級，關鍵在於：")
    st.write("")
    st.markdown("""
    * **📢 聲量先行：** 在投入大量轉換廣告前，先集中資源透過 UGC 與 Dcard 創造口碑。
    * **🔥 情境觸發：** 敏銳抓住時事（長榮空姐），將專業需求轉嫁到大眾市場。
    * **🤝 信任疊加：** 結合「媒體」、「KOL」、「素人」三方背書。
    * **🔄 全通路整合：** 線上廣告與線下門市緊密配合，O2O 導流順暢。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.caption("© 2025 DK White Sneaker Strategy Review | Created with Streamlit")
