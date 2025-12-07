import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ========= LOAD MODEL, SCALER, FEATURE NAMES, FEATURE STATS =========
model = joblib.load("best_xgb_model.pkl")
scaler = joblib.load("feature_scaler.pkl")
feature_stats = joblib.load("feature_stats.pkl")

with open("feature_names.txt") as f:
    FEATURE_NAMES = [line.strip() for line in f.readlines()]

# ========= FEATURE ENGINEERING (MUST MATCH NOTEBOOK) =========
def build_feature_vector(user_input: dict) -> pd.DataFrame:
    df_row = pd.DataFrame([user_input])

    # same extra features as notebook
    df_row["followers_log"] = np.log1p(df_row["followers"])
    df_row["hashtag_density"] = df_row["num_hashtags"] / (df_row["content_length"] + 1)
    df_row["account_age_years"] = df_row["account_age_days"] / 365

    cat_cols = ["platform", "media_type", "topic", "language", "location", "verified"]
    df_row = pd.get_dummies(df_row, columns=cat_cols)

    # ensure all training features exist
    for col in FEATURE_NAMES:
        if col not in df_row.columns:
            df_row[col] = 0

    df_row = df_row[FEATURE_NAMES]
    df_row = df_row.fillna(df_row.median(numeric_only=True))

    return df_row

# ========= FEATURE SCORING FUNCTION =========
def score_feature(value, stats, direction="higher_is_better"):
    """Score a feature based on dataset distribution.
    
    Returns:
        -2: really weak (below 25th percentile when higher is better)
        -1: slightly weak (below median)
         0: okay (below 75th percentile)
         1: above average
    """
    p25 = stats["p25"]
    median = stats["median"]
    p75 = stats["p75"]

    if direction == "higher_is_better":
        if value < p25:
            return -2
        elif value < median:
            return -1
        elif value < p75:
            return 0
        else:
            return 1
    else:  # lower is better (not used yet but nice to have)
        if value > p75:
            return -2
        elif value > median:
            return -1
        elif value > p25:
            return 0
        else:
            return 1

# ========= SMART TIPS GENERATOR =========
def generate_tips(features: dict, prob: float):
    """Generate data-driven recommendations based on feature distribution."""
    scores = {}

    # Score each numeric feature vs your dataset
    scores["followers"] = score_feature(
        features["followers"],
        feature_stats["followers"],
        direction="higher_is_better",
    )

    scores["account_age_days"] = score_feature(
        features["account_age_days"],
        feature_stats["account_age_days"],
        direction="higher_is_better",
    )

    scores["content_length"] = score_feature(
        features["content_length"],
        feature_stats["content_length"],
        direction="higher_is_better",
    )

    scores["num_hashtags"] = score_feature(
        features["num_hashtags"],
        feature_stats["num_hashtags"],
        direction="higher_is_better",
    )

    # Pick the weakest ones (most negative scores)
    weak_features = [f for f, s in scores.items() if s < 0]
    weak_features.sort(key=lambda f: scores[f])  # most negative first

    tips = []

    # Map each feature + score bucket to messages
    for feat in weak_features[:3]:  # at most 3 tips
        s = scores[feat]

        if feat == "followers":
            if s == -2:
                tips.append(
                    "Akunmu tergolong kecil dibanding dataset. Fokus dulu ke growth: collab, niche konten, dan konsistensi upload."
                )
            elif s == -1:
                tips.append(
                    "Followers-mu sedikit di bawah median. Tambah CTA follow dan manfaatkan niche hashtag & komunitas."
                )

        elif feat == "account_age_days":
            if s == -2:
                tips.append(
                    "Akun masih sangat baru. Algoritma kadang butuh waktu; jaga konsistensi posting biar sinyal trust kebentuk."
                )
            elif s == -1:
                tips.append(
                    "Akun relatif muda. Pastikan bio, profile picture, dan grid feed rapi supaya orang lebih mau follow & engage."
                )

        elif feat == "content_length":
            if s == -2:
                tips.append(
                    "Caption-mu jauh lebih pendek daripada kebanyakan. Tambahkan hook kuat dan sedikit konteks supaya orang tertarik berhenti scroll."
                )
            elif s == -1:
                tips.append(
                    "Caption agak singkat. Bisa coba tambah 1–2 kalimat yang menjelaskan value/cerita di balik konten."
                )

        elif feat == "num_hashtags":
            if s == -2:
                tips.append(
                    "Hashtag-mu jauh lebih sedikit daripada rata-rata. Coba pakai 3–5 hashtag niche yang relevan dengan konten."
                )
            elif s == -1:
                tips.append(
                    "Jumlah hashtag masih di bawah median. Tambah beberapa hashtag relevan (bukan cuma yang super umum)."
                )

    # If everything is okay-ish, still say something
    if not tips:
        if prob < 0.3:
            tips.append(
                "Setting akun dan metadata kontenmu sudah cukup standar. Untuk konten dengan base chance rendah, fokus di kualitas ide, hook 3 detik pertama, dan storytelling."
            )
        else:
            tips.append(
                "Secara angka kamu udah di atas rata-rata dataset. Eksperimen di sisi konten (thumbnail, hook, angle) bisa jadi pembeda terbesar."
            )

    return tips

# ========= UI =========
st.title("📈 Virality Predictor (Pre-Posting)")

st.subheader("Platform & Content")
platform = st.selectbox("Platform", ["Instagram", "TikTok", "Twitter", "YouTube", "Reddit"])
media_type = st.selectbox("Media Type", ["Image", "Video", "Text"])
topic = st.selectbox("Topic", ["Entertainment", "Education", "Finance", "Sports", "Gaming", "Food", "Lifestyle", "Other"])
language = st.selectbox("Language", ["English", "Spanish", "French", "Indonesian", "Other"])
location = st.selectbox("Location", ["North America", "South America", "Europe", "Asia", "Africa", "Oceania"])

st.subheader("Account & Content Details")
followers = st.number_input("Followers", min_value=0, step=10)
verified = st.checkbox("Verified Account?")
account_age_days = st.number_input("Account Age (days)", min_value=0, step=10)
content_length = st.number_input("Caption Length (characters)", min_value=0, step=5)
num_hashtags = st.number_input("Number of Hashtags", min_value=0, step=1)

if st.button("Hitung Probabilitas Viral"):
    user_input = {
        "platform": platform,
        "media_type": media_type,
        "topic": topic,
        "language": language,
        "location": location,
        "followers": followers,
        "verified": int(verified),
        "account_age_days": account_age_days,
        "content_length": content_length,
        "num_hashtags": num_hashtags,
    }

    X_new = build_feature_vector(user_input)
    X_new_scaled = scaler.transform(X_new)

    prob_viral = float(model.predict_proba(X_new_scaled)[0, 1])

    st.subheader(f"🔮 Probabilitas Viral: {prob_viral*100:.1f}%")

    if prob_viral < 0.8:
        st.markdown("---")
        st.subheader("💡 Rekomendasi buat ningkatin peluang viral")
        tips = generate_tips(user_input, prob_viral)
        for t in tips:
            st.write(f"- {t}")
    else:
        st.markdown("---")
        st.subheader("🔥 Peluang viral konten ini sudah tinggi banget!")
