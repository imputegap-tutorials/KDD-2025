==========
Algorithms
==========

To learn how to use an imputation algorithm, please refer to the `tutorial <tutorials.html#imputation>`_.


.. list-table::
   :header-rows: 1

   * - **Family**
     - **Algorithm**
     - **Venue -- Year**
   * - Deep Learning
     - MissNet [27]_
     - KDD -- 2024
   * - Deep Learning
     - BitGraph [32]_
     - ICLR -- 2024
   * - Deep Learning
     - BayOTIDE [30]_
     - PMLR -- 2024
   * - Deep Learning
     - MPIN* [25]_
     - PVLDB -- 2024
   * - Deep Learning
     - PRISTI [26]_
     - ICDE -- 2023
   * - Deep Learning
     - GRIN [29]_
     - ICLR -- 2022
   * - Deep Learning
     - DeepMVI [24]_
     - PVLDB -- 2021
   * - Deep Learning
     - HKMF_T [31]_
     - TKDE -- 2021
   * - Deep Learning
     - MRNN [22]_
     - IEEE Trans on BE -- 2019
   * - Deep Learning
     - BRITS [23]_
     - NeurIPS -- 2018
   * - Deep Learning
     - GAIN [28]_
     - ICML -- 2018
   * - Matrix Completion
     - CDRec [1]_
     - KAIS -- 2020
   * - Matrix Completion
     - TRMF [8]_
     - NeurIPS -- 2016
   * - Matrix Completion
     - GROUSE [3]_
     - PMLR -- 2016
   * - Matrix Completion
     - ROSL [4]_
     - CVPR -- 2014
   * - Matrix Completion
     - SoftImpute [6]_
     - JMLR -- 2010
   * - Matrix Completion
     - SVT [7]_
     - SIAM J. OPTIM -- 2010
   * - Matrix Completion
     - SPIRIT [5]_
     - VLDB -- 2005
   * - Matrix Completion
     - IterativeSVD [2]_
     - BIOINFORMATICS -- 2001
   * - Pattern Search
     - TKCM [11]_
     - EDBT -- 2017
   * - Pattern Search
     - STMVL [9]_
     - IJCAI -- 2016
   * - Pattern Search
     - DynaMMo [10]_
     - KDD -- 2009
   * - Machine Learning
     - IIM [12]_
     - ICDE -- 2019
   * - Machine Learning
     - XGBOOST [13]_
     - KDD -- 2016
   * - Machine Learning
     - MICE [14]_
     - Statistical Software -- 2011
   * - Machine Learning
     - MissForest [15]_
     - BioInformatics -- 2011
   * - Statistics
     - KNNImpute
     - _
   * - Statistics
     - Interpolation
     - _
   * - Statistics
     - MinImpute
     - _
   * - Statistics
     - ZeroImpute
     - _
   * - Statistics
     - MeanImpute
     - _
   * - Statistics
     - MeanImputeBySeries
     - _



.. _references:

References
----------

.. [1] Mourad Khayati, Philippe Cudré-Mauroux, Michael H. Böhlen: Scalable recovery of missing blocks in time series with high and low cross-correlations. Knowl. Inf. Syst. 62(6): 2257-2280 (2020)

.. [2] Olga G. Troyanskaya, Michael N. Cantor, Gavin Sherlock, Patrick O. Brown, Trevor Hastie, Robert Tibshirani, David Botstein, Russ B. Altman: Missing value estimation methods for DNA microarrays. Bioinform. 17(6): 520-525 (2001)

.. [3] Dejiao Zhang, Laura Balzano: Global Convergence of a Grassmannian Gradient Descent Algorithm for Subspace Estimation. AISTATS 2016: 1460-1468

.. [4] Xianbiao Shu, Fatih Porikli, Narendra Ahuja: Robust Orthonormal Subspace Learning: Efficient Recovery of Corrupted Low-Rank Matrices. CVPR 2014: 3874-3881

.. [5] Spiros Papadimitriou, Jimeng Sun, Christos Faloutsos: Streaming Pattern Discovery in Multiple Time-Series. VLDB 2005: 697-708

.. [6] Rahul Mazumder, Trevor Hastie, Robert Tibshirani: Spectral Regularization Algorithms for Learning Large Incomplete Matrices. J. Mach. Learn. Res. 11: 2287-2322 (2010)

.. [7] Jian-Feng Cai, Emmanuel J. Candès, Zuowei Shen: A Singular Value Thresholding Algorithm for Matrix Completion. SIAM J. Optim. 20(4): 1956-1982 (2010)

.. [8] Hsiang-Fu Yu, Nikhil Rao, Inderjit S. Dhillon: Temporal Regularized Matrix Factorization for High-dimensional Time Series Prediction. NIPS 2016: 847-855

.. [9] Xiuwen Yi, Yu Zheng, Junbo Zhang, Tianrui Li: ST-MVL: Filling Missing Values in Geo-Sensory Time Series Data. IJCAI 2016: 2704-2710

.. [10] Lei Li, James McCann, Nancy S. Pollard, Christos Faloutsos: DynaMMo: mining and summarization of coevolving sequences with missing values. 507-516

.. [11] Kevin Wellenzohn, Michael H. Böhlen, Anton Dignös, Johann Gamper, Hannes Mitterer: Continuous Imputation of Missing Values in Streams of Pattern-Determining Time Series. EDBT 2017: 330-341

.. [12] Aoqian Zhang, Shaoxu Song, Yu Sun, Jianmin Wang: Learning Individual Models for Imputation (Technical Report). CoRR abs/2004.03436 (2020)

.. [13] Tianqi Chen, Carlos Guestrin: XGBoost: A Scalable Tree Boosting System. KDD 2016: 785-794

.. [14] Royston Patrick , White Ian R.: Multiple Imputation by Chained Equations (MICE): Implementation in Stata. Journal of Statistical Software 2010: 45(4), 1–20.

.. [15] Daniel J. Stekhoven, Peter Bühlmann: MissForest - non-parametric missing value imputation for mixed-type data. Bioinform. 28(1): 112-118 (2012)

.. [22] Jinsung Yoon, William R. Zame, Mihaela van der Schaar: Estimating Missing Data in Temporal Data Streams Using Multi-Directional Recurrent Neural Networks. IEEE Trans. Biomed. Eng. 66(5): 1477-1490 (2019)

.. [23] Wei Cao, Dong Wang, Jian Li, Hao Zhou, Lei Li, Yitan Li: BRITS: Bidirectional Recurrent Imputation for Time Series. NeurIPS 2018: 6776-6786

.. [24] Parikshit Bansal, Prathamesh Deshpande, Sunita Sarawagi: Missing Value Imputation on Multidimensional Time Series. Proc. VLDB Endow. 14(11): 2533-2545 (2021)

.. [25] Xiao Li, Huan Li, Hua Lu, Christian S. Jensen, Varun Pandey, Volker Markl: Missing Value Imputation for Multi-attribute Sensor Data Streams via Message Propagation (Extended Version). CoRR abs/2311.07344 (2023)

.. [26] Mingzhe Liu, Han Huang, Hao Feng, Leilei Sun, Bowen Du, Yanjie Fu: PriSTI: A Conditional Diffusion Framework for Spatiotemporal Imputation. ICDE 2023: 1927-1939

.. [27] Kohei Obata, Koki Kawabata, Yasuko Matsubara, Yasushi Sakurai: Mining of Switching Sparse Networks for Missing Value Imputation in Multivariate Time Series. KDD 2024: 2296-2306

.. [28] Jinsung Yoon, James Jordon, Mihaela van der Schaar: GAIN: Missing Data Imputation using Generative Adversarial Nets. ICML 2018: 5675-5684

.. [29] Andrea Cini, Ivan Marisca, Cesare Alippi: Multivariate Time Series Imputation by Graph Neural Networks. CoRR abs/2108.00298 (2021)

.. [30] Shikai Fang, Qingsong Wen, Yingtao Luo, Shandian Zhe, Liang Sun: BayOTIDE: Bayesian Online Multivariate Time Series Imputation with Functional Decomposition. ICML 2024

.. [31] Liang Wang, Simeng Wu, Tianheng Wu, Xianping Tao, Jian Lu: HKMF-T: Recover From Blackouts in Tagged Time Series With Hankel Matrix Factorization. IEEE Trans. Knowl. Data Eng. 33(11): 3582-3593 (2021)

.. [32] Xiaodan Chen, Xiucheng Li, Bo Liu, Zhijun Li: Biased Temporal Convolution Graph Network for Time Series Forecasting with Missing Values. ICLR 2024
