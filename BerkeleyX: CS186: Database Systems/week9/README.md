# Transactions and Concurrency
Transaction Manager includes **Lock Manager** AND **Logging & Recovery**.
#### - Part 1: Concurrency Control
       - Correct/fast data access in the presence of concurrent work by many users
       - Disorderly processing that provides the illusion of order
#### - Part 2: Recovery
       - Ensure database is fault tolerant
       - Storage guarantees for mission-critical data
## Some Problems when several users are using the database at the same time:   
- Inconsistent Reads:    
   User reads in the middle of another user's transaction which is not a state intended by either user.
- Lost Update:    
   Two users update the same record at the same time so one of the updates gets lost.
- Dirty Reads:   
   A user updates the record while another user reads the record.
## Transactions
Our solution to the problem above is to try to make sure one user’s actions are all executed (or
aborted) before another user’s actions are executed. We will do this by using something called a
**transaction**, which is a sequence of multiple actions to be executed as an atomic unit. Here are
4 properties of transactions **ACID** we want so that we can avoid the problems from above:
- **Atomoicity:**  All actions in the Xact happen, or none happen.
- **Consistency:**  If the DB starts out consistent, it ends up consistent at the end of Xact
- **Isolation:**  Execution of each Xact is isolated from that of others
- **Durability:**   If a Xach commits, its effects persist.
## Concurrency Control
- Serial Schedual
- Conflict Dependency Graph
