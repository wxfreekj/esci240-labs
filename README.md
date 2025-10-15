# ESCI 240 Weather & Climate Labs

This repository contains all course materials for ESCI 240 Weather & Climate Labs with automated deployment to GitHub Pages.

## 📚 Labs Overview

All 10 labs are web-based, interactive assignments that students complete in their browser:

| Lab    | Topic                                 | Points | URL                                                  |
| ------ | ------------------------------------- | ------ | ---------------------------------------------------- |
| Lab 01 | Vertical Structure of the Atmosphere  | 30     | [View Lab](https://wxfreekj.github.io/lab01-student) |
| Lab 02 | Horizontal Temperature Patterns       | 30     | [View Lab](https://wxfreekj.github.io/lab02-student) |
| Lab 03 | Horizontal Pressure and Wind Patterns | 30     | [View Lab](https://wxfreekj.github.io/lab03-student) |
| Lab 04 | Atmospheric Moisture                  | 30     | [View Lab](https://wxfreekj.github.io/lab04-student) |
| Lab 05 | Solar & Terrestrial Radiation         | 30     | [View Lab](https://wxfreekj.github.io/lab05-student) |
| Lab 06 | Weather Map Analysis (Part 1)         | 30     | [View Lab](https://wxfreekj.github.io/lab06-student) |
| Lab 07 | Weather Map Analysis (Part 2)         | 30     | [View Lab](https://wxfreekj.github.io/lab07-student) |
| Lab 08 | Mid-Latitude Cyclones                 | 30     | [View Lab](https://wxfreekj.github.io/lab08-student) |
| Lab 09 | Weather Forecasting                   | 30     | [View Lab](https://wxfreekj.github.io/lab09-student) |
| Lab 10 | Severe Weather – Tornado Development  | 30     | [View Lab](https://wxfreekj.github.io/lab10-student) |

## 🎯 Features

- ✅ **Interactive web forms** - Students complete labs in browser
- ✅ **Progress tracking** - Save and resume progress
- ✅ **Text file export** - Easy submission to Canvas
- ✅ **Automatic deployment** - Push to GitHub → Labs auto-update
- ✅ **Responsive design** - Works on desktop, tablet, mobile
- ✅ **No dependencies** - Pure HTML/CSS/JavaScript

## 🚀 Deployment

This repository uses **GitHub Actions** to automatically deploy each lab to its own GitHub Pages site.

**How it works:**

1. Edit lab files in `web-components/labXX/`
2. Commit and push to the `main` branch
3. GitHub Actions automatically deploys affected labs
4. Students see updates at their lab URLs within 2-3 minutes

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed setup instructions.

## 📁 Repository Structure

```
esci240-labs/
├── .github/
│   └── workflows/          # GitHub Actions deployment configs
│       ├── deploy-lab01.yml
│       ├── deploy-lab02.yml
│       └── ... (10 total)
├── .vscode/
│   ├── tasks.json         # VS Code quick tasks
│   └── settings.json      # VS Code Git settings
├── web-components/
│   ├── shared/            # Shared utilities and styles
│   │   ├── styles/
│   │   └── utils/
│   ├── lab01/            # Individual lab folders
│   ├── lab02/
│   └── ... (10 total)
├── grading-system/       # Private grading tools (not deployed)
└── docs/                 # Course documentation
```

## 🔧 For Instructors

### Making Changes to Labs

1. Open the project in VS Code
2. Edit lab files in `web-components/labXX/`
3. Use Source Control panel to commit and push
4. Wait 2-3 minutes for automatic deployment

### Adding New Labs

1. Create new folder: `web-components/lab11/`
2. Copy workflow: `.github/workflows/deploy-lab11.yml`
3. Update workflow with lab11 paths
4. Create GitHub repo: `lab11-student`
5. Enable GitHub Pages in repo settings

### Quick Tasks

Press `Ctrl+Shift+P` and type "Tasks: Run Task":

- **Push All Changes** - Quick commit and push
- **View All URLs** - See all deployed lab links
- **Check Status** - View git status

## 👥 For Students

Students access labs directly through their browser:

- No installation required
- No account needed
- Works on any device
- Export answers as text file for submission

## 📖 Documentation

- [**Deployment Flow Chart**](DEPLOYMENT_FLOWCHART.md) - Visual guide showing correct deployment order
- [Full Deployment Guide](DEPLOYMENT_GUIDE.md) - Complete setup instructions
- [Quick Start Guide](QUICK_START.md) - Cheat sheet for common tasks

## 🛠️ Technical Details

**Technologies:**

- Pure HTML5, CSS3, JavaScript (ES6+)
- No frameworks or build tools required
- GitHub Actions for CI/CD
- GitHub Pages for hosting

**Browser Support:**

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

## 📊 Grading System

The grading system is stored in the `grading-system/` folder and is **NOT** deployed to student-facing sites. It includes:

- Canvas API integration
- Automated grading tools
- Assignment management
- Grade export utilities

## 📝 License

Course materials © 2025 - For educational use only.

## 🆘 Support

For setup issues or questions:

1. Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. View deployment status: https://github.com/wxfreekj/esci240-labs/actions
3. Check individual lab repo issues

---

**Repository maintained by:** wxfreekj  
**Course:** ESCI 240 - Weather & Climate  
**Last updated:** October 2025
