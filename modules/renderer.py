import streamlit as st
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
    def _render_custom(slide: Dict[str, Any]):
        # Header Section
        if slide.get("titulo"): 
            st.markdown(f'<h1>{slide["titulo"]}</h1>', unsafe_allow_html=True)
        if slide.get("subtitulo"): 
            st.markdown(f'<h2>{slide["subtitulo"]}</h2>', unsafe_allow_html=True)
        
        # Main Body
        if slide.get("texto"): 
            st.markdown(f'<div class="slide-text">{slide["texto"]}</div>', unsafe_allow_html=True)
        
        # Visual Assets
        imagens = slide.get("imagens", [])
        for img in imagens:
            src = img.get("src")
            desc = img.get("desc")
            if src and os.path.exists(src):
                # Using width='content' to avoid warning and center
                st.image(src, caption=desc if desc else None, width='content')
            elif desc:
                st.info(f"💡 Visão Sugerida: {desc}")

        if slide.get("mermaid"): 
            st.markdown(f"```mermaid\n{slide['mermaid']}\n```")
        
        if slide.get("yaml"): 
            st.markdown(f"```yaml\n{slide['yaml']}\n```")
        
        if slide.get("link"): 
            st.caption(f"🔗 [Fonte do Estudo]({slide['link']})")

        # Speaker Notes
        if slide.get("falas"):
            with st.expander("🎙️ Notas do André"):
                falas_content = slide["falas"]
                st.markdown(f'<div class="notinha">{falas_content}</div>', unsafe_allow_html=True)
