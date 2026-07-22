import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

try:
    from sentence_transformers import SentenceTransformer, util
    import torch
    # Suppress verbose warnings
    import warnings
    warnings.filterwarnings("ignore")
    EMBEDDER = SentenceTransformer('all-MiniLM-L6-v2')
except ImportError:
    EMBEDDER = None
    logger.warning("sentence-transformers not installed. Falling back to naive matching.")

class GraphAugmentedRIA:
    """
    Core fusion algorithm that injects graph context into candidate skills 
    to prevent long-tail knowledge loss.
    """
    
    def __init__(self, graph_data: Dict[str, Any]):
        """
        Initializes the augmenter with graph data (from Engine A / Graphify).
        graph_data is expected to have 'nodes' and 'edges'.
        """
        self.graph = graph_data
        self.nodes = {str(node.get('id')): node for node in self.graph.get('nodes', []) if 'id' in node}
        self.edges = self.graph.get('edges', [])
        
        # Precompute node adjacency for quick lookup
        self.adjacency = {}
        for edge in self.edges:
            src = str(edge.get('source'))
            tgt = str(edge.get('target'))
            if src and tgt:
                self.adjacency.setdefault(src, []).append(tgt)
                self.adjacency.setdefault(tgt, []).append(src)

    def _find_related_context(self, concept_keywords: List[str], max_depth: int = 1) -> List[Dict[str, Any]]:
        """
        Finds related graph nodes based on concept keywords.
        """
        related_nodes = []
        matched_node_ids = set()
        
        # Step 1: Semantic Match or Direct match
        query = " ".join([kw for kw in concept_keywords if kw.strip()])
        
        if EMBEDDER is not None and query:
            node_ids = list(self.nodes.keys())
            node_labels = [str(self.nodes[nid].get('label', '')) for nid in node_ids]
            
            if node_labels:
                # Calculate embeddings and cosine similarity
                query_emb = EMBEDDER.encode(query, convert_to_tensor=True)
                node_embs = EMBEDDER.encode(node_labels, convert_to_tensor=True)
                
                # Find top 5 matches
                hits = util.semantic_search(query_emb, node_embs, top_k=5)[0]
                for hit in hits:
                    if hit['score'] > 0.3: # Threshold for relatedness
                        matched_nid = node_ids[hit['corpus_id']]
                        matched_node_ids.add(matched_nid)
                        related_nodes.append(self.nodes[matched_nid])
        else:
            # Fallback naive matching
            for node_id, node_data in self.nodes.items():
                node_label = str(node_data.get('label', '')).lower()
                if any(kw.lower() in node_label for kw in concept_keywords if kw.strip()):
                    matched_node_ids.add(node_id)
                    related_nodes.append(node_data)
                
        # Step 2: Neighbor traversal
        if max_depth > 0:
            neighbor_ids = set()
            for n_id in matched_node_ids:
                neighbors = self.adjacency.get(n_id, [])
                for neighbor_id in neighbors:
                    if neighbor_id not in matched_node_ids:
                        neighbor_ids.add(neighbor_id)
                        
            for neighbor_id in neighbor_ids:
                if neighbor_id in self.nodes:
                    related_nodes.append(self.nodes[neighbor_id])
                    
        return related_nodes

    def inject_context(self, candidate_skills: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Takes a set of candidate skills (from Engine B / Cangjie) and augments
        them with related graph context.
        """
        augmented_skills = []
        
        for skill in candidate_skills:
            # Extract keywords or main concepts from the skill
            skill_name = skill.get('name', '')
            skill_keywords = [skill_name] + skill.get('tags', [])
            
            # Fetch related context from the graph
            related_context = self._find_related_context(skill_keywords)
            
            # Inject context into the skill
            augmented_skill = skill.copy()
            augmented_skill['graph_context'] = {
                'related_nodes': related_context,
                'injected': True
            }
            
            augmented_skills.append(augmented_skill)
            
            logger.debug(f"Augmented skill '{skill_name}' with {len(related_context)} related nodes.")
            
        return augmented_skills
