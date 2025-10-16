# AI-Powered Grading System for ESCI 240 Labs

## Overview

This system uses OpenAI's GPT models (ChatGPT) to automatically grade subjective student responses in lab assignments. The AI provides:

- **Detailed feedback** for each answer
- **Rubric-based scoring** with partial credit
- **Confidence ratings** for each grade
- **Automatic flagging** of responses that need human review
- **Batch processing** for entire classes

## Setup

### 1. Install Required Packages

```bash
pip install openai>=1.0.0 python-dotenv
```

Or install all requirements:

```bash
pip install -r requirements.txt
```

### 2. Get an OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "+ Create new secret key"
4. Give it a name (e.g., "ESCI 240 Grading")
5. Copy the key (starts with `sk-...`)
6. **Save it immediately** - you won't see it again!

### 3. Add API Key to .env File

Edit `canvas-api/.env` and add:

```bash
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4o-mini
AI_AUTO_APPROVE_THRESHOLD=90
AI_GRADING_TEMPERATURE=0.3
REQUIRE_HUMAN_REVIEW=false
```

**Security Note:** Never commit your .env file to Git! It's already in .gitignore.

## Configuration Options

| Setting                     | Default       | Description                                    |
| --------------------------- | ------------- | ---------------------------------------------- |
| `OPENAI_API_KEY`            | (required)    | Your OpenAI API key                            |
| `OPENAI_MODEL`              | `gpt-4o-mini` | Which GPT model to use                         |
| `AI_AUTO_APPROVE_THRESHOLD` | `90`          | Percentage threshold for auto-approval (0-100) |
| `AI_GRADING_TEMPERATURE`    | `0.3`         | AI creativity (0=consistent, 1=creative)       |
| `REQUIRE_HUMAN_REVIEW`      | `false`       | If true, ALL grades are flagged for review     |

### Model Comparison

| Model         | Cost (per 1M tokens) | Speed  | Quality   | Recommended For             |
| ------------- | -------------------- | ------ | --------- | --------------------------- |
| `gpt-4o-mini` | $0.15 / $0.60        | Fast   | Good      | Large classes, most labs    |
| `gpt-4o`      | $2.50 / $10.00       | Medium | Excellent | Complex essays, final exams |
| `gpt-4-turbo` | $10 / $30            | Slower | Excellent | Maximum accuracy needed     |

**Recommendation:** Use `gpt-4o-mini` for routine grading. It's 16x cheaper than gpt-4-turbo and works great for structured assignments.

## Usage

### Grade All Lab 1 Submissions

```bash
cd canvas-api/graders
python grade_lab01_ai.py
```

Output:

```
Grading all submissions in C:\...\submissions\lab01\raw
Grading Test_Student_6299...
  Score: 28/30 (93.3%) - A
✅ Grading complete!
   Total submissions: 1
   Results saved to: C:\...\submissions\lab01\graded\grades.json
```

### Grade a Single Student

```bash
python grade_lab01_ai.py --student Test_Student_6299
```

### Custom Output Location

```bash
python grade_lab01_ai.py --output ../submissions/lab01/graded/my_grades.json
```

## Grading Workflow

1. **Download submissions** from Canvas:

   ```bash
   cd downloads
   python download_lab01_submissions.py
   ```

2. **Grade with AI**:

   ```bash
   cd ../graders
   python grade_lab01_ai.py
   ```

3. **Review flagged submissions**:

   - Open `submissions/lab01/graded/grades.json`
   - Look for `"flagged_for_review": true`
   - Manually adjust scores if needed

4. **Upload grades to Canvas** (coming soon):
   ```bash
   cd ../uploads
   python upload_grades.py --lab 1
   ```

## Output Format

The grader produces `submissions/lab01/graded/grades.json`:

```json
{
  "lab_number": 1,
  "graded_at": "2025-10-15T20:30:00",
  "total_submissions": 1,
  "student_grades": {
    "Test_Student_6299": {
      "total_points_earned": 28,
      "total_points_possible": 30,
      "percentage": 93.3,
      "letter_grade": "A",
      "flagged_for_review": false,
      "grading_method": "AI (OpenAI API)",
      "status": "graded",
      "question_results": {
        "q1a": {
          "points_earned": 3,
          "points_possible": 3,
          "percentage": 100.0,
          "feedback": "✓ Strengths: Student correctly identifies...",
          "confidence": 0.95,
          "flagged": false
        }
      }
    }
  }
}
```

## When Submissions Are Flagged

The AI automatically flags submissions for human review when:

1. **Low AI confidence** (<70%)
2. **Low score** (below auto-approve threshold, default 90%)
3. **Empty response**
4. **Potential plagiarism** detected
5. **AI-generated content** suspected
6. **Unusual patterns** or concerns

### Reviewing Flagged Submissions

```json
{
  "flagged_for_review": true,
  "flagged_questions": ["q2", "q4a"],
  "review_reason": "Low AI confidence (65%)"
}
```

**What to do:**

1. Read the student's response
2. Read the AI's feedback
3. Adjust the score if needed
4. Mark as reviewed: `"status": "reviewed"`

## Grading Rubric (Lab 1)

| Question  | Points | Criteria                                                  |
| --------- | ------ | --------------------------------------------------------- |
| Q1a       | 3      | Identifies naturalism (science studies natural phenomena) |
| Q1b       | 3      | Explains uniformity (laws are consistent everywhere)      |
| Q2        | 3      | Rejects fixed steps + explains variability                |
| Q3        | 3      | Explains indirect evidence (fossils, etc.)                |
| Q4a       | 3      | Identifies bias sources                                   |
| Q4b       | 3      | Describes safeguards against bias                         |
| Q5a       | 3      | Explains science not based on authority                   |
| Q5b       | 3      | Evidence-based acceptance process                         |
| Q6a       | 3      | Identifies ethical challenge #1                           |
| Q6b       | 3      | Identifies ethical challenge #2                           |
| **Total** | **30** |                                                           |

## Cost Estimation

### Lab 1 (30 points, 6 questions)

- **Input tokens per submission:** ~2,000
- **Output tokens per submission:** ~800
- **Cost per submission (gpt-4o-mini):** ~$0.001 (1/10th of a cent)
- **Cost for 30 students:** ~$0.03

### Full Semester (10 labs, 30 students)

- **Total submissions:** 300
- **Estimated cost (gpt-4o-mini):** ~$0.30
- **Estimated cost (gpt-4o):** ~$4.80

**Conclusion:** AI grading is extremely cost-effective!

## Quality Control

### Best Practices

1. **Spot Check** - Manually review 10-20% of AI grades
2. **Review Flagged** - Always review submissions flagged by AI
3. **Track Accuracy** - Compare AI grades to your manual grades
4. **Adjust Threshold** - Raise/lower `AI_AUTO_APPROVE_THRESHOLD` based on accuracy
5. **Provide Context** - The more context you give the AI, the better it grades

### Improving Accuracy

1. **Add reference answers** to the grading criteria
2. **Include lecture notes** as context
3. **Use higher-quality model** (gpt-4o vs gpt-4o-mini)
4. **Lower temperature** for more consistency (0.1 vs 0.3)
5. **Refine rubric** based on common student mistakes

## Customization

### Creating Graders for Other Labs

Copy `grade_lab01_ai.py` and modify:

1. **Update criteria** in `_define_criteria()`:

   ```python
   "q1": [
       GradingCriteria(
           name="Identifies concept",
           description="Student correctly identifies...",
           points=5
       )
   ]
   ```

2. **Update parsing** if format differs
3. **Update context** with relevant reading/lectures

### Adding Reference Answers

```python
reference_answers = {
    "q1a": "Science assumes naturalism - it studies only natural, observable phenomena and does not invoke supernatural explanations.",
    "q1b": "Science assumes uniformity - the basic laws of nature are the same throughout the universe."
}

result = self.ai_grader.grade_response(
    question_prompt=prompt,
    student_response=response,
    criteria=self.question_criteria[q_id],
    reference_answer=reference_answers.get(q_id),
    context="From Science for All Americans, Chapter 1"
)
```

## Troubleshooting

### "OPENAI_API_KEY not set"

- Check that you added it to `.env`
- Make sure `.env` is in `canvas-api/` directory
- Verify no extra spaces around `=`

### "Rate limit exceeded"

- You're grading too fast
- Add delays between submissions:
  ```python
  import time
  time.sleep(1)  # Wait 1 second between requests
  ```

### "Model not found"

- Check your model name in `.env`
- Valid models: `gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`

### Grades seem too harsh/generous

- Adjust `AI_GRADING_TEMPERATURE` (lower = stricter)
- Modify grading criteria descriptions
- Add reference answers for comparison

### API costs higher than expected

- Check your usage: https://platform.openai.com/usage
- Switch to `gpt-4o-mini` (cheapest option)
- Grade in smaller batches

## Security & Privacy

- ✅ **API keys** are in `.gitignore` (never committed)
- ✅ **Student data** stays local (not stored by OpenAI beyond API call)
- ✅ **FERPA compliant** - no PII sent except as needed for grading
- ⚠️ **Use school account** if available for better data protection
- ⚠️ **Review API terms** - ensure compliance with your institution's policy

## Support

For issues:

1. Check this README
2. Review error messages
3. Check OpenAI API status: https://status.openai.com/
4. Test with a single submission first

## Future Enhancements

- [ ] Web UI for reviewing flagged submissions
- [ ] Comparative grading (student vs. class average)
- [ ] Grade appeal workflow
- [ ] Export to Canvas with comments
- [ ] Plagiarism detection integration
- [ ] Multi-language support
