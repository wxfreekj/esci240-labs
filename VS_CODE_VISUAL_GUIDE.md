# 🖱️ VS Code Visual Workflow Guide

This guide shows you exactly **where to click** in VS Code to deploy your labs - no command line needed!

---

## 📍 Finding Things in VS Code

### Left Sidebar Icons (from top to bottom):
1. 📁 **Explorer** - See your files and folders
2. 🔍 **Search** - Find text in files
3. 🌿 **Source Control** - This is where Git lives! (Ctrl+Shift+G)
4. 🐛 **Run and Debug** - Not needed for deployment
5. 🧩 **Extensions** - Install VS Code add-ons

---

## 🌿 Source Control Panel - Your Main Tool

### First Time: Initialize Repository
1. Click **Source Control icon** (🌿) in left sidebar
2. Click big blue button: **"Initialize Repository"**
3. All your files appear under "Changes"

### Every Time: Committing Changes

**What you'll see:**
```
SOURCE CONTROL
├── Message box (type your commit message here)
├── ✓ Commit button (or Ctrl+Enter)
└── Changes (X)  ← Click "+" to stage all
    ├── .github/workflows/deploy-lab01.yml  M
    ├── web-components/lab01/index.html  M
    └── ... (more changed files)
```

**What to do:**
1. **Type a message** in the text box at top (e.g., "Updated Lab 5")
2. **Stage files**: Hover over "Changes" → Click the **"+"** icon
   - Or click **"+"** next to individual files
3. **Commit**: Click the **✓ checkmark** icon (or press Ctrl+Enter)
4. **Push**: Click **"Sync Changes"** button that appears

---

## 🎯 Three Dots Menu (•••)

Click the **three dots** in Source Control panel to see:

### First Time Setup:
- **Remote** → **Add Remote...** → Enter: `https://github.com/wxfreekj/esci240-labs.git`
- **Push to...** → Select **origin**

### Daily Use:
- **Pull** - Get latest changes from GitHub
- **Push** - Send your changes to GitHub
- **Sync** - Pull and push in one action

---

## ⚡ Quick Tasks (Time Savers!)

**How to access:**
1. Press **Ctrl+Shift+P** (or F1)
2. Type: `Tasks: Run Task`
3. Choose from the list:

### Available Tasks:
- 🚀 **Push All Changes to Main Repo**
  - Automatically stages, commits, and pushes everything
  - Good for quick updates
  
- 📊 **Check Git Status**
  - Shows what files you've changed
  - Like running `git status`
  
- 🔄 **Pull Latest Changes**
  - Gets updates from GitHub
  - Good before starting work
  
- 🌐 **View All GitHub Pages URLs**
  - Shows all your deployed lab links
  - Copy/paste to share with students
  
- ✅ **Create Initial Commit** (First time only)
  - Commits everything with a standard message
  
- 🔗 **Connect to GitHub** (First time only)
  - Sets up the remote repository link

---

## 📋 Step-by-Step Visual Checklist

### FIRST TIME ONLY: Initial Setup

#### Part 1: GitHub Website (Before VS Code)
```
GitHub.com → Your profile (wxfreekj)
├── Create 10 new repositories
│   ├── lab01-student (Public, empty)
│   ├── lab02-student (Public, empty)
│   └── ... through lab10-student
│
├── For each repository:
│   └── Settings → Pages → Deploy from branch: main
│
├── Generate Personal Access Token
│   ├── Settings → Developer settings → Tokens
│   ├── Generate new token (classic)
│   ├── Check "repo" scope
│   └── COPY THE TOKEN! (ghp_xxxxx...)
│
└── Add token to esci240-labs
    └── Settings → Secrets → Actions → New secret
        ├── Name: DEPLOY_TOKEN
        └── Value: (paste your token)
```

#### Part 2: VS Code
```
VS Code
├── File → Open Folder → (select esci240-labs)
│
├── Copy deployment files to project:
│   ├── Drag .github folder into your project root
│   └── Drag .vscode folder into your project root
│
├── Source Control panel (Ctrl+Shift+G)
│   ├── Click "Initialize Repository"
│   ├── Stage all files (click + next to Changes)
│   ├── Type message: "Initial commit: All labs ready"
│   ├── Click ✓ to commit
│   │
│   ├── Three dots (•••) → Remote → Add Remote
│   │   └── URL: https://github.com/wxfreekj/esci240-labs.git
│   │
│   └── Three dots (•••) → Push to → origin
│
└── Wait 2-3 minutes
    └── Check: https://github.com/wxfreekj/esci240-labs/actions
        └── Should see 10 green checkmarks ✅
```

---

### DAILY WORKFLOW: Updating Labs

```
VS Code
├── Make changes to lab files (edit, save)
│
├── Source Control panel (Ctrl+Shift+G)
│   ├── See your changed files listed
│   ├── Stage files (click + button)
│   ├── Write commit message
│   ├── Click ✓ to commit
│   └── Click "Sync Changes" button
│
└── DONE! Labs auto-deploy in 2-3 minutes
```

**Even Faster:**
```
Press Ctrl+Shift+P
Type: Tasks: Run Task
Choose: 🚀 Push All Changes to Main Repo
DONE!
```

---

## 🎨 What Each Button Does

### In Source Control Panel:

| Button | Icon | What It Does |
|--------|------|--------------|
| **Refresh** | ↻ | Reload the list of changes |
| **Stage All** | + (next to Changes) | Prepare all files for commit |
| **Unstage All** | − (next to Staged) | Remove files from commit |
| **Commit** | ✓ | Save staged changes locally |
| **Sync Changes** | ↕ | Push to and pull from GitHub |
| **More Actions** | ••• | Opens menu with more options |

### Commit Button States:
- **Commit** - Normal state
- **Commit & Push** - If you set "auto-push" in settings
- **Commit & Sync** - Same as above

---

## 🎯 Status Indicators

Files show letters to indicate their status:

| Letter | Meaning |
|--------|---------|
| **M** | Modified (file changed) |
| **A** | Added (new file) |
| **D** | Deleted |
| **U** | Untracked (new file, not staged) |

---

## 🔍 Finding Your Deployed Labs

After pushing, your labs are automatically deployed to:

```
https://wxfreekj.github.io/lab01-student
https://wxfreekj.github.io/lab02-student
https://wxfreekj.github.io/lab03-student
https://wxfreekj.github.io/lab04-student
https://wxfreekj.github.io/lab05-student
https://wxfreekj.github.io/lab06-student
https://wxfreekj.github.io/lab07-student
https://wxfreekj.github.io/lab08-student
https://wxfreekj.github.io/lab09-student
https://wxfreekj.github.io/lab10-student
```

**Quick way to view all URLs:**
1. Press Ctrl+Shift+P
2. Type: Tasks
3. Choose: 🌐 View All GitHub Pages URLs

---

## ❗ Common Situations

### "Nothing to commit"
- **Meaning**: You haven't changed any files
- **What to do**: Edit a file, save it, then try again

### "Sync Changes" button is grayed out
- **Meaning**: Everything is already synced
- **What to do**: Nothing needed! You're good.

### "Failed to push"
- **Meaning**: GitHub has changes you don't have locally
- **What to do**: Click three dots → Pull, then try pushing again

### "Conflicts" appear
- **Meaning**: GitHub and your local changes overlap
- **What to do**: Click on the file, VS Code will show you both versions. Choose which to keep.

---

## 🎓 Pro Tips

### Keyboard Shortcuts
- `Ctrl+Shift+G` - Open Source Control
- `Ctrl+Enter` - Commit staged changes
- `Ctrl+Shift+P` - Open command palette (access tasks)
- `Ctrl+S` - Save current file
- `Ctrl+K Ctrl+S` - Save all files

### VS Code Git Settings
Your `.vscode/settings.json` already configures:
- ✅ Auto-fetch from GitHub every minute
- ✅ Smart commits (commit all if nothing staged)
- ✅ Sync on commit (optional auto-push)

### Viewing Deployment Progress
While labs are deploying:
1. Go to: https://github.com/wxfreekj/esci240-labs/actions
2. Click on the running workflow
3. Watch the progress in real-time
4. Green checkmark = success! ✅

---

## 📱 Bottom Status Bar

Look at the bottom of VS Code:

```
[main] ↻0 ↓0 ↑1  ← Git info
```

- **main** - Current branch name
- **↻** - Syncing changes
- **↓0** - 0 commits to pull from GitHub
- **↑1** - 1 commit to push to GitHub

Click this status to see more options!

---

## ✅ Success Checklist

You've done everything right when:
- [ ] All 10 `labXX-student` repos created on GitHub
- [ ] GitHub Pages enabled on all 10 repos
- [ ] DEPLOY_TOKEN secret added to esci240-labs
- [ ] .github and .vscode folders in your project
- [ ] Source Control shows green checkmark (nothing to commit)
- [ ] All 10 workflows show green checkmarks at /actions
- [ ] All 10 lab URLs are accessible

---

## 🎉 You're Now a VS Code Git Expert!

Remember:
1. **Edit** → **Source Control** → **Stage** → **Commit** → **Sync**
2. Or use the quick task: **Push All Changes**
3. Wait 2-3 minutes for auto-deployment
4. Share the GitHub Pages URLs with students

**No command line needed!** 🎊
