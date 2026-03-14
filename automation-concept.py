
import json


# Load test cases from the JSON file
def load_tests(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["test_cases"]


# Send a message to Claude and get a response
# In real use, replace this with an actual Claude API call
def ask_chatbot(system_prompt, user_message): 
    return "Replace with real API call."


# Check if the response contains the expected elements
def check_response(response, expected_elements):
    missing = []
    for element in expected_elements:
        # Simple check: is the keyword somewhere in the response?
        if element.lower() not in response.lower():
            missing.append(element)
    
    passed = len(missing) == 0
    return passed, missing


# Run all tests and print results
def run_all_tests(system_prompt, test_cases):
    passed = 0
    failed = 0
    results = []

    for test in test_cases:
        print(f"Running test {test['id']}...")

        # Get chatbot response
        response = ask_chatbot(system_prompt, test["input"])

        # Check if response is good
        test_passed, missing = check_response(response, test["expected_elements"])

        if test_passed:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        results.append({
            "id": test["id"],
            "status": status,
            "missing_elements": missing
        })

        print(f"  {status} - missing: {missing}")

    # Print summary
    total = len(test_cases)
    print("\n--- RESULTS ---")
    print(f"Passed: {passed}/{total}")
    print(f"Failed: {failed}/{total}")
    print(f"Pass rate: {round(passed / total * 100)}%")

    if failed == 0:
        print("All tests passed! Safe to deploy.")
    else:
        print("Some tests failed. Fix the prompt before deploying.")

    return results


# Main function
def main():
    # Load the system prompt
    with open("prompt.md", "r") as f:
        system_prompt = f.read()

    # Load test cases
    test_cases = load_tests("test-cases.json")

    print(f"Loaded {len(test_cases)} test cases.")
    print("Starting tests...\n")

    # Run all tests
    results = run_all_tests(system_prompt, test_cases)

    # Save results to a file
    with open("latest-test-results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nResults saved to latest-test-results.json")


# Run the script
if __name__ == "__main__":
    main()
