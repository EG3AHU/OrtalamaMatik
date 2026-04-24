import streamlit as st
import scipy.stats as stats
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="MIS Not Hesaplayıcı | حاسبة درجات MIS", layout="centered", page_icon="🎓")

# دالة توليد الصورة
def create_result_image(current_score, target_score, required_final, expected_final, total_expected, lang_code):
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor('#f0f2f6')
    ax.axis('off')
    
    if lang_code == "TR":
        title = "MIS Not Raporu"
        text = (f"Su anki Puaniniz: {current_score:.2f} / 100\n\n"
                f"Hedeflenen Toplam Not: {target_score}\n"
                f"Finalde Gereken Not: {required_final:.1f}\n\n"
                f"Beklenen Final Notu: {expected_final}\n"
                f"Tahmini Donem Sonu Notu: {total_expected:.2f}")
    else:
        title = "MIS Grade Report"
        text = (f"Current Points: {current_score:.2f} / 100\n\n"
                f"Target Total Score: {target_score}\n"
                f"Required in Final: {required_final:.1f}\n\n"
                f"Expected Final Score: {expected_final}\n"
                f"Estimated Total Grade: {total_expected:.2f}")

    # رسم النصوص على الصورة
    ax.text(0.5, 0.9, title, ha='center', va='center', fontsize=18, weight='bold', color='#1f77b4')
    ax.text(0.5, 0.4, text, ha='center', va='center', fontsize=14, color='#333333', 
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='#cccccc', boxstyle='round,pad=1'))

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=200)
    buf.seek(0)
    plt.close(fig)
    return buf

# قاموس اللغات
translations = {
    "Türkçe (TR)": {"code": "TR", "title": "🎓 Üniversite Not Hesaplayıcı", "desc": "Dersin mevcut durumunu ve geçmek için finalde kaç alman gerektiğini öğren.", "dist_title": "1. Not Dağılımı (%)", "w_ara": "Ara Sınav Ağırlığı (%)", "w_final": "Final Ağırlığı (%)", "w_uyg": "Uygulama Ağırlığı (%)", "num_odev": "Ödev Sayısı", "w_odev": "Ödev {} Ağırlığı (%)", "err_total": "⚠️ Mevcut toplam %{}!", "succ_total": "✅ Oranların toplamı doğru.", "curr_title": "2. Mevcut Notlarınız", "score_ara": "Ara Sınav Notunuz", "avg_ara": "Ara Sınav Sınıf Ortalaması", "score_uyg": "Uygulama Notunuz", "odev_scores_msg": "Ödev Notlarınız:", "score_odev": "Ödev {} Notu", "results_title": "📊 Analiz ve Sonuçlar", "rank_title": "🏆 Ara Sınav Tahmini Sıralamanız", "rank_info": "Notunuz ( {} ) ve Ortalaması ( {} ) ile:", "rank_stats": "📈 Sınıfın **%{}**'ini geride bıraktınız!", "rank_succ": "Tebrikler! Sınıfın en iyileri arasındasınız.", "final_title": "🧮 Finalde Kaç Almanız Gerekiyor?", "curr_points": "Toplanan puan: {} üzerinden **{:.2f}**", "target_score": "Dönem sonu toplam notunuz kaç olsun?", "final_err": "Finalde {:.1f} almanız gerekiyor (İmkansız).", "final_warn": "🎯 **{}** toplamı için finalde gereken: **{:.1f} / 100**", "final_cap": "Not: Dersi geçmek için finalden en az 50 almanız zorunludur.", "calc_title": "🤔 Tahmin Hesaplayıcı", "exp_final": "Finalde kaç bekliyorsunuz?", "exp_err": "⚠️ Finalde {} alırsanız dersten kalırsınız (FF).", "exp_succ": "Genel ortalamanız: **{:.2f} / 100**", "download_btn": "📥 Sonucu Resim Olarak İndir", "download_file": "sonuc_raporu.png"},
    "العربية (AR)": {"code": "EN", "title": "🎓 حاسبة درجات الجامعة", "desc": "اعرف وضعك الحالي ومحتاج كام في الفاينال.", "dist_title": "1. تقسيم الدرجات (%)", "w_ara": "نسبة الميدتيرم (%)", "w_final": "نسبة الفاينال (%)", "w_uyg": "نسبة العملي (%)", "num_odev": "عدد التكليفات", "w_odev": "نسبة Ödev {} (%)", "err_total": "⚠️ المجموع الحالي %{}!", "succ_total": "✅ مجموع النسب مظبوط.", "curr_title": "2. درجاتك الحالية", "score_ara": "درجة الميدتيرم", "avg_ara": "متوسط الميدتيرم", "score_uyg": "درجة العملي", "odev_scores_msg": "درجات التكليفات:", "score_odev": "درجة Ödev {}", "results_title": "📊 تحليلات ونتائج", "rank_title": "🏆 ترتيبك التقريبي", "rank_info": "مع درجتك ( {} ) والمتوسط ( {} ):", "rank_stats": "📈 أنت تتفوق على **%{}** من الدفعة!", "rank_succ": "أنت من أوائل الدفعة!", "final_title": "🧮 محتاج كام في الفاينال؟", "curr_points": "رصيدك: **{:.2f}** من أصل {}", "target_score": "عايز مجموعك النهائي يكون كام؟", "final_err": "محتاج {:.1f} في الفاينال وده مستحيل.", "final_warn": "🎯 عشان توصل لـ **{}**، محتاج: **{:.1f} / 100**", "final_cap": "ملاحظة: لازم 50 في الفاينال عشان تنجح.", "calc_title": "🤔 حاسبة التوقعات", "exp_final": "تتوقع تجيب كام في الفاينال؟", "exp_err": "⚠️ لو جبت {} هتسقط (FF).", "exp_succ": "مجموعك الكلي هيكون: **{:.2f} / 100**", "download_btn": "📥 تحميل النتيجة كصورة", "download_file": "grade_report.png"},
    "English (EN)": {"code": "EN", "title": "🎓 Grade Calculator", "desc": "Calculate your standing and required final score.", "dist_title": "1. Grade Weights (%)", "w_ara": "Midterm Weight (%)", "w_final": "Final Weight (%)", "w_uyg": "Lab Weight (%)", "num_odev": "Number of Assignments", "w_odev": "Assignment {} Weight (%)", "err_total": "⚠️ Total is {}%!", "succ_total": "✅ Weights total 100%.", "curr_title": "2. Current Grades", "score_ara": "Midterm Grade", "avg_ara": "Midterm Average", "score_uyg": "Lab Grade", "odev_scores_msg": "Assignment Grades:", "score_odev": "Assignment {} Grade", "results_title": "📊 Results", "rank_title": "🏆 Estimated Rank", "rank_info": "Grade ( {} ) vs Average ( {} ):", "rank_stats": "📈 You beat **{}%** of the class!", "rank_succ": "Top of the class!", "final_title": "🧮 Required Final Score", "curr_points": "Points: **{:.2f}** / {}", "target_score": "Target total score?", "final_err": "Need {:.1f} on final (Impossible).", "final_warn": "🎯 For **{}**, you need: **{:.1f} / 100**", "final_cap": "Note: Minimum 50 required on final.", "calc_title": "🤔 Prediction", "exp_final": "Expected final score?", "exp_err": "⚠️ Final of {} means fail (FF).", "exp_succ": "Total grade: **{:.2f} / 100**", "download_btn": "📥 Download Result Image", "download_file": "grade_report.png"}
}

selected_lang = st.selectbox("🌐 Dil / اللغة / Language", ["Türkçe (TR)", "العربية (AR)", "English (EN)"])
t = translations[selected_lang]

if selected_lang == "العربية (AR)":
    st.markdown('<div dir="rtl">', unsafe_allow_html=True)
    st.markdown("""<style>.stNumberInput, .stSlider, .stMarkdown, h1, h2, h3 {text-align: right !important;}</style>""", unsafe_allow_html=True)

st.title(t["title"])
st.markdown(t["desc"])
st.divider()

st.header(t["dist_title"])
col1, col2 = st.columns(2)
with col1:
    w_ara = st.number_input(t["w_ara"], min_value=0, max_value=100, value=30)
    w_final = st.number_input(t["w_final"], min_value=0, max_value=100, value=50)

with col2:
    w_uygulama = st.number_input(t["w_uyg"], min_value=0, max_value=100, value=0)
    num_odevs = st.number_input(t["num_odev"], min_value=0, max_value=5, value=1)

w_odevs = []
if num_odevs > 0:
    cols = st.columns(num_odevs)
    for i in range(num_odevs):
        with cols[i]:
            weight = st.number_input(t["w_odev"].format(i+1), min_value=0, max_value=100, value=20 if num_odevs==1 else 10)
            w_odevs.append(weight)

total_weight = w_ara + w_final + w_uygulama + sum(w_odevs)

if total_weight != 100:
    st.error(t["err_total"].format(total_weight))
else:
    st.success(t["succ_total"])
    st.divider()

    st.header(t["curr_title"])
    col3, col4 = st.columns(2)
    with col3:
        score_ara = st.number_input(t["score_ara"], min_value=0.0, max_value=100.0, value=90.0)
    with col4:
        avg_ara = st.number_input(t["avg_ara"], min_value=0.0, max_value=100.0, value=64.12)

    score_uygulama = 0.0
    if w_uygulama > 0:
        score_uygulama = st.number_input(t["score_uyg"], min_value=0.0, max_value=100.0, value=0.0)

    score_odevs = []
    if num_odevs > 0:
        st.write(t["odev_scores_msg"])
        cols_odev_scores = st.columns(num_odevs)
        for i in range(num_odevs):
            with cols_odev_scores[i]:
                score = st.number_input(t["score_odev"].format(i+1), min_value=0.0, max_value=100.0, value=0.0)
                score_odevs.append(score)
    
    st.divider()

    st.header(t["results_title"])
    
    # 1. الترتيب
    st.subheader(t["rank_title"])
    std_dev = 15.0 
    z_score = (score_ara - avg_ara) / std_dev
    percentile = stats.norm.cdf(z_score) * 100
    
    st.info(t["rank_info"].format(score_ara, avg_ara))
    st.write(t["rank_stats"].format(round(percentile, 1)))
    
    # 2. حساب الفاينال
    current_total = (score_ara * w_ara / 100) + (score_uygulama * w_uygulama / 100)
    for i in range(len(score_odevs)):
        current_total += (score_odevs[i] * w_odevs[i] / 100)
        
    st.subheader(t["final_title"])
    st.write(t["curr_points"].format(current_total, 100 - w_final))
    
    target_score = st.slider(t["target_score"], min_value=50, max_value=100, value=60)
    required_in_final = ((target_score - current_total) * 100) / w_final
    actual_required = max(required_in_final, 50.0)
    
    if actual_required > 100:
        st.error(t["final_err"].format(required_in_final))
    else:
        st.warning(t["final_warn"].format(target_score, actual_required))
        if actual_required == 50.0 and required_in_final < 50:
            st.caption(t["final_cap"])
            
    # 3. التوقع
    st.subheader(t["calc_title"])
    expected_final = st.number_input(t["exp_final"], min_value=0.0, max_value=100.0, value=50.0)
    final_expected_total = 0.0
    
    if expected_final < 50:
        st.error(t["exp_err"].format(expected_final))
    else:
        final_expected_total = current_total + (expected_final * w_final / 100)
        st.success(t["exp_succ"].format(final_expected_total))

    st.divider()
    
    # 4. توليد الصورة وزر التحميل
    if expected_final >= 50 and actual_required <= 100:
        img_buffer = create_result_image(current_total, target_score, actual_required, expected_final, final_expected_total, t["code"])
        
        col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
        with col_btn2:
            st.download_button(
                label=t["download_btn"],
                data=img_buffer,
                file_name=t["download_file"],
                mime="image/png",
                use_container_width=True
            )

if selected_lang == "العربية (AR)":
    st.markdown('</div>', unsafe_allow_html=True)