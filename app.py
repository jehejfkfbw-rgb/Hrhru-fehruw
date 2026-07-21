import streamlit as st

# إعدادات الصفحة وعنوان المتصفح
st.set_page_config(
    page_title="خدماتنا الرقمية - حلول متكاملة",
    page_icon="💻",
    layout="centered"
)

# تصميم وتنسيق الواجهة العامة (تتأقلم مع جميع الشاشات والموبايل واللابتوب)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at top, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    
    .hero-container {
        text-align: center;
        padding: 20px 10px;
        margin-bottom: 10px;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #00ff87);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #cfd8dc;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .service-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .service-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
        text-align: right;
    }
    
    .service-list {
        list-style: none;
        padding: 0;
        margin: 0 0 15px 0;
    }
    
    .service-list li {
        font-size: 0.9rem;
        color: #b0bec5;
        margin-bottom: 6px;
        position: relative;
        padding-right: 18px;
        text-align: right;
    }
    
    .service-list li::before {
        content: "✔";
        position: absolute;
        right: 0;
        color: #00ff87;
        font-size: 0.8rem;
    }
    
    .price-box {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 12px;
    }
    
    .price-label {
        font-size: 0.75rem;
        color: #90a4ae;
        display: block;
    }
    
    .price-value {
        font-size: 1.3rem;
        font-weight: 900;
        color: #00ff87;
    }
    
    .whatsapp-btn {
        display: block;
        background: linear-gradient(135deg, #25d366, #128c7e);
        color: white !important;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
    }
    
    .contact-footer {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    
    .phone-number {
        font-size: 1.6rem;
        font-weight: 900;
        color: #00f2fe;
        letter-spacing: 2px;
        margin: 8px 0;
        direction: ltr;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">خدماتنا الرقمية</h1>
    <p class="hero-subtitle">حلول برمجية وتصميمية متكاملة لرفع كفاءة نجاح مشروعك</p>
</div>
""", unsafe_allow_html=True)

# رقم الواتساب الموحد
phone_number = "201213783090"

# تقسيم الشاشة إلى عمودين (يتكيف بذكاء مع الموبايل ليصبحوا عموداً واحداً تلقائياً)
col1, col2 = st.columns(2, gap="medium")

with col1:
    msg1 = "مرحباً، أرغب في الاستفسار عن خدمة تصميم وتطوير مواقع الويب (تبدأ من 2,500 جنيه)."
    st.markdown(f"""
    <div class="service-card">
        <div>
            <div class="service-title">🌐 01. تصميم وتطوير مواقع الويب</div>
            <ul class="service-list">
                <li>تصميم احترافي وعصري متجاوب</li>
                <li>توافق تام مع جميع الأجهزة والشاشات</li>
                <li>سرعة فائقة وأداء عالي الجودة</li>
                <li>تهيئة وتحسين محركات البحث SEO</li>
            </ul>
        </div>
        <div>
            <div class="price-box">
                <span class="price-label">تبدأ الأسعار من</span>
                <span class="price-value">2,500 جنيه</span>
            </div>
            <a href="https://wa.me/{phone_number}?text={msg1}" target="_blank" class="whatsapp-btn">
                💬 اطلب الخدمة عبر الواتساب
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    msg3 = "مرحباً، أرغب في الاستفسار عن خدمة تطوير المتاجر الإلكترونية (تبدأ من 3,500 جنيه)."
    st.markdown(f"""
    <div class="service-card">
        <div>
            <div class="service-title">🛒 03. تطوير المتاجر الإلكترونية</div>
            <ul class="service-list">
                <li>متجر إلكتروني احترافي متكامل</li>
                <li>ربط بوابات الدفع الإلكتروني</li>
                <li>إدارة متطورة للمنتجات والمخزون</li>
                <li>تقارير شاملة ومتابعة دقيقة للمبيعات</li>
            </ul>
        </div>
        <div>
            <div class="price-box">
                <span class="price-label">تبدأ الأسعار من</span>
                <span class="price-value">3,500 جنيه</span>
            </div>
            <a href="https://wa.me/{phone_number}?text={msg3}" target="_blank" class="whatsapp-btn">
                💬 اطلب الخدمة عبر الواتساب
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    msg2 = "مرحباً، أرغب في الاستفسار عن خدمة تطوير تطبيقات أندرويد (تبدأ من 3,000 جنيه)."
    st.markdown(f"""
    <div class="service-card">
        <div>
            <div class="service-title">📱 02. تطوير تطبيقات أندرويد</div>
            <ul class="service-list">
                <li>تطبيقات احترافية بأحدث التقنيات</li>
                <li>تصميم واجهات مستخدم عصرية</li>
                <li>أداء سريع، سلس، وآمن تماماً</li>
                <li>دعم فني وتحديثات مستمرة</li>
            </ul>
        </div>
        <div>
            <div class="price-box">
                <span class="price-label">تبدأ الأسعار من</span>
                <span class="price-value">3,000 جنيه</span>
            </div>
            <a href="https://wa.me/{phone_number}?text={msg2}" target="_blank" class="whatsapp-btn">
                💬 اطلب الخدمة عبر الواتساب
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    msg4 = "مرحباً، أرغب في الاستفسار عن خدمة الجرافيك ديزاين (تبدأ من 1,500 جنيه)."
    st.markdown(f"""
    <div class="service-card">
        <div>
            <div class="service-title">🎨 04. قسم الجرافيك ديزاين</div>
            <ul class="service-list">
                <li>تصميم شعارات وهوية بصرية كاملة</li>
                <li>تصاميم إعلانية ومنشورات سوشيال ميديا</li>
                <li>تصميم بروفايل شركات وعروض تقديمية</li>
                <li>إبداع فني وجودة طباعة عالية</li>
            </ul>
        </div>
        <div>
            <div class="price-box">
                <span class="price-label">تبدأ الأسعار من</span>
                <span class="price-value">1,500 جنيه</span>
            </div>
            <a href="https://wa.me/{phone_number}?text={msg4}" target="_blank" class="whatsapp-btn">
                💬 اطلب الخدمة عبر الواتساب
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# شريط التواصل السفلي
st.markdown(f"""
<div class="contact-footer">
    <h3>📞 تواصل معنا مباشرة الآن</h3>
    <div class="phone-number">01213783090</div>
    <p style="color: #90a4ae; margin-bottom: 12px; font-size: 0.9rem;">نحن جاهزون للرد على كافة استفساراتكم وتنفيذ مشاريعكم بكفاءة عالية</p>
    <a href="https://wa.me/{phone_number}?text=مرحباً، تواصلت معكم من الموقع وأرغب في الاستفسار عن الخدمات." target="_blank" class="whatsapp-btn" style="max-width: 260px; margin: 0 auto; font-size: 1rem;">
        💬 تواصل معنا عبر واتساب
    </a>
</div>
""", unsafe_allow_html=True)
