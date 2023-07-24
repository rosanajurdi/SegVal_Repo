from texttable import Texttable
import latextable

from texttable import Texttable
import latextable
import pandas as pd
from pathlib import Path
import argparse

# defining dictionary parameters possibilities:
subsamples = {'Task001_SegVal_BrainTumor': 334, 'Task004_SegVal_Hippocampus': 110 }
dictt = {'Framework-B2D': '2D-Unet', 'FrameWork-B': '3D-Unet',
             'Task001_SegVal_BrainTumor': 'Brain Tumour dataset',
            'Task004_SegVal_Hippocampus': 'Hippocampus dataset',
             'DSC': 'Dice Accuracy', 'HD': 'Haussdorf Distance'
             }
label = {'Framework-B2D': '2D',
        'Task001_SegVal_BrainTumor': 'Brain',
         'Task004_SegVal_Hippocampus': 'Hippo', 'DSC': 'Dice', 'HD': 'Haussdorf'}



def Write_to_textable(df,K_samples):
    latex_list_k = []
    for k in K_samples:
        print(k)
        if k <K_samples[-1]:
            df_sample = df[df['sample-set'] == k]
            mean_variation = '${} \pm {}$ '.format(df_sample['u-kj'].mean().round(3), df_sample['u-kj'].std().round(3))
            std_variation = '${} \pm {}$'.format(df_sample['sigma-kj'].mean().round(3),
                                                 df_sample['sigma-kj'].std().round(3))
        if k == K_samples[-1]:
            df_sample = df[df['sample-set'] == k]
            mean_variation = '${}$ '.format(df_sample['u-kj'].mean().round(3))
            std_variation = '${} $'.format(df_sample['sigma-kj'].mean().round(3))
        SEM = '${}$ '.format(df_sample['SEM-kj'].mean().round(3))
        width_k = df_sample['w-kj'].mean().round(2)
        width_norm = width_k / df_sample['u-kj'].mean().round(3)
        CI = [-width_k / 2, width_k / 2]  # this needs to be symmetric since it follows the gaussian distribution

        mean_variation_star = '${} \pm {}$ '.format(df_sample['u-kj-star'].mean().round(3),
                                                    df_sample['u-kj-star'].std().round(3))
        SEM_star = '${}$'.format(df_sample['SEM-kj-star'].mean().round(3))
        Width_star = '${}$'.format(df_sample['w-kj-star'].mean().round(3))
        Width_star_norm = df_sample['w-kj-star'].mean().round(3) / df_sample['u-kj-star'].mean().round(3)
        CI_star = '$[{}, {}]$'.format(df_sample['A-kj-star'].mean().round(3),
                                      df_sample['B-kj-star'].mean().round(3))


        latex_list_k.append([k, mean_variation,std_variation, SEM, CI, width_norm,
                             mean_variation_star,SEM_star,  CI_star, Width_star_norm ])

    return latex_list_k





def get_caption(path):
    p = Path(path)
    framework = dictt[p.parts[6]]
    metric = dictt[p.parts[8].split('-')[2]]
    dataset = dictt[p.parts[7]]
    k = subsamples[p.parts[7]]
    caption_1 = '{}, {}, {}. Results on subsamples of size $k \leq {}$. Results are shown as mean'.format(dataset,
                                                                                                 framework,
                                                                                                 metric, k)
    caption_2 = '$\pm$ std where mean and std are the mean and standard-deviation of the {}'.format(metric)
    caption_3 = 'over all the subsamples Sk,j of a given size k (k is fixed and $j \in [1, . . . , n]$) with n = {}'.format(k)
    label_t = "table:{}-{}-{}".format(label[p.parts[7]],p.parts[8].split('-')[2],framework.split('-')[0] )
    return caption_1 + caption_2 + caption_3, label_t

def run(args: argparse.Namespace):
    path = args.path
    key = args.key
    table_1 = Texttable()

    df = pd.read_csv(path)
    caption = ""

    k_dict = {'hippo': [10, 20, 30, 50, 100, 110],
                  'brain': [10, 20, 30, 50, 100, 150, 200,250,300,334]}
    table_content = Write_to_textable(df, k_dict[key])
    table_1.set_cols_align(["l","ccccc", "cccc", 'c', "c", "c", "c", "c", "c", "c"])
    table_1.set_cols_valign(["m", "m", "m", "m", "m", "m", 'm', 'm', 'm', 'm'])
    table_1.set_deco(Texttable.HEADER)
    latex_rows = [["Subsample size $k$", "$\mu_k$", "$\sigma_k$", "SEM", "CI", "$w_n$", "$\mu ^*_k$", "$SEM^*_k$", "$CI ^ * $", "$w^*_n$"]]

    for row in table_content:
        latex_rows.append(row)

    caption, label = get_caption(path)
    table_1.add_rows(latex_rows)

    print('Texttable Output:')
    print(table_1.draw())
    print('\nLatextable Output:')

    print(latextable.draw_latex(table_1, caption=caption, label=label))
"""

def get_args()-> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Hyperparams')
    parser.add_argument('--path', type=str, default="/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Stats/FrameWork-B/Task004_SegVal_Hippocampus/subsampled-stats-DSC-Hippocampus-Jan1118/subsampled-stats-DSC-Hippocampus-Jan11.csv")
    parser.add_argument('--key', type=str, default='hippo')

    args = parser.parse_args()
    print(args)
    return args
if __name__ == '__main__':

    run(get_args())

"""
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Hyperparams')
    parser.add_argument('--path', type=str, required=True, help='Path to the CSV file')
    parser.add_argument('--key', type=str, required=True, choices=['hippo', 'brain'], help='Specify the key (hippo or brain)')
    args = parser.parse_args()
    print(args)
    return args

if __name__ == '__main__':
    args = get_args()
    run(args)
