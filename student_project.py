import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# STEP 1: LOAD DATASET
# =========================

df = pd.read_csv("student-por.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# =============================
# STEP 2: CHECK MISSING VALUES
# =============================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# STEP 3: CHECK DUPLICATES
# ==========================

print("\nDuplicate Records:")
print(df.duplicated().sum())

# =============================
# STEP 4: SAVE CLEANED DATASET
# =============================

df.drop_duplicates(inplace=True)

df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

# =========================
# STEP 5: VISUALIZATION 1
# FINAL GRADE DISTRIBUTION
# =========================

plt.figure(figsize=(8,5))
plt.hist(df['G3'], bins=10)
plt.title('Distribution of Final Grades (G3)')
plt.xlabel('Final Grade')
plt.ylabel('Number of Students')
plt.show()

# =========================
# STEP 6: VISUALIZATION 2
# GENDER VS FINAL GRADE
# =========================

plt.figure(figsize=(8,5))
sns.boxplot(x='sex', y='G3', data=df)
plt.title('Gender vs Final Grade')
plt.show()

# ==========================
# STEP 7: VISUALIZATION 3
# STUDY TIME VS FINAL GRADE
# ==========================

plt.figure(figsize=(8,5))
sns.boxplot(x='studytime', y='G3', data=df)
plt.title('Study Time vs Final Grade')
plt.show()

# ==========================
# STEP 8: VISUALIZATION 4
# INTERNET ACCESS VS GRADE
# ==========================

plt.figure(figsize=(8,5))
sns.boxplot(x='internet', y='G3', data=df)
plt.title('Internet Access vs Final Grade')
plt.show()

# ==========================
# STEP 9: VISUALIZATION 5
# ABSENCES VS GRADE
# ==========================

plt.figure(figsize=(8,5))
sns.scatterplot(x='absences', y='G3', data=df)
plt.title('Absences vs Final Grade')
plt.show()

# ============================
# STEP 10: CORRELATION HEATMAP
# ============================

numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='coolwarm')

plt.title('Correlation Heatmap')
plt.show()

# ============================
# STEP 11: Summary Statistics
# ============================

print("\nSummary Statistics:")
print(df.describe())

# ============================