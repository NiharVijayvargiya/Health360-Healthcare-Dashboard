# Health360: Comprehensive Healthcare Risk & Disease Analysis

Tableau dashboard and data story on a 5,000-record healthcare dataset, embedded in a Flask web app.

## Links
- Dashboard: https://public.tableau.com/app/profile/nihar.vijayvargiya/viz/Health360_17934468105130/Health360Dashboard
- Story: https://public.tableau.com/app/profile/nihar.vijayvargiya/viz/Health360_17934468105130/Health360Story
- Demo video: https://drive.google.com/file/d/1HwZMmzwnsz3MI2uoAWj93sWubI4FbPbZ/view?usp=drive_link

## What is inside
- 9 visualizations, 1 dashboard, 1 story (Tableau Public)
- Calculated fields: Age Group, Bmi Category, Exercise Label
- Flask app that embeds the dashboard and story
- `data/smart_healthcare_dataset.csv`: source dataset

## Run locally
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Key findings
- Age is the strongest factor: no patient aged 50 or under has any of the three conditions.
- Heart disease rate rises with BMI: Underweight 20.5%, Normal 26.0%, Overweight 32.9%, Obese 40.0%.
- 54.9% of patients have blood pressure of 130 or above.

The dataset looks synthetic. This is a learning project, not medical advice.
