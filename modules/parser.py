import yaml
import re
from typing import List, Dict, Any

class SlideParser:
    SLIDE_SEPARATOR = r'\n---+\n'

    @staticmethod
    def get_raw_blocks(content: str) -> List[str]:
        return [b.strip() for b in re.split(SlideParser.SLIDE_SEPARATOR, content) if b.strip()]

    @staticmethod
    def parse_block(block: str) -> Dict[str, Any]:
        try:
            data = yaml.safe_load(block)
            if isinstance(data, dict):
                return {
                    "type": "custom",
                    "titulo": data.get("titulo", ""),
                    "subtitulo": data.get("subtitulo", ""),
                    "texto": SlideParser._format_text(data.get("texto", "")),
                    "falas": SlideParser._format_list(data.get("falas", [])),
                    "mermaid": data.get("mermaid", ""),
                    "yaml": data.get("yaml", ""),
                    "link": data.get("link", ""),
                    "imagens": SlideParser._extract_images(data.get("imagem", []))
                }
        except Exception:
            pass
            
        return {"type": "markdown", "content": block}

    @staticmethod
    def _format_text(text: Any) -> str:
        if isinstance(text, list):
            return "\n".join([str(i) for i in text])
        if isinstance(text, dict):
            return "\n".join([str(v) for v in text.values()])
        return str(text) if text else ""

    @staticmethod
    def _format_list(items: Any) -> str:
        if isinstance(items, list):
            return "\n\n".join([str(i) for i in items])
        if isinstance(items, dict):
            return "\n\n".join([str(v) for v in items.values()])
        return str(items) if items else ""

    @staticmethod
    def _extract_images(img_data: Any) -> List[Dict[str, str]]:
        """Extracts a list of image dictionaries."""
        images = []
        if isinstance(img_data, list):
            for i in img_data:
                if isinstance(i, dict):
                    images.append({
                        "src": i.get("src", ""),
                        "desc": i.get("descricao", ""),
                        "pos": i.get("posicao", "centro")
                    })
        elif isinstance(img_data, dict):
            images.append({
                "src": img_data.get("src", ""),
                "desc": img_data.get("descricao", ""),
                "pos": img_data.get("posicao", "centro")
            })
        return images
