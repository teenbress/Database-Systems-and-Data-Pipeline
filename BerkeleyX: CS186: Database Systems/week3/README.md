# B+ Trees & Indices
### B+ Tree Indexes
---
### Index
Index is datastructure that enables fast **lookup** and **modification** of data entries by **search key**
- **lookup**: may support many different operations
   - **Equality**: 1-d range, 2-d region
- **Search key:** Any subset of columns in the relation
   - Do not need to be unique e.g.: first name or first name - last name
- **Data Entries:** items stored in the index
   - Assume for today: a pair(k, recordId)...
      - Pointers to records in Heap Files!
      - Easy to generalize later
- **Modification:** want to support fast insert and delete
Many Types of indexes exist: B+-Tree, Hash, R-Tree, GiST,...
### ISAM (an old- fashioned idea / 1960)
- Data entries in sorted heap files
- High fan-out static tree index
- Fast search + good locality
   - Assuming nothing changes
- Insert into overflow pages
- Tips:
   - If a new value is added and there is no room for it, then a likned list is appended to the appropriate leaf page and becomes a store for overflow pages
   - ISAM is good for : 
      - 1-record lookup by search key(assume not many overflow pages)
      - Scan all records (assume many overflow pages)
      - Scan a range of records by search key(assume not many overflow pages)
      - but not good for : balance after insertion(because its linked-list)
###**B+-TREE** 
- B+ Tree Insert
1. Find the correct leaf L.
2. Put data entry onto L.
   - If L has enough space, done
   - Else, must split L into L and a new node L2
      - Redistribute entries evenly, copy up middle key
      - Insert index entry pointing to L2 into parent of L, BUT push up middle key(Contrast with leaf splits).
- B+ Tree Deletion
   Just delete and keep the space
- B+ Bulk Loading
  leaves and internal nodes mostly half-empty: lower left part of the tree is never touched again
  - Fewer I/Os during build
  - Leaves will be stored sequentially(and linked, of course)
  - Can control "fill factor" on pages
### **Summary**
A Visualization of a B+ Tree: [USFCA](https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html)
- ISAM is a static structure
   - **Only leaf pages modified**; overflow pages needed
   - Overflow **chains can degrade performance** unless size of data set and data distribution stay constant

-  **B+ Tree is a dynamic structure**
   - Inserts/deletes leave tree height-balanced; log_FN cost
   - High fanout(F) means depth rarely more than 3 or 4
   - Almost always better than maintaining a sorted file.
   - Typically, 67% occupancy on average
   - Usually preferable to ISAM; adjusts to growth gracefully.
   - Bulk loading can be much faster than repeated inserts for creating a B+ tree on a larfe data set.
   - B+ tree widely used because of its versatility
      - One of the most optimized components of a DBMS
      - Concurrence Updates
      - In-memory efficiency 
## Refinements on Indexes and B+ Trees

**General characteristics of an index:**
Issues to consider in any index structure (not just B+ -trees)
- Query support: what class of queries does the index allow?
- Choice of  Search Key
   - Affects the queries for which we can use an index
- Data Entry Storage
   - Affects performance of the index
- Variable-length key tricks
   - Affects performance of the index
- Cost Model for Index vs Heap vs Sorted File
#### Query Support Overview   
<key><op><constant>   
- Equality selections or Range selections: B+-trees provide both, focus on 1-d range search
- Composite of Search Keys     
- **A Composite Key** on columns(k_1, k_2, ..., k_n) "matches" a query if:
   - The query is a conjunction of m >= 0 equality clauses of the form:
   k_1 = <val_1> AND k_2 = <val_2> AND ... AND k_m = <val_m>
   and at most 1 additional range clause of the form: k_m+1 {<,>} <val>

#### Data Entry Storage
- 3 Basuc alternatives for data entries in any index:
   - By value (tuples)
   - By reference (recordIds)
   - By List of references (list of recordIds)
- Heap file could be clustered or unclustered(only Alt2&3)
#### Variable Length Keys
- Prefix or Suffix?
#### B+ Trees Cost Modeling
- Attractive big-O
- Don't forget constant factors of random I/O
   - Hard to beat sequential I/O of scans unless very selectivs
- Indexes beyond B+-trees for more complex searches   
![cost model] (https://github.com/teenbress/Still_Hungry_Still_Foolish/blob/master/BerkeleyX:%20CS186:%20Database%20Systems/images/class%20cost%20model.png)



