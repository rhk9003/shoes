import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 1. 頁面設定 ---
st.set_page_config(
    page_title="DK小白鞋行銷戰役覆盤",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. 自定義 CSS (為了讓介面更像簡報風格) ---
st.markdown("""
<style>
    /* 標題樣式 */
    h1 { color: #1e3a8a; font-family: 'Helvetica', sans-serif; }
    h2 { color: #1e3a8a; border-left: 5px solid #3b82f6; padding-left: 15px; margin-top: 30px; }
    h3 { color: #334155; }
    
    /* 指標卡片樣式 */
    div[data-testid="metric-container"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* 自定義容器樣式 (模擬 FB/Dcard 貼文框) */
    .post-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .highlight-text { color: #2563eb; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 3. 側邊欄導航 ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=DK+Logo", use_container_width=True) # 這裡換成 DK Logo
    st.title("導航目錄")
    section = st.radio("前往章節：", 
        ["1. 戰績總覽 (Key Wins)", 
         "2. 聲量趨勢分析", 
         "3. 策略飛輪 (Strategy)", 
         "4. 執行：口碑與信任", 
         "5. 執行：權威背書", 
         "6. 執行：社群與廣告",
         "7. 結論"]
    )
    st.divider()
    st.info("💡 提示：此儀表板為 DK 小白鞋行銷專案之數據覆盤。")

# --- 4. 主要內容 ---

if section == "1. 戰績總覽 (Key Wins)":
    st.title("DK小白鞋：從新品到市場冠軍的勝利方程式")
    st.markdown("### 🏆 6個月內逆勢突圍的整合行銷戰役")
    
    # 英雄圖片區 (建議放產品圖)
    # st.image("your_local_image_path/white_sneaker_hero.jpg", use_container_width=True)
    
    st.divider()
    
    # 關鍵數據指標 (Big Numbers)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="市場聲量排名", value="NO.1", delta="超越競品")
        st.caption("品牌產品字搜尋量全面制霸")
    with col2:
        st.metric(label="銷售排名", value="TOP 3", delta="常態熱銷")
        st.caption("位居全公司原價鞋款前三")
    with col3:
        st.metric(label="團購爆發銷量", value="400+", delta="雙/月")
        st.caption("七月單月團購活動銷量")
    with col4:
        st.metric(label="網路聲量成長", value="2X", delta="100%")
        st.caption("帶動品牌整體 YOY 翻倍")

elif section == "2. 聲量趨勢分析":
    st.header("📈 市場聲量：在對手退步時一飛沖天")
    st.markdown("推出僅兩個月，Google 搜尋量即追平對手，半年內實現反超並拉開差距。")
    
    # 模擬數據 (根據您 PDF 中的圖表趨勢重建)
    data = {
        'Month': ['2022-08', '2022-10', '2022-12', '2023-02', '2023-04', '2023-05', '2023-06', '2023-07'],
        'DK': [10, 12, 15, 30, 80, 450, 300, 750],
        'Vanger': [50, 55, 60, 55, 50, 45, 40, 35],
        '林果': [80, 75, 70, 65, 60, 65, 60, 55]
    }
    df = pd.DataFrame(data)
    
    # 使用 Plotly 繪製互動式折線圖
    fig = go.Figure()
    
    # 競品線 (灰色/虛線)
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Vanger'], mode='lines', name='Vanger (-34%)', line=dict(color='#94a3b8', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['林果'], mode='lines', name='林果 (-29%)', line=dict(color='#cbd5e1', width=2, dash='dot')))
    
    # DK 線 (藍色/粗線/強調)
    fig.add_trace(go.Scatter(x=df['Month'], y=df['DK'], mode='lines+markers', name='DK (+177%)', line=dict(color='#2563eb', width=5)))
    
    # 圖表美化
    fig.update_layout(
        title="品牌搜尋量趨勢比較 (Google Trends)",
        xaxis_title="時間",
        yaxis_title="搜尋熱度",
        hovermode="x unified",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        height=500
    )
    
    # 標註關鍵點
    fig.add_annotation(x='2023-05', y=450, text="策略啟動點", showarrow=True, arrowhead=1)
    fig.add_annotation(x='2023-07', y=750, text="歷史新高", showarrow=True, arrowhead=1)
    
    st.plotly_chart(fig, use_container_width=True)

elif section == "3. 策略飛輪 (Strategy)":
    st.header("🔄 成功來自環環相扣的策略飛輪")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="post-card" style="border-top: 5px solid #3b82f6;">
            <h3 style="text-align:center;">🛡️ 建立信任</h3>
            <p style="text-align:center; color:#64748b;">Build Trust</p>
            <hr>
            <ul>
                <li><strong>雜誌廣編：</strong>美麗佳人背書</li>
                <li><strong>KOL 合作：</strong>空姐/職場見證</li>
                <li><strong>UGC：</strong>會員試穿好評</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="post-card" style="border-top: 5px solid #ef4444;">
            <h3 style="text-align:center;">🔥 創造需求</h3>
            <p style="text-align:center; color:#64748b;">Create Demand</p>
            <hr>
            <ul>
                <li><strong>Meta 廣告：</strong>分層溝通</li>
                <li><strong>Dcard：</strong>議題操作</li>
                <li><strong>情境：</strong>解決穿搭痛點</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="post-card" style="border-top: 5px solid #10b981;">
            <h3 style="text-align:center;">💰 驅動轉換</h3>
            <p style="text-align:center; color:#64748b;">Drive Conversion</p>
            <hr>
            <ul>
                <li><strong>Google Ads：</strong>關鍵字攔截</li>
                <li><strong>團購：</strong>限時爆發</li>
                <li><strong>促銷：</strong>庫存告急/新客折抵</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif section == "4. 執行：口碑與信任":
    st.header("Step 1: 真實口碑建立信任護城河")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("### 👥 會員試穿活動 (UGC)")
        st.info("**策略：** 透過「送購物金」與「實體贈品」，邀請會員到店試穿並分享真實心得。")
        st.markdown("""
        * **步驟 1：** 門市拍照
        * **步驟 2：** 掃碼進入貼文
        * **步驟 3：** 上傳照片 + 50字心得
        * **步驟 4：** 現場兌換贈品
        """)
        st.metric("貼文互動數", "377 Likes", "33 則留言")

    with col2:
        # 這裡可以使用 st.image 放入您的截圖 "11.41.05.jpg"
        # 由於我無法讀取本地檔案，這裡用文字框示意圖片位置
        st.markdown("#### 🖼️ 參考素材：FB 募集活動貼文")
        st.image("https://placehold.co/600x400?text=FB+UGC+Post+Screenshot", caption="請替換為您的截圖: 11.41.05.jpg")
        
    st.divider()
    
    st.markdown("### 🗣️ 社群議題操作 (Dcard)")
    d_col1, d_col2 = st.columns([1, 2])
    with d_col1:
         st.markdown("**Dcard 穿搭板 #請益**")
         st.markdown("透過「#請益 這雙小白鞋好穿嗎？」的標題，引發大學生與年輕上班族的自然討論，降低廣告感，累積 SEO 搜尋結果。")
    with d_col2:
         # 這裡放入 Dcard 截圖 "11.42.03.jpg"
         st.image("https://placehold.co/600x300?text=Dcard+Post+Screenshot", caption="請替換為您的截圖: 11.42.03.jpg")

elif section == "5. 執行：權威背書":
    st.header("Step 2 & 3: 權威媒體與 KOL 背書")
    
    tab1, tab2 = st.tabs(["Marie Claire 雜誌", "KOL 白白 Abby"])
    
    with tab1:
        st.markdown("### 👠 時尚權威認證")
        st.markdown("> **「小白鞋完美拯救妳的穿搭荒！DK會呼吸的小白鞋，結合百搭經典款式與專利技術！」**")
        col_mc1, col_mc2 = st.columns(2)
        with col_mc1:
            # 這裡放入美麗佳人截圖 "11.41.34.jpg" 或 "11.41.41.jpg"
            st.image("https://placehold.co/500x500?text=Marie+Claire+Article", caption="請替換為您的截圖: 11.41.34.jpg")
        with col_mc2:
            st.success("策略意圖：藉由時尚媒體廣編，將「機能鞋」提升至「時尚單品」的層次，解決消費者覺得機能鞋不好看的痛點。")

    with tab2:
        st.markdown("### ✈️ 長榮空姐的真實推薦")
        st.markdown("**背景：** 抓住長榮航空換鞋潮，與空姐 KOL 合作。")
        col_kol1, col_kol2 = st.columns([1.5, 1])
        with col_kol1:
             # 這裡放入 KOL 截圖 "11.41.56.jpg"
             st.image("https://placehold.co/600x400?text=KOL+Abby+Post", caption="請替換為您的截圖: 11.41.56.jpg")
        with col_kol2:
             st.markdown("""
             **貼文重點：**
             * 強調「久站」、「舒適」。
             * 場景化行銷：從工作到休閒的轉換。
             * "忍不住去門市試穿了一下，立刻帶走兩雙"
             """)

elif section == "6. 執行：社群與廣告":
    st.header("Step 4 & 5: 精準廣告投放與收割")
    st.markdown("針對不同階段的消費者，投遞不同的廣告素材與訊息。")
    
    # 建立三欄式佈局來展示廣告圖 (模仿 11.41.20.jpg)
    ad1, ad2, ad3 = st.columns(3)
    
    with ad1:
        st.markdown("#### 🅰️ 節慶/折扣型")
        # 圖片: 11.41.20.jpg 的左邊部分
        st.image("https://placehold.co/300x400?text=Mothers+Day+85+Off", caption="母親節 85折")
        st.caption("針對價格敏感客群，利用節慶促銷驅動下單。")
        
    with ad2:
        st.markdown("#### 🅱️ 稀缺/急迫型")
        # 圖片: 11.41.20.jpg 的中間部分
        st.image("https://placehold.co/300x400?text=Low+Stock+Warning", caption="庫存告急！")
        st.caption("「全台剩不到100雙」，製造FOMO (錯失恐懼)，加速決策。")
        
    with ad3:
        st.markdown("#### 🆎 新客誘因型")
        # 圖片: 11.41.20.jpg 的右邊部分
        st.image("https://placehold.co/300x400?text=New+Member+Discount", caption="新會員折$300")
        st.caption("降低首次購買門檻，利用 APP 下載優惠鎖定顧客。")

    st.divider()
    st.markdown("### 📦 團購最後一哩路")
    st.success("在累積了足夠聲量後，與高黏著度 KOL (如阿淇博士) 進行團購，單次合作創造 **232雙+** 的銷量，實現流量變現。")

elif section == "7. 結論":
    st.header("🎯 總結：DK 小白鞋勝利方程式")
    
    # 使用 expander 讓結論更有層次
    with st.expander("1. 聲量先行 (Volume First)", expanded=True):
        st.write("在投入大量轉換廣告前，先集中資源透過 UGC 與 Dcard 創造口碑與搜尋熱度。")
        
    with st.expander("2. 情境觸發 (Contextual Triggers)", expanded=True):
        st.write("敏銳抓住長榮空姐換鞋事件，將專業舒適的需求轉嫁到休閒小白鞋上。")
        
    with st.expander("3. 信任疊加 (Layered Trust)", expanded=True):
        st.write("結合「媒體(權威)」、「KOL(影響力)」、「素人(真實性)」三方背書，消除對機能鞋外觀的疑慮。")
        
    with st.expander("4. 全通路整合 (Omni-Channel)", expanded=True):
        st.write("線上廣告(Meta/Google) 與線下門市(試穿活動) 緊密配合，O2O 導流順暢。")

# 頁尾
st.markdown("---")
st.caption("© 2025 DK White Sneaker Strategy Review | Created with Streamlit")
