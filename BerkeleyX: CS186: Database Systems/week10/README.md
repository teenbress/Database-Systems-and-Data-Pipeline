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
- Key Constraints: 1-to-many, many-to-many, many-to-1, 1-to-1
- Participation Constraints
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



   
 
