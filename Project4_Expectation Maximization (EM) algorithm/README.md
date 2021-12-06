The task is to build a mixture model for collaborative filtering. 
The data matrix is given - containing movie ratings made by users where the matrix is extracted from a much larger Netflix database. 
Any particular user has rated only a small fraction of the movies so the data matrix is only partially filled. 
The goal is to predict all the remaining entries of the matrix.

To solve this problem the mixtures of Gaussians are used. 
The model assumes that each user's rating profile is a sample from a mixture model. 
In other words, we have K possible types of users and, in the context of each user, we must sample a user type and then the rating profile from the Gaussian distribution associated with the type. 

The Expectation Maximization (EM) algorithm is used to estimate such a mixture from a partially observed rating matrix. 
The EM algorithm proceeds by iteratively assigning (softly) users to types (E-step) and subsequently re-estimating the Gaussians associated with each type (M-step). 
Once we have the mixture, we can use it to predict values for all the missing entries in the data matrix.
