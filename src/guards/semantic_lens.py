import json
import sys
from pathlib import Path

# BSF 作弊防线 - 语义透视镜 (Semantic Lens)
# 职责：检测并拦截大模型利用“概念拼贴”或“废话轰炸”绕过 Judge Agent 审计的行为。

# 无价值的微观废话黑名单（用于拦截 Pixel Spam 攻击）
TRIVIAL_WORDS = {"时间", "方法", "人", "的", "和", "是", "在", "了", "有", "我", "他", "这", "中", "大", "小"}

def analyze_pixel_spam(concepts: list) -> bool:
    """像素轰炸校验：检查提取的实体是否全是无意义的废话"""
    if not concepts:
        return False
        
    trivial_count = 0
    for c in concepts:
        name = c.get("name", "").strip()
        if name in TRIVIAL_WORDS or len(name) < 2:
            trivial_count += 1
            
    # 如果超过 50% 都是废话微观实体，判定为作弊
    spam_ratio = trivial_count / len(concepts)
    if spam_ratio > 0.5:
        print(f"[Semantic Lens] 🚨 拦截 Pixel Spam 攻击！废话实体占比高达 {spam_ratio:.0%}")
        return True
    return False

def analyze_collage_loophole(mindsets: list) -> bool:
    """
    拼贴欺骗校验：
    (注：由于架构规范禁止纯 Python 直接调 LLM，这里仅作规则校验或通过 IPC 通知专职 Agent 进行二次查验)
    目前使用启发式：心法句子如果过短且未包含标点符号，极有可能是生硬拼凑。
    """
    for m in mindsets:
        text = m.get("content", "").strip()
        # 真正的心法应该是一句有逻辑张力的话。如果没有逗号/句号且字数极少，疑似拼贴。
        if len(text) < 10 and not any(p in text for p in ['，', '。', '！', '？', ',', '.']):
            print(f"[Semantic Lens] 🚨 疑似概念拼贴 (Collage Loophole): {text}")
            return True
    return False

def inspect_submission(json_path: Path):
    if not json_path.exists():
        print(f"[ERROR] 找不到提交的文件: {json_path}")
        return False
        
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[ERROR] JSON 解析失败: {e}")
        return False
        
    concepts = data.get("concepts", [])
    mindsets = data.get("mindsets", [])
    
    is_spam = analyze_pixel_spam(concepts)
    is_collage = analyze_collage_loophole(mindsets)
    
    if is_spam or is_collage:
        print("\n" + "!"*50)
        print("💥 [FRAUD DETECTED] 语义透视镜发现作弊行为，已拦截该管线的成绩提交！")
        print("!"*50 + "\n")
        return False
        
    print(f"✅ [Semantic Lens] 审查通过，未发现明显的拼贴欺骗与废话轰炸。")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python semantic_lens.py <submission.json>")
        sys.exit(1)
        
    success = inspect_submission(Path(sys.argv[1]))
    if not success:
        sys.exit(1)
