# IBM Data Science Capstone — SpaceX Falcon 9 Landing Prediction

This repository is organized in the same order as the IBM Applied Data Science Capstone workflow: data collection, web scraping, wrangling, EDA, SQL, Folium, Plotly Dash, classification, and final reporting.

## Project question
Can we predict whether the Falcon 9 first stage will land successfully from launch and payload characteristics?

## Reproducible study dataset
The analysis uses the standard 90-record Falcon 9 capstone extract covering June 2010 through November 2020. `data/dataset_part_1.csv` contains 17 columns. The target `Class` is derived from the landing outcome.

## Workflow
1. `notebooks/01_data_collection_api.ipynb` — SpaceX REST API
2. `notebooks/02_web_scraping.ipynb` — Wikipedia scraping
3. `notebooks/03_data_wrangling.ipynb` — cleaning + target creation
4. `notebooks/04_eda_visualization.ipynb` — EDA charts
5. `notebooks/05_eda_sql.ipynb` — SQL analysis
6. `notebooks/06_folium_map.ipynb` — interactive maps
7. `notebooks/07_dashboard_analysis.ipynb` + `dashboard/app.py` — Dash dashboard
8. `notebooks/08_machine_learning.ipynb` — classification + GridSearchCV
9. `Data Science Capstone Project Report.pdf` — final presentation

## Key reproducible results
- 90 Falcon 9 launches
- 66.7% overall first-stage landing success
- CCAFS SLC 40: 55 launches
- KSC LC 39A: 22 launches, 77.3% success ratio
- VAFB SLC 4E: 13 launches
- Logistic Regression, SVM and Decision Tree: 83.33% test accuracy in the reproduced split
- KNN: 77.78% test accuracy
- Decision Tree: strongest GridSearchCV score in the reproduced run (~89.1%)

## Sources
- SpaceX API: https://api.spacexdata.com/v4/launches/past
- SpaceX API documentation: https://github.com/r-spacex/SpaceX-API
- Wikipedia launch history: https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches
- IBM Applied Data Science Capstone course workflow and dataset conventions.

## Run locally
```bash
pip install -r requirements.txt
jupyter notebook
python dashboard/app.py
```

Then open the Dash app at `http://127.0.0.1:8050/`.

## GitHub submission
Create a new public repository, copy this folder into it, then run:

```bash
git init
git add .
git commit -m "Complete IBM Data Science Capstone SpaceX project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your actual repository before pushing.
