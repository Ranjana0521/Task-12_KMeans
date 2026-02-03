#  Mall Customer Segmentation Using K-Means Clustering

## 📌 Project Overview

This project performs **customer segmentation** using **K-Means clustering** on the Mall Customer dataset from Kaggle. The goal is to group customers based on **Annual Income** and **Spending Score** to help businesses understand customer behavior and design targeted marketing strategies.

---

## 📊 Dataset

**Name:** Mall Customer Segmentation Dataset
**Source:** Kaggle

### Features Used for Clustering:

* **Annual Income (k$)** – Customer yearly income
* **Spending Score (1-100)** – Spending behavior score assigned by the mall

---

## 🛠 Tools & Technologies

* **Python**
* **Pandas** – Data manipulation
* **Scikit-learn** – KMeans clustering & StandardScaler
* **Matplotlib** – Data visualization

---

##  Project Workflow

###  Load Dataset

* Imported the dataset using Pandas.
* Inspected the structure and verified required columns.


###  Data Preprocessing

* Removed the `CustomerID` column since it does not contribute to clustering.
* Selected **Annual Income** and **Spending Score** for analysis.


###  Feature Scaling

* Applied **StandardScaler** to normalize feature values.
* Ensured balanced distance calculation for K-Means algorithm.
  

###  Elbow Method for Optimal K

* Trained K-Means with cluster values from **K = 1 to 10**.
* Stored inertia values.
* Plotted elbow curve to find the optimal number of clusters.


###  Model Training

* Selected the optimal cluster count from elbow plot.
* Trained final K-Means model.
* Generated cluster labels for customers.


###  Cluster Visualization

* Created scatter plot using scaled features.
* Visualized customer groups based on income and spending behavior.


###  Export Segmented Dataset

* Added cluster labels to original dataset.
* Saved output as a CSV file for business analysis.


## 📈 Results

### ✔ Elbow Plot

Used to determine optimal number of clusters.

### ✔ Cluster Visualization

Scatter plot showing distinct customer groups.

### ✔ Segmented Dataset

Final dataset containing cluster labels for each customer.

Output File:

```
Mall_Customers_Segmented.csv
```
---


Just say 👍

