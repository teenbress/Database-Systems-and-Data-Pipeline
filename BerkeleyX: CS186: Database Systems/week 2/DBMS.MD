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
   
