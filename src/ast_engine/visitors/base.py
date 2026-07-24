from typing import List
from markdown_it.token import Token

class BaseVisitor:
    """Base class for all AST visitors."""
    
    def __init__(self):
        self.source_text = ""
        
    def set_source_text(self, text: str):
        """Called before parsing begins."""
        self.source_text = text
        
    def visit_token(self, token: Token, index: int, tokens: List[Token]):
        """Generic fallback for unhandled tokens."""
        pass
        
    def finalize(self):
        """Called when parsing is complete."""
        pass
