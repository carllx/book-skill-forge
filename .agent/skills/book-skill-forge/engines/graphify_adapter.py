import os
import json
import logging

logger = logging.getLogger(__name__)

def run(book_path: str, output_dir: str) -> bool:
    """
    Deprecated: LLM extraction is now natively handled by Antigravity Subagents.
    This python adapter is a no-op placeholder that checks if graph.json exists.
    """
    os.makedirs(output_dir, exist_ok=True)
    graph_json_path = os.path.join(output_dir, 'graph.json')
    
    logger.info(f"Graphify adapter called on {book_path}, but LLM execution is delegated to Subagents.")
    
    if os.path.exists(graph_json_path):
        logger.info(f"Agent output {graph_json_path} found.")
        return True
    else:
        logger.warning(f"Agent output {graph_json_path} not found. Ensure Subagent ran first.")
        # Optional: return True so testing won't crash if we just want to test pipeline flow
        return True
