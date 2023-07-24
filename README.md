# SegVal_TMI
Code used to re-generate the results and tables for the paper entitled: "Confidence intervals for performance estimates in 3D medical image segmentation". 





# Training

For the training we have used the original implementation of nnUnet. The code is forked from the initial directory and can be found following this [link](https://github.com/rosanajurdi/nnUNet_SegVal)

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

## Arguments of the main script:

the main script has some arguments that help you generate sub-sampling data and their corresponding visualizations.

-  --subsampling : should be set to true if you want the script to sub-sample and generate sub-sampling results. (is set to falso only when debugging).
-  --root_path' : is defined by the script itself, when you define the path to Stats.
    #/Users/rosana.eljurdi/PycharmProjects/nnUNet_SegVal/nnUNet_preprocessed/Task001_SegVal_BrainTumor/results-hauss-3D-L1.csv
    parser.add_argument('--visualize' ,  type=str, default=True)
    parser.add_argument('--visualize_sabsamples', type=str, default=False)
    parser.add_argument('--K_samples', type=list,
                        default=k_dict[dataset])

# Generating the latex table results: 

The tables in the paper are generated via the following [latex_generator]() script. The script takes an input two arguments: 
-path : the path to the csv file containing the sub-sampled results. ( sub-sampled results are the results of the metrics and confidence intervals over all sub-samples both bootstrap and parametric. They are usually found in: )
-key : which dataset we are using hippo for hippocampus and brain for the Brain tumor dataset 

The output is the printed latex table: 

Example

```python
python3 Latex_Generator.py --path /Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv --key  hippo
```

