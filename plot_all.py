
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.patches as patches


def plot_all(Device_name ,device_number ,W ,L ,nf ,SETUP_linear_1 ,SETUP_linear_2 ,SETUP_sat_1 ,SETUP_sat_2 ,VB_Bias
             ,VD_linear ,VD_sat ,VG_linear ,path_assessment_curves ,path_point_meas ,filename ,point_data_flname):


    with open(path_assessment_curves + filename) as f:
        df = pd.read_csv(f, sep="\t", header=None)

    df.columns = ["W", "L", "VB", "VG", "VD", "ID", "IB", "TEMP", "SETUP", "NF", "SA" ,"EMPTY"]


    df_id_vg_1 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_linear_1) & (df['VB'] == VB_Bias)]
    df_id_vg_2 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_linear_2) & (df['VB'] == VB_Bias)]



    df_id_vg_fin1 =df_id_vg_1[(df_id_vg_1['VG' ]==VG_linear)]
    df_id_vg_fin2 =df_id_vg_2[(df_id_vg_2['VG' ]==VG_linear)]


    Idlin_assessment_curve_1 =df_id_vg_fin1['ID']
    Idlin_assessment_curve_2 =df_id_vg_fin2['ID']






    df_id_vg_sat_1 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_sat_1) & (df['VB'] == VB_Bias)]
    df_id_vg_sat_2 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_sat_2) & (df['VB'] == VB_Bias)]



    df_id_vg_sat_fin1 =df_id_vg_sat_1[(df_id_vg_sat_1['VG' ]==VG_linear)]
    df_id_vg_sat_fin2 =df_id_vg_sat_2[(df_id_vg_sat_2['VG' ]==VG_linear)]


    Idsat_assessment_curve_1 =df_id_vg_sat_fin1['ID']
    Idsat_assessment_curve_2 =df_id_vg_sat_fin2['ID']






    with open(path_point_meas + point_data_flname) as f:
        ff = pd.read_csv(f, delim_whitespace=True ,header=None)
    #    ff2 = ff.dropna()
    #      print(ff)
    #      print(len(ff))

    # SIT DNO REP  SU        W        L  NF  TMP           VG        VBULK           VD           VS        VSMU5           IG        IBULK           ID           IS        ISMU5

    ff.columns = ["SIT", "DNO", "REP", "SU", "W", "L", "NF", "TMP", "VG", "VBULK", "VD", "VS", "VSMU5", "IG", "IBULK", "ID",
                  "IS", "ISMU5"]
    print(ff)

    ff_Idlin = ff[(ff['VD'] == VD_linear) & (ff['VG'] == VG_linear)]

    ff_Idsat = ff[(ff['VD'] == VD_sat) & (ff['VG'] == VG_linear)]


    print('now')

    print(ff_Idlin)
    print(ff_Idsat)

    # ff_Idlin=ff_Idlin.assign(Meas_number= [1, 2, 3, 4, 5, 6,7,8,9,10,11,12])
    # ff_Idlin=ff_Idsat.assign(Meas_number= [1, 2, 3, 4, 5, 6,7,8,9,10,11,12])


    print(ff['ID'].iloc[0])
    print(ff['ID'].iloc[1])
    print(ff['ID'].iloc[2])
    print(ff['ID'].iloc[3])
    print(ff['ID'].iloc[4])
    print(ff['ID'].iloc[8])
    print(ff['ID'].iloc[9])
    print(ff['ID'].iloc[10])
    print(ff['ID'].iloc[11])


    Id_half_meas_1 =ff['ID'].iloc[0]
    Idlin_meas_1 =ff['ID'].iloc[1]

    Id_half_meas_2 =ff['ID'].iloc[2]
    Idlin_meas_2 =ff['ID'].iloc[3]



    Id_half_meas_3 =ff['ID'].iloc[8]
    Idlin_meas_3 =ff['ID'].iloc[9]

    Id_half_meas_4 =ff['ID'].iloc[10]
    Idlin_meas_4 =ff['ID'].iloc[11]

    # difference

    Idlin_difference_to_first_meas =[]

    Idlin_difference_to_first_meas_2 =(Idlin_meas_1 -Idlin_meas_2 ) *100 /Idlin_meas_1
    Idlin_difference_to_first_meas_3 =(Idlin_meas_1 -Idlin_meas_3 ) *100 /Idlin_meas_1
    Idlin_difference_to_first_meas_4 =(Idlin_meas_1 -Idlin_meas_4 ) *100 /Idlin_meas_1



    print(Idlin_difference_to_first_meas_2 ,Idlin_difference_to_first_meas_3 ,Idlin_difference_to_first_meas_4)

    print(ff_Idlin['ID'])
    print(ff_Idsat['ID'])

    mp.scatter(ff_Idlin['ID'], ff_Idsat['ID'])
    mp.show()

    print(ff_Idlin)
    print(ff_Idsat)
    # ff_id_vg_1 = ff[(ff['W'] == W) & (ff['L'] == L) & (ff['VD'] == VD_linear) & (ff['VG'] > 0.9)]

    print(ff_Idlin['ID'])
    print(ff_Idsat['ID'])

    print(len(ff_Idlin['ID']))
    print(len(ff_Idsat['ID']))

    time =[]

    for i in range(len(ff_Idlin['ID'])):
        time.append(i)


    print(time)
    fig, ax = mp.subplots()

    mp.scatter(time ,ff_Idlin['ID'] ,color='blue')
    mp.plot(13 ,Idlin_assessment_curve_1, linewidth=1.0, linestyle="", marker="^", color="red")
    mp.plot(14 ,Idlin_assessment_curve_2, linewidth=1.0, linestyle="", marker="^", color="magenta")


    mp.legend(['point-meas' ,'Idlin_IV_sweep1' ,'Idlin_IV_sweep1'])

    picname = Device_name + "_" + device_number + "_W=" + str(W) + "_L=" + str(L) + "_Idlin_xTP25.png"


    mp.title(picname)

    mp.savefig(picname)
    mp.xlabel('Sequence of Measurement-Die25')
    mp.ylabel('Idlin (A)')
    mp.grid()
    mp.show()




    fig, bx = mp.subplots()

    mp.scatter(time ,ff_Idsat['ID'] ,color='blue')
    mp.plot(13 ,Idsat_assessment_curve_1, linewidth=1.0, linestyle="", marker="^", color="red")
    mp.plot(14 ,Idsat_assessment_curve_2, linewidth=1.0, linestyle="", marker="^", color="magenta")


    mp.legend(['point-meas' ,'Idsat_IV_sweep1' ,'Idsat_IV_sweep1'])

    picname = Device_name + "_" + device_number + "_W=" + str(W) + "_L=" + str(L) + "_" + str(nf)+ "_" + "_Idsat_xTP25.png"


    mp.title(picname)

    mp.savefig(picname)
    mp.xlabel('Sequence of Measurement-Die25')
    mp.ylabel('Idsat (A)')
    mp.grid()
    mp.show()






