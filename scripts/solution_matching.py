"""Conservative matching within ONE source document pair and knowledge point."""
import re
from collections import Counter


def signature(question):
    if not question.blocks:
        return None
    parts = []
    for block in question.blocks:
        for unit in block.units:
            if unit.kind == 'text':
                value = unit.value
                marker = re.search(r"【(?:答案|解析|分析|详解)】", value)
                if marker:
                    parts.append(re.sub(r'\s+', '', value[:marker.start()]))
                    return ''.join(parts) or None
                parts.append(re.sub(r'\s+', '', value))
            elif unit.kind == 'image':
                match = re.search(r'-([0-9a-f]{10})\.', unit.value)
                if not match:
                    return None
                parts.append('IMAGE:' + match.group(1))
    return ''.join(parts) or None


def match_solutions(questions, solutions):
    """Never fall back to position, and fail closed on duplicate source numbers."""
    key = lambda q: (q.number, signature(q))
    qc = Counter(key(q) for q in questions)
    sc = Counter(key(q) for q in solutions)
    by_key = {key(s): s for s in solutions if sc[key(s)] == 1}
    return [by_key.get(key(q)) if signature(q) and qc[key(q)] == 1 else None
            for q in questions]



PENDING = ':::solution 解析待核验\n\n尚未确认原题号与题干匹配，请由教师核对后使用；不按题目顺序猜配答案。\n\n:::'
