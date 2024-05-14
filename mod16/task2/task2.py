import sqlite3

with sqlite3.connect('hw.db') as conn:
    cur = conn.cursor()
    res1 = cur.execute('''SELECT customer.full_name, manager.full_name, 'order'.date, 'order'.purchase_amount FROM customer
    JOIN 'order' on customer.customer_id = 'order'.customer_id
    JOIN manager on customer.manager_id = manager.manager_id''').fetchall()
    print(res1)

    res2 = cur.execute('''SELECT full_name FROM customer
                WHERE NOT EXISTS(
                SELECT purchase_amount FROM "order"
                WHERE 'order'.customer_id = customer.customer_id
                )''').fetchall()
    print(res2)

    res3 = cur.execute('''SELECT customer.full_name, manager.full_name, o.order_no FROM customer
    JOIN "order" as o on customer.customer_id = o.customer_id
    JOIN manager on manager.manager_id = customer.manager_id
    WHERE customer.city != manager.city''').fetchall()
    print(res3)
    res4 = cur.execute('''select customer.full_name, 'order'.order_no from customer 
    join 'order' on customer.customer_id = 'order'.customer_id 
    where customer.manager_id is null
    ''').fetchall()
    print(res4)