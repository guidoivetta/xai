def lime_explain(f, x, x_prime, pi_x, K, N):
    """
    f       : black-box model (callable)
    x       : original instance
    x_prime : interpretable representation of x (binary vector)
    pi_x    : proximity function centered at x
    K       : max number of features in explanation
    N       : number of samples
    """
    Z = []
    for _ in range(N):
        # Step 1: perturb x' by randomly turning off components
        z_prime = random_mask(x_prime)

        # Step 2: map back to original representation
        z = h_x(z_prime, x)

        # Step 3: query the black-box model
        label = f(z)

        # Step 4: compute proximity weight
        weight = pi_x(z)

        Z.append((z_prime, label, weight))

    # Step 5: fit sparse linear model with at most K features
    g = k_lasso(Z, K)

    return g