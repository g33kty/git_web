SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.student_name = 'Lisa Miles';