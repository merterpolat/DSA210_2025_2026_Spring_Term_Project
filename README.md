# Quantitative Analysis of Grappling and Striking Metrics on Win Probabilities in UFC

## Motivation and Problem Definition
The objective of this project is to investigate the statistical impact of different combat disciplines—specifically **grappling** and **striking**—on victory outcomes in the Ultimate Fighting Championship (UFC). 

While MMA is a blend of styles, there is a continuous debate on which skill set is a better predictor of success. This project will quantitatively analyze whether:
* **Grappling Efficiency:** Takedown accuracy and submission attempts.
* **Striking Efficiency:** Significant strike accuracy and volume.

By analyzing historical performance data, the goal is to uncover the underlying patterns of dominance between these two fundamental combat pillars and determine which has a stronger correlation with winning a fight.

---

## Data Source and Collection
The primary data is sourced from the **UFC Fight Historical Data** (scraped from the official UFC database).

* **`data.csv`**: Contains fight-by-fight metrics.
* **`raw_fighter_details.csv`**: Contains physical attributes and biographical info.
* **Enrichment:** To satisfy project requirements, external MMA databases will be used to collect data regarding "National Wrestling/Striking Backgrounds" and "Fighter Experience Levels" to analyze the influence of a fighter’s origin on their style.

---

##  Data Characteristics
The dataset is comprehensive, containing over **5,000 unique fight observations** spanning from 1993 to 2021, featuring more than **140 variables**.

### Key Performance Indicators (KPIs):
| Category | Metrics |
| :--- | :--- |
| **Grappling Metrics** | `avg_TD_landed`, `avg_TD_pct`, `avg_SUB_ATT`, `avg_CTRL_time` |
| **Striking Metrics** | `avg_SIG_STR_landed`, `avg_SIG_STR_pct`, `avg_KD` (Knockdowns) |
| **Physical Features** | `Height_cms`, `Reach_cms`, `Weight_lbs` |
| **Target Variable** | `Winner` (Red or Blue fighter) |

---

## Planned Methodology
The project will follow a structured data science workflow:

1.  **Exploratory Data Analysis (EDA):** Visualizing win ratios based on performance metrics to identify initial trends.
2.  **Statistical Testing:** Performing **Independent T-tests** to determine if there is a statistically significant difference between the win rates of "high-efficiency grapplers" vs. "high-efficiency strikers."
3.  **Machine Learning:** Implementing a **Logistic Regression** model (and potentially other classifiers) to predict the winner based on these quantitative inputs.
