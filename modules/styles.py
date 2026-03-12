import streamlit as st

class StyleManager:
    @staticmethod
    def apply_styles():
        st.markdown("""
            <style>
            /* 1. Global Reset - Very Dark Slate */
            [data-testid="stAppViewContainer"] {
                background-color: #0d1117 !important;
                color: #c9d1d9 !important;
            }
            
            [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0) !important;
            }

            /* 2. Sidebar - GitHub Dark style */
            [data-testid="stSidebar"] {
                background-color: #010409 !important;
                border-right: 1px solid #30363d !important;
            }
            
            [data-testid="stSidebar"] * {
                color: #8b949e !important;
            }

            /* 3. The Slide Card - Professional & Centered */
            .slide-card {
                margin: 2vh auto;
                padding: 5vh 5vw;
                border-radius: 12px;
                background: #161b22;
                border: 1px solid #30363d;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                min-height: 80vh;
                max-height: 85vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                overflow-y: auto;
            }

            /* 4. Typography - High Contrast, No Fluorescent Colors */
            h1 {
                color: #f0f6fc !important;
                font-size: 3.5rem !important;
                font-weight: 700 !important;
                margin-bottom: 0.8rem !important;
                line-height: 1.2 !important;
            }
            h2 {
                color: #7ee787 !important; /* Soft medical green/teal */
                font-size: 2rem !important;
                font-weight: 300 !important;
                margin-bottom: 1.5rem !important;
            }
            .slide-text {
                font-size: 1.625rem !important;
                line-height: 1.6 !important;
                color: #c9d1d9 !important;
                max-width: 850px;
                margin: 0 auto !important;
            }

            /* 5. Progress & Navigation */
            .stProgress > div > div > div {
                background-color: #238636 !important; /* Success Green */
            }
            
            .stButton>button {
                background-color: #21262d;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 12px 24px;
                transition: 0.2s;
            }
            .stButton>button:hover {
                background-color: #30363d !important;
                border-color: #8b949e !important;
                color: #ffffff !important;
            }

            /* 6. Image Management */
            .stImage img {
                max-height: 40vh !important;
                border-radius: 8px;
                border: 1px solid #30363d;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            }

            /* 7. Hide Junk */
            header, footer, #MainMenu {
                visibility: hidden;
            }
            
            /* Notes Section */
            .notinha {
                background: #0d1117;
                border-left: 4px solid #238636;
                padding: 1.5rem;
                text-align: left;
                font-size: 1.25rem;
                color: #8b949e;
            }
            </style>
        """, unsafe_allow_html=True)
