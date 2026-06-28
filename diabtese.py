import streamlit as st
import numpy as np
import time

# پیج کی سیٹنگز
st.set_page_config(page_title="ذیابیطس چیک اپ", page_icon="🩺")

# ایپ کا عنوان اور تعارف
st.title("ذیابیطس کی تشخیص کی ایپ 🩺")
st.write("یہ ایپ آپ کی دی گئی معلومات کی بنیاد پر ذیابیطس کے خطرے کا اندازہ لگاتی ہے۔")

st.markdown("---") # یہ ایک لائن لگائے گا

# یوزر سے معلومات لینے کے لیے دو حصے (Columns) بنانا
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("حمل کی تعداد (Pregnancies)", min_value=0, max_value=20, value=0)
    glucose = st.number_input("گلوکوز لیول (Glucose)", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("بلڈ پریشر (Blood Pressure)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("جلد کی موٹائی (Skin Thickness)", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("انسولین (Insulin)", min_value=0, max_value=1000, value=79)
    bmi = st.number_input("بی ایم آئی (BMI)", min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree = st.number_input("خاندانی ذیابیطس (Pedigree)", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("عمر (Age)", min_value=1, max_value=120, value=33)

st.markdown("---")

# پیشین گوئی کرنے والا بٹن
if st.button("ذیابیطس کا خطرہ چیک کریں", use_container_width=True):
    
    # یہ تھوڑا انتظار کروائے گا تاکہ اصلی مشین لرننگ کا احساس ہو
    with st.spinner('ڈیٹا چیک کیا جا رہا ہے...'):
        time.sleep(2)
    
    st.subheader("نتیجہ:")
    
    # یہ ایک فرضی فارمولا ہے جو عارضی طور پر جواب دے گا
    # (بعد میں ہم اسے آپ کی اصل ماڈل کی فائل سے بدل دیں گے)
    risk_score = (glucose * 0.4) + (bmi * 0.3) + (age * 0.2)
    
    if risk_score > 75: # یہ ایک فرضی حد ہے
        st.error("⚠️ ہوشیار رہیں! دی گئی معلومات کے مطابق آپ کو ذیابیطس کا خطرہ ہو سکتا ہے۔ براہ کرم ڈاکٹر سے رجوع کریں۔")
    else:
        st.success("✅ مبارک ہو! دی گئی معلومات کے مطابق فی الحال آپ کو ذیابیطس کا خطرہ نظر نہیں آ رہا۔")

st.caption("نوٹ: یہ فی الحال ایک آزمائشی ایپ ہے اور اصلی میڈیکل ٹیسٹ کا متبادل نہیں ہے۔")
