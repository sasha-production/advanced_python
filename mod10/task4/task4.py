import sqlite3

with sqlite3.connect('hw_4_database.db') as conn:
    cur = conn.cursor()
    # c = cur.execute(f"select count(salary) from salaries").fetchone()
    # print(c)
    poor_people = cur.execute(f"select count(salary) "
                              f"from salaries "
                              f"where salary < 5000 ").fetchone()
    print(poor_people[0], 'человек за чертой бедности')
    mid_salary = cur.execute(f"select avg(salary) "
                             f"from salaries").fetchone()
    print(mid_salary[0], ' - средняя зарплата')

    median_salary = cur.execute("""SELECT AVG(salary) as median 
    FROM (SELECT salary FROM salaries ORDER BY salary LIMIT 1 OFFSET (SELECT COUNT(*) FROM salaries) / 2) AS subquery;""").fetchone()
    print(median_salary[0], ' - медианная зарплата')


    cur.execute("select count(salary) from salaries")
    total = cur.fetchone()[0]
    cur.execute(f"select sum(salary) from (select * from salaries order by salary desc limit 0.1 * {total})")
    top10 = cur.fetchone()[0]
    cur.execute(f"select sum(salary) from (select * from salaries order by salary asc limit 0.9 * {total})")
    bottom90 = cur.fetchone()[0]
    print(round(top10 / bottom90 * 100, 2), '% - социальное неравенство F')
