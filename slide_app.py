import streamlit as st
import os
from modules.styles import StyleManager
from modules.parser import SlideParser
from modules.renderer import SlideRenderer

# --- Constants ---
MAIN_MD_FILE = os.path.join("content", "palestra_v4.md")

def main():
    st.set_page_config(page_title="Debugando a Exaustão", layout="wide", initial_sidebar_state="collapsed")
    
    # 1. Apply Centralized Styles and Animations
    StyleManager.apply_styles()

    # 2. Load and Parse Content
    if not os.path.exists(MAIN_MD_FILE):
        st.error(f"Arquivo {MAIN_MD_FILE} não encontrado.")
        return

    with open(MAIN_MD_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        raw_blocks = SlideParser.get_raw_blocks(content)
        slides_data = [SlideParser.parse_block(b) for b in raw_blocks]

    # 3. State Management (Current Slide Index)
    if 'idx' not in st.session_state: 
        st.session_state.idx = 0

    # 4. Sidebar: Navigation & Settings
    st.sidebar.title("📺 Controles")
    
    # 5. Settings Expander (Making it "collapsible" as requested)
    with st.sidebar.expander("⚙️ Gestão de Slides"):
        # File Uploader
        uploaded_file = st.file_uploader("Subir novo Markdown (.md):", type=["md"])
        if uploaded_file is not None:
            save_path = os.path.join("content", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            if 'last_uploaded' not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
                st.session_state.last_uploaded = uploaded_file.name
                st.rerun()

        # File Selector
        content_files = [f for f in os.listdir("content") if f.endswith(".md")]
        selected_file_name = st.selectbox(
            "Alternar Apresentação:", 
            content_files, 
            index=content_files.index(os.path.basename(MAIN_MD_FILE)) if os.path.basename(MAIN_MD_FILE) in content_files else 0
        )
    
    current_md_path = os.path.join("content", selected_file_name)
    
    # Load and Parse Selected Content
    with open(current_md_path, "r", encoding="utf-8") as f:
        content = f.read()
        raw_blocks = SlideParser.get_raw_blocks(content)
        slides_data = [SlideParser.parse_block(b) for b in raw_blocks]

    # --- Content Rendering (Main Focus Area) ---
    SlideRenderer.render(slides_data[st.session_state.idx])

    st.divider()

    # 6. Navigation UI (Bottom Bar - High Visibility)
    nav_col1, nav_col2, nav_col3 = st.columns([2, 5, 2])
    with nav_col1:
        if st.button("⬅️ ANTERIOR", use_container_width=True) and st.session_state.idx > 0:
            st.session_state.idx -= 1
            st.rerun()
    with nav_col2:
        # Progress indicator
        st.progress((st.session_state.idx + 1) / len(slides_data))
        st.markdown(f"<div style='text-align:center; color:#7ee787;'>Slide {st.session_state.idx + 1} de {len(slides_data)}</div>", unsafe_allow_html=True)
    with nav_col3:
        if st.button("PRÓXIMO ➡️", use_container_width=True) and st.session_state.idx < len(slides_data) - 1:
            st.session_state.idx += 1
            st.rerun()

    # 7. Speaker Notes (Outside the Slide Card)
    SlideRenderer.render_notes(slides_data[st.session_state.idx])

    # Quick Jump Selector
    selected_slide = st.sidebar.selectbox(
        "Pular para:", 
        range(len(slides_data)), 
        index=st.session_state.idx if st.session_state.idx < len(slides_data) else 0,
        format_func=lambda x: f"Slide {x+1}: {slides_data[x].get('titulo', 'Sem Título')[:30]}..."
    )
    
    if selected_slide != st.session_state.idx:
        st.session_state.idx = selected_slide
        st.rerun()

    st.sidebar.divider()
    st.sidebar.caption("🩺 Dr. André Quadros | GDG 2026")
    st.sidebar.caption("Modo Apresentação v5.1 (Medical Dark)")

    # 6. Ghost Navigation (V6.5 - Resilient Dual-Level)
    st.markdown("""
        <script>
        const nav = (dir) => {
            const parentDoc = window.parent.document;
            const buttons = Array.from(parentDoc.querySelectorAll('button'));
            const search = dir === 'next' ? 'PRÓXIMO' : 'ANTERIOR';
            const btn = buttons.find(b => b.textContent.toUpperCase().includes(search));
            if (btn) btn.click();
        };

        // 1. Keyboard Listeners (Capture everywhere)
        const setupKeys = (win) => {
            win.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight') nav('next');
                if (e.key === 'ArrowLeft') nav('prev');
            }, true);
        };
        setupKeys(window);
        setupKeys(window.parent);

        // 2. Click Overlays & Floating Button (Inject into parent for full coverage)
        const parentDoc = window.parent.document;
        if (!parentDoc.getElementById('nav-overlay-v65')) {
            const overlay = parentDoc.createElement('div');
            overlay.id = 'nav-overlay-v65';
            overlay.style.cssText = 'position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:999999;';
            overlay.innerHTML = `
                <!-- Invisible Side Zones -->
                <div onclick="window.parent.postMessage('nav-prev', '*')" style="position:absolute; top:0; left:0; width:10vw; height:100%; pointer-events:auto; cursor:pointer; background:transparent;"></div>
                <div onclick="window.parent.postMessage('nav-next', '*')" style="position:absolute; top:0; right:0; width:10vw; height:100%; pointer-events:auto; cursor:pointer; background:transparent;"></div>
                
                <!-- Visible Floating Button (Bottom-Right) -->
                <div onclick="window.parent.postMessage('nav-next', '*')" style="
                    position: absolute;
                    bottom: 25px;
                    right: 25px;
                    width: 70px;
                    height: 70px;
                    background-color: #238636;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
                    cursor: pointer;
                    pointer-events: auto;
                    font-size: 30px;
                    user-select: none;
                    transition: transform 0.2s, background-color 0.2s;
                    border: 2px solid #2ea043;
                    font-family: sans-serif;
                " onmouseover="this.style.transform='scale(1.1)'; this.style.backgroundColor='#2ea043';" 
                  onmouseout="this.style.transform='scale(1)'; this.style.backgroundColor='#238636';">
                  ➜
                </div>
            `;
            parentDoc.body.appendChild(overlay);
        }

        // 3. Message Listener for the overlays
        window.parent.addEventListener('message', (e) => {
            if (e.data === 'nav-next') nav('next');
            if (e.data === 'nav-prev') nav('prev');
        });
        </script>
    """, unsafe_allow_html=True)

    # --- App Footer/End ---

if __name__ == "__main__":
    main()
