# B+ Trees & Indices
### Tree Indexes
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
