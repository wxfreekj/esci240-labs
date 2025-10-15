# 🔄 ESCI 240 Labs Deployment Flow

## The Correct Order (Visual Guide)

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Create 10 Empty Repositories on GitHub            │
│  ✓ lab01-student through lab10-student                     │
│  ✓ All PUBLIC, no initialization                           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Create Personal Access Token                      │
│  ✓ Copy token (starts with ghp_...)                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Add Token to Main Repo                            │
│  ✓ Settings → Secrets → DEPLOY_TOKEN                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 4-8: Push Your Code to Main Repo                     │
│  ✓ Initialize git in VS Code                               │
│  ✓ Commit all files                                        │
│  ✓ Push to github.com/wxfreekj/esci240-labs               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 9: GitHub Actions Run Automatically! 🎉               │
│  ✓ 10 workflows start                                       │
│  ✓ Each pushes content to its lab repo                     │
│  ✓ Wait 2-3 minutes for green checkmarks                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  NOW THE REPOS HAVE CONTENT! ✓                             │
│  ✓ lab01-student has index.html, shared/, etc.            │
│  ✓ lab02-student has index.html, shared/, etc.            │
│  ✓ ... and so on for all 10 labs                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 10: Enable GitHub Pages (NOW IT WORKS!)              │
│  For each lab repo:                                         │
│  ✓ Settings → Pages                                        │
│  ✓ Deploy from branch: main                                │
│  ✓ Folder: / (root)                                        │
│  ✓ Save                                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 11: Your Labs Are Live! 🚀                           │
│  https://wxfreekj.github.io/lab01-student                  │
│  https://wxfreekj.github.io/lab02-student                  │
│  ... and so on!                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Key Points

### Why You Couldn't Enable Pages Initially

❌ **Wrong Order:**

```
Create empty repos → Try to enable Pages → ERROR: No branches found
```

✅ **Correct Order:**

```
Create empty repos → Push to main repo → Actions populate repos → Enable Pages
```

### What GitHub Actions Does

When you push to the main repo, each workflow:

1. Detects changes in its lab folder
2. Copies lab files to a temporary directory
3. Pushes those files to the corresponding `labXX-student` repo
4. Creates the `main` branch with actual content

**Only after this can you enable Pages!**

### After Initial Setup

Once everything is configured, future updates are simple:

```
Edit lab files → Commit → Push → Actions deploy automatically
                                    ↓
                      Updates live in 2-3 minutes! ✅
```

No need to touch Pages settings again - it's all automatic!

## 📊 Quick Checklist

- [ ] Created 10 empty repositories
- [ ] Created personal access token
- [ ] Added DEPLOY_TOKEN to main repo secrets
- [ ] Pushed code to main repository
- [ ] Waited for all 10 GitHub Actions to complete ✅
- [ ] Verified all lab repos now have content
- [ ] Enabled Pages for all 10 lab repositories
- [ ] Tested all 10 lab URLs

## 🆘 Still Having Issues?

1. **Check Actions:** https://github.com/wxfreekj/esci240-labs/actions

   - All workflows should have green checkmarks
   - Click on failed ones to see error details

2. **Check Token Permissions:**

   - Token must have `repo` scope
   - Token must not be expired
   - Token name should be in repo secrets as `DEPLOY_TOKEN`

3. **Check Repository Names:**

   - Must be exactly: `lab01-student`, `lab02-student`, etc.
   - Case-sensitive!
   - Owned by: `wxfreekj`

4. **Check Repository Content:**

   - Visit https://github.com/wxfreekj/lab01-student
   - Should see: index.html, shared/ folder, etc.
   - If empty, GitHub Actions didn't run successfully

5. **Manual Trigger:**
   - Go to Actions tab on main repo
   - Select a workflow
   - Click "Run workflow" button
   - Choose `main` branch
   - Click green "Run workflow" button
