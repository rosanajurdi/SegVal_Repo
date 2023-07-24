# SegVal_TMI
Code used to re-generate the results and tables for the paper entitled: "Confidence intervals for performance estimates in 3D medical image segmentation". 





# Training

For the training we have used the original implementation of nnUnet. The code is forked from the initial directory and can be found following this [link](https://github.com/rosanajurdi/nnUNet_SegVal). We will skip the documentation for this step as it is a specification of the model you are using. You can refer for the link above for the documentation on nnUnet training, or for our previous [repo]() for a framework we did via regular Unet. The functions and modalities in this repo are independent of the training. 

# Creating Sub-sampled Data

The sub-sampled data is generated via the [Confidence Interval]() directory. The full code can be launched from its main script. Within the parameters of the main.py script, you only need to specify the path to the directory **Stats** which containts you results. The results need to be under the following format: 

Stats Directory Structure

```
Stats Directory Structure
Path/to/Stats/ 
├── FrameWork-B
│   ├── Task001_SegVal_BrainTumor
│   │   ├── Distribution-Brain Tumor-3D-DSC.svg (to be generated)
│   │   ├── Distribution-Brain Tumor-3D-HD.svg (to be generated)
│   │   ├── Distribution-Brain Tumor-DSC.png (to be generated)
│   │   ├── Distribution-Brain Tumor-DSC.svg (to be generated)
│   │   ├── results-Dice-3D-L1.csv (input)
│   │   ├── results-hauss-3D-L1.csv (input)
│   │   ├── subsampled-stats-DSC-Brain Tumor-Jan1118 (to be generated)
│   │   │   ├── Boot_txt_log.txt
│   │   │   ├── full_txt_log.txt
│   │   │   ├── results.xlsx
│   │   │   ├── subsampled-stats-DSC-Brain Tumor-Jan11.csv
│   │   │   └── txt_log.txt
│   │   ├── subsampled-stats-HD-Brain Tumor-Jan1118 (to be generated)
│   │   │   ├── Boot_txt_log.txt
│   │   │   ├── full_txt_log.txt
│   │   │   ├── results.xlsx
│   │   │   ├── subsampled-stats-HD-Brain Tumor-Jan11.csv
│   │   │   └── txt_log.txt

```

Before the main script runs, Stats directory has to have two the csv files belonging to the performances of the patients under the format name 
results-metric-(3D or 2D)-region.csv (ex: results-Dice-3D-L1.csv, or results-HD-2D-L2.CSV). 

The sub-sampling directory will contain the following information: 
- Boot_txt_log.txt : results from bootstrapping on the different sub-sample sizes
-  full_txt_log.txt : results on the entire dataset for the 3D metrics (analystical + bootstrapping values)
- results.xlsx : the results but in as an excel sheet
- subsampled-stats-DSC-Brain Tumor-Jan11.csv : the sub-sampled results for all 100 random selections and their corresponding results
- txt_log.txt : the analytical values obtained from the Gaussian model estimation


## Arguments of the main script:

the main script has some arguments that help you generate sub-sampling data and their corresponding visualizations.

-  --subsampling : should be set to true if you want the script to sub-sample and generate sub-sampling results. (is set to falso only when debugging).
-  --root_path : is defined by the script itself, when you define the path to Stats.
- --visualize : if set to true, Visualizes the Distribution of the entire dataset through box plots
- -- --visualize_sabsamples: to visualize box plots of each sub-sample
- '--K_samples': predefined, entire testset size, no need to set a value, it is automatically done for hippo and brain-tumor dataset

  The most important parameter to be set to true is the subsampling parameter. If set to true, it will generate a sub-directory of FrameWork-* with the following format :subsampled-stats-metric-Bdataset-data (ex: subsampled-stats-DSC-Brain Tumor-Jan1118). The code will generate this for all frameworks within the Stats directory. 

# Other functions in the Confidence Interval Directory
aside from the confidence intervals based on the variable sample size, you can also generate the confidence intervals basing on the Gaussian assumption via the following python script : [Generate_Gaussian_Dist_CV_Table.py]()

# Generating the latex table results: 

The tables in the paper are generated via the following [latex_generator]() script. The script takes an input two arguments: 
-path : the path to the csv file containing the sub-sampled results. ( sub-sampled results are the results of the metrics and confidence intervals over all sub-samples both bootstrap and parametric. They are usually found in: )
-key : which dataset we are using hippo for hippocampus and brain for the Brain tumor dataset 

# Additional Data: 

In addition to the tables and results, you can also have access to the meta data of the survey conducted in [statistics]()



```python
python3 Latex_Generator.py --path /Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv --key  hippo
```

