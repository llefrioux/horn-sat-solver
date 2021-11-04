#### USEFUL FUNCTIONS FOR CLAUSES AND LITERALS ####

# Return true if the clause is unit, false otherwise.
def is_unit_clause(clause):
   return len(clause) == 1

# Return true if the clause is empty, false otherwise.
def is_empty_clause(clause):
   return len(clause) == 0

# Return true if the literal is positive, false otherwise
def is_positive_literal(lit):
   return lit > 0

# Return the variable associated to a given literal
def lit_to_var(lit):
   return abs(lit)


#### MAIN ####

if __name__ == "__main__":
    
   # Read the DIMACS header
   unused1, unused2, V, C = input().split()
   V = int(V)                      # Number of variables 
   C = int(C)                      # Number of clauses
   
   # Declaration of the structures
   lit_to_cls = { i : [] for i in range(-V, V + 1) } # Index of clauses containing a literal
   clauses    = [None] * C                           # The formula represented by a list of clauses
   model      = [None] * (V + 1)                     # The current assignement
   units      = []                                   # All literals that should be propagated
   sat        = True                                 # Is the formula satisfiable?
   
   # Read the clauses
   for id_cls in range(C):
      # Read the clause and do not forget to remove the '0'
      clause = [int(lit) for lit in input().split()[:-1]]
   
      # Update the structures
      clauses[id_cls] = clause
   
      # Update reference from lit to clause index
      for lit in clause:
         lit_to_cls[lit] += [id_cls]
   
      if is_unit_clause(clause):    # The clause is unit and is added for propafgation
         units += [clause[0]]
      elif is_empty_clause(clause): # The formula contains an empty clause
         sat = False                # it is then unsatisfiable
   
   # Until there is propagation to do and the formula is not unsatisfiable
   while len(units) and sat:
      lit   = units.pop()
      var   = lit_to_var(lit)
      value = is_positive_literal(lit) 
      
      if model[var] == None:    # The variable as not a value yet
         model[var] = value
      elif model[var] != value: # There is a conflict => unsatisfaible
         sat = False
         break
      else:                     # Already been assigned to this value
         continue
   
      # Manage clauses containing the literal
      for id_cls in lit_to_cls[lit]:
         clauses[id_cls] = None      # The clause is satisfied and can be forgotten
   
      # Manage clauses containing the inverted literal
      for id_cls in lit_to_cls[-lit]:
         clause = clauses[id_cls]
   
         if clause == None: # The clause has already been satisfied
            continue
   
         clause.remove(-lit) # The literal is false, it is deleted from the clause
   
         if is_unit_clause(clause):    # The clause has became unit
            units += [clause[0]]
         elif is_empty_clause(clause): # The clause has became empty
            sat = False                # The formula is then unsatisfiable
            break
   
   # Print the coresponding answer in DIMACS format
   if sat:                        # SAT
      print("s SATISFIABLE")
      for var in range(1, V + 1):
         if model[var] == None:
            model[var] = False
      out_model = ["v"]
      for var in range(1, V + 1):
         if not model[var]:
            var = -var
         out_model += [var]
      out_model += [0]
      print(*out_model)
   else:                          # UNSAT
      print("s UNSATISFIABLE")
