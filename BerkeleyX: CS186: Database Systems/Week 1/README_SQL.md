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

#### Aliases and Self-Joins

#### Set Semantics
- Set: a collection of distinct elements
- Standard ways of manipulating/combining sets
   - Union
   - Intersect
   - Except
- Treat tuples within a relation as elements of a set
   - Union All: sum(A+B)
   - Intersect All: MIN(A,B)
   - EXCEPT ALL: Difference(A-B)
#### Nested Queries
- IN
-NOT IN

#### Argmax query
```
SELECT *  
FROM Sailors S  
WHERE S.rating >= ALL  
(SELECT S2.rating  
FROM Sailors S2);  // Maybe contain 3 rows, not only 1 record;
```
**VS**
```
SELECT *  
FROM Sailors S  
WHERE S.rating =   
(SELECT MAX(S2.rating)   
FROM Sailors S2);  
```
**VS**
```
SELECT *
FROM Sailors S
ORDER BY rating DESC
LIMIT 1;
```
#### Subqueries in FROM : Like a "view on the fly"~
```
SELECT bname, scount
FROM Boars2 B,
(SELECT B.bid, COUNT(* )
        FROM Boats2 B, Reserves2 R
        WHERE R.bid = B.bid AND B.color = 'red'
        GROUP BY B.bid) AS **Reds(bid, scount)**
WHERE Reds.bid=B.bid AND scount < 10
```
#### WITH a.k.a common table expression(CTE)
```
WITH Reds(bid, scount) AS
       (SELECT B.bid, COUNT(*)
       FROM Boats2 B, Reserves2 R
       WHERE R.bid = B.bid AND B.color = 'red'
       GROUP BY B.bid)
SELECT bname, scount
FROM Boats2 B, Reds
WHERE Reds.bid=B.bid
AND scount < 10
```


