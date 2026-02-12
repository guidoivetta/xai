A = fp_growth(data, min_support=0.1, max_cardinality=2) # Step 1: Mine candidate rules
d = sample_from_prior(A, lambda_=3, eta=1) # Step 2: Initialize a random decision list from the prior

for iteration in range(n_iterations): # Step 3: MCMC - sample from posterior
    
    # Propose a new list by randomly choosing one of three moves:
    move = random.choice(["move", "add", "remove"])
    
    if move == "move": d_proposed = move_rule(d) # move a rule to a different position
    elif move == "add": d_proposed = add_rule(d, A) # add a new rule from A
    else: d_proposed = remove_rule(d) # remove a rule from d
    
    # Compute acceptance probability (posterior ratio)
    likelihood_current = compute_likelihood(d, X, y, alpha)  # uses N_j and alpha directly
    likelihood_proposed = compute_likelihood(d_proposed, X, y, alpha)
    prior_current = compute_prior(d, A, lambda_, eta)
    prior_proposed = compute_prior(d_proposed, A, lambda_, eta)
    
    acceptance = min(1, (likelihood_proposed * prior_proposed) /
                        (likelihood_current  * prior_current))
    
    d = d_proposed if random.uniform(0, 1) < acceptance else d # Accept or reject
    posterior_samples.append(d)

# Step 4: Extract point estimate
d_hat = brl_point(posterior_samples)