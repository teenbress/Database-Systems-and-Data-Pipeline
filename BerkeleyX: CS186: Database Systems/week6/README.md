# Iterators and Joins
- Cost Notation
  - [R]: the number of pages to store schemaR
  - P_R: number of records per page of schemaR
  - |R|: the cardinality(number of records) of schemaR: |R| = P_R * [R]   
  eg: Let R be a table with 1000 pages and **5000** records. Let S be a table with 500 pages and **1000** records. 
     Schema Reserves: [R]=1000, |R|=5,000
     Schema Sailors: [S]=500, |S|=1,000
### 1. Simple Nested Loop Join(**SNLJ**)  
   for every sing record in R, Search all in S.  
   I/O cost: [R] + |R|[S] = 1000 + (1,000*5,000)*500 = 2500,001,000
### 2. Page Nested Loop Join(**PNLJ**)   
   with R as the outer relation:  As join each page in R:
   I/O cost: [R] + [R][S] = 1000 + 1000*500 = 501,000
### 3. Block Nested Loop Join(**BNLJ**)  
   For each chunk of R, match all the records in S against all the records in the chunk.if B pages in memory, use B-2 for R, then 1 page in memory for read s, 1 page in memeory for output.
   I/O cost: [R] + [[R]/(B-2)][S] = 1000+[1000/(4-2)]*500=251,000 (each B-2 Pages, read whole    S a time)
### 4. Index Nested Loop Join(**INLJ**)   
   I/O cost is [R] + |R|∗(cost to look up matching records in S).   
   eg: Assume that on S we have  Alternative 2 B+ Tree of Height 3.
   I/O cost: [R] +=[R]* (P_R) * (4+1)    
   (Explanation: For every record in R, it takes 4 to traverse the B+ Tree and 1 to read the data)
### 5. Hash Join
 - I/Os
   - Partition phase: read+write both relations: 2([R]+[S]) I/Os
   - Matching phase: read both trlations, forward output: ([R]+[S])I/Os
   - Total cost of 2-pass hash join: 3([R]+[S]) I/Os
 - Memory Requirements
 Build hash table on R with uniform partitioning
   - **Partitioning Phase devides R into (B-1) runs of size [R]/(B-1)**  
   - **Matching Phase requires each [R]/(B-1) < (B-2)**  
   - **R < (B-1)(B-2) < B^2**  
   - Note: no constraint on size of S(probing relation)!
