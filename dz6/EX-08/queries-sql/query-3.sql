SELECT groups.group_name, AVG(grades.grade) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject_name = 'Music'
GROUP BY groups.group_name;