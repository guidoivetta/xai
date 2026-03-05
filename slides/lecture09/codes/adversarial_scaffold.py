"""
Adversarial Scaffolding Classifier
===================================
Implementation of the "Fooling LIME and SHAP" framework (Slack et al., 2020).
Follows the scikit-learn predictor interface (fit / predict / predict_proba).
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted


class AdversarialScaffold(BaseEstimator, ClassifierMixin):
    """
    Wraps a biased classifier f with an innocuous classifier psi.
    At prediction time, routes each input through f (real data)
    or psi (OOD / perturbation) based on an internal OOD detector.

    Parameters
    ----------
    f : sklearn-compatible classifier
        The biased black-box classifier to hide.
    psi : sklearn-compatible classifier
        An unbiased classifier used on OOD (perturbed) inputs.
    ood_classifier : sklearn-compatible classifier, optional
        Classifier used to detect OOD samples.
        Defaults to RandomForestClassifier(n_estimators=100).
    perturbation : str, optional
        Strategy to generate perturbations for training the OOD detector.
        'lime'  — additive Gaussian noise ~ N(0, 1)  [default]
        'shap'  — random feature masking with background mean
    ood_threshold : float, optional
        Minimum distance from real data for a perturbation to be labelled OOD.
        Perturbations closer than this (L2) are discarded. Default: 0.0.
    random_state : int, optional
    """

    def __init__(
        self,
        f,
        psi,
        ood_classifier=None,
        perturbation="lime",
        ood_threshold=0.0,
        random_state=42,
    ):
        self.f = f
        self.psi = psi
        self.ood_classifier = ood_classifier
        self.perturbation = perturbation
        self.ood_threshold = ood_threshold
        self.random_state = random_state

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _perturb_lime(self, X):
        """Add Gaussian noise N(0,1) to every feature."""
        rng = np.random.RandomState(self.random_state)
        return X + rng.randn(*X.shape)

    def _perturb_shap(self, X):
        """Randomly replace a subset of features with their column means."""
        rng = np.random.RandomState(self.random_state)
        X_p = X.copy().astype(float)
        background = X.mean(axis=0)
        mask = rng.randint(0, 2, size=X.shape).astype(bool)
        X_p[mask] = np.tile(background, (X.shape[0], 1))[mask]
        return X_p

    def _generate_perturbations(self, X):
        if self.perturbation == "lime":
            return self._perturb_lime(X)
        elif self.perturbation == "shap":
            return self._perturb_shap(X)
        else:
            raise ValueError(f"Unknown perturbation strategy: {self.perturbation}")

    def _filter_too_close(self, X_real, X_perturbed):
        """Remove perturbed points that are too close to real data."""
        if self.ood_threshold <= 0.0:
            return X_perturbed
        kept = []
        for xp in X_perturbed:
            dists = np.linalg.norm(X_real - xp, axis=1)
            if dists.min() > self.ood_threshold:
                kept.append(xp)
        return np.array(kept) if kept else X_perturbed  # fallback: keep all

    # ------------------------------------------------------------------
    # sklearn interface
    # ------------------------------------------------------------------

    def fit(self, X, y):
        """
        Fit f, psi, and the OOD detector on training data X, y.

        Steps
        -----
        1. Fit the biased classifier f.
        2. Fit the unbiased classifier psi.
        3. Generate perturbations and train the OOD detector.
        """
        X = np.array(X)
        y = np.array(y)

        # 1. Fit biased classifier
        self.f.fit(X, y)

        # 2. Fit unbiased classifier
        self.psi.fit(X, y)

        # 3. Build OOD training set
        X_perturbed = self._generate_perturbations(X)
        X_ood = self._filter_too_close(X, X_perturbed)

        X_ood_train = np.vstack([X, X_ood])
        y_ood_train = np.array(
            [False] * len(X) + [True] * len(X_ood)  # False=real, True=OOD
        )

        # 4. Train OOD detector
        if self.ood_classifier is None:
            self.ood_classifier_ = RandomForestClassifier(
                n_estimators=100, random_state=self.random_state
            )
        else:
            self.ood_classifier_ = self.ood_classifier

        self.ood_classifier_.fit(X_ood_train, y_ood_train)

        self.classes_ = np.unique(y)
        self.is_fitted_ = True
        return self

    def _route(self, X):
        """Return boolean array: True where x is OOD (route to psi)."""
        check_is_fitted(self, "is_fitted_")
        return self.ood_classifier_.predict(X).astype(bool)

    def predict(self, X):
        """
        Predict class labels.
        Real data → f(x),  OOD/perturbations → psi(x).
        """
        X = np.array(X)
        is_ood = self._route(X)

        predictions = np.empty(len(X), dtype=object)
        if (~is_ood).any():
            predictions[~is_ood] = self.f.predict(X[~is_ood])
        if is_ood.any():
            predictions[is_ood] = self.psi.predict(X[is_ood])

        return predictions.astype(self.classes_.dtype)

    def predict_proba(self, X):
        """
        Predict class probabilities.
        Real data → f.predict_proba(x),  OOD → psi.predict_proba(x).
        """
        X = np.array(X)
        is_ood = self._route(X)

        n_classes = len(self.classes_)
        probas = np.zeros((len(X), n_classes))

        if (~is_ood).any():
            probas[~is_ood] = self.f.predict_proba(X[~is_ood])
        if is_ood.any():
            probas[is_ood] = self.psi.predict_proba(X[is_ood])

        return probas


# ======================================================================
# Example usage
# ======================================================================
if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split

    # Toy dataset
    X, y = make_classification(n_samples=500, n_features=10, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    # f  — biased classifier (here just a RF as placeholder)
    f = RandomForestClassifier(n_estimators=50, random_state=0)

    # psi — unbiased classifier
    psi = LogisticRegression()

    # Build and fit adversarial scaffold
    scaffold = AdversarialScaffold(
        f=f,
        psi=psi,
        perturbation="lime",   # use 'shap' to mimic SHAP perturbations
        ood_threshold=0.5,
        random_state=42,
    )
    scaffold.fit(X_train, y_train)

    # Predict on real test data  → should route through f
    preds = scaffold.predict(X_test)
    probas = scaffold.predict_proba(X_test)

    print("Predictions:", preds[:10])
    print("Probabilities:\n", probas[:10].round(3))

    # Verify routing: real data should mostly go to f
    is_ood = scaffold._route(X_test)
    print(f"\nRouting on real test data:")
    print(f"  → f   (real): {(~is_ood).sum()} / {len(X_test)}")
    print(f"  → psi (OOD):  {is_ood.sum()} / {len(X_test)}")
