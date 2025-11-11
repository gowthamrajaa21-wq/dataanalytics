use fitaproject
select * from students

select * from students order by MovieID asc Limit 1000

-- movies by title,Rating,Releaseyear --
        select Title,Rating,Genre from students
	    select Title,Genre,Rating,ReleaseYear from students where Genre ="Thriller" and Rating >= "4.5" order by Rating asc
        select Title,Genre,Rating,ReleaseYear from students where Genre ="Action" and Rating >= "4.6" order by Rating asc
        select Title,Genre,Rating,ReleaseYear from students where Genre ="Comedy" and Rating >= "4.4" order by Rating asc

-- top Rated movies --

        select * from students where Rating >="4.5"
        
-- tamil movies --
        select * from students where Language ="Tamil"
        
-- actor ajith kumar's same year Release movies --
		select * from students where Actor="Ajith Kumar" and ReleaseYear>="2005";
        
-- actor suriya's movies Released in amazon prime --
		select * from students where Actor="Suriya" and Streaming_platform ="Amazon Prime";

-- full joins for movie Rating --
        select s.Title,s.Genre,s.Rating,s.Actor,s.Director from students s
       