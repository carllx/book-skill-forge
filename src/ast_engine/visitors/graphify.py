from typing import List, Dict, Any
from markdown_it.token import Token
from .base import BaseVisitor
import re

class GraphNode:
    def __init__(self, title: str, level: int):
        self.title = title
        self.level = level
        self.content = []
        self.children = []
        self.page_coord = None
        
    def to_dict(self):
        return {
            "title": self.title,
            "level": self.level,
            "content": "\n".join(self.content),
            "page_coord": self.page_coord,
            "children": [c.to_dict() for c in self.children]
        }

class GraphifyVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()
        self.root = GraphNode("[Document_Root]", 0)
        self.stack = [self.root]
        self.page_pattern = re.compile(r'\*+\[Page\s+(\d+)\]\*+')
        self.current_page = None
        self.in_heading = False
        
    def visit_heading_open(self, token: Token, index: int, tokens: List[Token]):
        self.in_heading = True
        level = int(token.tag[1]) # 'h1' -> 1, 'h2' -> 2
        
        # Heading text is usually in the next token of type 'inline'
        title = ""
        if index + 1 < len(tokens) and tokens[index+1].type == "inline":
            title = tokens[index+1].content
            
        new_node = GraphNode(title, level)
        new_node.page_coord = self.current_page
        
        while self.stack and self.stack[-1].level >= level:
            self.stack.pop()
            
        if not self.stack:
            self.stack = [self.root]
            
        self.stack[-1].children.append(new_node)
        self.stack.append(new_node)
        
    def visit_heading_close(self, token: Token, index: int, tokens: List[Token]):
        self.in_heading = False
        
    def visit_inline(self, token: Token, index: int, tokens: List[Token]):
        if not token.content:
            return
            
        matches = self.page_pattern.findall(token.content)
        if matches:
            self.current_page = int(matches[-1])
            
        if not self.in_heading:
            clean_text = self.page_pattern.sub('', token.content).strip()
            if clean_text:
                self.stack[-1].content.append(clean_text)
                
    def get_results(self) -> Dict[str, Any]:
        return self.root.to_dict()
