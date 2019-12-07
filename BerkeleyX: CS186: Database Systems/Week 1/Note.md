### Strings comparison
- Old-school SQL  
       SELECT S.sname FROM Sailors S WHERE **S.sname LIKE 'B_%'**
- Standard Regular SQL  
       SELECT S.sname FROM Sailors S WHERE **S.sname ~ 'B.*'**
       
