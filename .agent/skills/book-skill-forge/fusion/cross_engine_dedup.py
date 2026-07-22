import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class CrossEngineDedup:
    """
    Utility to deduplicate concepts that both engines found.
    """
    
    @staticmethod
    def _compute_similarity(concept1: str, concept2: str) -> float:
        """
        Simple Jaccard similarity for concept names.
        In production, this might use embeddings or more sophisticated NLP.
        """
        set1 = set(concept1.lower().split())
        set2 = set(concept2.lower().split())
        
        if not set1 or not set2:
            return 0.0
            
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return len(intersection) / len(union)

    @classmethod
    def deduplicate(cls, engine_a_concepts: List[Dict[str, Any]], engine_b_concepts: List[Dict[str, Any]], threshold: float = 0.7) -> List[Dict[str, Any]]:
        """
        Merges two lists of concepts, deduplicating those that are highly similar.
        Preserves metadata from both engines when a merge happens.
        """
        merged_concepts = []
        # Keep track of Engine B concepts that have been merged
        b_merged_indices = set()
        
        for a_concept in engine_a_concepts:
            a_name = a_concept.get('name', '')
            best_match_idx = -1
            best_score = 0.0
            
            for i, b_concept in enumerate(engine_b_concepts):
                if i in b_merged_indices:
                    continue
                    
                b_name = b_concept.get('name', '')
                score = cls._compute_similarity(a_name, b_name)
                
                if score > best_score:
                    best_score = score
                    best_match_idx = i
                    
            if best_score >= threshold:
                # Merge the concepts
                b_match = engine_b_concepts[best_match_idx]
                b_merged_indices.add(best_match_idx)
                
                merged_concept = {
                    'name': a_name,  # Prefer Engine A's naming or combine
                    'sources': ['Engine_A', 'Engine_B'],
                    'engine_a_data': a_concept,
                    'engine_b_data': b_match
                }
                merged_concepts.append(merged_concept)
                logger.info(f"Merged concept '{a_name}' with '{b_match.get('name', '')}' (Score: {best_score:.2f})")
            else:
                # No match, keep Engine A's concept standalone
                merged_concepts.append({
                    'name': a_name,
                    'sources': ['Engine_A'],
                    'engine_a_data': a_concept
                })
                
        # Add remaining standalone Engine B concepts
        for i, b_concept in enumerate(engine_b_concepts):
            if i not in b_merged_indices:
                merged_concepts.append({
                    'name': b_concept.get('name', ''),
                    'sources': ['Engine_B'],
                    'engine_b_data': b_concept
                })
                
        return merged_concepts
