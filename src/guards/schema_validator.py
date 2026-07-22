import json
import jsonschema
from jsonschema import validate

# 强制性 JSON Schema: 只允许输出 evidence_anchor 字符串和 boolean 命中，绝对禁止整数评分
MATCHES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "evidence_anchor": {
                "type": "string",
                "description": "原书切片中找到的具体证据锚点字符串"
            },
            "is_matched": {
                "type": "boolean",
                "description": "是否命中证据"
            }
        },
        "required": ["evidence_anchor", "is_matched"],
        "additionalProperties": False  # 严禁大模型擅自添加类似 "score": 85 的非法字段
    }
}

def validate_matches_json(json_data):
    """
    如果 Agent 试图输出带有 0-100 整数的非法 JSON，这里将直接抛出异常，阻断流水线。
    """
    try:
        validate(instance=json_data, schema=MATCHES_SCHEMA)
        print("[Schema Guard] Validation passed. No subjective integer scores detected.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        raise ValueError(f"【脱水评测红线违规】Judge Agent 输出非法字段！严禁主观打分。错误详情: {err.message}")

if __name__ == "__main__":
    # Test
    test_data = [
        {"evidence_anchor": "建筑的本质在于建构", "is_matched": True}
    ]
    validate_matches_json(test_data)
