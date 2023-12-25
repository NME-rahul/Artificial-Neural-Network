# Knowledge Repersentation

### Notational System

A Notational system also known as symbolic notation, is a set of symbols and rules used to repersent and convey information. Notational system is used in various filed such as mathematics, science, music, linguistic, and computer programming. They provide a structured way to express complex concepts and ideas.

**Mathematical Notational System**

1. Arithmatic notation

$$4 + 5 = 9$$

2. Algebric notation

$$3x + 5 = 9$$

3. Set Notation

$$A = {1, 4, 5, 2, 3}$$

4. calculus notation

$$\int{2x}{dx} = x^2 + c$$

$$\frac{\mathrm}{\mathrm x}$$

5. Matrix notation

$$A = [1, 2, 3, 4]$$


### Tree

Tree-based knwoledge repersentation is a method of structuring and organizing information heirarchy using a tree like structure. This appraoch is particulary used for repersenting heirarchical inforamtion and their relationships and way that is to nevigate and understand. Tree structures are commonly used in computer science, information reterival, linguistic.

![avl tree](https://static.javatpoint.com/ds/images/avl-tree.png)

**Repersentation**
**1. Nodes**
Each node repsents a piece of information or a concept. Node can contain data, attribute or values.

**2. Edges**
Edges connects node and repersent relationship between them.

**feature**
* Heirarchical sructure
* Efficient Navigation
* Clarity and Readability
* Scalabilty
* Simple implementation

**Limitation**

* limited for some relationship
Trees are not suitable for repesenting complex relationship that may have multiple parents or corss links.

* Redundacny
in some cases, information may be repeated in multiple branches, leading to redundancy.

* Rgidity
Once a tree structure is established, it can be challenging to accommodate new relationships or changes in the knwoledge base without restructring.


### Graph

Graph knowledge representation is a method of strcturing and organizing information using a network of nodes and edges, where nodes repersents entites or concepts and edges repersents relationship between them. This approach is highley flexible and versatile, making it suitable for representing complex and interconnected knowledge. Graphs are used in various domains such as AI, database system, social network, and recommendation system.

![](https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Graph/FIGS/Dijkstra/weight01.gif)

**Reprsentation**
**1. Node:**
Nodes represent entites, concepts or data points. Each node can have attributes or properties associates with it.

**2. Edges:** Edges connect nodes and represent relationship or associations between them. Edge can be directed(from one node to another) or undirected(bi-directional).

**Types of graphs**
1. Directed graphs
In directed graphs, edges have a direction. A directed edge from node A to node B implies a relationship from A to B but not from B to A.

2. Undirected graphs
In undirected graphs, edges have no direction, indicating relationship between nodes is symmetric. An edge between node A and B implies a mutual relationship.

3. Weighted graphs
Weighted graphs assign a weight or numerical value to each edge, representing the strength or importance of the relationship between nodes.


**Features**
* Flexibility
* Efficient querying
* Scalability
* Rich semantics
* visual representation

**Limitation**
* complexity
Managing and quering large grpahs can be computationally intesive.

* Data integration
Integrating data from multiple sources into a single coherent graphs can be challenging.

* Schema variablity
Hadling schema changes or evolving knwoledge representations may require constant adjustments.


### Hierarchical

Hierarchical knwoledge representation is a method of organizing and structuring information in a hierarchy or tree-like fashion, where knwoledge is arranged in parent-child relationship. This appraoch is useful for represntting knowledge that shows a clear heirarchy of categories, or concepts. Hierarchical structures are commonly used in various fields, including taxonomy, file systems, organizational charts, and classification systems.

**Represntation**

**1. Node:** Each node represents a concept, category or enitity. Node can contain data or attributes associated with the enitity they represent.

**2. Parent-child relationship:** Nodes are connected through parent-child relationship. Each node has one parent node, and node with the same parents are considered sibilings.

- Animals (Root)
  |- Mammals
  |  |- Carnivores
  |  |  |- Lion
  |  |  |- Tiger
  |  |  |- Wolf
  |  |
  |  |- Herbivores
  |  |  |- Elephant
  |  |  |- Giraffe
  |
  |- Birds
  |  |- Eagles
  |  |- Sparrows
  |
  |- Reptiles
	 |- Snakes
  	 |- Lizards


**Features**
* Clarity and structure
* simplicity
* Efficient categorization
* Scalability
* Faciliates inference

**Limitation**
* Rigidiy
* Limited for some relationship
* Redundancy


### Frame

A Frame is technique of organizing or arranging data in a structure, which consists of a collection of attributes and its value to describe an entity in the world. It consists of a acollections of slots and slot values. These slots may be of nay type and size. slots have names and values which are callled faccets.

A frame may consist any number of slots and a slot may include any number of facets and facets may have any number of values. Frames are derives from sementic network and later evolved in or modern-day classes and objects. A single frame is not much useful. Frames system consist of collection of frames which are connected.

eg. 
Slots	Filters
Title	Artificial Intelligence
Genre	Computer Science
Author	Peter Norvig
Edition	Third Edition
Year	1996
Page	1152

**Features**

* Easy to process: The frame knowledge representation makes the programming easier by gruping the related data.
* Flexibility: The frame representation is comparably flexible and used by many applications in AI.
* Scalabilty: It is very easy to add slots for new attribute and realtions.
* Search: It is easy to include default data and search for missing values.
* Easy to understand: frame representation is easy to understand.

**Issues**

* In frame system inference mechanism is not easily processed.
* Inference mechanism cannot be smoothly processed by frame representation.
* Frame representation has a much generalizeed appraoch.


### Constraint

Constraint knowledge representation is the way of organizing and structuring information, particulary in context of constraint statisfaction problems(CSPs) and constraint based reasoning systems. It invloves specifying relationship and restrictions among variables, allowing for the efficient solution of complex problems that involve statifying a set of constraint.

**Representation**

**1. Variable:** In constraints knowledge representation, variables represent the entites or elements of interset in aproblem. These variabless can take on vaule from a predefined domain.

**2. Domain:** Domains define the set of poosible value that each variable can take. Domains  can be finite or infinite, and they constrain the search space for solutions.

**3. Constraints:** Constraints represents realtionship or conditions that must be satisfied between variables. Constraints specify which combinations of variable assignments are valid and which are not.

**Variables and Domain:** The Combinations of varibles and their associates domains forms the variable assignment space. Each assignment of values to variables is a candidate solution, and constriant deterine whether a candidate solution is valid.

eg. Sudoku: In a sudoku puzzle, each cell is variable wth a domain of numbers from 1 to 9 constraints specify that no two cells in the same row, column, or 3x3 block can have the same value.


**Features**
* Expressivness
* Efficiency
* Flexibility
* Applicability

### Conceptual dependecy

Conceptual dependency is a knowledge representation framework used to model and represent the sementics of natural language sentences. It was developed in 1970s as part of the filed natural language processing and atificial intelligence. The main idea behind conceptual dependency is, it break down sentences into primitive semantic structures or "conceptual dependency" that capture the essential meaning of the sentences. Each Conceptual dependcy represents a specific sematic relationship or action between concepts.

**Representation**
**2. Act:** The act specifies the type of action or relationship between concetps. It represents the sementic role played by the concepts in the sentence. Common acts include "Agent", "Action", "Patient", "Instrument" and more.

**1. Concepts:** Concept represents the entites or thing reffered to in the sentences. They can be objets, actions or attributes.

**3. Conceptual Relationship:** These relationship capture the sementic connections between concepts. For example "Agent" and "Action" have "perform" relationship, indicating that the agent is performing action.

eg. sentence "Ram ate a pizza"

Agent represents the concept "Ram", who performs action. "ate" represents the action or event of eating. "Pizza" repreent the Patient on which action is happen.

**Features**

* Sementic Clarity
* Robustness
* Natural Language understanding
* Interpretation and inference
* Knowledge integraion


**Issues**

* Complexity: reprsentig complex sentences with many interelates concepts and dependencies can be challenging.
* Ambiguity: differnet interpretation of sentences may lead to different sets of conceptual dependencies.
* Scalability
* Lack of formalization
* Integraion with real-world knowledge


### Database

A database can serve as a knowledge represetation system, particulary when it is used to store, orgnaize and manage structured data. A databse reprsets knwoledge about a particular domain or subject matter. A database act as repository for information retrieval, data analysis and knowledge based systems. A databse is a electronic way of storing data.

**Components**

**1. Data tables:** Database cosist of data tables, where each table repersents a specific entity or concept within domain. Each row in a table represents an instance of that entity and columns represents attributes or properties.

**2. Realtions:** Database often icludes relationship between tables. These relationships represents associations or connections between different entities or tables. for example a databse might represents relationship between customer and their orders.

**4. Queries:** Users and application can query the databse to retrievve specfic piece of information or to perform complex data analysis. SQL is commonly used for querying relational database.

**Advantages**

* Structures representation
* Efficient data retieval
* Data integrity
* Concurrrency control
* Scalabilty
* Security
* Transaction management
* Backup and recovery

**Disadvantages**
* Complexity
* Data redundancy
* Schema changes
* Performance tunning
* Data integraion
* security risk
* Scalability challenge
* Vendor lock-in
* Data migration