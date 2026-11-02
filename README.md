# Health360: Comprehensive Healthcare Risk & Disease Analysis

Health360 is an interactive Tableau analytics project and Flask web application built on a 5,000-record healthcare dataset.

## Problem
Chronic diseases such as heart disease, diabetes and stroke are often detected late because reviewing patient records by hand hides broader population trends. Health360 transforms static patient records into an interactive dashboard so those trends become visible quickly.

## Links
- Dashboard: https://public.tableau.com/app/profile/nihar.vijayvargiya/viz/Health360_17934468105130/Health360Dashboard
- Story: https://public.tableau.com/app/profile/nihar.vijayvargiya/viz/Health360_17934468105130/Health360Story
- Demo Video: https://drive.google.com/file/d/1HwZMmzwnsz3MI2uoAWj93sWubI4FbPbZ/view?usp=drive_link

## Dashboard
<img width="800" alt="Health360 Dashboard" src="https://github.com/user-attachments/assets/7cb6345b-a7ca-4888-9b84-c69e6eb28621" />

## Story
<img width="800" alt="Health360 Story" src="https://github.com/user-attachments/assets/e52b56eb-305d-454d-ba2a-dd2260c2dd9a" />

## Key Analytical Findings
- **Age Threshold:** Age is the strongest factor; no patient aged 50 or under has any of the three conditions.
- **BMI Progression:** Heart disease rate rises consistently with BMI: Underweight (20.5%), Normal (26.0%), Overweight (32.9%), and Obese (40.0%).
- **Blood Pressure:** 54.9% of patients have a blood pressure reading of 130 or above.

The dataset looks synthetic. This is a learning project, not medical advice.

## What is inside
- 1 dashboard & 1 story (Tableau Public)
- Calculated fields: Age Group, Bmi Category, Exercise Label
- Flask app that embeds the dashboard and story
- `data/smart_healthcare_dataset.csv`: source dataset

## Run locally
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000
