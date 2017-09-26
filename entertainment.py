import media
import fresh_tomatoes

# 1. Minions 3
minions = media. Movie( "Minions",
"Minions are the numerous creatures that appear in the Despicable Me franchise,which began with the eponymous 2010 film.","https://i.pinimg.com/736x/48/bd/3f/48bd3f6e928d7cb4b8d499cb0f96b8a8--despicable-minions-funny-minion.jpg",
 "https://www.youtube.com/watch?v=7AFUch5JZaQ") 


# 2. Frozen
frozen = media. Movie( "Frozen",
"Here is a Trailer for Frozen: Olaf´s Adventure",
"http://images6.fanpop.com/image/photos/36300000/Elsa-and-Anna-club-frozen-image-elsa-and-anna-club-frozen-36381121-500-307.jpg",
"https://www.youtube.com/watch?v=fhTuBlG8WHg") 

# 3.Harry Potter
harry = media. Movie( "Harry Potter",
"Harry Potter is a series of fantasy novels written by British author J. K. Rowling. The novels chronicle the life of a young wizard,Harry Potter",
"http://s2.thingpic.com/images/Mp/as5CY7hswEt2WScvrkEmduY7.jpeg",
            "https://www.youtube.com/watch?v=L8-e_VdwAME") 

# 4.King Kong
king = media. Movie( "King Kong",
"King Kong is a giant movie monster, resembling a giant ape, that has appeared in various media since 1933. ",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjYxYmRlZWYtMzAwNC00MDA1LWJjNTItOTBjMzlhNGMzYzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
"https://www.youtube.com/watch?v=7-zYoocu2Jo") 

# 5. Minions 3
sherlock = media. Movie( "Sherlock Holmes",
"A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.","http://www.pbs.org/wgbh/masterpiece/wp-content/uploads/2017/01/Sherlock-S4-Tableau.jpg",
 "https://www.youtube.com/watch?v=xK7S9mrFWL4")


movies= [minions,frozen,harry,king,sherlock]
fresh_tomatoes.open_movies_page(movies)
