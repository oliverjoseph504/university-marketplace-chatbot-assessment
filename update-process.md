# Update Process

## Overview
This document explains how to update the chatbot prompt safely without breaking
anything that already works.

## Step by step workflow
1. Someone notices a problem or a new feature is needed
        
2. Edit prompt.md with the changes

3. Run all 30 test cases manually on Poe.com
        
4. Did all tests pass? (If yes, continue to step 5. If no, fix the prompt and go back to step 3).
     
5. Get someone else to review the changes
        
6. Save the old prompt as prompt-v1.md (backup)
       
7. Upload the new prompt.md to the chatbot on Poe.com
        
8. Monitor for 24 hours to check for complaints

9. If something breaks, restore from the backup file

## Version control
I keep old versions of the prompt by saving them with version numbers:
- prompt-v1.md (original)
- prompt-v2.md (first update)
- prompt.md (always the current version)

This way I can always go back to an older version if something goes wrong.

## Rules for making changes
- Always test before deploying
- Always keep a backup of the previous version
- Safety-related changes need to be reviewed by another person
- Keep a record of what changed and why in a CHANGELOG.txt file

## Seasonal update
Some updates are needed at specific times of year:

| Time of year | What to update |

| Start of semester (Aug-Dec) | Add reminders about textbook listings |
| Exam season, depending on the school curriculum| Add warnings about prohibited exam content |
| Move out week (Dec-Jan) | Add tips for listing furniture |

## Rollback
If the new prompt causes problems:
1. Open Poe.com
2. Go to bot settings
3. Replace the system prompt with the contents of the previous version backup
