/*邬宗圆的多表查询SQL代码*/
/*查出至少有一个员工的部门，显示部门编号、部门名称、部门位置、部门人数*/
SELECT deptno,dname,loc,COUNT(*) FROM dept NATURAL JOIN emp WHERE dept.deptno = emp.deptno
GROUP BY deptno HAVING COUNT(*)>1;
/*列出所有员工的姓名及其直接上级的姓名*/
SELECT a.empno,a.ename,a.mgr,b.ename FROM (SELECT * FROM emp) AS a LEFT JOIN (SELECT * FROM emp)
AS b ON a.mgr = b.empno;
/*列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称*/
SELECT a.empno,a.ename,d.dname FROM emp AS a RIGHT JOIN emp AS b ON a.mgr = b.empno RIGHT JOIN
dept AS d ON a.deptno = d.deptno WHERE a.hiredate < b.hiredate;
/*列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门*/
SELECT emp.* , dept.* FROM dept LEFT JOIN emp ON dept.deptno = emp.deptno;
/*列出最低薪金大于15000的各种工作及从事此工作的员工人数*/
SELECT job , MIN(sal) FROM emp WHERE sal > 15000 GROUP BY job;
/*列出在公关部工作的员工的姓名，假定不知道公关部的部门编号*/
SELECT ename FROM emp WHERE deptno = (SELECT deptno FROM emp WHERE job = "公关部" LIMIT 1);
/*列出薪金高于公司平均薪金的所有员工信息，所有部门名称，上级领导，工资等级*/
SELECT * FROM emp,salgrade,dept WHERE emp.deptno = dept.deptno AND emp.sal >= salgrade.losal AND
emp.sal <= salgrade.hisal AND emp.sal > (SELECT AVG(emp.sal) FROM emp);
/*列出与张飞从事相同工作的所有员工及部门名称*/
SELECT ename,dname FROM emp AS e LEFT JOIN dept AS d ON e.deptno = d.deptno WHERE job = (SELECT 
job FROM emp WHERE ename = "张飞");
/*列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称*/
SELECT ename,sal,dname FROM emp AS e LEFT JOIN dept AS d ON e.deptno = d.deptno WHERE sal > (SELECT
MAX(sal) FROM emp WHERE deptno = "30");