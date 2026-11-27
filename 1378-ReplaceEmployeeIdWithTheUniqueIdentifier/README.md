# 1378. Replace Employee ID With the Unique Identifier

**Difficulty:** Easy<br>
[View on LeetCode](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)

---

The `Employees` table contains employee IDs and names. The `EmployeeUNI`
table maps some employee IDs to unique IDs. Return each employee's name and
unique ID; use `NULL` when an employee has no mapping.

**Example:**

Employees:

| id | name |
|---:|---|
| 1 | Alice |
| 3 | Jonathan |

EmployeeUNI:

| id | unique_id |
|---:|---:|
| 3 | 1 |

Result:

| unique_id | name |
|---:|---|
| NULL | Alice |
| 1 | Jonathan |
