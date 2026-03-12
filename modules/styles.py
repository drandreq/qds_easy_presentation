import streamlit as st

class StyleManager:
    @staticmethod
    def apply_styles(dark_mode: bool = True):
        # 1. Define Theme Tokens
        if dark_mode:
            # Dark Medical Theme (GitHub-ish)
            bg_app = "#0d1117"
            bg_sidebar = "#010409"
            bg_card = "#161b22"
            text_main = "#c9d1d9"
            text_hdr = "#f0f6fc"
            accent = "#7ee787"  # Medical Green
            border = "#30363d"
            shadow = "rgba(0,0,0,0.6)"
            btn_bg = "#21262d"
            btn_hover = "#30363d"
        else:
            # Light Medical Theme (Clean & Professional)
            bg_app = "#f6f8fa"
            bg_sidebar = "#ffffff"
            bg_card = "#ffffff"
            text_main = "#24292f"
            text_hdr = "#1b1f24"
            accent = "#2da44e"  # Brighter Green
            border = "#d0d7de"
            shadow = "rgba(140, 149, 159, 0.15)"
            btn_bg = "#f3f4f6"
            btn_hover = "#ebecf0"

        st.markdown(f"""
            <style>
            /* 1. Global Reset */
            [data-testid="stAppViewContainer"] {{
                background-color: {bg_app} !important;
                color: {text_main} !important;
            }}
            
            [data-testid="stHeader"] {{
                background-color: rgba(0,0,0,0) !important;
            }}

            /* 2. Sidebar */
            [data-testid="stSidebar"] {{
                background-color: {bg_sidebar} !important;
                border-right: 1px solid {border} !important;
            }}

            /* 3. Viewport-Safe Slide Card */
            [data-testid="stVerticalBlock"] > div > [data-testid="stVerticalBlock"] {{
                padding: 3vh 3vw !important;
                border-radius: 20px !important;
                background-color: {bg_card} !important;
                border: 1px solid {border} !important;
                box-shadow: 0 10px 40px {shadow} !important;
                
                height: 80vh !important;
                min-height: 600px;
                max-height: 80vh !important;
                
                display: flex !important;
                flex-direction: column !important;
                justify-content: space-evenly !important;
                align-items: center !important;
                text-align: center !important;
                overflow: hidden !important;
            }}

            /* 4. Typography */
            h1 {{
                color: {text_hdr} !important;
                font-size: clamp(1.8rem, 5vh, 3.2rem) !important;
                font-weight: 800 !important;
                margin: 0 auto 0.5rem auto !important;
                line-height: 1.1 !important;
                text-align: center !important;
                width: 100%;
            }}
            h2 {{
                color: {accent} !important;
                font-size: clamp(1.2rem, 3.5vh, 1.8rem) !important;
                font-weight: 300 !important;
                margin: 0 auto !important;
                text-align: center !important;
                width: 100%;
            }}
            .slide-text {{
                font-size: clamp(1rem, 2.8vh, 1.4rem) !important;
                line-height: 1.4 !important;
                color: {text_main} !important;
                max-width: 900px;
                margin: 0 auto !important;
                flex-shrink: 1;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }}

            /* 4.1 Topics List */
            .topics-list {{
                text-align: left !important;
                display: inline-block !important;
                margin: 1rem auto !important;
                padding-left: 2rem !important;
                list-style-type: none !important;
            }}
            .topics-list li {{
                margin-bottom: 0.8rem !important;
                position: relative;
            }}
            .topics-list li::before {{
                content: "•";
                color: {accent};
                font-weight: bold;
                display: inline-block;
                width: 1em;
                margin-left: -1em;
            }}

            /* 4.2 Generic Markdown Lists inside Slide Text */
            .slide-text ul {{
                text-align: left !important;
                display: inline-block !important;
                margin-left: 2rem !important;
            }}
            .slide-text li {{
                margin-bottom: 0.5rem !important;
            }}
            .slide-text li::marker {{
                color: {accent} !important;
            }}

            /* 5. Adaptive Images */
            .stImage img {{
                max-height: 45vh !important;
                width: auto !important;
                object-fit: contain !important;
                border-radius: 12px;
                border: 1px solid {border};
                flex-grow: 1;
                flex-shrink: 1;
                margin: 1vh auto !important;
            }}

            /* 6. Navigation Controls */
            .stButton>button {{
                background-color: {btn_bg};
                color: {text_main};
                border: 1px solid {border};
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
            }}
            .stButton>button:hover {{
                background-color: {btn_hover} !important;
                border-color: {accent} !important;
                color: {accent} !important;
            }}
            
            footer, #MainMenu {{ visibility: hidden; }}
            
            /* Notas Section */
            .notinha {{
                background: {bg_app};
                border-left: 3px solid {accent};
                padding: 1rem;
                text-align: left;
                font-size: 0.9rem;
                color: {text_main};
                opacity: 0.8;
            }}
            </style>
        """, unsafe_allow_html=True)
