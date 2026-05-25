Send a message to your collaborator that will appear in their next Claude Code session.

Arguments: $ARGUMENTS
Format: `<recipient> <message>`
Recipients: `jon` or `richie`

Steps:
1. Run `git config user.name` to identify yourself (the sender)
2. Map the sender to their canonical name: richardisho = richie, corleoneshow = jon
3. Parse $ARGUMENTS — first word is the recipient, everything after is the message
4. Run `date +%Y-%m-%d-%H-%M` to get a timestamp
5. Create the file `.claude/inbox/<timestamp>-from-<sender>-to-<recipient>.md` with this exact format:

```
---
from: <sender>
to: <recipient>
date: <YYYY-MM-DD>
---

<message content>
```

6. Run: `git add .claude/inbox/ && git commit -m "Message: <sender> → <recipient>" && git push origin HEAD`
7. Confirm the message was sent and will appear at the start of <recipient>'s next session.
