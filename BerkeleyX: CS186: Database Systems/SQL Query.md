# [41 SQL Essential Questions Notes](https://www.toptal.com/sql/interview-questions#form)

### 1.UION & difference between UNION ALL
- UNION merges the contents of two structure-compatibility tables into a single combined table.
- UNION ALL include **duplicate** records but UNION will omit duplicate records
- UNION ALL typically better than UNION- UNION requires the server to do the additional work of removing any duplicates
#### UNION ALL -> UNION   
   - WHERE a!= X   
      
### 2.FOREIGN & FRIMARY KEY
    - PRIMARY KEY: unique, not NULL
    - FOREIGN KEY: reference PRIMARY KEY in another table(can be null or duplicate)   
       
### 3. List of different JOINS   
    - 1. INNER JOIN(default): return all rows for which where is at least one match in BOTH TABLES
    - 2. LEFT JOIN: returns all rows from the left table and the matched rows from the right table
    - 3. RIGHT JOIN: return all rows from the right table, and the matched rows from the left table;
    - 4. FULL JOIN: returns all rows for which there is a match in either of the TABLES; combines the effect of applying both a LEFT JOIN and RIGHT JOIN; its result is equivalent to performing a UNION of the result of LEFT and RIGHT outer queries.
    - 5.
    

    
