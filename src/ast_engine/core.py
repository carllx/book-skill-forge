from typing import Any, List
from markdown_it import MarkdownIt
from markdown_it.token import Token

class DocumentASTParser:
    def __init__(self):
        self.md = MarkdownIt("commonmark").enable("table")
        
    def parse(self, text: str, visitor: Any):
        """
        Parses the markdown text and traverses the AST using the provided visitor.
        """
        # Store original text in visitor if it needs it
        if hasattr(visitor, "set_source_text"):
            visitor.set_source_text(text)
            
        tokens = self.md.parse(text)
        
        for i, token in enumerate(tokens):
            method_name = f"visit_{token.type.replace('-', '_')}"
            visit_method = getattr(visitor, method_name, None)
            if visit_method:
                visit_method(token, i, tokens)
                
            generic_visit = getattr(visitor, "visit_token", None)
            if generic_visit:
                generic_visit(token, i, tokens)
                
        if hasattr(visitor, "finalize"):
            visitor.finalize()
