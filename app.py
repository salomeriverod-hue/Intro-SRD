import streamlit as st

st.set_page_config(page_title="Portafolio Salomé", page_icon="✨", layout="wide")

# =========================
# 🎨 ESTILO PRO
# =========================
st.markdown(
    """
    <style>

    body {
        background-color: #F6F1E8;
    }

    .main {
        background-color: #F6F1E8;
    }

    /* HERO */
    .hero {
        background: linear-gradient(135deg, #4B1E2F, #7A2E3A);
        padding: 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    }

    .hero h1 {
        color: white;
        font-size: 42px;
        margin-bottom: 5px;
    }

    .hero p {
        color: #F3E9E2;
        font-size: 18px;
    }

    /* CARD */
    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #E8DCD3;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.06);
        transition: transform 0.2s ease;
        height: 170px;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .card h4 {
        color: #4B1E2F;
        margin-bottom: 8px;
    }

    .card p {
        color: #555;
        font-size: 14px;
    }

    /* TAG */
    .tag {
        display: inline-block;
        background: #7A2E3A;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HERO SECTION
# =========================
st.markdown(
    """
    <div class="hero">
        <h1>✨ Salomé Rivero</h1>
        <p>Portafolio de proyectos en Inteligencia Artificial · Python · Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# BUSCADOR
# =========================
search = st.text_input("🔎 Buscar proyecto")

# =========================
# APPS
# =========================
apps = [
    {"name": "Yolo", "desc": "Detección de objetos con YOLO", "url": "https://yolov5srd.streamlit.app/"},
    {"name": "WordCloud", "desc": "Nube de palabras automática", "url": "https://wordcloudsrd.streamlit.app/"},
    {"name": "Vision App", "desc": "Procesamiento de imágenes", "url": "https://visionappsalorivero.streamlit.app/"},
    {"name": "Voz a Texto", "desc": "Convierte voz en texto", "url": "https://traductorvozatextosrd.streamlit.app/"},
    {"name": "TF-IDF EN", "desc": "Análisis de texto en inglés", "url": "https://tfidfsrd.streamlit.app/"},
    {"name": "Texto a Audio", "desc": "Texto convertido a voz", "url": "https://textoaudio2.streamlit.app/"},
    {"name": "Sentimientos", "desc": "Análisis emocional de texto", "url": "https://sentimentasalo.streamlit.app/"},
    {"name": "OCR", "desc": "Reconocimiento de texto en imágenes", "url": "https://ocrsalorivero.streamlit.app/"},
    {"name": "Control por Voz", "desc": "Interacción por comandos de voz", "url": "https://ctrlvoicesrd.streamlit.app/"},
    {"name": "RAG Chat", "desc": "Chat con documentos inteligentes", "url": "https://chatpdfsalorivero.streamlit.app/"},
]

# =========================
# FILTRO
# =========================
if search:
    apps = [
        a for a in apps
        if search.lower() in a["name"].lower()
        or search.lower() in a["desc"].lower()
    ]

# =========================
# GRID
# =========================
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <h4>{app['name']}</h4>
                <p>{app['desc']}</p>
                <div class="tag">Ver proyecto →</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button("🚀 Abrir App", app["url"])

        st.markdown("<br>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#7A2E3A;'>Hecho con ❤️ · Portafolio IA & Data</p>",
    unsafe_allow_html=True
)
