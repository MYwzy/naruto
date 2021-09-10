/*邬宗圆的单表查询SQL代码*/
/*deptno为部门编号,empno为员工编号,ename为员工姓名,MGR为上级领导,
hiredate为入职日期,sal为薪资,comm为奖金*/
/*1.查询出部门编号为30的所有员工*/
SELECT * FROM t_employees WHERE(deptno = 30);
/*2.所有经理的姓名、编号和部门编号*/
SELECT empno , ename , deptno FROM t_employees WHERE(job = "经理");
/*3.找出奖金高于工资的员工*/
SELECT * FROM t_employees WHERE comm > sal;
/*4.找出奖金高于工资60%的员工*/
SELECT * FROM t_employees WHERE comm > sal*"0.6";
/*5.找出部门编号为10的所有经理和部门编号为20的所有分析员的详细资料*/
SELECT * FROM t_employees WHERE (deptno = 10 AND job = "经理") OR (deptno = 20 AND job = "分析员");
/*6.找出部门编号为10的所有经理、部门编号为20的所有分析员、还有既不是经理又不是
武装上将但其工资大于或等于3000的所有员工的详细资料*/
SELECT * FROM t_employees WHERE (deptno = 10 AND job = "经理") OR (deptno = 20 AND job = "分析员")
OR (job NOT IN ("经理" , "武装上将") AND sal >= 3000);
/*7.无奖金或奖金低于1000的员工*/
SELECT * FROM t_employees WHERE comm IS NULL OR comm < 1000;
/*8.查询名字由三个字组成的员工*/
SELECT * FROM t_employees WHERE ename LIKE "___";
/*9.查询2000年以及以后入职的员工*/
SELECT * FROM t_employees WHERE hiredate > "2000-01-01";
/*10.查询所有员工详细信息，用编号升序排序*/
SELECT * FROM t_employees ORDER BY empno ASC;
/*11.查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序*/
SELECT * FROM t_employees ORDER BY sal DESC , hiredate ASC;
/*12.查询每个部门的平均工资*/
SELECT AVG(sal) FROM t_employees WHERE deptno = 10;
SELECT AVG(sal) FROM t_employees WHERE deptno = 20;
SELECT AVG(sal) FROM t_employees WHERE deptno = 30;
SELECT AVG(sal) FROM t_employees WHERE deptno = 40;
/*13.查询每个部门的雇员数量*/
SELECT deptno , COUNT(*) FROM t_employees GROUP BY deptno;
/*14.查询每种工作的最高工资、最低工资*/
SELECT MAX(sal) FROM t_employees WHERE job = "高级公关";
SELECT MIN(sal) FROM t_employees WHERE job = "高级公关";
SELECT MAX(sal) FROM t_employees WHERE job = "武装教习";
SELECT MIN(sal) FROM t_employees WHERE job = "武装教习";
SELECT MAX(sal) FROM t_employees WHERE job = "武装副司令";
SELECT MIN(sal) FROM t_employees WHERE job = "武装副司令";
SELECT MAX(sal) FROM t_employees WHERE job = "经理";
SELECT MIN(sal) FROM t_employees WHERE job = "经理";
SELECT MAX(sal) FROM t_employees WHERE job = "武装司令";
SELECT MIN(sal) FROM t_employees WHERE job = "武装司令";
SELECT MAX(sal) FROM t_employees WHERE job = "武装上将";
SELECT MIN(sal) FROM t_employees WHERE job = "武装上将";
SELECT MAX(sal) FROM t_employees WHERE job = "董事长";
SELECT MIN(sal) FROM t_employees WHERE job = "董事长";
SELECT MAX(sal) FROM t_employees WHERE job = "人事专员";
SELECT MIN(sal) FROM t_employees WHERE job = "人事专员";
SELECT MAX(sal) FROM t_employees WHERE job = "分析员";
SELECT MIN(sal) FROM t_employees WHERE job = "分析员";
SELECT MAX(sal) FROM t_employees WHERE job = "中级公关";
SELECT MIN(sal) FROM t_employees WHERE job = "中级公关";
SELECT MAX(sal) FROM t_employees WHERE job = "武装大校";
SELECT MIN(sal) FROM t_employees WHERE job = "武装大校";