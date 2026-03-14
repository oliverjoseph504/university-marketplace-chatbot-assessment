# University Marketplace Chatbot Assessment

# What is this?
This is my submission for the UniMart chatbot take-home assessment.
The chatbot helps university students buy and sell items on a campus marketplace.

# How to review my work
- `prompt.md` - the chatbot's instructions
- `prompt-analysis.md` - why I wrote the prompt in this way
- `test-cases.json` - test cases to check the chatbot works
- `testing-framework.md` - how I tested the chatbot
- `testing-result.md` - what happened when I ran the tests
- `update-process.md` - how to update the chatbot in the future
- `automation-concept.py` - a script to automate testing
- `marketplace-insights.md` - what I know about university marketplaces
- `PROCESS_LOG.md` - my thinking process throughout this project

# Assumptions I made
- Users are local university students with a valid university email (edu.sg)
- The platform is similar to Carousell but only for students of a specific university
- Meetups happen on campus
- Payment is done via PayNow or cash

# Time breakdown
- Prompt design: 60 mins
- Test cases: 90 mins
- Automation: 60 mins
- Marketplace insights: 15 mins
- Prototype: 15 mins
- Total: about 3 hours

# Next steps if this were a real project
- Connect the chatbot to a real database of listings
- Add proper user login
- Build a proper web interface instead of using Poe.com
- Add support for more languages

# Hardest part
Writing the test cases was the hardest part because I had to think about
all the weird ways a user might ask a question, not just the normal ones.
Not having much experience when it comes to University marketplace also was 
unfavourable for me. 

# Three approaches I considered
1. Using a simple decision tree (if user says X, reply Y) - rejected because it can't handle questions that weren't pre-programmed
2. Writing the prompt as plain paragraphs with no structure - rejected because it was hard to read and update
3. Building a custom chatbot from scratch in Python - rejected because it would take too long and Poe.com already does this for free

# My experience with university marketplaces
Not much experience in this but I have bought and sold NUS merchandise through various student groups and CCAs.
When buying, there would always be logistical issues such as running out of stock or not the sizing being off. 
When selling, pricing the items at a right price is tough as we are selling to other students and we would need to make enough money on the sales. 


