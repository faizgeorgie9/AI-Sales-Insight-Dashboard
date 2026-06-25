from modules.validation import validate_data
from modules.agents import generate_insight
from modules.preprocess import preprocess
from modules.kpi import calculate_kpi
import streamlit as st
import pandas as pd

# ==================================================
# CONFIG PAGE
# ==================================================
st.set_page_config(
    page_title="Sales Insight AI Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Insight AI Dashboard")
st.write("Dashboard  monitoring penjualan dan menghasilkan insight otomatis.")

# ==================================================
# UPLOAD FILE
# ==================================================
uploaded_file = st.file_uploader(
    "Upload Data Penjualan",
    type=["xlsx", "csv"]
)

if uploaded_file is not None:

    # ==================================================
    # LOAD DATA
    # ==================================================
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    st.success(f"Data berhasil dimuat ({len(df)} transaksi)")

    # ==================================================
    # VALIDASI DATA
    # ==================================================
    errors = validate_data(df)

    if len(errors) > 0:
        st.error("Terdapat kesalahan pada data:")

        for error in errors:
            st.error(error)

        st.stop()

    st.success("✅ Data valid")

    # ==================================================
    # PREPROCESSING
    # ==================================================
    df = preprocess(df)

    # ==================================================
    # PREVIEW DATA
    # ==================================================
    with st.expander("Preview Data"):
        st.dataframe(df)

    # ==================================================
    # KPI
    # ==================================================
    total_omzet, total_target, achievement = calculate_kpi(df)

    st.header("📊 KPI Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Omzet",
            f"Rp {total_omzet:,.0f}"
        )

    with col2:
        st.metric(
            "Target Penjualan",
            f"Rp {total_target:,.0f}"
        )

    with col3:
        st.metric(
            "Achievement",
            f"{achievement:.2f}%"
        )

    # ==================================================
    # TREND PENJUALAN
    # ==================================================
    st.header("📈 Trend Penjualan")

    daily_sales = (
        df.groupby("Tanggal")["Omzet"]
        .sum()
    )

    st.line_chart(daily_sales)

    # ==================================================
    # TOP CUSTOMER
    # ==================================================
    top_customer = (
        df.groupby("Customer")["Omzet"]
        .sum()
        .sort_values(ascending=False)
    )

    # ==================================================
    # TOP PRODUCT
    # ==================================================
    top_product = (
        df.groupby("Produk")["Omzet"]
        .sum()
        .sort_values(ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top Customer")
        st.bar_chart(top_customer.head(10))

    with col2:
        st.subheader("📦 Top Product")
        st.bar_chart(top_product.head(10))

    # ==================================================
    # SALES PERFORMANCE
    # ==================================================
    sales_perf = (
        df.groupby("Sales")["Omzet"]
        .sum()
        .sort_values(ascending=False)
    )

    st.header("👨‍💼 Sales Performance")

    st.bar_chart(sales_perf)

    # ==================================================
    # AI INSIGHT
    # ==================================================
    st.header("🤖 AI Sales Assistant")

    question = st.text_area(
        "Tanyakan sesuatu mengenai data penjualan"
    )

    if st.button("Generate Insight"):

        with st.spinner("Analyzing data..."):

            answer = generate_insight(
                question,
                df
            )

        st.success(answer)

else:
    st.info("Silakan upload file Excel atau CSV untuk memulai.")