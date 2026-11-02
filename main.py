from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # Questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Do you want a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    if input("Do you want to play games? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is it for the office only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    if input("Do you prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you need Linux compatibility? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    return facts

def main():
    #Load rules from JSON and create an engine with them
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)

    #Put user's answers into working memory and run the engine
    engine.assert_facts(collect_initial_facts())
    engine.run()
    results = engine.conclusions()
    print()

    #Display each recommendation and the rule that produced it
    if results["recommendations"]:
        for step in engine.trace:
            if step["then"].startswith("recommend:"):
                print(f"> Recommendation: {step['then'].split(':',1)[1]}")
                print(f"> Explanation: Derived from rule: {step['rule']}")
    else:
        print("No recommendation could be made with the given facts.")

    #Display specifications and other derived facts 
    if results["specs"]:
        print("\nSpecifications:")
        for spec in results["specs"]:
            print(f"- {spec}")
    if results["other"]:
        print("\n> Other derived facts:", ",".join(results["other"]))

    #Prints trace of every rule that fired, in firing order.
    print("\n> Fired rules:")
    if engine.trace:
        for step in engine.trace:
            print(f" {step['step']}. {step['rule']}" f"IF {' AND '.join(step['if'])} THEN {step['then']}")

    else:
        print(" (none)")
if __name__ == "__main__":
    main()