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
    - 4. FULL JOIN: returns all rows for which there is a match in either of the TABLES; combines the effect of 
    applying both a LEFT JOIN and RIGHT JOIN; its result is equivalent to performing a UNION of the result of LEFT and RIGHT outer queries.
    - 5. CROSS JOIN: returns all records where each row from the first table is combined with each row from the second table(i.e., returns the Cartesian product of the sets of rows from the joined tables);
    (a) be specified using the CROSS JOIN syntax("explicit join notation")
    (b) FROM clause separated by commas without using a WHERE ("implicit join notation")
    - 6. INNER JOIN   
       
### 4. NVL(exp1, exp2), NVL 2(exp1, exp2, exp3)
    - 1. Both check the value exp1 to see if it is NULL
    - 2. NVL: if exp1 is NOT NULL, exp1 is returned; otherwise, exp2
    - 3. NVL2: If exp1 is NOT NULL, exp2 is returned, otherwise exp3
### 5. RANK() and DENSE_RANK()
    - 1. Only difference: where there is a "tie"
    - 2. RANK() will assign non-consecutive "ranks" to the values in the set(resulting in gaps between the integer ranking values when there is a tie)
    - 3. DENSE_RANK() will assign consecutive ranks to the values in the set(so there will be no gaps between the integer ranking values in the case of a tie)
### 6. WHERE and HAVING
    - 1. When GROUP BY is not used, essentially equivalent
    - 2. WHEN GROUP BY is used
          a. WHERE: filter records from a result. Filtering occurs before any groups are made.
          b. HAVING: filter values from a group. Filtering occurs after aggregation into groups are performed.
### 7. SINGLE ROW vs MULTIPLE ROW functions
    - 1. SINGLE ROW: work on a single row and return one output per row(e.g. length and case conversation)
    - 2. MULTIPLE ROW: work upon group of rows and return one result for the complete set of rows(a.k.a GROUP functions)
### 8. CHAR vs VARCHAR vs VARCHAR2
    - 1. **CHAR**
        - fixed length, regardless of the string it holds(any remaining space in the field is padded with blanks)
    - 2. **VARCHAR** variable length, takes up 1 byte per character, + 2 bytes to hold length information(holds only the characters you assign to it)
    - 3. **VARCHAR2** Oracle, similar to VARCHAR but does not distinguish between a NULL and empty string, and never will
    - 4. **TRADEOFFS** When store, choose VARCHAR because take less spaces; when index, choose CHAR because require less string manipulation and faster
### 9. COUNT(), SUM(), COUNT(1), SUM(1), COUNT(2), SUM(2)
   - 1. COUNT(), COUNT(1), COUNT(2),SUM(1)- same result to count numbers including NULL; avoid using SUM(1) because it's less efficient
   - 2. SUM(2)= SUM(1)*2
   - 3. COUNT(column) Doesn't count NULL values
### 10. GROUP BY
   - 

    

    
