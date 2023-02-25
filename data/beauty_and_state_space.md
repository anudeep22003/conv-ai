Sense of beauty and state space reduction

I have been teaching myself reinforcement learning and have made some interesting connections that I want to share. In reinforcement learning (RL), you use games as a substrate to teach an AI how to learn the optimal strategy to win. You craft an algorithm that the RL agent, given enough computing power, can theoretically converge to the optimal strategy to play the game. 

The way you do this is to teach an agent the value of the specific state the game can take. An RL algorithm has a few essential components, an environment, a state, a transition function, a value function, and a reward function. 


Environment
In the context of an RL agent, this is the game you are playing. So if an agent has been trained on the game of chess, then the board, the pieces, the rules to their movement is the environment. Essentially the game is where the agent gets to play and receive feedback on the moves they make. 
Since RL algorithms are so deeply inspired by biological agents such as humans, the analog to an environment for RL agents in the real world. The universe and the earth we inhabit are the environments where we act in, and give us feedback on our actions. 

state 
Each distinct configuration of the environment is a state. So in the case of the chess board, a specific position of the pieces is a state. The total number of possible states in chess is humongous, but these also include impossible states given the game. (e.g.: while a state where the king is in the front row and a pawn is behind it in the zeroth row is technically possible, but impossible given how the game starts and is played.)
Even considering all possible legal states of a chess board, the number is humongous - it is on the order of 1E45.

action
An action is the set of allowed moves that the agent can take that transitions the environment from one state to another. For example, moving the pawn one step ahead transitions the environment from one state to another. 

transition function 
This is a learned function that takes as an input the current state, and an action and outputs the resulting state of the environment i.e., how to transition the environment from one state to another given an action. (e.g.: moving the pawn by one step forward is the action, the current configuration is the input state, and the resulting configuration is the output)
Since many moves are possible, the transition function may have many entries for a particular state, but for the combination of state and action, there is only one possible mapping.

value function 
this is the value of every state that has been encountered. The value is learned through the algorithm, and this entry is how the RL agent decides which action to take, given their current state. If two different actions are possible, transitioning into two different resulting states, and the value of the first state is higher than the second, then the agent will choose the first action. 
The concept of value is an abstract measure of how valuable a state is in attaining the final goal. In chess, the goal is to win the game, and not all prior states are equal in value. The ones where you control more of the board and more of your pieces are on the board is a better state to be in. In comparison, having your opponent control most of the board and have more pieces in play than you is a worse state to be in. Thus these intermediary states have differing abstract values in the pursuit of the win. It is these values that the RL algorithm learns. 

reward function
The reward for the action you take. In its purest definition, the only reward of playing a game of chess is if you win. The complexity is in figuring out intermediate rewards, otherwise the agent would be randomly moving through the state space until it reaches a win. This is akin to a group of monkeys randomly banging on a typewriter for perpetuity, and ultimately one of the random combinations would be a coherent sentence and one would be Shakespeare's works. 

Now we have a sense of the essential components of an RL algorithm. As we start with simple games, we can encounter every state and create an entry in the "value function" table. For example, in the game of tic-tac-toe, there are 3^9 (or 19,683 possibilities) which a computer can easily work with. Note that this number includes illegal states, so the actual number is smaller. A minor upgrade to a game like (Connect-4)[https://en.wikipedia.org/wiki/Connect_Four] where you drop a coin and aim to make the longest sequence of 4 coins, the number of states explodes to 3^42 (or 1.09418989E20)! The total bytes of information humanity has produced so far in totality is estimated to be 1E22 bytes. This is comparable to the state space of a simple children's game! It is a wonder we are able to play it at all. 

If you start conjuring up state spaces for games like chess and Go, the number of possible states is truly mind-boggling. Go, for example, has 1E170 (1 followed by 170 zeros!) possible states. The total number of atoms in the universe is estimated to be 1E80. So you can appreciate the magnitude of the size of the state space of Go. Yet we humans play it, and the experts play it profoundly well. 

Ultimately, the reason that RL works is that it is modeled after human intelligence. When we are born, we are not given 10,000 labeled images of a car; we see a car, we interact with it, which is feedback from the environment and store quite quickly the concept of a car. This is especially more visible in our actions as adults. If we decide to go to the supermarket, there are theoretically infinite number of microsteps we take to reach our goal. If a particular road is blocked, we find a way around it. Even if this means passing through an unfamiliar part of the environment, we do it since our focus is on reaching the supermarket. A game is a "toy environment" created to exercise the same faculties. 

When we play a game, we do not map the entire state space and calculate the best move. In some intuitive way, we know which of the intermediate states are valuable and which positions are advantageous even if we haven't seen or experienced those states before. That is how we can comprehend a game like Go with its mind-boggling complexity and still play creatively. 

I posit that the abstract word we use, "beauty," encapsulates the value of state space. This word may go down as the most complex word to mathematically define because if we can, then we can program it into an AI. The AI then may be able to exercise creativity of the sort that is, even now (with all the advance of AI), firmly in the human realm of possibility. Mathematicians talk about elegance and beauty as a precept for the correctness of new mathematical work. The greatest equations are often transfixingly simple looking. Scientists who discovered new paradigms like how atoms are structured, how electricity flows, and the influence of DNA on life, know they are right even if they don't have the proof yet. The ideas often seep into their minds years before they rigorously prove their idea. Einstein, as an example, called the first time he thought of the equivalence of frames of reference for acceleration as his (happiest thought)[https://www.sciencemusings.com/albert-einsteins-most-happy-thought/]. It took him many years to compose it into a Theory of Relativity. 

If a simple-looking game like Go has so many possible states, imagine the game of life. The number of possible states is truly and completely infinite, in the most infinite sense of the word infinity. We still manage to move forward and, most interestingly, discover new science. We are able to because we are guided by our innate sense of beauty that has guided us with an intuitive sense of valuing states. When you learn new science, and you truly understand, you experience that sense of beauty. Over time you hone that sense and start recognizing new ideas that have the potential of greatness. 

An AI does not yet have that ability to distinguish beauty or feel that trembling sense of awe when you understand how sunlight is converted to glucose in chlorophyll, and how that is responsible for the complex life on earth. It even applies to other humans; we see beauty in people (both physical and beyond), it is that same sense at play. The truly deep experiencers of life have figured out a way to recognize this sense of beauty at levels deeper than the our automatic reflex sense. 

We all have the mechanism to recognize beauty, it is on us to put it to practice. 

