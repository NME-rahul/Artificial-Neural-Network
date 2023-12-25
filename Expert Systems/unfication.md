## Unification

* Unification is the process of making two different predicate logical expression identical by finding a substitute.
* It depends on the substitution process.
* It takes two literals as input and makes them identical using substitution.

let, {Knig(x), King(John)} are two different predicate logic, to make them identical,

assume $$\Psi_1 = King(x)$$ and $$\Psi_2 = King(john)$$

then substitute john with x $$\Theta = {john|x}$$


### Conditions for unification

1. Predicate symbol must be same, atoms or expressions with different symbol can never be unified.

$$Like(x) then Like(apple)$$

2. Number of arguments in both expressions must be identical.

$$Human(x, y, z) then Human(u, v, w)$$

3. Unification will if there are two similar variables present in the same expression.

$$Play(x, w, x)$$

4. If expression in both predicates are function then they must be smilar.

$$Love(f(y)) then Love(f(n))$$


### Algorithm

1. Initialize the subtitution set to empty.
2. Recusively unify the atomic sentences.
	* Check for identical expression match.
		* if yes
			then fail
	* if one expression has a variable xi and the other has ti(which does not contain xi), then:
		* Add ti with xi(ti|xi) in the substitution set.
		* if both expressions are functions, then function name must be simlar, and the number of arguments must be the same in both the exression.
		

**Examples**

1.  find the MGU(most general unifier) of {p(f(a), g(Y)) and p(X, X)}
sol.	$$\Psi_1 = p(f(a), g(Y))$$
$$\Psi_2 = p(X, X)$$

in the second predicate both the expressions/variable are same

hence, unification failed

2. Find the MGU of {p(b, X, f(g(Z))) and p(Z, f(Y), f(Y))}
sol. $$\Psi_1 = p(b, X, f(g(Z)))$$
$$\Psi_2 = p(Z, f(Y), f(Y))$$

substitute $$\Theta_1 = {Z/b}$$
$$\Theta_2 = {f(Y)/X}$$
$$\Theta_2 = {g(Z)/Y}$$

3. Find the MGU of {p(X, X) and p(Z, f(Z))}
sol. both variables in first predicate are identical and if expression is function then they must be similar in both predicates.


4. Find the MGU of {Q(a, g(x, a), f(y)) and Q(a, g(f(b), a), x)}
sol. $$\Psi_1 = Q(a, g(x, a), f(y))$$
$$\Psi_2 = Q(a, g(f(b), a), x))$$

sbstitute $$\Theta_1 = {f(b) | x}

then $$\Psi_1 = Q(a, g(f(b), a), f(y))$$
$$\Psi_2 = Q(a, g(f(b), a), f(b)))$$

substitute  $$\Theta_2 = {b | y}

then $$\Psi_1 = Q(a, g(f(b), a), f(y))$$
$$\Psi_2 = Q(a, g(f(b), a), f(y)))$$


5. unify {Knows(Richar, X), Knows(Richard, jhon)}

$$\Psi_1 = Knows(Richard, X)$$
$$\Psi_2 = Knows(Richard, jhon)$$

substitute  $$\Theta_2 = {X | jhon}

then $$\Psi_1 = Knows(Richard, X)$$
$$\Psi_2 = Knows(Richard, x)$$

6. Unify {Prime(11), Prime(y)}

$$\Psi_1 = Prime(11)$$
$$\Psi_2 = Prime(y)$$

substitute  $$\Theta_2 = {y | 11}

then $$\Psi_1 = Prime(y)$$
$$\Psi_2 = Prime(y)$$