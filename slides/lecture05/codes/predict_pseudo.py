    def predict_label(N, alpha, L=2):
        total = sum(alpha[k] + N[k] for k in range(L))
        probs = [(alpha[l] + N[l]) / total for l in range(L)]
        return probs

    # Rule j captured 7 strokes and 3 no-strokes
    N     = [7, 3]
    alpha = [1, 1]  # uniform prior

    probs = predict_label(N, alpha)
    print(f"Stroke probability:    {probs[0]:.2%}")  # (1+7)/(12) = 66.67%
    print(f"No-stroke probability: {probs[1]:.2%}")  # (1+3)/(12) = 33.33%