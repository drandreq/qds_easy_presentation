import streamlit as st

class StyleManager:
    @staticmethod
    def apply_styles():
        st.markdown("""
            <style>
            /* 1. Global Reset */
            [data-testid="stAppViewContainer"] {
                background-color: #0d1117 !important;
                color: #c9d1d9 !important;
            }
            
            [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0) !important;
            }

            /* 2. Sidebar */
            [data-testid="stSidebar"] {
                background-color: #010409 !important;
                border-right: 1px solid #30363d !important;
            }

            /* 3. Viewport-Safe Slide Card */
            /* Using a specific selector for the internal stVerticalBlock of the container */
            [data-testid="stVerticalBlock"] > div > [data-testid="stVerticalBlock"] {
                padding: 3vh 3vw !important;
                border-radius: 20px !important;
                background-color: #161b22 !important;
                border: 1px solid #30363d !important;
                box-shadow: 0 10px 40px rgba(0,0,0,0.6) !important;
                
                /* CRITICAL: Locking height to prevent scroll */
                height: 80vh !important;
                min-height: 600px;
                max-height: 80vh !important;
                
                display: flex !important;
                flex-direction: column !important;
                justify-content: space-evenly !important; /* Distributed space */
                align-items: center !important;
                text-align: center !important;
                overflow: hidden !important; /* NO SCROLL */
            }

            /* 4. Responsive Typography */
            h1 {
                color: #f0f6fc !important;
                font-size: clamp(1.8rem, 5vh, 3.2rem) !important; /* Scale with viewport height */
                font-weight: 800 !important;
                margin: 0 !important;
                line-height: 1.1 !important;
            }
            h2 {
                color: #7ee787 !important;
                font-size: clamp(1.2rem, 3.5vh, 1.8rem) !important;
                font-weight: 300 !important;
                margin: 0 !important;
            }
            .slide-text {
                font-size: clamp(1rem, 2.8vh, 1.4rem) !important;
                line-height: 1.4 !important;
                color: #adbac7 !important;
                max-width: 800px;
                margin: 0 auto !important;
                flex-shrink: 1;
            }

            /* 5. Adaptive Images - Viewport Safe & Space Filling */
            .stImage img {
                max-height: 45vh !important; /* Increased slightly */
                width: auto !important;
                object-fit: contain !important;
                border-radius: 12px;
                border: 1px solid #30363d;
                flex-grow: 1; /* Favor filling space */
                flex-shrink: 1;
                margin: 1vh auto !important;
            }

            /* 6. Navigation Zones - Side Clicking */
            .nav-zone {
                position: fixed;
                top: 0;
                bottom: 0;
                width: 15vw;
                z-index: 999;
                cursor: pointer;
                transition: background 0.2s;
            }
            .nav-left { left: 0; }
            .nav-right { right: 0; }
            .nav-zone:hover {
                background: rgba(255, 255, 255, 0.02);
            }

            /* 7. Navigation Controls - Muted but Large */
            .stButton>button {
                background-color: #21262d;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #30363d !important;
                border-color: #8b949e !important;
                color: #ffffff !important;
            }
            
            /* Hide Default Shrapnel */
            header, footer, #MainMenu { visibility: hidden; }
            
            /* Notas Section - Small and discrete */
            .notinha {
                background: #0d1117;
                border-left: 3px solid #7ee787;
                padding: 1rem;
                text-align: left;
                font-size: 0.9rem;
                color: #8b949e;
            }
            </style>
        """, unsafe_allow_html=True)
