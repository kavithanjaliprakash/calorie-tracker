"""Phase 0 check page: proves hosting, secrets, database, Gemini and phone camera all work.

Replace this with the real Today screen in Phase 3.
"""
import streamlit as st

st.set_page_config(page_title="Calorie Tracker", page_icon="🥗", layout="centered")

st.title("Calorie Tracker")
st.write("Hello! Phase 0 setup check.")

# 1. Secrets ---------------------------------------------------------------
st.subheader("1. Secrets")
missing = [k for k in ("NEON_DATABASE_URL", "GEMINI_API_KEY", "GEMINI_MODEL") if k not in st.secrets]
if missing:
    st.error(f"Missing secrets: {', '.join(missing)}")
else:
    st.success("All secrets found.")

# 2. Database ---------------------------------------------------------------
st.subheader("2. Neon database")
if st.button("Test database connection"):
    try:
        import psycopg2

        with psycopg2.connect(st.secrets["NEON_DATABASE_URL"]) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                st.success("Connected: " + cur.fetchone()[0][:60] + "…")
    except Exception as e:
        st.error(f"Database error: {e}")

# 3. Gemini -----------------------------------------------------------------
st.subheader("3. Gemini")
if st.button("Test Gemini"):
    try:
        from google import genai

        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        resp = client.models.generate_content(
            model=st.secrets["GEMINI_MODEL"],
            contents="Reply with exactly: Gemini is working",
        )
        st.success(resp.text)
    except Exception as e:
        st.error(f"Gemini error: {e}")

# 4. Phone camera -----------------------------------------------------------
st.subheader("4. Camera (try this on your phone)")
tab_cam, tab_upload = st.tabs(["Take photo", "Upload photo"])
with tab_cam:
    photo = st.camera_input("Take a picture of a snack pack")
    if photo:
        st.image(photo, caption="Captured with camera_input")
with tab_upload:
    upload = st.file_uploader("Or upload / use your phone camera", type=["jpg", "jpeg", "png"])
    if upload:
        st.image(upload, caption="Uploaded photo")
st.caption("Compare the two: which opens the back camera, and which gives a sharper label?")
