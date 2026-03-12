import streamlit as st
import os
from typing import Dict, Any

class SlideRenderer:
    @staticmethod
    def render(slide: Dict[str, Any]):
        st.markdown('<div class="slide-card">', unsafe_allow_html=True)
        
        if slide["type"] == "markdown":
            st.markdown(f'<div class="slide-text">{slide["content"]}</div>', unsafe_allow_html=True)
        else:
            SlideRenderer._render_custom(slide)
            
        st.markdown('</div>', unsafe_allow_html=True)

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
        
        # Visual Assets (Images, Mermaid, YAML)
        # In Single Column, these appear below text for impact
        
        # Render all images in the list
        imagens = slide.get("imagens", [])
        for img in imagens:
            src = img.get("src")
            desc = img.get("desc")
            if src and os.path.exists(src):
                st.image(src, caption=desc if desc else None, width='content') 
            elif desc:
                st.info(f"💡 Visão Sugerida: {desc}")

        if slide.get("mermaid"): 
            st.markdown(f"```mermaid\n{slide['mermaid']}\n```")
        
        if slide.get("yaml"): 
            st.markdown(f"```yaml\n{slide['yaml']}\n```")
        
        if slide.get("link"): 
            st.caption(f"🔗 [Fonte do Estudo]({slide['link']})")

        # Speaker Notes - Keep at bottom or as expander if needed
        if slide.get("falas"):
            with st.expander("🎙️ Notas do André"):
                falas_content = slide["falas"]
                st.markdown(f'<div class="notinha">{falas_content}</div>', unsafe_allow_html=True)
