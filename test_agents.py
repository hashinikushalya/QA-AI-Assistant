from agents.router import route_user_query
from agents.testcase_agent import generate_test_cases
from agents.rag_agent import answer_qa_question
from agents.review_agent import review_and_refine_output

def run_agentic_pipeline(user_query: str):
    print(f"\n==================================================")
    print(f"--- Processing Query: '{user_query}' ---")
    print(f"==================================================")
    
    # Step 1: Routing Intent
    intent = route_user_query(user_query)
    print(f"[1. Router Agent] Detected Intent: {intent}")
    
    # Step 2: Specialized Agent Execution
    if intent == "TESTCASE":
        print("[2. Execution] Calling Test Case Generator Agent...")
        raw_result = generate_test_cases(user_query)
        sources = []
    else:
        print("[2. Execution] Calling QA Knowledge (RAG) Agent...")
        raw_result, sources = answer_qa_question(user_query)
        
    # Step 3: Output Review & Refinement
    print("[3. Review Agent] Polishing and Reviewing Output...")
    final_output = review_and_refine_output(user_query, raw_result, intent)
    
    print("\n--- Final Reviewed Response ---")
    print(final_output)
    
    if sources:
        print("\n--- Sources Retrieved ---")
        for src in sources:
            print(f"- {src}")

if __name__ == "__main__":
    # Test Scenario 1: Test Case Generation Test
    run_agentic_pipeline("Generate test cases for user login with email and password")
    
    # Test Scenario 2: QA Knowledge Search Test
    run_agentic_pipeline("What is Boundary Value Analysis in software testing?")