#### Collection of projects related to Data Science skillsets that I want to build

1. Collecting data
   - Scraping seems the most readily available method as an individual
   - Find sites that contain collected data such as fivethirtyeight or Kaggle
2. Clean and process data
   - Pandas deal with missing values, normalization
3. Exploratory data anaylsis
   - Identify what to look for and what methods are utilized
4. Model building
   - Understanding the algorithm behind each models
   - Voting models
   - Tuning hypeparameters
5. Model production
   - Advancement of model from planning and testing on previous data into working with live data

#### Dependencies

To install dependencies:

```console
pip install -r requirements.txt
```

### Setting Up Pre-Commit Hooks
After installing dependencies:
```console
pre-commit install
```

Pre-commit hooks will run upon commit on staged .ipynb files. To apply them to all .ipynb files without committing: 

```console
pre-commit run --all-files
```