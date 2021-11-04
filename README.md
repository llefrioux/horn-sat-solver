# Horn-SAT solver

A Horn-SAT solver written in Python and based on the DIMACS input and output
format.

## What is the Horn-SAT problem?

To understand preciasely the Horn-SAT problem we introduced some definitions.

A **literal** is a boolean variable or its negation. For the variable `X` we
have the **positive literal** `X` and the **negative literal** `-X` (NOT).

A **Horn clause** is finite disjunction (OR) of literals with **at most one
positive literal**, called the head of the clause, and any number of negative
literals, forming the body of the clause.

A **Horn formula** is a finite conjunction (AND) of Horn clauses.

A Horn formula is **satisfiable** if there exists at least one assignment of
the variables of the formula that makes it true, this assignment is a **model**
of the formula. It is **unsatisfiable** otherwise.

In formal logic, **Horn-satisfiability**, or **Horn-SAT**, is the problem of
deciding whether a given Horn formula is satisfiable or unsatisfiable.

## Algorithm description

An algorithm for Horn-SAT is based on the rule of **unit propagation**.

If the formula contains a clause composed of a single literal `L` (called
**unit clause**) the value of the variable should be forced (propagated) in
order to satisfied this clause. Hence, all clauses containing `L` can be
removed because they are now satisfied. Secondly, all clauses containing `-L`
have this literal removed, because this literal has became false and can not
satisfied these clauses any more. The result of the second rule may generate
new unit clauses, which are propagated in the same manner.

If there are no unit clauses left, the formula can be satisfied by simply
setting all remaining variable to false, the resulting model is the minimal
model of the formula.

The formula is unsatisfiable if the propagation generates an empty clause, and
forces a variable to be set simultaneously to true and false.

## DIMACS format

This Horn-sat sovler is based on well established DIMACS format for input and
ouput.

### Input Horn formula

Note that variable are numbered from *1* to `V`.

One line is a header giving the number of variables (`V`) and clauses (`C`):

```
p cnf V C
```

Followed `C` lines, one per Horn-clause. Each line is the list of literal(s) of
the current clause. The line always finishes by a *0*.

There could be some comment lines everywhere in the file, these lines always
started by *c*. For instance:

```
c This is a one line DIMACS comment.
```

### Output result

The results starts with can be either **satisfiable** or **unsatisfiable**.

If the formula is satisfiable, results will start with the line:

```
s SATISFIABLE
```

Plus one line corresponding to the minimal model of the formula.  The line
begins by a *v*, gives the values for the `V` variables in increasing order,
and ends by a *0*. For instance, if the variables *1*, *3*, *4* are false, and
the variable *2* and *5* are true, the resulting line will be:

```
v -1 2 -3 -4 5 0
```

Otherwise, the formula is unsatisfiable result will be:

```
s UNSATISFIABLE
```
