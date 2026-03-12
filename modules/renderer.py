import streamlit as st
import streamlit.components.v1 as components
import os
from typing import Dict, Any

class SlideRenderer:
    @staticmethod
    def render(slide: Dict[str, Any]):
        # Use a native container to ensure all elements are wrapped for CSS targeting
        with st.container():
            if slide["type"] == "markdown":
                st.markdown(f'<div class="slide-text">{slide["content"]}</div>', unsafe_allow_html=True)
            else:
                SlideRenderer._render_custom(slide)

    @staticmethod
    def render_notes(slide: Dict[str, Any]):
        # Speaker Notes - Rendered OUTSIDE and COLLAPSED by default
        if slide.get("falas"):
            with st.expander("🎙️ Ver Notas do André", expanded=False):
                falas_content = slide["falas"]
                if isinstance(falas_content, list):
                    falas_content = "<br>".join([f"• {f}" for f in falas_content])
                st.markdown(f'<div class="notinha">{falas_content}</div>', unsafe_allow_html=True)

    @staticmethod
    def _render_custom(slide: Dict[str, Any]):
        # Header Section - Titles are centered via CSS
        if slide.get("titulo"): 
            st.markdown(f'<h1>{slide["titulo"]}</h1>', unsafe_allow_html=True)
        if slide.get("subtitulo"): 
            st.markdown(f'<h2>{slide["subtitulo"]}</h2>', unsafe_allow_html=True)
        
        # Main Body
        if slide.get("texto"): 
            texto = slide["texto"]
            if isinstance(texto, list):
                # Use a specific div for lists to allow for better CSS control if needed
                list_items = "".join([f"<li style='margin-bottom: 0.5rem;'>{t}</li>" for t in texto])
                texto = f"<ul style='list-style-type: disc; text-align: left; display: inline-block; padding-left: 20px;'>{list_items}</ul>"
            st.markdown(f'<div class="slide-text">{texto}</div>', unsafe_allow_html=True)
        
        # Mermaid Rendering - High Priority
        if slide.get("mermaid"): 
            mermaid_code = slide['mermaid']
            html_code = f"""
            <div class="mermaid" style="display: flex; justify-content: center; background: transparent;">
                {mermaid_code}
            </div>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{ 
                    startOnLoad: true, 
                    theme: 'dark',
                    securityLevel: 'loose',
                    flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }}
                }});
            </script>
            """
            components.html(html_code, height=500, scrolling=True)

        # Visual Assets (Images)
        imagens = slide.get("imagens", [])
        # Handle both single dict and list of dicts for backward compatibility
        if isinstance(imagens, dict):
            imagens = [imagens]
            
        for img in imagens:
            src = img.get("src")
            desc = img.get("desc")
            # Custom width support centered
            width = img.get("width", "content")
            if src and os.path.exists(src):
                st.image(src, caption=desc if desc else None, width=width)
            elif desc:
                st.info(f"💡 Visão Sugerida: {desc}")
        
        if slide.get("yaml"): 
            st.markdown(f"```yaml\n{slide['yaml']}\n```")
        
        if slide.get("link"): 
            st.caption(f"🔗 [Fonte do Estudo]({slide['link']})")
