## Structure of an Expert System
The Expert system relflects the understanding of the methods of repersenting knowledge  and how to perform intelligent decision making tasks with the support of a computer based system. Complex decision involves complex combination of factual and heuristic knowledge and In order to efficently use of this knowledge the system is organized in an esasily accessible format.

In laymen terms whatever rules are there inside a persons head, e translate them to a program and let the machine decides the final output. This program is generally a combination of if-else conditions.

Expert systems are organized in three distinct levels.

#### a. Knowledge Base :-
A Knowledge base is created by knowledge engineers, who translate the knolwdgw of real huann experts into rules and strategies. The Knowledge constitutes the problem solving rules, facts or itution that a expert might use in slving problems in a given problem domain. The knowldge base is usually stored in terms of if-then rules. A knowledge base is the nucleus of expert system.

#### b. Working Memory :-
It refers to task specific data for the problem under conideration. It consists of an essential component called database. it Contains a set of rules that to be used by a system at a given moment.

#### c.  Inference Engine :-
This is a genric control mechanism that applies the axiomatic knwledge in the knowledge base to the task specific data to arrive at some solution or conclusion. Inference in production system is accomplished by a process of channg through the rules recursively, either in a forward or in a backward direction until a conclusion is reached.

![expertsystem](https://static.javatpoint.com/tutorial/ai/images/expert-systems-in-ai.png)

## Areas addressed by an expert system
* Interpretation
* Prediction
* Diagnosis
* Design
* Planning
* Monitoring
* Debugging
* Repair
* Instruction
* Control

## Types of expert system
1. Rule based expert system
2. Fuzzy expert system
3. Frame based expert system
4. Hybrid expert system
5. Neural expert system
6. Neuro-Fuzzy system

##### The Success of any expert system majorly depends on the quality, completeness and accuracy of the inforation stored in the knowledge base.

## Web-based expert system
Web-based expert systems(WBESs) provide the benifits of both expert systems tecnology and web technology. The use of web service deilver functionalities of WBESs allows the interation of these system in web-portals. WEBSs are used in diversitty of areas like engineering, management, medicine, agriculture, education, tourism, finance etc. A study on the various features of WEBESs like knowledge-repersentation, reasononig, languages, implementation tools, use of various web service related process such as discovery, selecton, composition etc.


## Difference between Human and Expert System
				Expert system										Human experts
	-> It express(process) it's knowledge in the		-> A human expert expresses it knowledge in human
	   the form of rules and heruistic values.			   in human language and in rules.
	-> Expert system helps in tracing the rules that	-> It is capable of explaining reasoning line and provide
	   produce during solving a problem.				   details.
	-> An expert system is avialable all the day		-> A human expert is available at only specific time
	   you want and cheaper in compare					   and cosltly as compare.
	-> It might generate false output on incomplete		-> A human expert can deal with uncertain and fuzzy information.
	   uncertain and fuzzy information.
	-> An expert system enhance it's knowledge by		-> A human expert enhace his/her knowledge by problem
	   adding new rules or by adjusting old ones.	       solving and years of learning and practical training.
	-> To solve ay problem it takes very short time.    -> a human expert can take variable time based on the size of
														   problem.
    -> It is replaceable.								-> it is not replaceable.
	

## Expert system and Machine learning
An expert system is a intelligent system that machine learning algorithms to produce results.

## Socital impacts
An Expert system creates substantial empact on an orgnaization that changes it's overall shape. How?, ES technology improve the productivity, effectiveness and improving quality of work life by changing the fundamental nature of orgnaizational knowledge processing. Further, it xploits technological advances to find better solutions to problems.

we should aware of that technical innovation repersents risks thus we should examines the problem and impacts of implementing ES tech.

## Knowledge acquistion
What is knowledge base?
A knowledge base contains domain-specific and high-quality knowledge. The sucess of any ES majorly depends upon the collection oh highly accurate and precise knowledge.

Components of knowledge base

1. Factual knowledge - a knwoledge base contains the factual information accepted by data engineers and scholars.
2. Heuristic knowledge - it is about practice, accurate judgement, ability of evaluation, and guessing.

He/she aquire information from subject expert by recording, interviewing, and observing him at work etc. He/She then catergorize and orgnaize the information in a maeaningful way, in the form of if-then-else rules, to be used by inference machine.

The knwoledge base is forms by reading from various experts, scholars and the Knowledge Engineers.


## Development of an Expert System
1. Identify problem Domain - 
-> The problem must be suittable for an expert system to solve it.
-> Find the experts in task domain for ES project.

2. Design the system - 
-? identify ES technology
-> know and establish the degree of integraion with other systems and database.
-> Realize how the concepts can repersent the domain knowledge best.

3. Develope the prototype - 
-> acquire domain knowledge and repersent it in the if-then-else rules.
-> Test and refine the prototype by using sample cases to test for any deficiencies in performance.
-> Test the ES with the end user.

4. Develope and complete the ES - 
-> Remove any errors that found in test.
-> Ensures the integration of database and other information system.
-> Train the user to use ES.

5. Maintain the system - 
-> Keep the knowledge base up-to-date.

## Case-Based Reasoning(CBR)
Case-Based resoning use a Database of problem solutions to solve new problems. it stores the tuples or cases of problem-solving as complex symbolic descpition.

How it works?
1. when a new case arises CBR first checks if an identical training case exists. if one is found produce solution to that case.
2. if no identical case id found, then the CBR will search for training cases having similar components to new case(training case are conisdered as neighbours of the new case).
3. if cases are repersented as graphs, this involves searching for subgraphs that are similar to subgraphs within the new case.
4. Then CBR tries to combine the solutions of the neighbouring training cases to propose a solution. if compatibility arises with the solutions, then backtracking to search fo other solutions.

The CBR may employ backgorund knowledge and problem-solving stratergies to propose a feasible solution.

* Application of CBR - 
-> Customer service
-> Engineering and law
-> Medical educations



