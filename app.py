import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Portafolio", page_icon="✨", layout="wide")

# =========================
# 🎨 ESTILO PERSONALIZADO
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
        font-family: 'Arial';
    }

    p {
        color: #3A3A3A;
    }

    .card {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #E6D7D0;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.05);
        height: 180px;
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
st.title("✨ Mi Portafolio")
st.markdown("<p class='tagline'>Minimalista · Moderno · Proyectos en Streamlit</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# BUSCADOR
# =========================
search = st.text_input("🔎 Buscar proyecto")

# =========================
# 📦 APPS
# =========================
apps = [
    {
        "name": "App 1",
        "url": "https://tu-app-1.streamlit.app",
       
    },
    {
        "name": "App 2",
        "url": "https://tu-app-2.streamlit.app",
        
    },
    {
        "name": "App 3",
        "url": "https://tu-app-3.streamlit.app",
        
    },
     {
        "name": "App 1",
        "url": "https://tu-app-1.streamlit.app",
       
    },
     {
        "name": "App 1",
        "url": "https://tu-app-1.streamlit.app",
       
    },

    # 👉 duplica hasta 20
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
                <h4 style="color:#4B1E2F;">{app['name']}</h4>
                <p>{app['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("")

        st.link_button("🔗 Ver proyecto", app["url"])
        st.link_button("💻 GitHub", app["github"])

        st.markdown("<br>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#7A2E3A;'>Hecho con ❤️ · Portafolio personal</p>",
    unsafe_allow_html=True
)
