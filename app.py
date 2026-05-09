import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Portafolio Salomé", page_icon="✨", layout="wide")

# =========================
# 🎨 ESTILO MINIMALISTA BORGOÑA / CREMA
# =========================
st.markdown(
    """
    <style>
    body {
        background-color: #F7F1E3;
    }

    .main {
        background-color: #F7F1E3;
    }

    h1, h2, h3, h4 {
        color: #4B1E2F;
        font-family: Arial;
    }

    p {
        color: #3A3A3A;
    }

    .card {
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 14px;
        border: 1px solid #E6D7D0;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.05);
        height: 160px;
    }

    .tagline {
        color: #7A2E3A;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================
st.title("✨ Portafolio de Salomé Rivero")
st.markdown("<p class='tagline'>Proyectos en Python · Streamlit · IA · Data</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# BUSCADOR
# =========================
search = st.text_input("🔎 Buscar proyecto")

# =========================
# APPS
# =========================
apps = [
    {"name": "Yolo", "description": "Detección de objetos con YOLO", "url": "https://yolov5srd.streamlit.app/"},
    {"name": "WordCloud", "description": "Generador de nubes de palabras", "url": "https://wordcloudsrd.streamlit.app/"},
    {"name": "Vision App", "description": "Procesamiento de visión por computador", "url": "https://visionappsalorivero.streamlit.app/"},
    {"name": "Voz a Texto", "description": "Conversión de voz a texto", "url": "https://traductorvozatextosrd.streamlit.app/"},
    {"name": "TF-IDF Inglés", "description": "Análisis de texto en inglés", "url": "https://tfidfsrd.streamlit.app/"},
    {"name": "Texto a Audio", "description": "Convierte texto en audio", "url": "https://textoaudio2.streamlit.app/"},
    {"name": "TF-IDF Español", "description": "Análisis de texto en español", "url": "https://tdfespsrd.streamlit.app/"},
    {"name": "Sentimientos", "description": "Análisis de sentimientos", "url": "https://sentimentasalo.streamlit.app/"},
    {"name": "Send MQTT", "description": "Comunicación MQTT", "url": "https://sendcmqttsalorive.streamlit.app/"},
    {"name": "OCR", "description": "Reconocimiento óptico de caracteres", "url": "https://ocrsalorivero.streamlit.app/"},
    {"name": "OCR Audio", "description": "OCR + salida en audio", "url": "https://ocraudiosrd.streamlit.app/"},
    {"name": "Intro", "description": "App introductoria", "url": "https://introprofesrd.streamlit.app/"},
    {"name": "Dígitos Mano", "description": "Reconocimiento de dígitos escritos a mano", "url": "https://handwsrd.streamlit.app/"},
    {"name": "Draw / Tablero", "description": "Reconocimiento de dibujos", "url": "https://drawrecogsrd.streamlit.app/"},
    {"name": "Detector Gestos", "description": "Detección de gestos", "url": "https://detecgestossr.streamlit.app/"},
    {"name": "Control por Voz", "description": "Control de comandos por voz", "url": "https://ctrlvoicesrd.streamlit.app/"},
    {"name": "RAG", "description": "Chat con documentos (RAG)", "url": "https://chatpdfsalorivero.streamlit.app/"},
    {"name": "Mi App (Portafolio)", "description": "Portafolio principal", "url": "https://salolamejor.streamlit.app/"}
]

# =========================
# FILTRO
# =========================
if search:
    apps = [
        a for a in apps
        if search.lower() in a["name"].lower()
        or search.lower() in a["description"].lower()
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
                <p>{app['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button("🔗 Ver App", app["url"])

        st.markdown("<br>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("<p style='text-align:center; color:#7A2E3A;'>Hecho con ❤️ por Salomé Rivero</p>", unsafe_allow_html=True)
