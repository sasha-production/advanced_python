import sqlite3

with sqlite3.connect('homework.db') as conn:
    cur = conn.cursor()
    res11 = cur.execute(
        """
        SELECT teachers.full_name, AVG(grade) AS avg_grade FROM assignments_grades
        JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
        JOIN teachers ON assignments.teacher_id = teachers.teacher_id
        GROUP BY teachers.full_name
        ORDER BY avg_grade
        LIMIT 1
        """
    ).fetchall()
    print(res11)
    res2 = cur.execute(
        """
        select avg(grade) as avg_grade, students.full_name as full_name from assignments_grades
        join students on students.student_id = assignments_grades.student_id
        group by full_name
        order by avg_grade desc
        limit 10
        """
    ).fetchall()
    print(res2)

    res3 = cur.execute(
        """
        SELECT full_name FROM students s WHERE group_id IN (
    SELECT group_id FROM students_groups sg WHERE teacher_id = (
        SELECT teacher_id FROM (
            SELECT teacher_id, assignment_id, max(avg_score) as max_score FROM
            (
                SELECT a.teacher_id, ag.assisgnment_id, AVG(ag.grade)
                as avg_score
                FROM assignments_grades ag
                JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
                GROUP BY ag.assignment_id ORDER BY avg_score DESC
)))))
        """
    ).fetchall()
    print(res3)

    res4 = cur.execute(
        """
        SELECT MIN(expired), ROUND(AVG(expired)), MAX(expired) FROM
            (
            SELECT sg.group_id, count(ag.assisgnment_id) AS expired
            FROM students_groups sg
            JOIN assignments a on sg.group_id = a.group_id
            JOIN assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
            WHERE ag.date > a.due_date
            GROUP BY sg.group_id
            )
        """
    ).fetchall()
    print(res4)

    res5 = cur.execute(
        """
        select students.group_id, avg(grade) as avg_grade, count(student_id)
        """
    )

    res6 = cur.execute(
        """
        select avg(grade) as avg_grade from assignments_grades
        join assignments on assignments.assisgnment_id = assignments_grades.assisgnment_id
        where assignments.assignment_text like 'прочитать%' or assignments.assignment_text like 'выучить%'"""
    ).fetchall()
    print(res6)