# SegVal_TMI
Code used to re-generate the results and tables for the paper entitled: "Confidence intervals for performance estimates in 3D medical image segmentation". 





# Training

For the training we have used the original implementation of nnUnet. The code is forked from the initial directory and can be found following this [link](https://github.com/rosanajurdi/nnUNet_SegVal)

# Creating Sub-sampled Data

The sub-sampled data is generated via the [Confidence Interval]() directory. The full code can be launched from its main script. Within the parameters of the main.py script, you only need to specify the path to the directory **Stats** which containts you results. The results need to be under the following format: 

Stats Directory Structure

Stats
.
│ └── Task004_SegVal_Hippocampus
│ ├── Dice-Accuracy
│ │ └── results-Dice-3D-L1.csv
│ └── HD
│ ├── Boxplot-hippo-HD.png (to be generated)
│ ├── Distribution-hippo-HD.png  (to be generated)
│ ├── results-hauss-3D-L1.csv
│ └── subsampled-stats-HD-hippo-Dec0214  (to be generated)
│ ├── Boot_txt_log.txt
│ ├── subsampled-stats-HD-hippo-Dec02.csv
│ └── txt_log.txt
├── FrameWork-B
│ ├── Task001_SegVal_BrainTumor
│ │ ├── Distribution-Brain Tumor-3D-DSC.svg  (to be generated)
│ │ ├── Distribution-Brain Tumor-3D-HD.svg  (to be generated)
│ │ ├── Distribution-Brain Tumor-DSC.png  (to be generated)
│ │ ├── Distribution-Brain Tumor-DSC.svg  (to be generated)
│ │ ├── Distribution-Brain Tumor-HD.png (to be generated)
│ │ ├── results-Dice-3D-L1.csv  (required)
│ │ ├── results-hauss-3D-L1.csv  (required)
│ │ └── subsampled-stats-HD-Brain Tumor-Jul2419  (to be generated)
│ │ ├── Boot_txt_log.txt
│ │ ├── full_txt_log.txt
│ │ ├── results.xlsx
│ │ ├── subsampled-stats-HD-Brain Tumor-Jul24.csv
│ │ └── txt_log.txt
│ └── Task004_SegVal_Hippocampus

# Generating the latex table results: 

The tables in the paper are generated via the following [latex_generator]() script. The script takes an input two arguments: 
-path : the path to the csv file containing the sub-sampled results. ( sub-sampled results are the results of the metrics and confidence intervals over all sub-samples both bootstrap and parametric. They are usually found in: )
-key : which dataset we are using hippo for hippocampus and brain for the Brain tumor dataset 

The output is the printed latex table: 

Example

```python
python3 Latex_Generator.py --path /Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv --key  hippo


