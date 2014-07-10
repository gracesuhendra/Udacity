# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
# Some details:  Each sentence will be separated from one another with only
# a period (there will not be whitespace or new lines between sentences)
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Jeff likes to play Starfleet Commander, Ninja Hamsters.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures\."

example_input_alternate="""John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure

# The output of this data structure is a dictionary with the name 
# of user as the key and the connections and games of user as the value
# Example output: {'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']], 'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']], 'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']], 'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']], 'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']], 'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']], 'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 'John': [['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']], 'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}

def create_data_structure(string_input):
    network = {}
    lines = string_input.split('.')
    for line in lines:   
        if line.find('is connected to ') > 0: #to make sure if the line has the names of connections
            end_name = line.find('is connected to ')
            user = (line[:end_name]).strip()
            length_of_connected_to = len('is connected to ')
            network[user] = [[], []] #prepare the value of dictionary as a list
            network[user][0] = line[(end_name + length_of_connected_to): ].split(', ')       
        
        if line.find(' likes to play ') > 0: #to make sure if the line has user's games
            start_games = line.find(' likes to play ')
            length_of_likes_to_play = len(' likes to play ')
            network[user][1] = line[len(user) + length_of_likes_to_play+1:].split(', ')
    return network



# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  


def get_connections(network, user):
    if user not in network:
        return None
    else:
        return network[user][0] #if user has no connections, the dictionary will be {<user> : [[], [<game1>, <game2>, ...]],...} (it'll be defined in add_new_user procedure)
        

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.

def add_connection(network, user_A, user_B):
    if (user_A not in network) or (user_B not in network): 
        return False
    else:
        network[user_A][0].append(user_B) #update the list of connections of user_A with the new user_B as new connection
        return network
    

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#            ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.

def add_new_user(network, user, games):
    if user in network:
        network[user][1].extend(games) #if user is in network, update the games into the list in dictionary
    else:
        network[user]=[[], games] #if user is not in network, make a new user as a new key, but make an empty connection list because the user has no connection
    return network
        
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    secondary_connections = [] #prepare an empty list to store the names of secondary connections
    if user not in network: #if user is not in network, return None
        return None
    else:
        if network[user][0] == []:
            return []
        else:
            for e in get_connections(network, user): #program run through the elements in the user's primary connections
                union(secondary_connections, get_connections(network, e)) #call the connections of the user's primary connections, and store it into the list
            return secondary_connections


# -----------------------------------------------------------------------------     
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.

def connections_in_common(network, user_A, user_B):
    count = 0 
    if (user_A not in network) or (user_B not in network):
        return False
    else:
        for e in get_connections(network, user_A): 
            for f in get_connections(network, user_B): 
                if e == f: #when there is connections in common, add one to counter
                    count = count+1
        return count

   
# helper function, union

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

    
    
# ----------------------------------------------------------------------------- 
# path_to_friend(network, user, connection): 
#   Finds the connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#                   Solve this problem using recursion. 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hint: 
#   Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.

def path_to_friend(network, user, connection):
    path = [] 
    path.append(user) #user's name always comes first
    if (user not in network) or (connection not in network):
        return None
    
    else:    
        if connection in get_connections(network, user): 
            return path + [connection] #if connection is in the list of user's connections, add connection right away to the path
        else:
            for e in get_connections(network, user):
                connections_of_connections = path_to_friend(network, e, connection) #the function call itself with different input 
                union(path, connections_of_connections)
                return path 


# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun! 

# My MYOP will be a program that find the users that play the inputted game and connected to the inputted user
# This MYOP needs a helper function that takes network as the input and output a list of the games in network

def list_of_all_games(network):
    games_list = []
    for usr in network:
        for g in network[usr][1]:
            union(games_list, [g])
    return games_list


# The MYOP procedure is MYOP_connected_gamers(network, game, user) 
# It makes a list that contains the users that play a particular game and connected to a particular user

# Arguments: 
#   games_users_pairs: the output of the helper procedure
#   game             : the particular game 
#   user             : the particular user

# Return: 
#   A list of users that play that game and connected to the user. 
#   If the game or user is not in network, return None.  
#   If the none of the users that play the games is conencted to the user, return empty list.
#   For example, the game is "The Legend of Corgi" and the user is Walter. 
#   Therefore, the users that play that game are John, Mercedes, Olive, Levi
#   From those 4 users, only John and Levi are conencted to Walter
#   Therefore, the output of this function are ['John', 'Levi']

def MYOP_connected_gamers(network, game, user):
    games_list = list_of_all_games(network)
    gamers = []
    if (game not in games_list) or (user not in network):
        return None
    else:
        for usr in network:
            if game in network[usr][1]:
                union(gamers, [usr])  #make a list of users that play the game
        connected_gamers = []
        for gmrs in gamers:
            if gmrs in get_connections(network, user):
                connected_gamers.append(gmrs) 
        return connected_gamers



net = create_data_structure(example_input_alternate)
print net
print add_new_user(net, 'John', ['Star Wars']) #existing user, 1 game
print add_new_user(net, 'John', ['Star Wars', 'Star Moon']) #existing user, 2 games
print add_new_user(net, 'Grace', ['Popeye']) #new user, 1 game
print add_new_user(net, 'Grace', ['Star Trek', 'Sailor Moon']) #new user, 2 games

print get_connections(net, 'John') #existing user
print get_connections(net, 'Susi') #user doesn't have connections
print get_connections(net, 'Albert') #user not in network

print add_connection(net, 'John', 'Ollie') #user existing in network
print add_connection(net, 'John', 'Susi') #user_B not in network
print add_connection(net, 'Albert', 'John') #user_A not in network
print add_connection(net, 'Albert', 'Susi') #user_A and user_B not  in network

print get_secondary_connections(net, 'John') #user existing in network
print get_secondary_connections(net, 'Albert') # user not in network
print get_secondary_connections(net, 'Grace') #user don't have primary connections

print connections_in_common(net, 'John', 'Ollie')
print connections_in_common(net, 'John', 'Susi') #user_B not in network
print connections_in_common(net, 'Albert', 'John') #user_A not in network
print connections_in_common(net, 'Albert', 'Susi') #user_A and user_B not  in network

print path_to_friend(net, 'John', 'Olive')

print list_of_all_games(net)
print MYOP_connected_gamers(net, 'The Legend of Corgi', 'Jeff')
print MYOP_connected_gamers(net, 'Lilo', 'Bryant')
print MYOP_connected_gamers(net, 'Lilo', 'Jeff')
print MYOP_connected_gamers(net, 'The Legend of Corgi', 'Walter')
print MYOP_connected_gamers(net, 'The Legend of Corgi', 'Robin')





