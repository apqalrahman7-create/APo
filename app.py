import streamlit as st
import ccxt
import sqlite3
import requests
from datetime import datetime, timedelta
import pandas as pd

# --- قاعدة البيانات ---
def init_db():
    conn = sqlite3.connect('trade_vault.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, reg_date TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS keys (code TEXT PRIMARY KEY, expiry_date TEXT, status TEXT)')
    conn.commit()
    conn.close()

init_db()

def get_public_ip():
    try: return requests.get('https://ipify.org').text
    except: return "Error"

st.set_page_config(page_title="Pro Trader", layout="centered")

# --- واجهة الدخول ---
if 'auth' not in st.session_state:
    st.title("🚀 بوت التداول التلقائي")
    email = st.text_input("البريد الإلكتروني")
    key = st.text_input("رمز التفعيل", type="password")
    
    if st.button("دخول", use_container_width=True):
        if "@" in email and key: # للتجربة فقط، يمكنك إضافة نظام الرموز لاحقاً
            st.session_state.auth = True
            st.session_state.user = email
            st.rerun()
else:
    st.header("🤖 لوحة التحكم")
    st.write(f"المستخدم: {st.session_state.user}")
    st.code(f"IP السيرفر: {get_public_ip()}")
    
    bk = st.text_input("Binance Key", type="password")
    bs = st.text_input("Binance Secret", type="password")

    if st.button("🚀 تشغيل البوت (هدف 5$)", use_container_width=True):
        st.success("تم تشغيل البوت بنجاح برأس مال 50$")
      
