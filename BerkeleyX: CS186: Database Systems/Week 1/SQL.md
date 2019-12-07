#### SQL Cons and Pros:
- Declarative: Say what you want, not how to get it
- Implemented widely
- Constrained: Not targeted at Turing-complete tasks
- General-purpose and feature-rich: extensible: callouts to other languages, data sources

#### Relational Terminology
- **Database**: Set of named Relations
- **Relation** (Table):
   - Schema: description ("metadata")
   - Instance: set of data satisfying the schema
- **Attribute**(Column, Field)
- **Tuple** (Record, Row)

#### The SQL DDL: Primary Keys
- Primary Key column(s)
   - Provides a unique "lookup key" for the relation
   - Cannot have any duplicate values
   - Can be made up of > 1 column
      - E.g. firstname, lastname
#### Conceptual SQL Evaluation
![sql order](https://github.com/teenbress/Still_Hungry_Still_Foolish/blob/master/BerkeleyX:%20CS186:%20Database%20Systems/images/SQL%20orders.png)
