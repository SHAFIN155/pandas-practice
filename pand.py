import pandas as pd

# -----------------------------
# Step 1: Read a CSV file
# -----------------------------
# Example CSV (students.csv):
# ID,Name,Age,Department,Marks
# 1,John,20,Mechanical,85
# 2,Sarah,22,Civil,90
# 3,David,21,Electrical,75
# 4,Linda,23,Mechanical,88
# 5,James,22,Civil,60

df = pd.read_csv("students.csv")

print("------ First 5 rows ------")
print(df.head())

# -----------------------------
# Step 2: Explore the data
# -----------------------------
print("\n------ Info ------")
print(df.info())

print("\n------ Summary statistics ------")
print(df.describe())

print("\n------ Unique Departments ------")
print(df["Department"].unique())

# -----------------------------
# Step 3: Filtering
# -----------------------------
print("\n------ Students with Marks > 80 ------")
high_scores = df[df["Marks"] > 80]
print(high_scores)

# -----------------------------
# Step 4: Sorting
# -----------------------------
print("\n------ Sorted by Marks (descending) ------")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)

# -----------------------------
# Step 5: Adding a new column
# -----------------------------
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 70 else "Fail")
print("\n------ With Result Column ------")
print(df)

# -----------------------------
# Step 6: Grouping
# -----------------------------
print("\n------ Average Marks by Department ------")
print(df.groupby("Department")["Marks"].mean())

# -----------------------------
# Step 7: Save modified DataFrame to new CSV
# -----------------------------
df.to_csv("students_updated.csv", index=False)
print("\nUpdated CSV saved as 'students_updated.csv'")