# Titanic Survival — EDA & Data Prep

a structured exploratory data analysis (EDA) and data preparation notebook. The focus is on understanding the data, fixing quality issues, engineering explainable features, and summarising early insights that will feed into modelling in later parts.

---

## 1) Objectives

- Inspect the dataset schema and quality (types, missingness, duplicates).
- Perform **targeted cleaning** without distorting distributions.
- Engineer simple, interpretable features for survival analysis.
- Produce quick diagnostics and visuals that explain early patterns.

---

## 2) Dataset

- Source file: `Titanic.csv` (Kaggle-style Titanic passenger data)
- Rows: 891 | Key columns: `Survived`, `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Cabin`, `Embarked`, `Name`, `Ticket`.

**Known quirks**
- Missing values in **Age (~20%)**, **Cabin (~77%)**, and **Embarked (<1%)**.
- Some variables need categorical encoding / type fixes.

---

