# Prompt Analysis

## Why I structured it this way

I used markdown headers to organise the prompt into sections because it makes it easier
to read and update later. I separated the rules, response style, and specific situations
into different sections so the chatbot knows exactly what to do in each case.

I included a list of prohibited items because the chatbot needs to know specifically
what it cannot help with. Without this list it might accidentally help someone sell
something they should not be selling.

## Why I included specific situations

I wrote out what to do for buyers, sellers, scams, disputes and safety issues separately
because these are the most common things users will ask about. By giving the chatbot
a clear step by step process for each one, it is less likely to give a vague or wrong answer.

I learned from using Carousell that the most common problems are scams and no-shows,
so I made sure those were covered in detail.

## Safety guardrails

I added a section specifically for safety concerns because these are the most serious
situations. If someone is being threatened the chatbot should not try to handle it
itself. It should immediately tell the user to contact campus security and hand off
to a human. I made this very clear in the prompt so the chatbot does not try to
negotiate or de-escalate a dangerous situation on its own.
