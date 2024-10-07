SELECT teachers.teacher_name, AVG(grades.grade) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.teacher_name = 'Bradley Ramirez'
GROUP BY teachers.teacher_name;