import sqlite3
import matplotlib.pyplot as plt  # type: ignore[import-unresolved]

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

rows = conn.execute(query).fetchall()
order_ids = [row[0] for row in rows]
cumulative = []
running_total = 0

for _, total_price in rows:
    running_total += total_price
    cumulative.append(running_total)

print(rows)

plt.plot(
    order_ids,
    cumulative,
    color="green",
)
plt.title("Cumulative Revenue")

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.tight_layout()

plt.show()

conn.close()