-- 1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT students.student_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.student_name
ORDER BY average_grade DESC
LIMIT 5;

--2 Знайти студента із найвищим середнім балом з певного предмета.
SELECT students.student_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject_name = 'Music'
GROUP BY students.student_name
ORDER BY average_grade DESC
LIMIT 1;

--3 Знайти середній бал у групах з певного предмета.
SELECT groups.group_name, AVG(grades.grade) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject_name = 'Music'
GROUP BY groups.group_name;

--4 Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT AVG(grade) AS average_grade
FROM grades;

--5 Знайти які курси читає певний викладач.
SELECT subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.teacher_name = 'Tina Carrillo';

--6 Знайти список студентів у певній групі.
SELECT students.student_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.group_name = 'B-9';

--7 Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.student_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE groups.group_name = 'B-9'
  AND subjects.subject_name = 'Music'


--8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.teacher_name, AVG(grades.grade) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.teacher_name = 'Bradley Ramirez'
GROUP BY teachers.teacher_name;

--9 Знайти список курсів, які відвідує студент.
SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.student_name = 'Lisa Miles';


--10 Список курсів, які певному студенту читає певний викладач.
SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.student_name = 'Lisa Miles'
  AND teachers.teacher_name = 'Lisa Miles';
