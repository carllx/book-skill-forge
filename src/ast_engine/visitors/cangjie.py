from typing import List, Dict, Any
from markdown_it.token import Token
from .base import BaseVisitor
import re

class CangjieVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()
        self.clean_text_blocks = []
        self.offset_mapping = []  # List of dicts { start: int, end: int, page: int }
        self.current_page = None
        self.current_offset = 0
        self.page_pattern = re.compile(r'\*+\[Page\s+(\d+)\]\*+')
        
    def visit_inline(self, token: Token, index: int, tokens: List[Token]):
        if not token.content:
            return
            
        content = token.content
        matches = list(self.page_pattern.finditer(content))
        
        if matches:
            last_end = 0
            clean_parts = []
            
            for match in matches:
                before_text = content[last_end:match.start()]
                if before_text:
                    clean_parts.append(before_text)
                    self._add_text(before_text)
                    
                self.current_page = int(match.group(1))
                last_end = match.end()
                
            after_text = content[last_end:]
            if after_text:
                clean_parts.append(after_text)
                self._add_text(after_text)
        else:
            self._add_text(content)
            
        self._add_text("\n\n") 
            
    def _add_text(self, text: str):
        if not text:
            return
            
        start_off = self.current_offset
        end_off = start_off + len(text)
        self.clean_text_blocks.append(text)
        
        if self.current_page is not None:
            self.offset_mapping.append({
                "start": start_off,
                "end": end_off,
                "page": self.current_page
            })
            
        self.current_offset = end_off
        
    def get_results(self) -> Dict[str, Any]:
        return {
            "clean_text": "".join(self.clean_text_blocks),
            "offset_mapping": self.offset_mapping
        }
