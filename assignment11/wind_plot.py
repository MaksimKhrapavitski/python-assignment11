import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type="pandas")

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

# Convert strength to float
df["strength"] = (
    df["strength"]
    .str.replace("+", "", regex=False)
    .str.split("-")
    .str[0]
    .astype(float)
)

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency"
)

fig.write_html("wind.html", auto_open=True)