# Images to replace

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| `prior_work_diagram.png` | 2 | Diagrama: Training data → Model ← Test data (flechas negras), sin flecha de vuelta a training data |
| `saliency_example.png` | 3 | Lista de saliency methods (Gradient, SmoothGrad, LIME, etc.) + imagen de golden retriever con saliency map |
| `our_work_diagram.png` | 4 | Mismo diagrama Training data → Model ← Test data + flecha azul punteada "Influence functions" de Model hacia Training data |
| `dataset_debugging.png` | 5 | 4 imágenes histología (Tumor/Tumor/Normal/Normal) → Training → Model → Test point (histología) → predicción incorrecta "35% Normal" con X roja |
| `doctor_mislabeling.png` | 6 | Doctor con imagen histológica mislabeled + setup leave-one-out con flecha de vuelta a training data |
| `loo_approach.png` | 41 | Diagrama LOO: 4 imágenes histología con caja "Leave-one-out approach" superpuesta + flecha azul punteada a Training data + referencia [Quenouille,1956; Tukey,1958] |
| `loo_results.png` | 44 | LOO resultado 3: training data con imagen Normal eliminada (dashed) + pesos → Model → predicción cambió de 35% a 75% Normal (+40% en verde) |
| `upweighting_diagram.png` | 47 | Training data con 4 imágenes histología, primer imagen eliminada (dashed), pesos [0, 1, 1, 1] → Training → Model + Test point |
| `taylor_approx.png` | 48 | Gráfico: eje x = Weight (on training point) de 0 a 1, eje y = Change in prediction (on test point). Curva sólida púrpura (Actual change, Slow) y línea punteada azul (Estimated change, Fast). Punto en (1, 0) = Original model |
| `removing_single_points.png` | 59 | Scatter plot: eje x = Actual change in test loss, eje y = Estimated change in test loss (via influence functions). Logistic regression (MNIST). Puntos azules sobre diagonal. Cada punto = eliminar un training example |
| `where_to_apply.png` | 60 | Diagrama: Training data (azul claro) ← flecha azul punteada "Influence functions" — Model ← Training (flecha negra). Test data (salmón) → Evaluation → Model. Texto "Where can you apply influence functions?" |
