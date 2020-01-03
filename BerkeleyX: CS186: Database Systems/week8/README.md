# Parallel Queries
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
      
   
   
