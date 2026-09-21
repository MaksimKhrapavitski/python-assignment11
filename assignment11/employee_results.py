import sqlite3
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT last_name,
       SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o
    ON e.employee_id = o.employee_id
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

cursor = conn.execute(query)
employee_results = cursor.fetchall()

print(employee_results)

plt.bar(
    [row[0] for row in employee_results],
    [row[1] for row in employee_results],
    color="skyblue",
)
plt.title("Revenue by Employee")

plt.xlabel("Employee")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()

conn.close()