import matplotlib.pyplot as plt  # type: ignore[import-not-found]

# Load a dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300]
}

# Line Plot
plt.plot(data["Month"], data["Sales"], marker="o", label="Sales")
plt.plot(data["Month"], data["Expenses"], marker="o", label="Expenses")
plt.title("Sales vs. Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()

plt.show()

# Bar Plot
plt.bar(data["Month"], data["Sales"], color="skyblue")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()

plt.show()