# 🚀 Quick Start Cheat Sheet

## First Time Setup (Do Once)

1. ✅ Create 10 repos on GitHub: `lab01-student` through `lab10-student`
2. ✅ Enable GitHub Pages on each (Settings → Pages → main branch)
3. ✅ Create Personal Access Token (https://github.com/settings/tokens)
4. ✅ Add token as `DEPLOY_TOKEN` secret in esci240-labs repo
5. ✅ Copy `.github` and `.vscode` folders to your project
6. ✅ In VS Code Source Control: Initialize → Commit → Add Remote → Push

## Daily Workflow

1. **Edit labs** in VS Code
2. **Source Control panel** (Ctrl+Shift+G)
3. **Stage changes** (click + button)
4. **Write commit message**
5. **Commit** (click ✓)
6. **Sync Changes** (click sync button)
7. **Wait 2-3 minutes** → Labs auto-deploy! 🎉

## Quick Tasks (Ctrl+Shift+P → "Tasks: Run Task")

- 🚀 **Push All Changes** - One-click commit and push
- 📊 **Check Status** - See what changed
- 🌐 **View URLs** - See all deployed lab links

## Your Deployed Labs

- Lab 01: https://wxfreekj.github.io/lab01-student
- Lab 02: https://wxfreekj.github.io/lab02-student
- Lab 03: https://wxfreekj.github.io/lab03-student
- Lab 04: https://wxfreekj.github.io/lab04-student
- Lab 05: https://wxfreekj.github.io/lab05-student
- Lab 06: https://wxfreekj.github.io/lab06-student
- Lab 07: https://wxfreekj.github.io/lab07-student
- Lab 08: https://wxfreekj.github.io/lab08-student
- Lab 09: https://wxfreekj.github.io/lab09-student
- Lab 10: https://wxfreekj.github.io/lab10-student

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't push | Pull first (three dots → Pull) |
| Labs not deploying | Check https://github.com/wxfreekj/esci240-labs/actions |
| Changes not showing | Wait 2-3 min, hard refresh (Ctrl+Shift+R) |

## VS Code Git Shortcuts

- `Ctrl+Shift+G` - Open Source Control
- `Ctrl+Enter` - Commit staged changes
- Click "Sync" button - Push/pull changes

**Remember:** You only push to `esci240-labs` repo. GitHub Actions handles the rest!
