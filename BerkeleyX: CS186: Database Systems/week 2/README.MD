# Architecture of A DBMS
1. SQL Client  
   - eg: Websites, Apps
2. Query Parsing & Optimization
   - Parse, check, and verify the SQL, and translate into an efficient query plan
3. Relational Operators
   - Excute a dataflow by operating on **records** and **files**
4. Files and Index Management  
   - Organize tables and records as groups of pages in a logical file
5. Buffer Management
   - Provide the illusion of operating in memory
6. Disk Space Management
   - Translate page requests into physical bytes on one or more devices
## Disk Space Management
- Block Level Storage
   - Read and write large chunks of sequential bytes
   - Predict future behavior
      - Cache popular blocks
      - Pre-fetch likely-to-be-accessed blocks
      - More on these as we go
- A note on Terminology
   - **Block = Unit of transfer for disk read/write**  
   - **Page: a common synonym for "block"**
      - In some texts, "page" = a block-sized chunk of RAM
- Disk Space Management, cont
   - **Lowest layer of DBMS, manages space on disk**
   - **Purpose:**
      - Map pages to location on disk
      - Load pages from disk to memory
      - Save pages back to disk & ensuring writes
   - Higher levels call upon this layer to:
      - Read/write a page
      - Allocate/de-allocate logical pages
- Summary
   - Provide API to read and write pages to devices
   - Pages: block level organization of bytes on disk
   - Provides "next" locality and abstracts FS/device details

## Disk Representations: Files, Pages, Records(4.5)
## File Organization(05)
-Multiple File Organizations
   - Heap Files: Suitable when typical access is a full scan of all records
   - Sorted Files: Best for retrieval in order, or when a range of records is needed
   - Clustered Files & Indexes: Group data into clocks to enable fast lookup and efficient modifications
- Cost Model and Analysis
   - B: # of data blocks in the file
   - R: # of records per block
   - D: Avg time to read/write disk block
   
   - Foucs: Average case analysis for uniform random workloads
- Heap Files & Sorted Files
   - **B:** The number of data blocks = 5
   - **R:** Number of records per block = 2
   - **D:** (Average) time to read/write disk block = 5ms  
![heap files](https://github.com/teenbress/Still_Hungry_Still_Foolish/blob/master/BerkeleyX:%20CS186:%20Database%20Systems/images/heap%20files.png)


   
