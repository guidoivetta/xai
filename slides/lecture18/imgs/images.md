# Images to extract from Lecture_18.pdf

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| paper1_title.png | 1 | Título del Paper 1: "GANSpace: Discovering Interpretable GAN Controls" con autores |
| ganspace_motivation.png | 2 | Ejemplo motivacional de GANSpace (edición de imagen) |
| gan_background.png | 5 | Background: GANs — diagrama conceptual del generador/discriminador |
| biggan_background.png | 6 | Background: BigGAN — arquitectura y características |
| stylegan_background.png | 7 | Background: StyleGAN — mapping network + AdaIN |
| ganspace_pca_biggan.png | 21 | Diagrama de z→y (activation space)→z con flechas de BigGAN 2-step |
| ganspace_cats_grid.png | 23 | Grid de gatos: Fix first 8 PCA coord. vs Randomize first 8 PCA coord. |
| ganspace_variance_pdf.png | 24 | Gráfico de varianza por componente + 4 PDFs marginales de PCs |
| ganspace_class_independent.png | 25 | Grid de Husky/Castle/Lighthouse/Barn con dirección "translation" y "zoom" |
| ganspace_limitations.png | 26 | Cara femenina + cara masculina (wrinkles/makeup sin efecto en hombres) |
| ganspace_entanglement.png | 26 | Grid de autos (sportiness) + grid de perros (boca abierta al rotar) |
| ganspace_comparison.png | 27 | Grid de autos StyleGAN2: PCA vs random basis coords (fix/randomize first 5) |
| paper2_title.png | 36 | Título del Paper 2: "Interpreting the Latent Space of GANs for Semantic Face Editing" |
| gan_diagram.png | 41 | Diagrama GAN completo: Latent Space → G → Generated Fake Samples → D → Is D Correct? |
| latent_code_editing.png | 42 | Diagrama de edición semántica: vector de latent code → cara original y editada |
| interfacegan_subspace_projection.png | 49 | Diagrama 3D de n1, n2 con proyección n1 - (n1^T n2)n2 |
| pggan_architecture.png | 51 | Diagrama de entrenamiento progresivo de PGGAN + grid de caras CelebA-HQ |
| separation_hyperplane.png | 52 | Diagrama de hiperplano con emoji feliz (z1) y triste (z2) separados |
| interfacegan_separation_table.png | 53 | Tabla 1: Classification accuracy (%) on separation boundaries (Pose/Smile/Age/Gender/Eyeglasses) |
| interfacegan_separation_viz.png | 54 | Grid de caras a distancias +inf/0/-inf para Pose/Smile/Age/Gender/Eyeglasses |
| interfacegan_single_attr.png | 55 | Grid de rostros con manipulación de un atributo (Pose/Smile/Age/Gender/Eyeglasses) |
| interfacegan_distance_effect.png | 56 | Efecto de distancia: Female extreme → Near Boundary → Male extreme |
| interfacegan_artifacts.png | 57 | Artifacts Correction: grid 3×4 de caras con artefactos corregidos |
| interfacegan_correlation_tables.png | 58 | Tabla 2 (cosine similarity) y Tabla 3 (correlation coefficient) entre atributos |
| interfacegan_conditional_results.png | 60 | Figure 7: Age/Gender/Age w/ Gender Preserved + Eyeglasses/Age/Eyeglasses w/ Age Preserved |
| stylegan_architecture.png | 62 | Diagrama de arquitectura StyleGAN: Traditional generator vs Style-based generator |
| interfacegan_stylegan_results.png | 63 | Comparación W Space / Z Space / Z Space w/ Condition para dirección eyeglasses/age |
| interfacegan_real_image.png | 64 | Experiment 5: Real image inversion + Young/Old y Calm/Smile edits (PGGAN + StyleGAN) |
| interfacegan_encoder.png | 65 | Encoder-based inversion: diagrama Image→Encoder→Generator + LIA latent space results |
