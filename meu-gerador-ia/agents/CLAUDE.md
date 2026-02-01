# AIOS SYSTEM RULES & DEVOPS NOTEPAD

## 🛠 DEVOPS COMMANDS (Use with @CLAUDE.md)
* `help` - Show all available commands and current project status.
* `create-story` - Protocol for creating a new agent logic or feature.
* `task {name}` - Execute a specific agent task via terminal.
* `workflow {name}` - Run a complete business workflow.
* `logs` - View real-time agent thinking: `tail -f .aios/logs/agent.log`
* `debug` - Enable verbose mode: `export AIOS_DEBUG=true`

---

## 🚫 NEVER (Critical Prohibitions)
1. NEVER provide answers without verifying the root cause of an issue.
2. NEVER modify critical files or project structure without explicit confirmation.
3. NEVER ignore error logs in the `.aios/logs/` directory.
4. NEVER assume a task is finished without running a validation test.
5. NEVER use mock data when real data sources are available and configured.
6. NEVER ignore the instructions in the project's `.env` file.
7. NEVER overwrite existing logic in `agents/` without creating a backup.
8. NEVER delete files unless specifically instructed.
9. NEVER skip the "Thought" process before proposing a code change.
10. NEVER suggest third-party libraries not in `requirements.txt`.
11. NEVER provide generic solutions; always adapt to the AIOS workflow.

---

## ✅ ALWAYS (Critical Obligations)
1. ALWAYS investigate the root cause of any terminal error before suggesting a fix.
2. ALWAYS provide 3 numbered options (1, 2, 3) when a decision is required.
3. ALWAYS check if the `agents/` directory is properly mapped in `app.py`.
4. ALWAYS log the agent's thought process to `.aios/logs/agent.log`.
5. ALWAYS confirm that API keys (Gemini/OpenAI) are active before connecting.
6. ALWAYS keep this `CLAUDE.md` updated with new rules learned.
7. ALWAYS verify if the Streamlit server needs a restart after core changes.

---

## 🎯 PROJECT CONTEXT (Arbitragem AI)
- **Main Goal:** AI Agent for price scanning and arbitrage calculation.
- **Core Stack:** Python, Streamlit, Gemini API (AI Studio).
- **Structure:** `/agents` for logic, `app.py` for UI, `.aios` for system logs.