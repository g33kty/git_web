SELECT subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.teacher_name = 'Tina Carrillo';