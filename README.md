<img width="1700" height="1651" alt="16_story_full" src="https://github.com/user-attachments/assets/e52b56eb-305d-454d-ba2a-dd2260c2dd9a" />
<img width="1220" height="1497" alt="15_dashboard_full" src="https://github.com/user-attachments/assets/7cb6345b-a7ca-4888-9b84-c69e6eb28621" />
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
