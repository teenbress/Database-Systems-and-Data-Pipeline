# Parallel Queries
## Parallelism natural to query processing:
   - Both pipeline and partition
## Shared-nothing vs. Shared-Mem vs. Shared Disk
   - Shared-Mem easiest SW, costliest HW
      - Doesn'r scale indefinitely
   - Shared-nothing cheap, scales well, harder to implement
   - Shared disk a middle ground
    
## Kinds of query parallelism
- **Inter Query**  parallelism across queries
   - Each query runs on a separate processor
   - Does require parallel-aware concurrency control
- **Intra Query**(within a single query)
   - Inter-operator(between operators)
      - Pipeline parallelism
      - Bushy(Tree) parallelism
   - Intra-operator(within a single operator)
      - Partition Parallelism
## Parallel Hashing
- Phase 1: partition data across machines using a hashing function h1;   
- Phase 2: Each machine run the external hashing functions h2,...hk...independently;   
  ### Parallel Grace Hashing
  - Pass1: parallel streaming
     - stream building and probing tables through shuffle/partition
  - Pass 2: local Grace Hash Join per node
## Parallel Sorting
by partitioning using range
### Parallel Sort Merge Join

   
   
