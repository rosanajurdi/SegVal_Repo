# Import necessary libraries
"""
this script runs as input the path to the dataset and
runs an entire statistical analysis and Bootstrap analysis on
it. It is the script used to recreate the results in the paper.

input: just the csv file with the test set samples and their performance metric.

"""
import numpy as np
np.random.seed(42)
import pandas as pd
import seaborn as sns
from Confidence_Intervals.Statistical_functions import statistical_analysis, create_subsampling_data, Bootstrap_Analysis
import matplotlib.pyplot as plt
import os
from datetime import datetime
import argparse
from pathlib import Path
from typing import List

def plot_dist(data,metric_name, name, path):
    # data.boxplot(column='metric')
    # plt.title('Box Plot of {} Dataset.'.format(name))
    # plt.xlabel = metric_name
    # plt.savefig(os.path.join(path[0], 'Boxplot-{}-{}'.format(name, metric_name)))
    plt.figure()
    label = {'DSC': 'Dice Accuracy', 'HD': '95 % HD'}
    framework_dict = {'framework-b': '3D', 'framework-b2d': '2D'}

    sns.distplot(data['metric'], hist=True, kde=True,
                 bins=int(180 / 5), color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4},
                 axlabel=label[metric_name])

    # plt.legend(prop={'size': 16}, title='Hippo-Distribution')
    plt.title('Histogram and Density Distribution of {} Dataset.'.format(name))
    framework = framework_dict[Path(path[0]).parts[6].lower()]
    plt.savefig(os.path.join(path[0], 'Distribution-{}-{}-{}.svg'.format(name,framework, metric_name)))

def write_to_overleaf(df_sample, txt_file_Boot,  k):
    mean_variation = '{} $\pm$ {} '.format(df_sample['u-kj'].mean().round(3), df_sample['u-kj'].std().round(3))
    std_variation = '{} $\pm$ {}'.format(df_sample['sigma-kj'].mean().round(3), df_sample['sigma-kj'].std().round(3))
    SEM_Variation = '{} '.format(df_sample['SEM-kj'].mean().round(3))
    Width_Variation = '{} $\pm$ {}'.format(df_sample['w-kj'].mean().round(3), df_sample['w-kj'].std().round(3))
    width_k = df_sample['w-kj'].mean().round(2)
    CI = [-width_k/2, width_k/2]

    mean_variation_star = '{} $\pm$ {} '.format(df_sample['u-kj-star'].mean().round(3),
                                                df_sample['u-kj-star'].std().round(3))
    SEM_Variation_star = '{}'.format(df_sample['SEM-kj-star'].mean().round(3))
    Width_Variation_star = '{} \pm {}'.format(df_sample['w-kj-star'].mean().round(3),
                                              df_sample['w-kj-star'].std().round(3))
    CI_star = '[{}, {}]'.format(df_sample['A-kj-star'].mean(),
                                 df_sample['B-kj-star'].mean())

    txt_file_Boot.write('$k$ = ' + str(k) + "&" + mean_variation + "&" + std_variation + "&" + SEM_Variation +
                   "&" + str(CI) + "&" + mean_variation_star + "&" + SEM_Variation_star + "&" + CI_star + '\n')

    print( '$k$ = ' + str(k) + "&" + mean_variation + "&"
           + std_variation + "&" + SEM_Variation +
            "&" + str(CI) + "&" + mean_variation_star
           + "&" + SEM_Variation_star + "&" + CI_star + '\n')


def write_to_excel(df_sample,  k):
    mean_variation = df_sample['u-kj'].mean().round(3)
    std_variation = df_sample['sigma-kj'].mean().round(3)
    SEM_Variation = df_sample['SEM-kj'].mean().round(3)
    Width_Variation = df_sample['w-kj'].mean()
    width_k = df_sample['w-kj'].mean().round(2)
    CI = [df_sample['A-kj'].mean(), df_sample['B-kj'].mean()]
    #assert (CI[1] - CI[0]).round(3) == Width_Variation.round(3)

    list = [k, mean_variation, std_variation, SEM_Variation, Width_Variation, CI]

    return list






    pass








def run(args: argparse.Namespace):
    # Import the dataset
    # root_path = '/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/Brain_Tumor/test/my_name.csv'

    root_path = args.root_path

    visualize = args.visualize
    visualize_sabsamples = args.visualize_sabsamples
    subsampling = args.subsampling

    K_samples = args.K_samples

    path = root_path.split(os.path.basename(root_path))
    data = pd.read_csv(root_path)

    if len(data)==110:
        name = 'Task004_SegVal_Hippocampus'
    elif len(data) == 334:
        name = 'Brain Tumor'
    if len(data.columns) == 2:
        data.columns = ['index', 'metric']
    elif len(data.columns) == 3:
        data.columns = ['id', 'index', 'metric']
        data = data[['index', 'metric']]
    if 'hauss' in os.path.basename(root_path):
        metric_name = 'HD'

        #data['metric'] *= 100
        #data['metric'] = (data['metric']).round(2)
    elif 'dice' or 'Dice' in os.path.basename(root_path):
        metric_name = 'DSC'


    # create the sub-sample file
    today = datetime.now()
    d4 = today.strftime("%b%d%H")
    folder = "subsampled-stats-{}-{}-{}.csv".format(metric_name, name, str(d4))

    print("results will be saved under ", folder)
    # print Analytical statistical alues:
    print("Analytical statistical values")
    mean, std, SEM, w, CI = statistical_analysis(data)

    # Generate the Gaussian Table:
    #print("Generate the Gaussian Table")
    #Generate_gaussian_dist_table(std, path[0])

    print("Conduct Bootstrapping on the entire dataset")
    # Conduct Bootstrapping on the entire dataset.
    mu_star, sem_star, w_star, conf_interval, conf_interval_norm_star = Bootstrap_Analysis(data, skewness=True)
    #print(str(str(w) + "star:" + str(w_star)))


    #print("stats and bootstrapp: {}  &  {}  &  {}  &  [-{}, {}]  & {} &  {} &  [-{}, {}]".format(
    #    mean,std,SEM,-w / 2, w / 2,mu_star,sem_star,conf_interval[0], conf_interval[1]
    #))



    #Visualize the Distribution of the entire dataset:
    if visualize is True:
        plot_dist(data,metric_name, name, path)


    save_dir = os.path.join(path[0],folder.split('.csv')[0])


    if os.path.isdir(save_dir) is False:
        os.mkdir(save_dir)

    full_result = open(os.path.join(save_dir, 'full_txt_log.txt'), 'w')
    full_result.write(str("stats and bootstrapp: {}  &  {}  &  {}  &  [-{}, {}]  & {} &  {} &  [-{}, {}]".format(
        mean, std, SEM, -w / 2, w / 2, mu_star, sem_star, conf_interval_norm_star[0], conf_interval_norm_star[1])))

    if subsampling == True:
        a = create_subsampling_data(K_samples, data, save_dir, name, metric_name)
        root_path = a
        basepath = root_path.split(os.path.basename(root_path))[0]
        df = pd.read_csv(root_path)

        print("Statistical Analysis ")

        txt_file= open(os.path.join(save_dir, 'txt_log.txt'), 'a')
        txt_file_Boot = open(os.path.join(save_dir, 'Boot_txt_log.txt'), 'a')

        listt = []
        for k in K_samples:
            df_sample = df[df['sample-set']== k]
            #assert df_sample.__len__() == 100 # Make sure that there are only a 100 samples selected.
            l = write_to_excel(df_sample, k)

            write_to_overleaf(df_sample, txt_file_Boot, k)
            listt.append(l)

        df = pd.DataFrame(data=listt, columns=['k', 'Mean', 'STD', 'SEM', 'Width', 'CI'])
        writer = pd.ExcelWriter(os.path.join(save_dir, 'results.xlsx'), engine='xlsxwriter')
        df.to_excel(writer, index=False)
        writer.save()




def get_args(root, dataset) -> argparse.Namespace:
    k_dict = {'hippo': [10, 20, 30, 50, 100, 110],
              'brain': [10, 20, 30, 50, 100, 150, 200,250,300,334]}
    parser = argparse.ArgumentParser(description='Hyperparams')
    parser.add_argument('--dataset', type=str, default=dataset)
    parser.add_argument('--subsampling', type=str, default=True)

    parser.add_argument('--root_path', type=str,
                        default=root)
    #/Users/rosana.eljurdi/PycharmProjects/nnUNet_SegVal/nnUNet_preprocessed/Task001_SegVal_BrainTumor/results-hauss-3D-L1.csv
    parser.add_argument('--visualize' ,  type=str, default=True)
    parser.add_argument('--visualize_sabsamples', type=str, default=False)
    parser.add_argument('--K_samples', type=list,
                        default=k_dict[dataset])

    args = parser.parse_args()
    print(args)
    return args
    
if __name__ == '__main__':

    i = 0
    key = {'Task004_SegVal_Hippocampus': 'hippo', 'Task001_SegVal_BrainTumor': 'brain'}
    stats_path = '/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats'
    frameworks: List[Path] = list(Path(stats_path).rglob('FrameWork-*'))
    for framework in frameworks:
        for root, exp, csv_files in os.walk(os.path.join(stats_path, framework)):

            for exp in csv_files:
                root_path = os.path.join(root, exp)
                if i > 0 and os.path.splitext(exp)[1] == '.csv' and 'subsampled-stats' not in exp :
                    if 'results-hauss' in exp:
                        print("processing for " , root_path)
                        run(get_args(root_path, key[os.path.basename(root)]))
            i = i + 1
    
    """
    key = {'Task004_SegVal_Hippocampus': 'hippo', 'Task001_SegVal_BrainTumor': 'brain'}
    for root, exp, csv_files in os.walk('/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B2D'):
         for exp in csv_files:
             root_path = os.path.join(root, exp)
             if os.path.splitext(exp)[1] == '.csv' and 'results' in exp :
                run(get_args(root_path, key[os.path.basename(root)]))
    """



    #root_path = "/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/results-hauss-3D-L1.csv"

    #run(get_args(root_path, 'hippo'))


    #print("this is the Mac Version")


    #Generate_gaussian_dist_table("/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats")


