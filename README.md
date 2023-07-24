# SegVal_TMI
Code used to re-generate the results and tables for the paper entitled: "Confidence intervals for performance estimates in 3D medical image segmentation". 





# Training

For the training we have used the original implementation of nnUnet. The code is forked from the initial directory and can be found following this [link](https://github.com/rosanajurdi/nnUNet_SegVal)

# Creating Sub-sampled Data

The sub-sampled data is generated via the [Confidence Interval]() directory. The full code can be launched from its main script. Within the parameters of the main.py script, you only need to specify the path to the directory **Stats** which containts you results. The results need to be under the following format: 

Stats Directory Structure

```
Stats Directory Structure
.
├── 2D_Unet.zip
├── 3D_Unet.zip
├── Boxplots.py
├── FrameWork-A
│   ├── Task001_SegVal_BrainTumor
│   │   ├── Boxplot-Brain Tumor-DSC.png
│   │   ├── Boxplot-Brain Tumor-HD.png
│   │   ├── Distribution-Brain Tumor-DSC.png
│   │   ├── Distribution-Brain Tumor-HD.png
│   │   ├── results-Dice-3D-L1.csv
│   │   ├── results-hauss-3D-L1.csv
│   │   ├── subsampled-stats-DSC-Brain Tumor-Dec0811
│   │   │   ├── Boot_txt_log.txt
│   │   │   ├── subsampled-stats-DSC-Brain Tumor-Dec08.csv
│   │   │   └── txt_log.txt
│   │   ├── subsampled-stats-DSC-Brain Tumor-Dec0812
│   │   │   ├── Boot_txt_log.txt
│   │   │   ├── subsampled-stats-DSC-Brain Tumor-Dec08.csv
│   │   │   └── txt_log.txt
│   │   └── subsampled-stats-HD-Brain Tumor-Dec0812
│   │       ├── Boot_txt_log.txt
│   │       ├── subsampled-stats-HD-Brain Tumor-Dec08.csv
│   │       └── txt_log.txt
│   └── Task004_SegVal_Hippocampus
│       ├── Dice-Accuracy
│       │   └── results-Dice-3D-L1.csv
│       └── HD
│           ├── Boxplot-hippo-HD.png
│           ├── Distribution-hippo-HD.png
│           ├── results-hauss-3D-L1.csv
│           └── subsampled-stats-HD-hippo-Dec0214
│               ├── Boot_txt_log.txt
│               ├── subsampled-stats-HD-hippo-Dec02.csv
│               └── txt_log.txt
├── FrameWork-B
│   ├── Task001_SegVal_BrainTumor
│   │   ├── Distribution-Brain Tumor-3D-DSC.svg
│   │   ├── Distribution-Brain Tumor-3D-HD.svg
│   │   ├── Distribution-Brain Tumor-DSC.png
│   │   ├── Distribution-Brain Tumor-DSC.svg
│   │   ├── Distribution-Brain
```

# Generating the latex table results: 

The tables in the paper are generated via the following [latex_generator]() script. The script takes an input two arguments: 
-path : the path to the csv file containing the sub-sampled results. ( sub-sampled results are the results of the metrics and confidence intervals over all sub-samples both bootstrap and parametric. They are usually found in: )
-key : which dataset we are using hippo for hippocampus and brain for the Brain tumor dataset 

The output is the printed latex table: 

Example

```python
python3 Latex_Generator.py --path /Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv --key  hippo
```

