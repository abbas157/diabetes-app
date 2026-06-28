import streamlit as st
import pandas as pd
import pickle # یا joblib اگر آپ نے وہ استعمال کیا تھا
import numpy as np

# یہاں ہم اپنا ماڈل لوڈ کر رہے ہیں (فرض کریں آپ کی فائل کا نام model.pkl ہے)
# اگر آپ کی فائل کا نام کچھ اور ہے تو یہاں وہ نام لکھیں
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("ماڈل کی فائل نہیں ملی! براہ کرم چیک کریں کہ آپ نے GitHub پر ماڈل کی فائل اپلوڈ کی ہے یا نہیں۔")
    st.stop()


# ایپ کا عنوان
st.title("ذیابیطس کی تشخیص کی ایپ 🩺")
st.write("یہ ایپ مشین لرننگ کا استعمال کرتے ہوئے ذیابیطس کا خطرہ بتاتی ہے۔")

# یوزر سے معلومات لینے کے لیے خانے بنانا
st.header("اپنی معلومات درج کریں:")

# یہ وہ عام چیزیں ہیں جو ذیابیطس کے ڈیٹا میں ہوتی ہیں۔ آپ اپنے ڈیٹا کے حساب سے انہیں بدل سکتے ہیں۔
pregnancies = st.number_input("Pregnancies (حمل کی تعداد)", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose (گلوکوز لیول)", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure (بلڈ پریشر)", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness (جلد کی موٹائی)", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin (انسولین)", min_value=0, max_value=1000, value=79)
bmi = st.number_input("BMI (بی ایم آئی)", min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age (عمر)", min_value=1, max_value=120, value=33)

# پیشین گوئی کرنے والا بٹن
if st.button("ذیابیطس کا خطرہ چیک کریں"):
    
    # یوزر کا دیا ہوا ڈیٹا ایک ترتیب میں رکھنا
    user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    # ماڈل سے پیشین گوئی کروانا
    prediction = model.predict(user_data)
    
    st.subheader("نتیجہ:")
    
    # نتیجہ دکھانا
    if prediction[0] == 1:
        st.error("⚠️ ہوشیار رہیں! ماڈل کے مطابق آپ کو ذیابیطس کا خطرہ ہو سکتا ہے۔ براہ کرم ڈاکٹر سے رجوع کریں۔")
    else:
        st.success("✅ مبارک ہو! ماڈل کے مطابق فی الحال آپ کو ذیابیطس کا خطرہ نظر نہیں آ رہا۔")
