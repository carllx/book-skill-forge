from typing import List, Dict, Any
from markdown_it.token import Token
from .base import BaseVisitor
import re

class BookToSkillVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()
        self.chunks = []
        self.current_chunk = []
        self.page_anchors = []
        # Matches formats like **[Page 10]** or *[Page 10]*
        self.page_pattern = re.compile(r'\*+\[Page\s+(\d+)\]\*+')
        
    def visit_heading_open(self, token: Token, index: int, tokens: List[Token]):
        if token.tag in ['h1', 'h2']:
            if self.current_chunk:
                self.chunks.append("\n".join(self.current_chunk))
                self.current_chunk = []
                
    def visit_inline(self, token: Token, index: int, tokens: List[Token]):
        if not token.content:
            return
            
        matches = self.page_pattern.findall(token.content)
        for match in matches:
            self.page_anchors.append(int(match))
            
        self.current_chunk.append(token.content)
        
    def finalize(self):
        if self.current_chunk:
            self.chunks.append("\n".join(self.current_chunk))
            
    def get_results(self) -> Dict[str, Any]:
        return {
            "chunks": self.chunks,
            "page_anchors": self.page_anchors
        }
