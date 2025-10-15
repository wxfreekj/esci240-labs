# 🎉 Complete GitHub Deployment Package

Everything you need to deploy your 10 ESCI 240 labs to GitHub Pages using **only VS Code** - no command line required!

---

## 📦 What's Included

### Configuration Files (Copy these to your project)

#### `.github/workflows/` - Automatic Deployment
- `deploy-lab01.yml` - Auto-deploys Lab 1 to wxfreekj/lab01-student
- `deploy-lab02.yml` - Auto-deploys Lab 2 to wxfreekj/lab02-student
- `deploy-lab03.yml` - Auto-deploys Lab 3 to wxfreekj/lab03-student
- `deploy-lab04.yml` - Auto-deploys Lab 4 to wxfreekj/lab04-student
- `deploy-lab05.yml` - Auto-deploys Lab 5 to wxfreekj/lab05-student
- `deploy-lab06.yml` - Auto-deploys Lab 6 to wxfreekj/lab06-student
- `deploy-lab07.yml` - Auto-deploys Lab 7 to wxfreekj/lab07-student
- `deploy-lab08.yml` - Auto-deploys Lab 8 to wxfreekj/lab08-student
- `deploy-lab09.yml` - Auto-deploys Lab 9 to wxfreekj/lab09-student
- `deploy-lab10.yml` - Auto-deploys Lab 10 to wxfreekj/lab10-student

**How they work:** Each time you push changes to a lab folder in your main repo, GitHub Actions automatically deploys just that lab to its student-facing repository.

#### `.vscode/` - VS Code Integration
- `tasks.json` - Quick tasks you can run from VS Code
  - 🚀 Push All Changes to Main Repo
  - 📊 Check Git Status
  - 🔄 Pull Latest Changes
  - 🌐 View All GitHub Pages URLs
  - ✅ Create Initial Commit
  - 🔗 Connect to GitHub
  
- `settings.json` - Git configuration for VS Code
  - Enables auto-fetch from GitHub
  - Enables smart commits
  - Shows .git folder in explorer

### Documentation Files

#### `DEPLOYMENT_GUIDE.md` - Complete Setup Instructions ⭐
**START HERE!** This is your main reference.
- Step-by-step setup from beginning to end
- Screenshots and detailed explanations
- Troubleshooting section
- First-time setup and daily workflow

#### `VS_CODE_VISUAL_GUIDE.md` - Click-by-Click Reference
**Best for visual learners!**
- Shows exactly where to click in VS Code
- Explains every button and icon
- Common situations and how to handle them
- No command line needed

#### `QUICK_START.md` - Cheat Sheet
**Quick reference card!**
- One-page summary of everything
- Checklist format
- All your deployed lab URLs
- Keyboard shortcuts

#### `README.md` - Repository Documentation
**For your main GitHub repo**
- Professional overview of your labs
- Links to all deployed labs
- Technical documentation
- Student and instructor information

---

## 🎯 Your Final Project Structure

After copying these files, your project should look like:

```
esci240-labs/                        ← Your main repository
├── .github/
│   └── workflows/
│       ├── deploy-lab01.yml
│       ├── deploy-lab02.yml
│       ├── deploy-lab03.yml
│       ├── deploy-lab04.yml
│       ├── deploy-lab05.yml
│       ├── deploy-lab06.yml
│       ├── deploy-lab07.yml
│       ├── deploy-lab08.yml
│       ├── deploy-lab09.yml
│       └── deploy-lab10.yml
│
├── .vscode/
│   ├── tasks.json
│   └── settings.json
│
├── web-components/
│   ├── shared/
│   │   ├── styles/
│   │   └── utils/
│   ├── lab01/
│   ├── lab02/
│   ├── lab03/
│   ├── lab04/
│   ├── lab05/
│   ├── lab06/
│   ├── lab07/
│   ├── lab08/
│   ├── lab09/
│   └── lab10/
│
├── grading-system/          ← Not deployed to students
├── docs/
│
├── DEPLOYMENT_GUIDE.md
├── VS_CODE_VISUAL_GUIDE.md
├── QUICK_START.md
└── README.md
```

---

## 🚀 Quick Start (5 Steps)

### 1. GitHub Setup (Website)
- Create 10 repos: lab01-student through lab10-student
- Enable GitHub Pages on each
- Generate Personal Access Token
- Add DEPLOY_TOKEN secret to esci240-labs repo

### 2. Copy Files
- Copy `.github` folder to your project root
- Copy `.vscode` folder to your project root
- Copy all .md files to your project root

### 3. VS Code Setup
- Open your esci240-labs folder in VS Code
- Source Control → Initialize Repository
- Stage all files (click +)
- Commit with message
- Add remote: https://github.com/wxfreekj/esci240-labs.git
- Push to origin

### 4. Verify Deployment
- Go to https://github.com/wxfreekj/esci240-labs/actions
- Wait for green checkmarks (2-3 minutes)
- Visit your deployed labs

### 5. Daily Updates
- Edit files in VS Code
- Source Control → Stage → Commit → Sync
- Done! Auto-deploys in 2-3 minutes

---

## 🌐 Your Deployed Labs

After setup, students access labs at:

| Lab | URL |
|-----|-----|
| Lab 01 | https://wxfreekj.github.io/lab01-student |
| Lab 02 | https://wxfreekj.github.io/lab02-student |
| Lab 03 | https://wxfreekj.github.io/lab03-student |
| Lab 04 | https://wxfreekj.github.io/lab04-student |
| Lab 05 | https://wxfreekj.github.io/lab05-student |
| Lab 06 | https://wxfreekj.github.io/lab06-student |
| Lab 07 | https://wxfreekj.github.io/lab07-student |
| Lab 08 | https://wxfreekj.github.io/lab08-student |
| Lab 09 | https://wxfreekj.github.io/lab09-student |
| Lab 10 | https://wxfreekj.github.io/lab10-student |

---

## 📚 Which Guide to Read?

### I'm brand new to Git and VS Code
→ **Start with:** `DEPLOYMENT_GUIDE.md`
→ **Reference:** `VS_CODE_VISUAL_GUIDE.md`

### I know Git but new to VS Code GUI
→ **Start with:** `VS_CODE_VISUAL_GUIDE.md`
→ **Reference:** `QUICK_START.md`

### I just need a quick reminder
→ **Use:** `QUICK_START.md`

### I want to understand the technical details
→ **Read:** `README.md` sections on deployment

---

## ✅ Success Checklist

- [ ] Downloaded all files from this package
- [ ] Created 10 student repositories on GitHub
- [ ] Enabled GitHub Pages on all 10 repos
- [ ] Created Personal Access Token
- [ ] Added DEPLOY_TOKEN secret
- [ ] Copied .github and .vscode to project
- [ ] Initialized Git in VS Code
- [ ] Committed and pushed to GitHub
- [ ] Verified all 10 workflows ran successfully
- [ ] Tested at least one lab URL in browser
- [ ] Bookmarked the Actions page for monitoring

---

## 🎓 What This Package Does

### For You (Instructor)
✅ **One-time setup** (30-45 minutes)
✅ **Then super simple updates** - just save and click sync
✅ **Automatic deployment** to GitHub Pages
✅ **No command line** needed
✅ **Professional workflow** with version control
✅ **Easy to rollback** if mistakes happen

### For Students
✅ **Simple URLs** to access labs
✅ **No installation** required
✅ **Works on any device** (desktop, tablet, mobile)
✅ **Always get latest version** automatically
✅ **Export answers** for Canvas submission

---

## 🔧 Key Features

### GitHub Actions Workflows
- Trigger automatically on push to main branch
- Only deploy labs that changed (efficient)
- Deploy shared resources to all labs
- Complete in 2-3 minutes
- Visible status at /actions page

### VS Code Tasks
- Quick commit and push with one click
- View all lab URLs instantly
- Check status without terminal
- Keyboard shortcuts for speed
- Integrated with Git GUI

### Repository Structure
- Main repo (esci240-labs) stays private
- Student repos (labXX-student) are public
- Grading system never deployed
- Shared components deployed to all labs
- Clean separation of concerns

---

## 📞 Support Resources

### During Setup
- **Read:** DEPLOYMENT_GUIDE.md (comprehensive)
- **Follow:** VS_CODE_VISUAL_GUIDE.md (step-by-step with visuals)

### Daily Use
- **Check:** QUICK_START.md (fast reference)
- **Monitor:** https://github.com/wxfreekj/esci240-labs/actions

### Troubleshooting
- **DEPLOYMENT_GUIDE.md** has troubleshooting section
- **VS_CODE_VISUAL_GUIDE.md** explains common situations
- **GitHub Actions logs** show detailed error messages

---

## 🎉 You're Ready!

This complete package gives you everything needed to:
1. ✅ Deploy all 10 labs to GitHub Pages
2. ✅ Update labs with simple VS Code clicks
3. ✅ Share clean URLs with students
4. ✅ Maintain version control professionally
5. ✅ Never touch the command line

**Next Steps:**
1. Download all files from this package
2. Open DEPLOYMENT_GUIDE.md
3. Follow the step-by-step instructions
4. Reference VS_CODE_VISUAL_GUIDE.md as needed
5. Use QUICK_START.md for daily reminders

---

## 📄 File Manifest

```
github-deployment/
├── .github/
│   └── workflows/
│       ├── deploy-lab01.yml       (901 bytes)
│       ├── deploy-lab02.yml       (901 bytes)
│       ├── deploy-lab03.yml       (901 bytes)
│       ├── deploy-lab04.yml       (901 bytes)
│       ├── deploy-lab05.yml       (901 bytes)
│       ├── deploy-lab06.yml       (901 bytes)
│       ├── deploy-lab07.yml       (901 bytes)
│       ├── deploy-lab08.yml       (901 bytes)
│       ├── deploy-lab09.yml       (901 bytes)
│       └── deploy-lab10.yml       (901 bytes)
│
├── .vscode/
│   ├── tasks.json                 (2.2 KB)
│   └── settings.json              (266 bytes)
│
├── DEPLOYMENT_GUIDE.md            (8.9 KB) ⭐ START HERE
├── VS_CODE_VISUAL_GUIDE.md        (9.5 KB) 📖 VISUAL GUIDE
├── QUICK_START.md                 (2.0 KB) 🚀 CHEAT SHEET
├── README.md                      (4.9 KB) 📚 REPO DOCS
└── SUMMARY.md                     (THIS FILE)

Total: 17 files
```

---

**Created for:** wxfreekj  
**Repository:** esci240-labs  
**Date:** October 2025  
**Purpose:** Deploy ESCI 240 Weather & Climate Labs to GitHub Pages

🎊 **Happy Teaching!** 🎊
