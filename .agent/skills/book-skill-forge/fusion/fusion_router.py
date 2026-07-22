import json
import logging
from typing import Dict, Any, Optional
from enum import Enum

logger = logging.getLogger(__name__)

class BookType(Enum):
    METHODOLOGY = "Methodology"
    NARRATIVE = "Narrative"
    TECHNICAL = "Technical"
    UNKNOWN = "Unknown"

class FusionStrategy(Enum):
    STRUCTURAL_FIRST = "StructuralFirst"  # Best for Methodology
    THEMATIC_CLUSTERING = "ThematicClustering"  # Best for Narrative
    CODE_AND_GRAPH_DRIVEN = "CodeAndGraphDriven"  # Best for Technical
    DEFAULT = "Default"

class FusionRouter:
    """
    Analyzes a book's metadata to determine its type and recommends a fusion strategy.
    """
    
    METHODOLOGY_KEYWORDS = ["framework", "principles", "guide", "method", "system", "how-to", "strategy", "process", "model"]
    NARRATIVE_KEYWORDS = ["story", "biography", "history", "journey", "memoir", "tale", "fiction", "novel"]
    TECHNICAL_KEYWORDS = ["programming", "code", "development", "architecture", "algorithm", "data", "software", "engineering", "machine learning", "technical"]

    @classmethod
    def analyze_metadata(cls, metadata: Dict[str, Any]) -> BookType:
        """
        Determines the book type based on its metadata.
        """
        title = metadata.get("title", "").lower()
        summary = metadata.get("summary", "").lower()
        tags = [tag.lower() for tag in metadata.get("tags", [])]
        
        combined_text = f"{title} {summary} {' '.join(tags)}"
        
        scores = {
            BookType.METHODOLOGY: sum(1 for kw in cls.METHODOLOGY_KEYWORDS if kw in combined_text),
            BookType.NARRATIVE: sum(1 for kw in cls.NARRATIVE_KEYWORDS if kw in combined_text),
            BookType.TECHNICAL: sum(1 for kw in cls.TECHNICAL_KEYWORDS if kw in combined_text)
        }
        
        best_match = max(scores, key=scores.get)
        if scores[best_match] == 0:
            return BookType.UNKNOWN
            
        return best_match

    @classmethod
    def get_strategy(cls, metadata: Dict[str, Any]) -> FusionStrategy:
        """
        Returns the recommended fusion strategy for a given book's metadata.
        """
        book_type = cls.analyze_metadata(metadata)
        
        strategy_mapping = {
            BookType.METHODOLOGY: FusionStrategy.STRUCTURAL_FIRST,
            BookType.NARRATIVE: FusionStrategy.THEMATIC_CLUSTERING,
            BookType.TECHNICAL: FusionStrategy.CODE_AND_GRAPH_DRIVEN,
            BookType.UNKNOWN: FusionStrategy.DEFAULT
        }
        
        recommended_strategy = strategy_mapping.get(book_type, FusionStrategy.DEFAULT)
        logger.info(f"Analyzed book metadata. Type: {book_type.value}. Recommended Strategy: {recommended_strategy.value}.")
        
        return recommended_strategy
