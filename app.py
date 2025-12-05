import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# --- 1. 頁面設定 ---
st.set_page_config(
    page_title="DK小白鞋行銷戰役覆盤",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. 自定義 CSS ---
st.markdown("""
<style>
    h1 { color: #1e3a8a; font-family: 'Helvetica', sans-serif; margin-bottom: 0px; }
    h2 { color: #1e3a8a; border-left: 5px solid #3b82f6; padding-left: 15px; margin-top: 60px; margin-bottom: 30px;}
    h3 { color: #334155; margin-top: 20px; }
    .caption { color: #64748b; font-size: 14px; }
    
    /* 指標卡片優化 */
    div[data-testid="metric-container"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    /* 策略卡片 */
    .post-card {
        background-color: white;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    
    /* 章節容器 */
    .section-container {
        padding: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- 輔助函數：安全加載圖片 ---
def load_image(filename, caption=None, use_column_width=True):
    folder_path = os.path.join("images", filename)
    root_path = filename
    
    if os.path.exists(folder_path):
        st.image(folder_path, caption=caption, use_container_width=use_column_width)
    elif os.path.exists(root_path):
        st.image(root_path, caption=caption, use_container_width=use_column_width)
    else:
        st.warning(f"⚠️ 找不到圖片：{filename}")

# --- 3. 側邊欄 (僅作資訊展示與簡單目錄) ---
with st.sidebar:
    st.header("DK DR.KAO")
    st.markdown("### 呼吸空氣鞋行銷專案")
    st.markdown("---")
    st.markdown("**目錄：**")
    st.markdown("1. [戰績總覽](#1-key-wins)")
    st.markdown("2. [聲量趨勢](#2)")
    st.markdown("3. [策略飛輪](#3-strategy)")
    st.markdown("4. [口碑與信任](#4-step-1)")
    st.markdown("5. [權威背書](#5-step-2-3)")
    st.markdown("6. [社群與廣告](#6-step-4-5)")
    st.markdown("7. [結論](#7)")
    st.markdown("---")
    st.info("提示：直接向下捲動即可瀏覽完整報告。")

# --- 4. 主要內容 (單頁式垂直佈局) ---

# === Header ===
st.title("DK小白鞋：從新品到市場冠軍的勝利方程式")
st.markdown("#### 🏆 6個月內逆勢突圍的整合行銷戰役覆盤")
st.markdown("---")

# === Section 1: Key Wins ===
st.header("1. 戰績總覽 (Key Wins)")
col1, col2 = st.columns([1, 1])
with col1:
    load_image("截圖 2025-12-05 晚上11.40.59.png", "DK 呼吸空氣小白鞋")
with col2:
    st.markdown("### 我們達成了四個關鍵勝利")
    st.markdown("在此次行銷戰役中，我們不僅成功推廣了新品，更在各項指標上取得了顯著的突破。")
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.metric(label="市場聲量", value="NO.1", delta="超越競品")
        st.caption("品牌產品字搜尋量制霸")
        st.write("") # Spacer
        st.metric(label="團購銷量", value="400+", delta="雙/月")
        st.caption("七月單月爆發")
    with m_col2:
        st.metric(label="銷售排名", value="TOP 3", delta="常態熱銷")
        st.caption("全公司原價鞋款")
        st.write("") # Spacer
        st.metric(label="網路聲量", value="2X", delta="100%")
        st.caption("帶動品牌整體成長")

# === Section 2: Trend Analysis ===
st.header("2. 聲量趨勢：在對手退步時一飛沖天")
st.markdown("推出僅兩個月，Google 搜尋量即追平對手，半年內實現反超並拉開差距。")

# 模擬數據
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
    height=400,
    margin=dict(l=20, r=20, t=40, b=20)
)
fig.add_annotation(x='2023-05', y=450, text="策略啟動", showarrow=True, arrowhead=1)
st.plotly_chart(fig, use_container_width=True)

# === Section 3: Strategy Flywheel ===
st.header("3. 策略飛輪 (Strategy)")
st.markdown("我們的成功並非偶然，而是來自一個環環相扣的策略飛輪：")

s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    st.markdown("""
    <div class="post-card" style="border-top: 5px solid #3b82f6;">
        <h3 style="text-align:center;">🛡️ 建立信任</h3>
        <p style="text-align:center; color:#64748b;">Build Trust</p>
        <hr>
        <p>透過權威媒體、KOL與真實用戶口碑，奠定產品「好看又好穿」的市場共識。</p>
        <ul>
            <li>雜誌廣編</li>
            <li>KOL 內容</li>
            <li>會員試穿心得</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
with s_col2:
    st.markdown("""
    <div class="post-card" style="border-top: 5px solid #ef4444;">
        <h3 style="text-align:center;">🔥 創造需求</h3>
        <p style="text-align:center; color:#64748b;">Create Demand</p>
        <hr>
        <p>運用多元素材與社群議題操作，點燃潛在消費者的好奇心與購買慾。</p>
        <ul>
            <li>Meta 廣告</li>
            <li>Dcard 議題</li>
            <li>穿搭內容</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
with s_col3:
    st.markdown("""
    <div class="post-card" style="border-top: 5px solid #10b981;">
        <h3 style="text-align:center;">💰 驅動轉換</h3>
        <p style="text-align:center; color:#64748b;">Drive Conversion</p>
        <hr>
        <p>在高意圖渠道精準攔截，並以限時促銷加速決策，實現銷售收割。</p>
        <ul>
            <li>Google 關鍵字</li>
            <li>團購合作</li>
            <li>促銷活動</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === Section 4: Execution - Trust ===
st.header("4. 執行：口碑與信任 (Step 1)")
st.markdown("在正式開跑前，先用真實口碑建立信任護城河。")

col_ugc1, col_ugc2 = st.columns([1, 1])
with col_ugc1:
    st.subheader("👥 會員試穿活動 (UGC)")
    st.info("策略：透過「送購物金」與「實體贈品」，邀請會員到店試穿並分享真實心得。")
    load_image("截圖 2025-12-05 晚上11.41.05.jpg", "FB 募集活動貼文")
with col_ugc2:
    st.subheader("🗣️ 社群議題操作 (Dcard)")
    st.info("策略：在年輕族群中「種下問題」，引發自然討論與 SEO 佈局。")
    load_image("截圖 2025-12-05 晚上11.42.03.jpg", "Dcard 討論串")

# === Section 5: Execution - Authority ===
st.header("5. 執行：權威背書 (Step 2 & 3)")
st.markdown("結合時尚權威與真實體驗，解決「機能鞋不好看」的痛點。")

col_auth1, col_auth2 = st.columns(2)
with col_auth1:
    st.markdown("#### 👠 時尚權威認證")
    load_image("截圖 2025-12-05 晚上11.41.41.jpg", "美麗佳人廣編稿")
    st.caption("策略意圖：藉由時尚媒體廣編，將「機能鞋」提升至「時尚單品」的層次。")

with col_auth2:
    st.markdown("#### ✈️ KOL 真實推薦 (阿淇博士 & Abby)")
    
    tab_kol1, tab_kol2 = st.tabs(["空姐 Abby", "阿淇博士"])
    with tab_kol1:
        load_image("截圖 2025-12-05 晚上11.41.56.jpg", "KOL Abby 推薦")
        st.caption("抓住長榮航空換鞋潮，強調久站舒適與職場穿搭。")
    with tab_kol2:
        load_image("截圖 2025-12-05 晚上11.41.49.jpg", "阿淇博士推薦")
        st.caption("以「好穿到像走在雲上」為訴求，強化舒適度認知。")

# === Section 6: Execution - Conversion ===
st.header("6. 執行：社群與廣告 (Step 4 & 5)")
st.markdown("精準投放，分層收割。")

st.subheader("🎯 Meta 廣告分層策略")
st.write("針對不同階段消費者，投遞「節慶折扣」、「庫存告急」、「新客優惠」等不同訊息。")
load_image("截圖 2025-12-05 晚上11.41.20.jpg", "Meta 廣告素材總覽")

col_conv1, col_conv2 = st.columns(2)
with col_conv1:
    st.markdown("#### 🔍 Google 關鍵字攔截")
    load_image("截圖 2025-12-05 晚上11.41.27.jpg", "Google Ads 截圖")
with col_conv2:
    st.markdown("#### 📦 KOL 團購收割")
    st.success("在累積了足夠聲量後，進行團購轉化，單次合作創造 **232雙+** 的銷量。")
    load_image("截圖 2025-12-05 晚上11.42.09.jpg", "團購貼文")

# === Section 7: Conclusion ===
st.header("7. 結論")
st.markdown("""
<div style="background-color:#eff6ff; padding:30px; border-radius:15px; border-left: 10px solid #1e3a8a;">
    <h3 style="color:#1e3a8a; margin-top:0;">🎯 DK 小白鞋勝利方程式</h3>
    <p style="font-size:18px;">這不僅是一款產品的勝利，更是市場溝通策略的升級。</p>
    <ul>
        <li><strong>聲量先行：</strong>在投入大量轉換廣告前，先集中資源創造口碑。</li>
        <li><strong>情境觸發：</strong>敏銳抓住時事（長榮空姐），將專業需求轉嫁到大眾市場。</li>
        <li><strong>信任疊加：</strong>結合「媒體」、「KOL」、「素人」三方背書。</li>
        <li><strong>全通路整合：</strong>線上廣告與線下門市緊密配合，O2O 導流順暢。</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 DK White Sneaker Strategy Review | Created with Streamlit")
