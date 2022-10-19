

from  plot_all import plot_all as plot_all
from  plot_difference_function import plot_difference_function as plot_difference_function


Device_name="ESDPMOSM"
TYPE=-1
device_number = ["01","02","03","04","05","06","07","08","09","10","11","12"]

device_numbers=["01","02","03","04","05","06","07","08","09","10","11","12"]


W=[3.20e-05,6.40e-05,9.60e-05,6.40e-05,1.28e-04,1.92e-04,3.20e-05,6.40e-05,9.60e-05,6.40e-05,1.28e-04,1.92e-04]
L=[6.00e-07,6.00e-07,6.00e-07,6.00e-07,6.00e-07,6.00e-07,1.20e-06,1.20e-06,1.20e-06,1.20e-06,1.20e-06,1.20e-06]
nf=[2,2,2,4,4,4,2,2,2,4,4,4]

SETUP_linear_1=[1,11,21,31,41,51,61,71,81,91,101,111]
SETUP_linear_2=[6,16,26,36,46,56,66,76,86,96,106,116]

SETUP_sat_1=[2,12,22,32,42,52,62,72,82,92,102,112]
SETUP_sat_2=[7,17,27,37,47,57,67,77,87,97,107,117]


VB_Bias=[0,0,0,0,0,0,0,0,0,0,0,0]
if TYPE ==1:
    VD_linear = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    VD_sat = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    VG_linear = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
else:
    VD_linear = [-0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1]

    VD_sat = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]

    VG_linear = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]




path_assessment_curves= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\Assessment_curves\\"


path_point_meas= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\ESDPMOSM\\"



filename= Device_name + '_025.clr'


for iter in range(len(W)):
    point_data_flname = "M018xW6C442W14x025x" + Device_name + "x" + device_number[iter] + "xxTP25_clr.txt"
    plot_all(Device_name, device_number[iter], W[iter], L[iter], nf[iter], SETUP_linear_1[iter], SETUP_linear_2[iter], SETUP_sat_1[iter], SETUP_sat_2[iter], VB_Bias[iter]
             , VD_linear[iter], VD_sat[iter], VG_linear[iter], path_assessment_curves, path_point_meas, filename, point_data_flname)

    plot_difference_function(Device_name, device_number[iter], W[iter], L[iter], nf[iter], SETUP_linear_1[iter], SETUP_linear_2[iter], SETUP_sat_1[iter], SETUP_sat_2[iter], VB_Bias[iter]
             , VD_linear[iter], VD_sat[iter], VG_linear[iter], path_assessment_curves, path_point_meas, filename, point_data_flname)
