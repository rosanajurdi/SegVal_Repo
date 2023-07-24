# SegVal_TMI
Code used to re-generate the results and tables for the paper entitled: "Confidence intervals for performance estimates in 3D medical image segmentation". 





# Training

For the training we have used the original implementation of nnUnet. The code is forked from the initial directory and can be found following this [link](https://github.com/rosanajurdi/nnUNet_SegVal)


#Generating the latex table results: 

The tables in the paper are generated via the following [latex_generator]() script. The script takes an input two arguments: 
-path : the path to the csv file containing the sub-sampled results. ( sub-sampled results are the results of the metrics and confidence intervals over all sub-samples both bootstrap and parametric. They are usually found in: )
-key : which dataset we are using hippo for hippocampus and brain for the Brain tumor dataset 

The output is the printed latex table: 

Example

```python
python3 Latex_Generator.py --path /Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv --key  hippo
Namespace(key='hippo', path='/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv')
