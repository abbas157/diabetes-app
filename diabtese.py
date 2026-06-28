import streamlit as st
import pandas as pd
import numpy as np

# صفحے کی سیٹنگ
st.set_page_config(page_title="ذیابیطس ڈیٹا گراف", layout="wide")

st.title("📊 ذیابیطس کے مریضوں کا ڈیٹا اور گراف")
st.write("یہاں آپ دیکھ سکتے ہیں کہ مختلف مریضوں کی عمروں اور ان کے شوگر لیول میں کیا تعلق ہے۔")

st.markdown("---")

# 1. فرضی ڈیٹا بنانا تاکہ گراف بن سکے
# ہم 20 مریضوں کا فرضی ڈیٹا بنا رہے ہیں
np.random.seed(42)
data = pd.DataFrame({
    'عمر (Age)': np.random.randint(20, 70, 20),
    'گلوکوز لیول (Glucose)': np.random.randint(80, 200, 20),
    'مریض کا نمبر': range(1, 21)
})
# ڈیٹا کو عمر کے حساب سے ترتیب دینا
data = data.sort_values(by='عمر (Age)')

# 2. سکرین پر ڈیٹا کا ٹیبل دکھانا
st.subheader("📋 مریضوں کا فرضی ریکارڈ")
st.dataframe(data.set_index('مریض کا نمبر'), use_container_width=True)

st.markdown("---")

# 3. سکرین کو دو حصوں (Columns) میں بانٹنا تاکہ دو گراف ساتھ ساتھ نظر آئیں
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 عمر کے حساب سے گلوکوز لیول (Line Chart)")
    st.write("اس گراف میں آپ دیکھ سکتے ہیں کہ جیسے جیسے عمر بڑھتی ہے، گلوکوز لیول میں کیا تبدیلی آتی ہے۔")
    # سٹریم لٹ کا اپنا لائن چارٹ بنانا
    st.line_chart(data, x='عمر (Age)', y='گلوکوز لیول (Glucose)', height=350)

with col2:
    st.subheader("📊 ہر مریض کا گلوکوز لیول (Bar Chart)")
    st.write("یہ گراف ہر ایک مریض کا انفرادی شوگر لیول سیدھے ڈبوں (Bars) کی شکل میں دکھاتا ہے۔")
    # سٹریم لٹ کا اپنا بار چارٹ بنانا
    st.bar_chart(data, x='مریض کا نمبر', y='گلوکوز لیول (Glucose)', height=350)

st.success("✅ یہ گراف کامیابی سے بن گئے ہیں!")
