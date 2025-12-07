# biffron/decision.py

import numpy as np

def biffron_decision(corr_matrix, mu, k=None):
    """
    Implémentation minimaliste du critère BIFFRON.

    Paramètres
    ----------
    corr_matrix : numpy.ndarray (k x k)
        Matrice de corrélation entre critères.
    mu : float
        Force du signal (effet moyen de l'anomalie).
    k : int, optionnel
        Nombre de critères. Si None, déduit de la taille de corr_matrix.

    Retour
    ------
    dict
        {
            "rho": float,       # corrélation moyenne hors diagonale
            "rho_star": float,  # seuil théorique ρ*
            "optimal": str      # "biffron" ou "mono"
        }
    """
    # Si k n’est pas fourni, on le déduit de la matrice
    if k is None:
        k = len(corr_matrix)

    corr_matrix = np.asarray(corr_matrix)

    # Masque pour récupérer uniquement les termes hors diagonale (i < j)
    mask = np.triu(np.ones((k, k), dtype=bool), 1)

    # Corrélation moyenne absolue hors diagonale
    rho = np.abs(corr_matrix[mask]).mean()

    # Seuil théorique ρ*
    rho_star = 1 - 1 / (mu * np.sqrt(k))

    # Décision
    optimal = "biffron" if rho < rho_star else "mono"

    return {
        "rho": float(rho),
        "rho_star": float(rho_star),
        "optimal": optimal,
    }
