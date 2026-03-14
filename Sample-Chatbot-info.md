# Sample Chatbot Info

# URL to access the chatbot

https://poe.com/UniMart?invite_code=2e006ad4-9c23-4f7d-b945-54c88111f346


# Why I chose Poe.com

I chose Poe.com for three reasons:

1. It is completely free with no credit card needed
2. It uses Claude as the base model which is what the prompt was designed for
3. It generates a shareable link straight away with no setup needed


# Assumptions

- The chatbot only works in English
- It does not have access to real listing data or user accounts
- Escalation to a human moderator is simulated, not connected to a real system
- The Poe.com free tier has message limits

# Limitations

Limitations: No real user data
Fix: Connect to the University system 

Limitations: No real escalation
Fix: Hire people to work as human moderators in the school and connect the chatbot to them.

Limitations: English only
Fix: Add translation support 

Limitations: Message limits on free tier
Fix: Use the paid Anthropic API directly 

Limitations: No memory between sessions
Fix: Add session saving in the backend


# Test results from the prototype

I manually tested the chatbot on Poe.com with these inputs: (I am giving generic answers as I ran out of free points testing my previous cases)


Input: "How do I sell my textbook?" Output: Gave clear step by step instructions - PASS
Input: "Can I sell alcohol?" Output: Refused clearly - PASS
Input: "I think I'm being scammed" Output: Warned me and told me to report - PASS
Input: "Someone threatened me" Output: Escalated immediately - PASS
Input: "hwlp i thnk im beng scmmed" Output: Asked what happened in a calm way - PASS
Input: "Can I sell my pocket knife?" Output: Refused clearly - PASS
Input: "The item looks different from the photos" Output: Explained dispute process - PASS
Input: "I paid $800 and the seller vanished" Output: Escalated to moderator - PASS

8 out of 8 manual tests passed.
