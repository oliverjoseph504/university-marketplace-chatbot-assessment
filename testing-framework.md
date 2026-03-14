# Testing Framework

## What are golden tests?

Golden tests are a fixed set of questions with expected answers that I use to check
if the chatbot is working correctly. If I change the prompt, I run the same tests
again to make sure I did not break anything.

## How I organised the test cases

I split the tests into 5 categories:

1. Basic Navigation - questions about how to use the platform (5 tests) (nav_)
2. Transaction Support - questions about buying, selling, payments and disputes (6 tests) (txn_)
3. Safety and Guidelines - questions about prohibited items and scams (6 tests) (saf_)
4. Escalation Triggers - serious situations that need a human moderator (5 tests) (esc_)
5. Edge Cases - weird or unusual questions (8 tests) (edge_)

Total: 30 test cases

## How I evaluate each test

For each test I check if the chatbot response contains the expected elements listed
in the test case. I do this manually by reading the response.

I mark each test as:
- Pass - all expected elements are in the response
- Partial Pass - most expected elements are there but one or two are missing
- Fail - the response is wrong or missing important information

## Pass requirements

- Overall: at least 90% of tests must pass
- Safety and escalation tests: 100% must pass, no exceptions 
(because getting these wrong could put someone in danger)
- Escalation triggers: 100% pass rate, no exceptions

## How to run the tests

First layer checks:(Used for general test cases)
A secondary LLM (judge model) evaluates whether the chatbot response whether it
contains all expected elements.

Second Layer Check: (Used for high risk test cases)
1. Open Poe.com
2. Go through all the high risk cases
3. Copy them into the chat and manually ensure that 100% of these cases pass
4. Only if these high risk cases pass 100% of the time, the prompt will pass the evaluation


