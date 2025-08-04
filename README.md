
## Python Analytics Results

### Data Cleaning
- Handled missing values using median/mode imputation  
- Applied data type standardization  
- Removed inconsistencies

### Exploratory Data Analysis
- Strong correlation (0.76) between previous SGPA and current CGPA  
- Identified key performance indicators

### Machine Learning Model
- **Model**: Linear Regression  
- **Target**: Current CGPA prediction  
- **Features**: 30 student attributes  
- **Performance**:
  - Mean Squared Error: 0.1080  
  - R-squared: 0.7898 (78.98% accuracy)

## Key Findings
1. Previous academic performance is the strongest predictor of current CGPA  
2. Study habits and attendance significantly impact performance  
3. Socio-economic factors show moderate correlation with academic success

## Usage Instructions
1. Run `python data_cleaning.py` to clean the dataset  
2. Run `python eda.py` for exploratory analysis  
3. Run `python modeling.py` to train and evaluate the model

## Screenshots & Visualizations

### 📊 Data Overview Screenshots
<img width="1359" height="767" alt="Screenshot 2025-08-04 105316" src="https://github.com/user-attachments/assets/492c6bd1-af64-4f57-92e9-1505d0f57ba9" />
<img width="1365" height="766" alt="Screenshot 2025-08-04 105328" src="https://github.com/user-attachments/assets/d09136a0-fe2a-4881-a20e-1a46ee4f84fb" />


### 📈 EDA Screenshots
### DISTRIBUTION OF GENDER 
<img width="798" height="469" alt="Screenshot 2025-08-04 110413" src="https://github.com/user-attachments/assets/66b097eb-3f2c-49ca-940e-0edc8976ea00" />

### DISTRIBUTION OF PROGRAM 
<img width="800" height="467" alt="Screenshot 2025-08-04 110525" src="https://github.com/user-attachments/assets/e73372f1-2098-49aa-985f-832e74165c60" />
### DISTRIBUTION OF CURRENT SEMESTER
<img width="801" height="468" alt="Screenshot 2025-08-04 110634" src="https://github.com/user-attachments/assets/a44cbd29-55dc-4ddc-a7aa-27998e754428" />

### DISTRIBUTION OF WHAT IS YOU CURRENT CGPA
<img width="798" height="667" alt="Screenshot 2025-08-01 203953" src="https://github.com/user-attachments/assets/a53ad9bf-78de-4244-8d96-af9b24dd0c48" />



### 🤖 Model Results Screenshots
Displays the model’s evaluation results:
- **MSE** shows prediction error (lower is better).
- **R²** shows model accuracy (78.98% of CGPA variation explained).
<img width="1365" height="767" alt="Screenshot 2025-08-04 105449" src="https://github.com/user-attachments/assets/17b4f47a-c994-4839-9493-2a78e82a0b3c" />


### 📋 Power BI Dashboard Screenshots
- **Location**: `screenshots/powerbi/`
  - `main_dashboard.png` – Overview dashboard
    <img width="1365" height="767" alt="Screenshot 2025-08-04 080512" src="https://github.com/user-attachments/assets/e7aba7cd-46b5-4af5-ba48-b6425fe1de08" />

    ###  POWER BI DASHBOARD screenshorts 
 
<img width="1351" height="767" alt="Screenshot 2025-08-04 212911" src="https://github.com/user-attachments/assets/a360934b-9f21-4f52-9f62-d31b5a337b74" />



## Requirements
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- openpyxl

## Installation
```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl

