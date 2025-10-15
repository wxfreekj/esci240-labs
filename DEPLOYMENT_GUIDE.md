# 🎓 ESCI 240 Labs - VS Code Deployment Guide

This guide will help you deploy all 10 labs to GitHub Pages using **only VS Code's GUI** - no command line needed!

---

## 📋 Prerequisites Checklist

Before starting, make sure you have:

- [ ] VS Code installed
- [ ] Git installed on your computer
- [ ] A GitHub account (username: wxfreekj)
- [ ] All 10 labs completed in your `web-components` folder

---

## 🚀 One-Time Setup (Steps 1-5)

### Step 1: Create Student Lab Repositories on GitHub

You need to create 10 empty repositories on GitHub for your students to access:

1. Go to https://github.com/wxfreekj
2. Click the **"+"** button (top right) → **"New repository"**
3. Create these 10 repositories (one at a time):
   - `lab01-student`
   - `lab02-student`
   - `lab03-student`
   - `lab04-student`
   - `lab05-student`
   - `lab06-student`
   - `lab07-student`
   - `lab08-student`
   - `lab09-student`
   - `lab10-student`

For each repository:

- ✅ Make it **Public** (so students can access)
- ✅ **Do NOT** initialize with README, .gitignore, or license
- ✅ Click **"Create repository"**

### Step 2: Create Personal Access Token

This token allows GitHub Actions to automatically deploy your labs:

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Settings:
   - Note: `ESCI 240 Lab Deployment`
   - Expiration: **No expiration** (or 1 year)
   - Scopes: Check **`repo`** (this checks all sub-boxes)
4. Click **"Generate token"**
5. **COPY THE TOKEN** - you'll only see it once! (It looks like: `ghp_xxxxxxxxxxxxxxxxxxxx`)

### Step 3: Add Token to Main Repository

1. Go to https://github.com/wxfreekj/esci240-labs
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Name: `DEPLOY_TOKEN`
5. Secret: Paste your token from Step 3
6. Click **"Add secret"**

### Step 4: Open Your Project in VS Code

1. Open VS Code
2. File → Open Folder
3. Navigate to your `esci240-labs` folder (the one with all your labs)
4. Click **"Select Folder"**

---

## 📦 Initial Upload to GitHub (First Time Only)

### Step 5: Copy Configuration Files

1. Download all the files I created for you
2. In VS Code's Explorer panel (left side):
   - Copy the `.github` folder to your project root
   - Copy the `.vscode` folder to your project root

Your project should now look like:

```
esci240-labs/
├── .github/
│   └── workflows/
│       ├── deploy-lab01.yml
│       ├── deploy-lab02.yml
│       └── ... (all 10)
├── .vscode/
│   ├── tasks.json
│   └── settings.json
├── web-components/
│   ├── lab01/
│   ├── lab02/
│   └── ... (all 10)
└── ... (other files)
```

### Step 6: Initialize Git Repository (VS Code GUI)

1. In VS Code, click the **Source Control** icon (left sidebar - looks like a branch)
2. Click **"Initialize Repository"**
3. You'll see all your files listed as changes

### Step 7: Make Your First Commit

1. In the Source Control panel, you'll see a list of changed files
2. Hover over "Changes" and click the **"+"** icon to stage all files
3. In the message box at the top, type: `Initial commit: All 10 labs with auto-deployment`
4. Click the **✓ Checkmark** button (or press Ctrl+Enter)

### Step 8: Connect to GitHub and Push

1. Click the **three dots menu** (•••) in Source Control panel
2. Select **"Remote"** → **"Add Remote"**
3. Paste this URL: `https://github.com/wxfreekj/esci240-labs.git`
4. Name it: `origin`
5. Click **"Add remote"**

Now push your code:

1. Click the **three dots menu** (•••) again
2. Select **"Push to..."**
3. Choose **"origin"**
4. If prompted, log in to GitHub

🎉 **Your code is now on GitHub!**

### Step 9: Wait for Initial Deployment

The GitHub Actions workflows will now automatically push content to your 10 lab repositories:

1. Go to https://github.com/wxfreekj/esci240-labs/actions
2. You should see 10 workflows running (one for each lab)
3. Wait for all green checkmarks ✅ (takes about 2-3 minutes)

This first deployment pushes your lab content to each `labXX-student` repository.

### Step 10: Enable GitHub Pages for Each Lab

**Now that the repositories have content**, you can enable GitHub Pages:

For **each** of the 10 repositories:

1. Go to the repository (e.g., https://github.com/wxfreekj/lab01-student)
2. You should now see files in the repository (index.html, etc.)
3. Click **Settings** (top menu)
4. Scroll down to **Pages** (left sidebar)
5. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main** ← This option will now be available!
   - Folder: **/ (root)**
6. Click **Save**

Repeat for all 10 lab repositories:

- lab01-student through lab10-student

### Step 11: Verify Your Labs Are Live

### Step 11: Verify Your Labs Are Live

Wait about 2-3 minutes after enabling Pages, then check if your labs are accessible:

1. Go to https://github.com/wxfreekj/esci240-labs/actions
2. Verify all workflows completed successfully ✅

Your labs are now live at:

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

---

## 🔄 Daily Workflow (After Initial Setup)

Once everything is set up, updating labs is super easy:

### Making Changes to Labs

1. **Edit your lab files** in VS Code as normal
2. **Save your changes** (Ctrl+S)
3. Go to **Source Control panel** (left sidebar)
4. You'll see your changed files listed
5. **Stage changes**: Click the **"+"** next to each file (or stage all)
6. **Write a commit message**: e.g., "Updated Lab 5 questions"
7. **Commit**: Click the ✓ checkmark
8. **Push to GitHub**: Click the **"Sync Changes"** button (or three dots → Push)

That's it! GitHub Actions will automatically deploy the updated labs within 2-3 minutes.

### Using Quick Tasks

Press **Ctrl+Shift+P** and type "Tasks: Run Task", then choose:

- **🚀 Push All Changes to Main Repo** - Commits everything with a generic message and pushes
- **📊 Check Git Status** - See what files you've changed
- **🔄 Pull Latest Changes** - Get updates from GitHub
- **🌐 View All GitHub Pages URLs** - See all your deployed lab URLs

---

## 🎯 How Automatic Deployment Works

Every time you push code to GitHub:

1. GitHub Actions detects which lab folders changed
2. Only those labs are automatically redeployed
3. Takes 2-3 minutes
4. Students see the updated version at the GitHub Pages URL

**Example:** If you only edit Lab 5, only Lab 5 will be redeployed. The other 9 labs stay the same.

---

## 🆘 Troubleshooting

### "Failed to push" error

- **Solution**: Click three dots → Pull, then try pushing again

### Labs not deploying

- **Check**: Go to https://github.com/wxfreekj/esci240-labs/actions
- **Look for**: Red X marks (click to see error details)
- **Common fix**: Make sure DEPLOY_TOKEN secret is set correctly

### "Not a git repository" error

- **Solution**: Delete the `.git` folder and restart from Step 7

### Changes not showing on GitHub Pages

- **Wait**: Can take 2-3 minutes for deployment
- **Hard refresh**: Press Ctrl+Shift+R in your browser
- **Check**: Make sure you pushed to the main repo (not directly to lab repos)

---

## 📚 Understanding Your Repository Structure

```
Main Repository (esci240-labs)
├── Your work happens here
├── GitHub Actions deploy FROM here
└── Students never see this repo

Student Repositories (lab01-student, etc.)
├── Automatically updated by GitHub Actions
├── Students access these via GitHub Pages
└── You don't push directly to these
```

---

## 🎓 Sharing Labs with Students

Give students these direct links:

- Lab 01: https://wxfreekj.github.io/lab01-student
- Lab 02: https://wxfreekj.github.io/lab02-student
- _(etc.)_

Or share the pattern: `https://wxfreekj.github.io/labXX-student`

Students can:

- ✅ Complete the labs in their browser
- ✅ Export their answers as text files
- ✅ Submit to Canvas

Students **cannot** see your:

- ❌ Main repository code
- ❌ Grading system
- ❌ Other lab folders

---

## 🎉 You're Done!

You can now:

- ✅ Edit labs in VS Code
- ✅ Click a few buttons to deploy
- ✅ Share links with students
- ✅ Update anytime with automatic deployment

**No command line needed!** Everything is done through VS Code's GUI.

---

## � Troubleshooting Common Issues

### "Can't enable GitHub Pages - No branches found"

**Solution:** This happens if the repositories are still empty. Follow the correct order:

1. Create the empty repositories (Step 1)
2. Set up the token and push code from main repo (Steps 2-8)
3. Wait for GitHub Actions to run (Step 9) - this populates the repos
4. **Then** enable Pages (Step 10)

### "GitHub Actions workflow failed"

**Check:**

- Is `DEPLOY_TOKEN` set up correctly in main repo secrets?
- Does the token have `repo` scope permissions?
- Are the repository names exactly `lab01-student`, `lab02-student`, etc.?

**Fix:** Go to https://github.com/wxfreekj/esci240-labs/actions and click on the failed workflow to see error details.

### "Lab page shows 404 after enabling Pages"

**Solution:**

1. Wait 2-3 minutes - Pages take time to build
2. Check that Pages is set to deploy from `main` branch, `/` (root) folder
3. Verify the repository has content (not empty)
4. Check https://github.com/wxfreekj/lab01-student/deployments for build status

### "Need to manually trigger deployment"

**Solution:**

1. Go to https://github.com/wxfreekj/esci240-labs/actions
2. Click on the workflow for the lab you want to deploy (e.g., "Deploy Lab 01")
3. Click "Run workflow" → Select branch `main` → Click "Run workflow"

### "Made changes but lab didn't update"

**Check:**

- Did you commit AND push your changes?
- Did you push to the `main` branch?
- Check GitHub Actions to see if workflow ran
- Workflow only runs if you changed files in that specific lab folder

---

## �📞 Quick Reference Card

| What I want to do  | How to do it in VS Code                     |
| ------------------ | ------------------------------------------- |
| Save my changes    | Source Control → Stage → Commit → Sync      |
| See what changed   | Source Control panel (shows all changes)    |
| Push to GitHub     | Click "Sync Changes" button                 |
| Quick commit+push  | Ctrl+Shift+P → "Push All Changes"           |
| View deployed labs | Ctrl+Shift+P → "View All GitHub Pages URLs" |
| Undo last commit   | Three dots → Undo Last Commit               |

---

**Questions?** Check the GitHub Actions page for deployment status:
https://github.com/wxfreekj/esci240-labs/actions
