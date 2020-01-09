# 41 SQL Essential Questions Notes

### 1.UION & difference between UNION ALL
- UNION merges the contents of two structure-compatibility tables into a single combined table.
- UNION ALL include **duplicate** records but UNION will omit duplicate records
- UNION ALL typically better than UNION- UNION requires the server to do the additional work of removing any duplicates
#### UNION ALL -> UNION
   `WHERE a!= X`   
   
### 2.FOREIGN & FRIMARY KEY
    - PRIMARY KEY: unique, not NULL
    - FOREIGN KEY: reference PRIMARY KEY in another table(can be null or duplicate)   
       
### 3. List of different JOINS
    
