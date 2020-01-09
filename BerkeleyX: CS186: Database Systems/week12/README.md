# Recovery + ARIES
## Instruction to ARIES
**ARIES** is a recovery algorithm designed to work with a steal, no-force approach.After a crash, restart proceeds in three phases:
1. **Analysis**: Identifies dirty pages in the buffer pool(i.e. changes that have not been written to disk) and active transactions at the time of the crash.
2. **Redo**: Repeats all actions, starting from an appropriate point in the log, and restores the database state to what it was at the time of the crash.
3. **Undo**: Undoes the actions of transactions that did not commit, so that the databese reflects only the actions of committed transactions.
#### Three main priples behind the ARIES recovery algorithm:
- **Write-Ahead Logging**:
- **Repeating History During Redo**:
- **Logging Changes During Undo**:
