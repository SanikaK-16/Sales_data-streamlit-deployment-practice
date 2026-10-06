import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Predictor",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #0b1120;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .header {
        background: linear-gradient(135deg, #111827, #172554);
        border: 1px solid #1e3a8a;
        border-radius: 20px;
        padding: 32px 35px;
        margin-bottom: 25px;
    }

    .header-title {
        font-size: 36px;
        font-weight: 750;
        color: #ffffff;
        margin-bottom: 7px;
    }

    .header-subtitle {
        color: #94a3b8;
        font-size: 15px;
    }

    /* Metric cards */
    .metric-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 22px;
        min-height: 115px;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 13px;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 27px;
        font-weight: 700;
    }

    /* Section headings */
    .section-title {
        color: #f8fafc;
        font-size: 21px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 13px;
        margin-top: -8px;
        margin-bottom: 18px;
    }

    /* Prediction container */
    .prediction-card {
        background: linear-gradient(135deg, #111827, #172554);
        border: 1px solid #2563eb;
        border-radius: 20px;
        padding: 30px;
    }

    .prediction-label {
        color: #93c5fd;
        font-size: 14px;
    }

    .prediction-value {
        color: #ffffff;
        font-size: 42px;
        font-weight: 750;
        margin: 8px 0;
    }

    .prediction-description {
        color: #94a3b8;
        font-size: 13px;
    }

    /* Info box */
    .info-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 20px;
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #475569;
        font-size: 12px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #1f2937;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("sales_data.csv")


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

X = df[["advertising_spend"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)


st.title("📈 Sales Predictor")
st.caption("Sales insights and prediction powered by machine learning.")

# --------------------------------------------------
# SUMMARY CARDS
# --------------------------------------------------

avg_sales = df["sales"].mean()
highest_sales = df["sales"].max()
avg_spend = df["advertising_spend"].mean()
total_records = len(df)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Sales</div>
        <div class="metric-value">{avg_sales:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Highest Sales</div>
        <div class="metric-value">{highest_sales:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Ad Spend</div>
        <div class="metric-value">{avg_spend:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Records Analyzed</div>
        <div class="metric-value">{total_records}</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# SALES GRAPH
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Sales Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Sales trend across the available records</div>',
    unsafe_allow_html=True
)

chart_data = df[["sales"]]

st.line_chart(
    chart_data,
    height=330
)


# --------------------------------------------------
# ADVERTISING VS SALES
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Advertising Spend vs Sales</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Relationship between advertising investment and sales</div>',
    unsafe_allow_html=True
)

scatter_data = df[["advertising_spend", "sales"]].set_index(
    "advertising_spend"
)

st.line_chart(
    scatter_data,
    height=280
)


# --------------------------------------------------
# PREDICTION SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🔮 Predict Your Sales</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Enter your advertising budget to estimate your expected sales.'
    '</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1.3])

# --------------------------------------------------
# INPUT
# --------------------------------------------------

with left:

    st.write("### Advertising Budget")

    spend = st.number_input(
        "Enter amount",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=5.0,
        format="%.2f"
    )

    st.caption(
        "Enter the amount you plan to spend on advertising."
    )

    predict_button = st.button(
        "🔮 Predict Sales",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# RESULT
# --------------------------------------------------

with right:

    if predict_button:

        prediction = model.predict([[spend]])[0]

        st.success(
            f"Estimated sales: **{prediction:.2f}**"
        )

        st.metric(
            label="Predicted Sales",
            value=f"{prediction:.2f}"
        )

        st.caption(
            f"Based on an advertising budget of {spend:.2f}"
        )

    else:

        st.info(
            "Enter your advertising budget and click "
            "**Predict Sales** to see the estimated result."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    Sales Predictor • Built with Python, Streamlit & Scikit-learn
</div>
""", unsafe_allow_html=True)