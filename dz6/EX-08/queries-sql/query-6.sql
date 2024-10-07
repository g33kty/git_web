SELECT students.student_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.group_name = 'B-9';