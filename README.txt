CSI Internship – Week 4 Assignment
Name: Ankan Roy

Dataset: Kaggle Titanic Dataset (train.csv)

Tools: Google Colab, Python, pandas, seaborn, matplotlib

Data Preprocessing
Handled missing values in Age (filled with median)

Filled missing values in Embarked (mode)

Dropped or ignored Cabin due to excessive nulls

Converted categorical variables for analysis (e.g., Sex, Embarked)

Visualizations:
Age Distribution (Histogram)

Fare Outlier Detection (Boxplot)

Survival Count (Barplot)

Survival by Gender (Barplot with hue)

Survival by Class (Barplot with hue)

Age vs Survival (Histogram with hue)

Correlation Heatmap (numeric features only)

Insights:
Females had a significantly higher survival rate than males

Passengers from 1st class had better survival chances

Age is centered around 20–40 years; children had slightly better survival

Fare has major outliers and is skewed to the right

Embarked 'C' passengers had better survival rate

Correlation heatmap showed weak correlation of Survived with Age, Fare, and SibSp

