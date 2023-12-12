
import pandas as pd
import pandasql as ps
student_data = [
    {"name": "Alice", "age": 15, "grade": "A"},
    {"name": "Bob", "age": 16, "grade": "B"},
    {"name": "Charlie", "age": 17, "grade": "C"},
]
df = pd.DataFrame(student_data)
df
df2 = df.groupby(["name", "grade"])["age"].sum()
df2 = pd.DataFrame(df)
for index, row in df2.iterrows():
    print(index, row)


# Query the DataFrame using pandasql
sql_query = """
SELECT name, max(age) ma, sum(age) sa
FROM df
WHERE age < 17
GROUP BY name
"""
df_query = ps.sqldf(sql_query, locals())

# Print the results of the query
print(f" Query size: {df_query.size}")
print(df_query)
