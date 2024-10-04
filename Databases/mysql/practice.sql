-- 1.查询课程编号为“01”的课程比“02”的课程成绩高的所有学生的学号（重点）
SELECT
    a.s_id "s_no",
    a.s_score "01",
    b.s_score "02"
FROM
    ( SELECT s_id, c_id, s_score FROM Score WHERE c_id = "01" ) AS a
    INNER JOIN ( SELECT s_id, c_id, s_score FROM Score WHERE c_id = "02" ) AS b ON a.s_id = b.s_id
    -- inner join Student as c on c.s_id = a.s_id  -- 拿到名字

WHERE
    a.s_score > b.s_score;

-- 2、查询平均成绩大于60分的学生的学号和平均成绩（简单，第二道重点）
SELECT
    s_id,
    avg( s_score )
FROM
    Score
GROUP BY
    s_id
HAVING
    avg( s_score ) > 60;

-- 3、查询所有学生的学号、姓名、选课数、总成绩（不重要）
SELECT
    a.s_id,
    a.s_name,
    count( b.c_id ),
    sum( CASE WHEN b.s_score IS NULL THEN 0 ELSE b.s_score END )
FROM
    Student AS a
    LEFT JOIN Score AS b ON a.s_id = b.s_id
GROUP BY
    a.s_id;

-- 4、查询姓“猴”的老师的个数（不重要）
SELECT
    count( DISTINCT t.t_name ) -- t.t_id
FROM
    Teacher AS t
WHERE
    t.t_name LIKE '王%';

-- 5、查询没学过“张三”老师课的学生的学号、姓名（重点）
SELECT
    s_id,
    s_name
FROM
    Student
WHERE
    s_id NOT IN (
    SELECT
        s_id
    FROM
        Score
    WHERE
        c_id = ( SELECT c_id FROM Course WHERE t_id = ( SELECT t_id FROM Teacher WHERE t_name = "张三" ) )
    );

-- INNER JOIN 解法
SELECT
    s_id,
    s_name
FROM
    Student
WHERE
    s_id NOT IN (
    select s_id from Score as s
    INNER JOIN Course as c on s.c_id = c.c_id
    INNER JOIN Teacher as t on c.t_id = t.t_id
    where t.t_name = "张三"
)














