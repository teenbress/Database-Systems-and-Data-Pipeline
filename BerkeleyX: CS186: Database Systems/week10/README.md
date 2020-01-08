# Database Design 
## Overview of DB Design
### Steps in DB Design (not a DB System Design)
- **Requirements Analysis**
- **Conceptual Design**
   - high level description (often w/ER model)
   - Object-Relational Mappings(ORMs: Hibernate, Rails, Django, etc)
- **Logical Design**
   - translate ER into DBMS data model
   - ORMs often require you to help here too
- **Schema Refinement**
   - consistency, normalization
- **Physical Design** - indexes, disk layout
- **Security Design** - who accesses what, and how
## Conceptual Design: ER Model Basics(Cont.)
- Entity: A real world object that described by a set of attributes
- Relationship: Association among two or more entities
   - Relationship can have their owen attributes
- Relationship Constraints: 1-to-many, many-to-many, many-to-1, 1-to-1
   - Key Constraints: 1-to-many(->)
   - Participation Constraints: **at least one** relationship
- Weak Entities: A **weak entity** can be identified uniquely only by considering the primary key of another(owner) entity.
   - 1-to-many: one owner, many weak entities
   - have total participation in this identifying relationship set   
 O: 0 or many   
 |: 1 or more   
 |O: 1 or 0   
 ||: exactly 1   
 <-: many    
 ![ER Model](https://github.com/teenbress/Still_Hungry_Still_Foolish/blob/master/BerkeleyX:%20CS186:%20Database%20Systems/images/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200106170516.png)
- Design choices:
   - Entity or attribute?
   - Entity or relationship?
   - Relationships: **Binary or ternary? Aggregation?** 
### Logical Design:Convert ER to relational
In translating a **many-to- many** relationship set to a relation, attributes of the relation must include:
1) Keys for each participating entity set (as foreign keys). This set of attributes forms a **superkey** for the relation.
2) All descriptive attributes.
## DB Design: Fuctional Dependencies and Normalization
A functional dependency X −→ Y means that the X column determines Y column in a table R.   
A **superkey** is a set of columns that determine all the columns in the table.   
A **candidate** key is a **minimal** set of of columns that determine all the columns in the table.   
For example, if columns K, L determine all the columns in the table and K is also a primary key of the table (aka column K alone determins all the columns in the table) then K, L is superkey and K is a superkey and a candidate key.   
 ###    Decomposing a Relation
 
