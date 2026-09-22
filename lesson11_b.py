from importlib import import_module

try:
    px = import_module("plotly.express")
    pldata = import_module("plotly.data")
except ImportError as exc:
    raise SystemExit(
        "Plotly is required to run this script. Install it with: python -m pip install plotly"
    ) from exc

df = pldata.iris(return_type="pandas")

fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Iris Data, Sepal vs. Petal Length",
    hover_data=["petal_length"]
)

fig.write_html("iris.html", auto_open=True)