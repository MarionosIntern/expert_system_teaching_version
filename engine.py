from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return True if all antecedents are true and consequent not yet known."""
        return (rule.consequent not in self.facts and all(a in self.facts for a in rule.antecedents))

    def run(self) -> None:
        """Forward Chaining loop: keep firing rules until no more can fire."""

        step = 0
        while True:
            # Finds all rules that can fire.
            candidates = [r for r in self.rules if self.can_fire(r)]
            if not candidates:
                break
            # Picks highest priority rule, then the most specific rule. If still tied, max() returns the first one.
            rule = max(candidates, key = lambda r: (r.priority, len(r.antecedents)))
            self.facts.add(rule.consequent)

            # Records the rule firing in the trace.
            step = step + 1
            self.trace.append({
                "step": step,
                "rule": rule.name,
                "if": list(rule.antecedents),
                "then": rule.consequent,
            })

    def conclusions(self) -> Dict[str, List[str]]:
        """Return separated results (recommendations, specs, other facts)."""

        result = {"recommendations": [], "specs": [], "other": []}
        for step in self.trace:
            c = step["then"]
            if c.startswith("recommend:"):
                result["recommendations"].append(c.split(":", 1)[1])
            elif c.startswith("spec:"):
                result["specs"].append(c.split(":", 1)[1])
            else:
                result["other"].append(c)
        return result