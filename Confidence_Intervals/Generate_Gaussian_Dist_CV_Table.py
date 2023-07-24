"""
Script to generate the normal (gaussian) distribution confidence interval values. and print them onto a latex table
the mu : mean is set to 60
the standard deviation to a range of values between 0.6 (smallest case) and 60  (highest illogical case)
CV remains the same
N samples between 10 and 1000.

"""
#mu = 60
#sigma = [0.6,1.8,3.6,18,28.8, 36, 54,57.6,59.4]

"""
Script to generate the normal (gaussian) distribution confidence interval values. and print them onto a latex table
the mu : mean is set to 60
the standard deviation to a range of values between 0.6 (smallest case) and 60  (highest illogical case)
CV remains the same
N samples between 10 and 1000.

"""

import os
import numpy as np


def Generate_gaussian_dist_excel(save_dir):
    N_samples = [10, 20, 30, 50, 100, 200, 300, 500, 1000, 1500, 2000]
    sigma = [0.47, 0.81, 1, 2.79, 3.26,10.63, 11.26, 12, 13.13,20,30,50]
    if save_dir is not None:
        txt_file = open(os.path.join(save_dir, 'Gaussian_table_width.txt'), 'w')



    # for a 95 confidence interval statistic the rule is X - 2*sigma/sqrt(n)
    print('\hline')
    import pandas as pd
    listt = []
    txt_file.write('sigma = ' + str(sigma) )
    print('sigma = ' + str(sigma) )

    for k in N_samples:
        print('$k = {}$'.format(k))
        if save_dir is not None:
            txt_file.write('$k = {}$'.format(k))


        for s in sigma:
            ci = [np.round(-1.96 * s / np.sqrt(k), 2), np.round(1.96 * s / np.sqrt(k), 2)]
            listt.append([k, s, np.round(s/np.sqrt(k), 2),np.round(2*1.96 * s / np.sqrt(k), 2), ci ])

    df = pd.DataFrame(data=listt, columns=['k', 'sigma',  'sem', 'x', 'ci'])
    writer = pd.ExcelWriter(os.path.join(save_dir, 'gaussian_excel.xlsx'), engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()



def Generate_gaussian_dist_table(save_dir):
    N_samples = [10, 20, 30, 50, 100, 200, 300, 500, 1000, 1500, 2000, 2500, 3000]
    #sigma = [0.47, 0.81, 1, 2.79, 3.26,5, 10.63, 11.26, 12, 13.13,20,30,50]
    sigma = [13.12]
    if save_dir is not None:
        txt_file = open(os.path.join(save_dir, 'Gaussian_table_width.txt'), 'w')

    # for a 95 confidence interval statistic the rule is X - 2*sigma/sqrt(n)
    print('\hline')

    '''
    for n in N_samples:
        print('$k = {}$'.format(n))
        for s in sigma:
            print( "&", [np.round(mu - 1.96*s/np.sqrt(n),2), np.round(mu + 1.96*s/np.sqrt(n), 2)])
        print('\\ \ ')
    '''

    txt_file.write('sigma = ' + str(sigma) )
    print('sigma = ' + str(sigma) )
    for s in sigma:

        if save_dir is not None:
            # first we calculate SEM for variable k's
            txt_file.write(" \multirow{2}{*}" +"{" +"{}".format(s) + "} "+ "& $SEM$ ")
            for k in N_samples:
                print(" &" + str(np.round(s / np.sqrt(k), 2)) + '\n')
                txt_file.write(" &" + str(np.round(s / np.sqrt(k), 2))  )
            txt_file.write("\\\\  \n")

            txt_file.write(" & $CI$")
            for k in N_samples:
                ci = [np.round(-1.96 * s / np.sqrt(k), 2), np.round(1.96 * s / np.sqrt(k), 2)]
                txt_file.write(" &" + str(ci)  )
                print(" &" + str(ci))

            txt_file.write("\\\\ \hline \n")
            print("&", np.round(s / np.sqrt(k), 2), '&', ci)


if __name__ == '__main__':
    Generate_gaussian_dist_table('/Users/rosana.eljurdi/PycharmProjects/SegVal_Project/Confidence_Intervals')
