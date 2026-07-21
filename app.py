import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="خدماتنا - حلول رقمية متكاملة",
    page_icon="💻",
    layout="centered"
)

# تصميم وتنسيق الـ CSS (Glassmorphism & Custom Style)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .main {
        background: radial-gradient(circle at top left, #12002b, #080015);
    }
    
    .header-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        background: -webkit-linear-gradient(90deg, #38ef7d, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .header-sub {
        text-align: center;
        color: #a0a5c0;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    
    .service-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    .price-tag {
        font-size: 1.3rem;
        font-weight: bold;
        color: #38ef7d;
        margin-top: 10px;
    }
    
    .contact-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50px;
        padding: 15px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<div class="header-title">خدماااتنا</div>', unsafe_allow_html=True)
st.markdown('<div class="header-sub">حلول رقمية متكاملة لنجاح مشروعك</div>', unsafe_allow_html=True)

# محاكاة أو نظام تسجيل الدخول (Google Sign-In simulation / Session State)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.session_state.user_name = ""

if not st.session_state.logged_in:
    st.markdown("### 🔐 تسجيل الدخول لمتابعة الخدمات")
    # زر لتسجيل الدخول بحساب جوجل (افتراضي تجريبي متكامل)
    if st.button(" تسجيل الدخول باستخدام حساب جوجل", use_container_width=True):
        # هنا يتم ربط مكتبة المصادقة الحقيقية لاحقاً
        st.session_state.logged_in = True
        st.session_state.user_email = "mohamed.developer@gmail.com"
        st.session_state.user_name = "محمد (مطور)"
        st.rerun()
else:
    st.success(f"مرحباً بك يا {st.session_state.user_name} 👋 ({st.session_state.user_email})")
    if st.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()

st.write("---")

# عرض الأقسام والخدمات في أعمدة (Columns)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <h3>🌐 تصميم وتطوير مواقع الويب</h3>
        <p>• تصميم احترافي وعصري<br>• متجاوب مع جميع الأجهزة<br>• سرعة وأداء عالٍ<br>• تحسين لمحركات البحث SEO</p>
        <div class="price-tag">تبدأ من 2,500 جنيه</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="service-card">
        <h3>🛒 تطوير المتاجر الإلكترونية</h3>
        <p>• متجر احترافي متكامل<br>• دعم الدفع الإلكتروني<br>• إدارة المنتجات والمخزون<br>• تقارير ومتابعة المبيعات</p>
        <div class="price-tag">تبدأ من 3,500 جنيه</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h3>📱 تطوير تطبيقات أندرويد</h3>
        <p>• تطبيقات احترافية بأحدث التقنيات<br>• تصميم واجهات عصرية<br>• أداء سريع وسلس<br>• دعم وتحديثات مستمرة</p>
        <div class="price-tool" style="display:none"></div>
        <div class="price-tag">تبدأ من 3,000 جنيه</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="service-card">
        <h3>🎨 قسم الجرافيك ديزاين</h3>
        <p>• تصميم شعارات وهوية بصرية<br>• تصاميم إعلانية ومنشورات<br>• تصميم بروفايل وعروض تقديمية<br>• إبداع وجودة عالية</p>
        <div class="price-tag">تبدأ من 1,500 جنيه</div>
    </div>
    """, unsafe_allow_html=True)

# شريط التواصل
st.markdown("""
<div class="contact-box">
    <h3>📞 تواصل معنا الآن</h3>
    <h2 style="color: #00d2ff; direction: ltr;">01213783090</h2>
</div>
""", unsafe_allow_html=True)
