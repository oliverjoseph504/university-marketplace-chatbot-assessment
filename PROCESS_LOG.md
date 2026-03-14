# Process Log

This document explains how I approached each part of the assessment and what I was thinking at each step.

# Overall approach

I read the brief twice before starting. I noticed that the assessment was testing whether I could think about a chatbot as a whole system, not just write a few chat responses. So I tried to approach each part with that in mind.

I have some experience with Python and C but I have not built a chatbot before. I treated this like any other programming problem. So I broke it into smaller pieces, solved each one, then put it all together.

# Part 1 - Prompt Design

My first instinct was to just write a paragraph telling the chatbot what to do. But when I tried that it felt disorganised and hard to update.

I decided to use markdown headers to split the prompt into sections. This way if I need to change the scam handling section later I know exactly where to find it without reading the whole thing.

The hardest part was figuring out what situations to cover. I thought about my own experience using Carousell and other market places and wrote down the most common problems I ran into as a buyer and seller. Even though it was not specific to university, I made an assumption that the problems would be similar. That gave me the list of situations to cover.

# Part 2 - Test Cases

I started by writing test cases for the obvious happy paths (how to sell, how to buy). Then I thought about what could go wrong and wrote test cases for those too.

The edge cases were the hardest to think of. I asked myself "what's the weirdest thing someone might type?" and that helped me come up with things like the typo-filled message and the multi-topic question.

I kept the JSON structure simple and readable. I only used the fields asked for in the brief and did not add extra complexity.

# Part 3 - Automation

I kept the Python script as simple as possible. It does three things:
1. Loads the test cases from the JSON file
2. Sends each one to the chatbot
3. Checks if the response contains the right keywords

I used basic Python features I already know such as file reading, for loops, functions,and string checking. I did not use any libraries except json which is built in.

The API call part is commented out with a note explaining how to make it work for real. I wanted to show the full structure of the project to show understanding on this.

# Part 4 - Marketplace Insights

I drew mostly on my own experience here. I am a university student and me and my friends  have organised university sales and other events.

I added the seasonal patterns section because I noticed that the volume of requests for various items changed during different school periods. For instance, during holidays when students on campus move out, they tend to want to sell items that they havve no more use for. This seemed like useful information for a chatbot designer.

# Part 5 - Prototype

I chose Poe.com because it was the fastest way to get a working chatbot without any setup. I pasted the prompt in, selected Claude, and it worked. The UI for Poe.com was simple and since I have not done a project such as this, I was able to pick up on it quickly.

# Most challenging part

Writing the test cases was the hardest part. When you write code you can test it by running it and seeing if it crashes. But testing a chatbot is harder because there is no single correct answer. I had to think carefully about what a "good enough" response looks like and write that down clearly enough that someone else could evaluate it too.

# Three alternative approaches I considered

1. Decision tree instead of LLM prompt - I thought about building a simple if-else tree in Python where the chatbot picks a response based on keywords. I rejected this because it can only handle questions that were pre-programmed and would fail on anything unusual.

2. Plain paragraph prompt with no structure - I tried writing the prompt asone long paragraph first. It was hard to read and hard to update so I switched to using headers and sections.

3. Randomly sampling a few test cases from the 30 to test them - I did not do this, even though it is less time consuming, as this method might have skipped some of the high risk cases and if those cases were to fail during a real incident, that would be devastating and goes against the fundemental aim of any product, helping its users. 
