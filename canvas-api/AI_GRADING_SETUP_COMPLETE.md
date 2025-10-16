# AI Grading System - Setup Complete! ✅

## What We Built

You now have a complete AI-powered grading system for ESCI 240 labs that:

1. **Uses your course materials as reference** - The AI grader reads:
   - Lab assignment content (from `web-components/lab01/index.html`)
   - Required reading materials (Science for All Americans - Chapter 1)
   - Your custom grading rubric and criteria
2. **Follows your grading philosophy** - The AI applies:

   - Your specific instructions on tone, fairness, and partial credit
   - Consistent standards across all students
   - Detailed feedback format you prefer

3. **Auto-flags uncertain grades** - The system identifies:
   - Low confidence scores (<0.7)
   - Scores below your threshold (90%)
   - Potential issues (plagiarism, off-topic responses)

## Files Created

### Reference Materials

```
canvas-api/graders/
├── grading_instructions.md     # Your grading philosophy and guidelines
├── lab01_reference.md          # Lab 1 rubric and key concepts
└── lab_config.ini              # Configuration for all labs
```

### AI Grading System

```
canvas-api/graders/
├── ai_grader.py                # Core AI grading engine
├── grade_lab01_ai.py           # Lab 1 implementation
└── AI_GRADING_README.md        # Complete documentation
```

### Configuration

```
canvas-api/
└── .env                        # Contains:
                                # - OPENAI_API_KEY
                                # - OPENAI_MODEL=gpt-4o-mini
                                # - AI_AUTO_APPROVE_THRESHOLD=90
                                # - AI_GRADING_TEMPERATURE=0.3
```

## How to Use

### Grade a Single Student

```powershell
cd canvas-api\graders
python grade_lab01_ai.py --student Test_Student_6299
```

### Grade All Students

```powershell
cd canvas-api\graders
python grade_lab01_ai.py
```

### Review Flagged Submissions

Results saved to: `canvas-api/submissions/lab01/graded/{student_name}/{student_name}_grades.json`

Each result includes:

- Points earned per question
- Percentage and letter grade
- Detailed feedback with strengths and improvement areas
- Confidence rating (0-1)
- Flagged status and reason
- References to course materials

## Test Results

**Test Student (ID 6299) - Lab 1:**

- **Score**: 26.5/30 (88.3%) - B+
- **Flagged**: Yes (4 questions below 90% threshold)
- **Flagged Questions**: Q4a, Q5b, Q6a, Q6b
- **AI Model**: gpt-4o-mini
- **Cost**: ~$0.001 per submission

### Sample Feedback (Q5a - 100%)

```
✓ Strengths: You effectively explained that scientific truth is not determined
by authority, which is a critical concept in understanding the nature of science.

→ Areas for improvement: Adding more detail about the implications of this
principle in the scientific community could enhance your response.

Detailed feedback: Your response clearly articulates that scientific truth is
not determined by authority, emphasizing that no scientist has special access
to the truth. This aligns well with the concepts discussed in the required
reading, particularly the idea that evidence is paramount over credentials.
```

## Cost Estimate

Using **gpt-4o-mini** ($0.15 per 1M tokens):

- **Per submission**: ~$0.001
- **30 students**: ~$0.03 per lab
- **Full semester (10 labs)**: ~$0.30 total

Very affordable! 💰

## Next Steps

### Before Grading All Submissions

1. **Review Test Results**: Check Test Student's grades to ensure AI is grading fairly
   - Location: `canvas-api/submissions/lab01/graded/Test_Student_6299/Test_Student_6299_grades.json`
2. **Adjust Settings if Needed**:

   - Lower threshold: `AI_AUTO_APPROVE_THRESHOLD=85` (fewer flagged)
   - Higher confidence: `OPENAI_MODEL=gpt-4o` (more expensive but more accurate)
   - Adjust temperature: `AI_GRADING_TEMPERATURE=0.2` (more consistent) or `0.5` (more creative)

3. **Customize Instructions**: Edit `grading_instructions.md` to add any specific guidelines

### To Grade All Lab 1 Submissions

1. **Download all submissions**:

   ```powershell
   cd canvas-api\downloads
   python download_lab01_submissions.py
   ```

2. **Run batch grading**:

   ```powershell
   cd ..\graders
   python grade_lab01_ai.py
   ```

3. **Review flagged submissions**: Check grades marked `"status": "needs_review"`

4. **Upload grades to Canvas**: (Upload script coming next!)

### For Labs 2-10

1. **Create reference material**: Copy `lab01_reference.md` to `lab02_reference.md`, etc.
2. **Update criteria**: Copy `grade_lab01_ai.py` to `grade_lab02_ai.py` and update rubric
3. **Run grading**: Same process as Lab 1

## Customization

### Grading Instructions

Edit `canvas-api/graders/grading_instructions.md` to:

- Change feedback tone/style
- Adjust scoring guidelines
- Add lab-specific guidance
- Modify flagging criteria

### Lab Reference Material

Edit `canvas-api/graders/lab01_reference.md` to:

- Add expected answers
- Include key concepts
- Provide grading examples
- Reference specific course materials

### AI Settings

Edit `canvas-api/.env` to:

- Change AI model (gpt-4o for better quality)
- Adjust temperature (lower = more consistent)
- Change auto-approve threshold
- Enable/disable human review

## Quality Assurance

The AI grader now:

- ✅ References your lab assignment materials
- ✅ Follows your grading instructions
- ✅ Provides detailed, constructive feedback
- ✅ Flags uncertain grades for human review
- ✅ Maintains consistent standards
- ✅ Costs less than $0.30 for entire semester

## Support

### Common Issues

**"Token limit exceeded"**

- Solution: Shorten reference materials or use gpt-4o (larger context window)

**"Grades seem too harsh/lenient"**

- Solution: Adjust instructions in `grading_instructions.md`
- Or: Change `AI_GRADING_TEMPERATURE` in `.env`

**"Too many flagged submissions"**

- Solution: Lower `AI_AUTO_APPROVE_THRESHOLD` to 85 or 80

**"Not enough detail in feedback"**

- Solution: Add examples to `lab01_reference.md`
- Or: Switch to `gpt-4o` for better reasoning

### Need Help?

1. Check documentation: `canvas-api/graders/AI_GRADING_README.md`
2. Review examples: `canvas-api/submissions/lab01/graded/`
3. Test with single student before batch grading
4. Adjust settings incrementally

---

**System Status**: ✅ **READY TO GRADE**

You're all set! The AI grading system is configured and tested. When you're ready to grade all Lab 1 submissions, just download them and run the batch grading command.
